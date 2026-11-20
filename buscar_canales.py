#!/usr/bin/env python3
"""Busca canales pequeños (<50k subs) con Shorts recientes que rinden por encima de su tamaño.

Uso:  YOUTUBE_API_KEY=... python3 buscar_canales.py "excel tips" en
      (segundo argumento = código de idioma: en / es)

Cuota: cada búsqueda cuesta 100 unidades de las 10.000 diarias (verifica en Google Cloud Console).
NOTA: videoDuration=short devuelve videos de <4 min, no solo Shorts; revisa a mano que sean
verticales y de <=60 s, y que el canal no muestre cara. Script sin probar contra la API real.
"""
import json, os, sys, urllib.parse, urllib.request
from datetime import datetime, timedelta, timezone

KEY = os.environ.get("YOUTUBE_API_KEY")
if not KEY:
    sys.exit("Falta YOUTUBE_API_KEY (ver nicho.md, sección 'Cómo crear la clave').")
API = "https://www.googleapis.com/youtube/v3/"


def get(endpoint, **params):
    params["key"] = KEY
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


query = sys.argv[1]
lang = sys.argv[2] if len(sys.argv) > 2 else "en"
since = (datetime.now(timezone.utc) - timedelta(days=60)).strftime("%Y-%m-%dT%H:%M:%SZ")

videos = []
page = None
for _ in range(2):  # 2 páginas = 200 unidades de cuota
    p = dict(part="snippet", q=query + " #shorts", type="video", videoDuration="short",
             order="viewCount", publishedAfter=since, relevanceLanguage=lang, maxResults=50)
    if page:
        p["pageToken"] = page
    res = get("search", **p)
    videos += [(i["id"]["videoId"], i["snippet"]["channelId"]) for i in res.get("items", [])]
    page = res.get("nextPageToken")
    if not page:
        break

vid_ids = [v for v, _ in videos]
views = {}
for i in range(0, len(vid_ids), 50):
    r = get("videos", part="statistics", id=",".join(vid_ids[i:i + 50]))
    for it in r.get("items", []):
        views[it["id"]] = int(it["statistics"].get("viewCount", 0))

chan_ids = sorted({c for _, c in videos})
rows = []
for i in range(0, len(chan_ids), 50):
    r = get("channels", part="snippet,statistics", id=",".join(chan_ids[i:i + 50]))
    for c in r.get("items", []):
        st = c["statistics"]
        if st.get("hiddenSubscriberCount"):
            continue
        subs = int(st.get("subscriberCount", 0))
        if subs >= 50000 or subs == 0:
            continue
        best = max((views.get(v, 0) for v, ch in videos if ch == c["id"]), default=0)
        rows.append((best / subs, subs, best, c["snippet"]["title"],
                     "https://www.youtube.com/channel/" + c["id"]))

print("ratio_vistas_por_sub,subs,vistas_mejor_short,canal,url")
for ratio, subs, best, title, url in sorted(rows, reverse=True):
    print(f"{ratio:.1f},{subs},{best},{title.replace(',', ' ')},{url}")

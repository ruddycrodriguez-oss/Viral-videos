// Renderiza el vídeo: captura cada fotograma de la escena (Chromium sin pantalla + WebGL por software)
// y lo une con la voz en un MP4 vertical 1080x1920.
// Uso: node render.js <carpeta_con_timeline.json_y_voz.wav> <salida.mp4> [trabajadores]
//      node render.js --worker <k> <n> <carpeta> <carpeta_fotogramas>   (uso interno)
const { spawn, spawnSync } = require('child_process');
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const { iniciar } = require('./servir.js');
const FPS = 30;

async function trabajador(k, n, dir, frames) {
  const tl = JSON.parse(fs.readFileSync(path.join(dir, 'timeline.json'), 'utf8'));
  const total = Math.ceil(tl.duracion * FPS);
  const { server, port } = await iniciar();
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--enable-webgl'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', (e) => console.error('ERROR PAGINA:', e.message));
  const rel = path.relative(__dirname, path.join(dir, 'timeline.json')).split(path.sep).join('/');
  await p.goto(`http://127.0.0.1:${port}/escena.html?tl=${encodeURIComponent(rel)}`);
  await p.waitForFunction('window.__listo === true', null, { timeout: 120000 });
  for (let i = k; i < total; i += n) {
    await p.evaluate((x) => window.renderFrame(x), i / FPS);
    await p.screenshot({ path: path.join(frames, String(i).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 94 });
    if (i % (n * 60) === k) console.log(`trabajador ${k}: fotograma ${i}/${total}`);
  }
  await b.close(); server.close();
}

async function principal() {
  const a = process.argv.slice(2);
  if (a[0] === '--worker') return trabajador(parseInt(a[1]), parseInt(a[2]), a[3], a[4]);
  const [dir, salida, nTrab = '3'] = a;
  const frames = path.join(dir, 'fotogramas'); fs.rmSync(frames, { recursive: true, force: true }); fs.mkdirSync(frames, { recursive: true });
  const n = parseInt(nTrab);
  const procesos = [];
  for (let k = 0; k < n; k++) procesos.push(new Promise((res, rej) => { const c = spawn('node', [__filename, '--worker', String(k), String(n), dir, frames], { stdio: 'inherit' }); c.on('exit', (code) => code === 0 ? res() : rej(new Error('trabajador ' + k + ' falló'))); }));
  await Promise.all(procesos);
  // voz: normaliza el volumen y mezcla con el vídeo
  const voz = path.join(dir, 'voz.wav');
  const r = spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(frames, '%05d.jpg'), '-i', voz,
    '-filter_complex', '[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[a]', '-map', '0:v', '-map', '[a]',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.1', '-movflags', '+faststart',
    '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', salida], { stdio: 'inherit' });
  if (r.status !== 0) throw new Error('ffmpeg falló');
  fs.rmSync(frames, { recursive: true, force: true });
  console.log('listo:', salida);
}
principal().catch((e) => { console.error(e); process.exit(1); });

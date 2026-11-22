// Datazo · «Así se construye»: diorama 3D low-poly del Canal de Panamá, en corte longitudinal.
// Todo es geometría propia generada por código (Three.js). La función window.renderFrame(t) es determinista:
// el estado de la escena depende solo del tiempo t, para poder renderizar cada fotograma por separado.
import * as THREE from 'three';

const W = 1080, H = 1920;
const TL = await (await fetch(new URLSearchParams(location.search).get('tl') || './timeline.json')).json();   // { duracion, eventos:{nombre:segundos}, palabras:[{w,ini,fin,termino}] }
const EV = TL.eventos;
const ev = (n, d = 0) => (EV[n] ?? 1e9) + d;

// ---------------------------------------------------------------- utilidades
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const smooth = (t) => { t = clamp(t); return t * t * (3 - 2 * t); };
const easeOut = (t) => { t = clamp(t); return 1 - Math.pow(1 - t, 3); };
const prog = (t, t0, dur) => clamp((t - t0) / dur);
const hash = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };
const TAU = Math.PI * 2;

// ---------------------------------------------------------------- render
const canvas = document.getElementById('c');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1);
renderer.setSize(W, H, false);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x091830);
scene.fog = new THREE.Fog(0x091830, 38, 110);
const camera = new THREE.PerspectiveCamera(36, W / H, 0.5, 300);

scene.add(new THREE.HemisphereLight(0xdfeaff, 0x2b3a58, 1.05));
const sun = new THREE.DirectionalLight(0xfff3d6, 2.3);
sun.position.set(-8, 20, 14);
sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
Object.assign(sun.shadow.camera, { left: -26, right: 26, top: 14, bottom: -10, near: 1, far: 70 });
sun.shadow.bias = -0.0008;
sun.target.position.set(0, 0, -1);
scene.add(sun, sun.target);

const C = {
  grass: 0x66c35a, soil: 0x8a5428, soilD: 0xc9965a, rock: 0x7b8798, rockD: 0x5c6677, clay: 0xd2a05f, sand: 0xe6c88a, deep: 0x4a5568, water: 0x2f9bff, concrete: 0xdfe4ee,
  gate: 0xffd21f, hull: 0x1f3a6b, cabin: 0xffffff, yellow: 0xffd21f, red: 0xff3b30, trunk: 0x6b4423, leaf: 0x2f8f4e, leaf2: 0x3fae5f,
};
const mat = (color, extra = {}) => new THREE.MeshStandardMaterial({ color, flatShading: true, roughness: 0.92, metalness: 0, ...extra });
const waterMat = () => new THREE.MeshStandardMaterial({ color: C.water, transparent: true, opacity: 0.72, roughness: 0.25, flatShading: true });
const box = (w, h, d, m) => { const me = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); me.castShadow = true; me.receiveShadow = true; return me; };

// ---------------------------------------------------------------- terreno: columnas a lo largo del canal (x)
// Cada columna tiene dos tramos en z: A = canal (z de -1.5 a 0; z=0 es el plano de corte) y B = márgenes (z de -3 a -1.5).
const X0 = -18, X1 = 18, N = 72, DX = (X1 - X0) / N, BASE = -2.2;
const KEY = [[-18, -1.4], [-15, -1.2], [-13.6, -0.2], [-12.6, 0.6], [-9, 0.7], [-4, 0.9], [-1, 1.2], [1, 2.6], [3.2, 5.2], [5.2, 6.3], [7.2, 4.4], [8.6, 2.0], [10, 1.0], [12, 0.6], [13.8, 0.1], [15, -1.0], [18, -1.4]];
function H0(x) {
  for (let i = 0; i < KEY.length - 1; i++) {
    const [xa, ha] = KEY[i], [xb, hb] = KEY[i + 1];
    if (x >= xa && x <= xb) { const u = (x - xa) / (xb - xa); return lerp(ha, hb, (1 - Math.cos(Math.PI * u)) / 2); }
  }
  return -1.4;
}
const colX = (i) => X0 + (i + 0.5) * DX;
const jit = (i, k) => (hash(i * 7 + k) - 0.5);
const inR = (x, a, b) => x >= a && x <= b;

// locks
const LOCK_L = { gates: [-13.4, -11.8, -10.2, -8.6], levels: [0, 1, 2, 3], floors: [-0.5, 0.5, 1.5] };      // sube de 0 a 3 (≈26 m)
const LOCK_R = { gates: [9.0, 10.6, 12.2, 13.8], levels: [3, 2, 1, 0], floors: [1.5, 0.5, -0.5] };           // baja de 3 a 0
const LAKE = { x0: -8.6, x1: 9.0, level: 3.0 };
const TRENCH_FLOOR = -0.6, CUT_FLOOR = 2.0;
const wallTop = 3.7;

function lockFloorAt(x) {
  for (const L of [LOCK_L, LOCK_R]) {
    const [a, b] = [L.gates[0], L.gates[3]];
    if (x >= a && x < b) { const k = Math.min(2, Math.floor((x - a) / (L.gates[1] - L.gates[0]))); return L.floors[k]; }
  }
  return null;
}

// tiempos del argumento (derivados de los eventos de la narración)
const T_DIG = ev('excavar'), T_DIG_DUR = 5.0;
const T_SLIDE = ev('derrumbe'), T_FLOOD = ev('inunda');
const T_PLAN = ev('plan'), T_MORPH_DUR = 3.2;
const T_DAM = ev('presa'), T_LAKE = ev('lago');

const digFront = (t) => lerp(-14.4, 14.4, easeOut(prog(t, T_DIG, T_DIG_DUR)));
function trenchCut(x, t) { return smooth((digFront(t) - x) / 1.6) * (inR(x, -14.4, 14.4) ? 1 : 0); }
const morph = (t) => smooth(prog(t, T_PLAN, T_MORPH_DUR));

function heights(i, t) {
  const x = colX(i);
  const base = H0(x);
  const rough = base > 0.3 ? jit(i, 1) * 0.28 : 0;
  const bank0 = base + rough + (base > 1 ? jit(i, 5) * 0.35 : 0);
  const chan0 = base + rough;
  // plan 1: zanja a nivel del mar (con derrumbes)
  const cut = trenchCut(x, t);
  const slide = smooth(prog(t, T_SLIDE, 2.0)) * (0.35 + 0.65 * hash(i * 3.3)) * 0.9 * (inR(x, -9, 8) ? 1 : 0);
  let A = lerp(chan0, TRENCH_FLOOR, cut) + cut * slide;
  let B = bank0;
  // plan final: presa, lago, corte Culebra y esclusas
  const m = morph(t);
  let Af = chan0, Bf = bank0;
  if (inR(x, 0.4, 9.0)) Af = Math.min(chan0, CUT_FLOOR - 0.0 + jit(i, 2) * 0.1);
  const lf = lockFloorAt(x);
  if (lf !== null) { Af = lf; Bf = wallTop; }
  if (inR(x, LOCK_L.gates[3] + 0.05, -7.2)) Bf = wallTop + 0.2;   // presa (embankment) junto al lago
  if (inR(x, 9.0, 13.8)) Bf = wallTop;
  const damGrow = smooth(prog(t, T_DAM, 2.2));
  const lockGrow = smooth(prog(t, ev('esclusas', -0.5), 2.0));
  if (inR(x, LOCK_L.gates[3] + 0.05, -7.2)) Bf = lerp(bank0, wallTop + 0.2, damGrow);
  if (lf !== null) { Af = lerp(chan0, lf, lockGrow); Bf = lerp(bank0, wallTop, lockGrow); }
  if (inR(x, 9.0, 13.8) && lf === null) Bf = lerp(bank0, wallTop, lockGrow);
  A = lerp(A, Af, m); B = lerp(B, Bf, m);
  return [A, B];
}

const cols = [];
const sandM = mat(C.sand), deepM = mat(C.deep), grassM = mat(C.grass), soilM = mat(C.soil), soilDM = mat(C.soilD), rockM = mat(C.rock), rockDM = mat(C.rockD), concM = mat(C.concrete), clayM = mat(C.clay);
for (let i = 0; i < N; i++) {
  const x = colX(i);
  const seg = [];
  for (const [z0, z1] of [[-1.5, 0], [-3, -1.5]]) {
    const mk = (m) => { const b = box(DX * 0.995, 1, z1 - z0, m); b.position.z = (z0 + z1) / 2; b.position.x = x; scene.add(b); return b; };
    seg.push({ g: mk(grassM), b4: mk(sandM), b3: mk(soilM), b2: mk(clayM), b1: mk(rockM), b0: mk(deepM) });
  }
  cols.push(seg);
}
// franjas horizontales de tierra (estratos), iguales en todo el diorama: de abajo hacia arriba
const STRATA = [-99, -0.9, 0.9, 2.5, 4.3];   // límites inferiores de b0, b1, b2, b3, b4
function updateTerrain(t) {
  const lockCol = (x) => lockFloorAt(x) !== null;
  const setBox = (m, top, bot) => { const hh = top - bot; m.visible = hh > 0.002; if (!m.visible) return; m.scale.y = hh; m.position.y = (top + bot) / 2; };
  for (let i = 0; i < N; i++) {
    const [A, B] = heights(i, t);
    const x = colX(i);
    [A, B].forEach((h, k) => {
      const q = cols[i][k];
      const sea = h < -0.1;
      const concrete = (k === 1 && h > 3.3) || (k === 0 && lockCol(x) && morph(t) > 0.5);
      const capH = concrete ? (k === 1 ? Math.max(0.3, h - 1.2) : 0.5) : 0.26;
      const top = h - capH;
      const bands = [q.b4, q.b3, q.b2, q.b1, q.b0];
      const lows = [STRATA[4], STRATA[3], STRATA[2], STRATA[1], BASE];
      const highs = [1e9, STRATA[4], STRATA[3], STRATA[2], STRATA[1]];
      bands.forEach((m, j) => { setBox(m, Math.min(top, highs[j]), Math.max(BASE, lows[j])); m.material = [sandM, soilM, clayM, rockM, deepM][j]; });
      setBox(q.g, h, top); q.g.material = concrete ? concM : (sea ? soilDM : grassM);
    });
  }
}

// ---------------------------------------------------------------- agua
function waterBox(x0, x1, z0, z1) { const m = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), waterMat()); m.receiveShadow = true; m.userData = { x0, x1, z0, z1 }; scene.add(m); return m; }
function setWater(m, top, bot, x0 = m.userData.x0, x1 = m.userData.x1) {
  const hh = top - bot;
  m.visible = hh > 0.01 && x1 > x0;
  m.scale.set(x1 - x0, Math.max(0.001, hh), m.userData.z1 - m.userData.z0);
  m.position.set((x0 + x1) / 2, (top + bot) / 2, (m.userData.z0 + m.userData.z1) / 2);
}
const seaL = waterBox(-18, LOCK_L.gates[0], -3, 0), seaR = waterBox(LOCK_R.gates[3], 18, -3, 0);
const lake = waterBox(LAKE.x0, LAKE.x1, -3, 0);
const trenchW = waterBox(-14.4, 14.4, -1.5, 0);
const floodW = waterBox(-9, 1.5, -1.5, 0);
const chL = [0, 1, 2].map((k) => waterBox(LOCK_L.gates[k], LOCK_L.gates[k + 1], -1.5, 0));
const chR = [0, 1, 2].map((k) => waterBox(LOCK_R.gates[k], LOCK_R.gates[k + 1], -1.5, 0));

const T_LOCKS = ev('entra'), T_CLOSE = Math.max(ev('cierra'), ev('entra') + 2.2), T_FILL = Math.max(ev('llena'), T_CLOSE + 0.4);
const T_UP2 = Math.max(ev('sube2'), T_FILL + 3.3), T_UP3 = Math.max(ev('sube3'), T_UP2 + 3.9);
const T_CROSS = Math.max(ev('cruza'), T_UP3 + 5.5);
// niveles de las cámaras de la izquierda (suben) y de la derecha (bajan)
function chLevelL(k, t) {
  const L = LOCK_L.levels;
  const starts = [T_FILL, T_UP2 + 0.8, T_UP3 + 0.8], dur = [3.0, 2.4, 2.4];
  return lerp(L[k], L[k + 1], smooth(prog(t, starts[k], dur[k])));
}
function rightSchedule() { // inicio de cada paso al bajar
  const s0 = T_CROSS + 2.6; return [s0 + 0.8, s0 + 2.8, s0 + 4.8];
}
function chLevelR(k, t) {
  const L = LOCK_R.levels, st = rightSchedule();
  return lerp(L[k], L[k + 1], smooth(prog(t, st[k], 1.1)));
}
function updateWater(t) {
  const m = morph(t);
  setWater(seaL, 0, BASE); setWater(seaR, 0, BASE);
  // lago: sube cuando se forma
  const lakeLvl = lerp(0.2, LAKE.level, smooth(prog(t, T_LAKE, 3.2)));
  setWater(lake, lakeLvl, -1.2, LAKE.x0, LAKE.x1);
  lake.visible = t >= T_DAM && lakeLvl > 0.25;
  // agua de la zanja a nivel del mar (plan 1)
  const cut = smooth(prog(t, T_DIG, T_DIG_DUR));
  const front = digFront(t);
  setWater(trenchW, t < T_PLAN + 0.3 ? 0 : -9, -1.2, -14.4, Math.min(14.4, front));
  trenchW.visible = t >= T_DIG + 0.5 && t < T_PLAN + 1.5;
  // inundación del río Chagres
  const f = smooth(prog(t, T_FLOOD, 3.0));
  setWater(floodW, lerp(TRENCH_FLOOR + 0.1, 1.6, f) + 0.0, TRENCH_FLOOR - 0.2);
  floodW.visible = t >= T_FLOOD && t < T_PLAN + 1.2;
  chL.forEach((w, k) => { setWater(w, chLevelL(k, t), LOCK_L.floors[k] - 0.05); w.visible = m > 0.7; });
  chR.forEach((w, k) => { setWater(w, chLevelR(k, t), LOCK_R.floors[k] - 0.05); w.visible = m > 0.7; });
}
// nivel de agua en un punto x (para posar el barco)
function surfaceAt(x, t) {
  if (x < LOCK_L.gates[0]) return 0;
  for (let k = 0; k < 3; k++) if (x < LOCK_L.gates[k + 1]) return chLevelL(k, t);
  if (x < LAKE.x1) return LAKE.level;
  for (let k = 0; k < 3; k++) if (x < LOCK_R.gates[k + 1]) return chLevelR(k, t);
  return 0;
}

// ---------------------------------------------------------------- compuertas y estructuras de las esclusas
const gates = [];
function makeGate(xg, floorY, topY, side) {
  const g = new THREE.Group();
  const leaf = box(0.12, topY - floorY, 0.76, mat(C.gate));
  leaf.position.set(0, (topY - floorY) / 2, 0.39);
  g.add(leaf);
  g.position.set(xg, floorY, -1.5);
  scene.add(g);
  gates.push({ g, xg });
  return g;
}
const gateObjs = { L: [], R: [] };
LOCK_L.gates.forEach((xg, k) => { const fl = LOCK_L.floors[Math.min(k, 2)] - 0.05; gateObjs.L.push(makeGate(xg, fl, LOCK_L.levels[Math.min(3, k + 1)] + 0.5, 0)); });
LOCK_R.gates.forEach((xg, k) => { const fl = LOCK_R.floors[Math.min(k, 2)] - 0.05; gateObjs.R.push(makeGate(xg, fl, LOCK_R.levels[Math.max(0, k)] + 0.5, 0)); });
// ángulo 0 = cerrada (cruza el canal); ±90° = abierta (pegada al muro)
function updateGates(t) {
  const show = morph(t) > 0.7;
  const open = (t0, t1) => smooth(prog(t, t0, 0.7)) * (1 - smooth(prog(t, t1, 0.7)));
  const L = [open(T_LOCKS - 0.3, T_CLOSE), open(T_UP2 - 0.2, T_UP2 + 3.0), open(T_UP3 - 0.2, T_UP3 + 3.0), open(T_UP3 + 3.0, 1e9)];
  const st = rightSchedule();
  const R = [open(T_CROSS + 1.8, st[0] - 0.1), open(st[0] + 0.9, st[1] - 0.1), open(st[1] + 0.9, st[2] - 0.1), open(st[2] + 0.9, 1e9)];
  gateObjs.L.forEach((g, k) => { g.visible = show; g.rotation.y = -Math.PI / 2 * (1 - 0) * L[k] * 1; });
  gateObjs.R.forEach((g, k) => { g.visible = show; g.rotation.y = -Math.PI / 2 * R[k]; });
}

// ---------------------------------------------------------------- tubería (conductos): el agua baja del lago por gravedad
const pipe = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, LAKE.x0 - LOCK_L.gates[0] + 0.6, 10, 1, true), new THREE.MeshStandardMaterial({ color: 0xdfe4ee, transparent: true, opacity: 0.35, side: THREE.DoubleSide, flatShading: true }));
pipe.rotation.z = Math.PI / 2; pipe.position.set((LAKE.x0 + LOCK_L.gates[0]) / 2 + 0.0, -1.35, -0.4);
scene.add(pipe);
// ---------------------------------------------------------------- partículas
class Pool {
  constructor(color, max, size) {
    this.mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(size, size, size), mat(color), max);
    this.mesh.frustumCulled = false; this.mesh.castShadow = false; this.max = max; this.n = 0; this.d = new THREE.Object3D();
    scene.add(this.mesh);
  }
  begin() { this.n = 0; }
  add(x, y, z, s = 1, rot = 0) { if (this.n >= this.max) return; const d = this.d; d.position.set(x, y, z); d.scale.setScalar(s); d.rotation.set(rot, rot * 1.3, rot * 0.7); d.updateMatrix(); this.mesh.setMatrixAt(this.n++, d.matrix); }
  end() { this.mesh.count = this.n; this.mesh.instanceMatrix.needsUpdate = true; }
}
const dirt = new Pool(C.soil, 220, 0.16), stones = new Pool(C.rockD, 160, 0.2), drops = new Pool(C.water, 360, 0.11);

function updateParticles(t) {
  dirt.begin(); stones.begin(); drops.begin();
  // excavación: escombros que salen despedidos del frente de la zanja
  if (t > T_DIG && t < T_DIG + T_DIG_DUR + 0.6) {
    const fx = digFront(t);
    for (let k = 0; k < 26; k++) {
      const ph = ((t * 1.7 + k / 26) % 1), s = hash(k * 9.1);
      const x = fx + (s - 0.5) * 1.6 + ph * 1.2, y = H0(fx) * 0.6 + 4 * ph * (1 - ph) * 3.2, z = -0.2 - s * 1.0 + (hash(k) - 0.5) * 0.6;
      dirt.add(x, Math.max(y, -0.3), z - 1.1, 1.1 - ph * 0.5, ph * 6);
    }
  }
  // derrumbes: rocas que resbalan por las paredes de la zanja
  if (t > T_SLIDE && t < T_FLOOD + 6) {
    for (let k = 0; k < 44; k++) {
      const cyc = 2.2 + hash(k) * 1.2, ph = (((t - T_SLIDE) / cyc) + hash(k * 2.1)) % 1;
      const x = -8 + hash(k * 3.7) * 15.5, y0 = Math.max(H0(x), 1.2) + 0.1, z = -1.6 + (hash(k * 5.3)) * 1.5;
      stones.add(x + ph * 0.5, lerp(y0, TRENCH_FLOOR + 0.2, ph * ph), z - 0.1, 0.8 + hash(k) * 0.9, ph * 8);
    }
  }
  // río Chagres: gotas que bajan por la ladera hacia la zanja
  if (t > T_FLOOD && t < T_PLAN + 1.0) {
    for (let k = 0; k < 90; k++) {
      const ph = ((t - T_FLOOD) * 0.9 + k / 90) % 1, s = hash(k * 1.9);
      const x = -3.5 + (s - 0.5) * 0.9, z = lerp(-3.0, -1.2, ph), y = lerp(2.0, 0.9, ph) + 0.12 * Math.sin(ph * 20 + k);
      drops.add(x, y, z, 1.2, k);
    }
  }
  // presa: el río alimenta el lago desde atrás
  if (t > T_DAM && t < T_LAKE + 4) {
    for (let k = 0; k < 70; k++) {
      const ph = ((t - T_DAM) * 0.8 + k / 70) % 1, s = hash(k * 2.7);
      drops.add(-4.5 + (s - 0.5) * 0.8, lerp(2.6, LAKE.level, ph * ph), lerp(-3, -1.0, ph), 1.2, k);
    }
  }
  // llenado por gravedad: agua por el conducto del lago a la cámara que se llena
  const fillWin = [[T_FILL, 3.0, 0], [T_UP2 + 0.8, 2.4, 1], [T_UP3 + 0.8, 2.4, 2]];
  for (const [t0, d, k] of fillWin) {
    if (t > t0 && t < t0 + d + 0.4) {
      const xa = LAKE.x0 - 0.2, xb = (LOCK_L.gates[k] + LOCK_L.gates[k + 1]) / 2;
      for (let q = 0; q < 34; q++) {
        const ph = ((t - t0) * 1.4 + q / 34) % 1;
        drops.add(lerp(xa, xb, ph), -1.35 + 0.04 * Math.sin(q), -0.4 + (hash(q) - 0.5) * 0.18, 1.3, q);
      }
      // chorro que sube a la cámara
      for (let q = 0; q < 16; q++) {
        const ph = ((t - t0) * 2.0 + q / 16) % 1, floor = LOCK_L.floors[k];
        drops.add(xb + (hash(q * 3) - 0.5) * 0.4, lerp(-1.35, floor + 0.3 + ph * 0.6, ph), -0.4 + (hash(q * 7) - 0.5) * 0.2, 1.2, q);
      }
    }
  }
  dirt.end(); stones.end(); drops.end();
}

// ---------------------------------------------------------------- flechas rojas (fuerzas)
const arrows = [];
function makeArrow() {
  const g = new THREE.Group();
  const m = new THREE.MeshStandardMaterial({ color: C.red, emissive: 0x6a0f0a, flatShading: true, roughness: 0.5 });
  const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 1, 8), m); shaft.position.y = 0.5;
  const head = new THREE.Mesh(new THREE.ConeGeometry(0.2, 0.4, 8), m); head.position.y = 1.2;
  g.add(shaft, head); g.visible = false; scene.add(g); return { g, shaft, head };
}
for (let i = 0; i < 10; i++) arrows.push(makeArrow());
function setArrow(i, from, to, a) {   // de `from` a `to`; a = 0..1 (crece)
  const A = arrows[i];
  if (a <= 0.01) { A.g.visible = false; return; }
  const v = new THREE.Vector3(to[0] - from[0], to[1] - from[1], to[2] - from[2]);
  const len = v.length() * a;
  A.g.visible = true;
  A.g.position.set(...from);
  A.g.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), v.clone().normalize());
  A.shaft.scale.set(1, Math.max(0.01, len - 0.35), 1); A.shaft.position.y = (len - 0.35) / 2;
  A.head.position.y = len - 0.2;
}
function updateArrows(t) {
  for (let i = 0; i < arrows.length; i++) arrows[i].g.visible = false;
  const pulse = 0.9 + 0.1 * Math.sin(t * 6);
  // gravedad en los derrumbes
  if (t > T_SLIDE + 0.4 && t < T_FLOOD + 1.0) {
    const a = smooth(prog(t, T_SLIDE + 0.4, 0.6)) * (1 - smooth(prog(t, T_FLOOD + 0.3, 0.5)));
    setArrow(0, [-4.6, 3.3, -1.2], [-4.6, 1.2, -1.2], a * pulse);
    setArrow(1, [0.6, 4.3, -1.2], [0.6, 2.2, -1.2], a * pulse);
    setArrow(2, [4.4, 6.3, -1.8], [4.4, 4.3, -1.8], a * pulse);
  }
  // presión del agua del río sobre la zanja
  if (t > T_FLOOD + 0.8 && t < T_PLAN + 0.6) {
    const a = smooth(prog(t, T_FLOOD + 0.8, 0.6)) * (1 - smooth(prog(t, T_PLAN, 0.5)));
    setArrow(3, [-3.5, 1.2, -3.3], [-3.5, 1.0, -1.6], a * pulse);
    setArrow(4, [-5.5, 1.1, -3.3], [-5.5, 0.9, -1.6], a * pulse);
  }
  // el peso del agua del lago empuja la presa
  if (t > T_LAKE + 2.4 && t < ev('esclusas', 0.2)) {
    const a = smooth(prog(t, T_LAKE + 2.4, 0.6)) * (1 - smooth(prog(t, ev('esclusas', -0.3), 0.5)));
    setArrow(5, [-6.4, 3.0, -2.2], [-8.4, 3.0, -2.2], a * pulse);
  }
  // gravedad al llenar las cámaras (agua que baja del lago)
  const wins = [[T_FILL, 3.0], [T_UP2 + 0.8, 2.4], [T_UP3 + 0.8, 2.4]];
  wins.forEach(([t0, d], k) => {
    const a = smooth(prog(t, t0, 0.5)) * (1 - smooth(prog(t, t0 + d - 0.2, 0.5)));
    if (a > 0) setArrow(6 + k, [LAKE.x0 + 0.2, 3.4, -1.0], [LAKE.x0 + 0.2, 2.1, -1.0], a * pulse);
  });
}

// ---------------------------------------------------------------- árboles, nubes
const trees = [];
for (let i = 0; i < N; i += 2) {
  const x = colX(i);
  if (hash(i * 4.4) < 0.28) continue;
  const g = new THREE.Group();
  const s = 0.6 + hash(i) * 0.5;
  const trunk = box(0.12 * s, 0.42 * s, 0.12 * s, mat(C.trunk)); trunk.position.y = 0.21 * s;
  const c1 = new THREE.Mesh(new THREE.ConeGeometry(0.42 * s, 0.9 * s, 6), mat(hash(i * 2) > 0.5 ? C.leaf : C.leaf2)); c1.position.y = 0.8 * s; c1.castShadow = true;
  const c2 = new THREE.Mesh(new THREE.ConeGeometry(0.32 * s, 0.7 * s, 6), mat(C.leaf2)); c2.position.y = 1.25 * s; c2.castShadow = true;
  g.add(trunk, c1, c2); g.userData = { i, x, z: -1.9 - hash(i * 3) * 0.9 }; scene.add(g); trees.push(g);
}
function updateTrees(t) {
  for (const g of trees) {
    const { i, x, z } = g.userData;
    const B = heights(i, t)[1];
    const concrete = B > 3.3, flooded = B < lakeLevelAt(x, t) - 0.05;
    g.visible = !concrete && B > 0.5 && !flooded && !(inR(x, -14, 14.5) && B < 0.9);
    g.position.set(x, B, z);
    g.scale.setScalar(smooth(prog(t, 0.2, 1.0)));
  }
}
function lakeLevelAt(x, t) { return (inR(x, LAKE.x0, LAKE.x1) && t > T_DAM) ? lerp(0.2, LAKE.level, smooth(prog(t, T_LAKE, 3.2))) : -9; }
const clouds = [];
for (let k = 0; k < 5; k++) {
  const g = new THREE.Group();
  for (let q = 0; q < 4; q++) { const s = new THREE.Mesh(new THREE.IcosahedronGeometry(0.55 + hash(k * 5 + q) * 0.45, 0), new THREE.MeshStandardMaterial({ color: 0xffffff, flatShading: true, roughness: 1, transparent: true, opacity: 0.95 })); s.position.set(q * 0.7 - 1, hash(q + k) * 0.3, hash(q * 3 + k) * 0.4); g.add(s); }
  g.userData = { x0: -22 + k * 9.5, y: 9 + hash(k) * 2.6, z: -2 - hash(k * 2) * 3, v: 0.12 + hash(k * 7) * 0.12 };
  scene.add(g); clouds.push(g);
}
function updateClouds(t) { for (const g of clouds) { const u = g.userData; g.position.set(((u.x0 + t * u.v + 30) % 60) - 30, u.y, u.z); } }

// ---------------------------------------------------------------- barco
const ship = new THREE.Group();
{
  const hull = box(1.6, 0.24, 0.6, mat(C.hull)); hull.position.y = 0.12; ship.add(hull);
  const cab = box(0.42, 0.34, 0.5, mat(C.cabin)); cab.position.set(-0.55, 0.41, 0); ship.add(cab);
  const st = box(0.12, 0.24, 0.12, mat(C.yellow)); st.position.set(-0.55, 0.7, 0); ship.add(st);
  const colors = [0xffd21f, 0xffffff, 0xf59d2a, 0x4dc3ff, 0xffd21f];
  for (let q = 0; q < 5; q++) { const c = box(0.22, 0.2, 0.46, mat(colors[q])); c.position.set(-0.05 + q * 0.24, 0.34, 0); ship.add(c); }
  const bow = new THREE.Mesh(new THREE.ConeGeometry(0.3, 0.4, 4), mat(C.hull)); bow.rotation.z = -Math.PI / 2; bow.position.set(0.95, 0.12, 0); bow.rotation.x = Math.PI / 4; ship.add(bow);
  ship.traverse((o) => { o.castShadow = true; });
}
ship.position.z = -0.75; scene.add(ship);
const shipKeys = () => {
  const cL = (k) => (LOCK_L.gates[k] + LOCK_L.gates[k + 1]) / 2;
  const cR = (k) => (LOCK_R.gates[k] + LOCK_R.gates[k + 1]) / 2;
  const st = rightSchedule();
  return [
    [0, -16.5], [T_DIG, -16.5], [ev('barco'), -16.5], [ev('barco', 4.2), -1.5], [ev('derrumbe', -0.2), -1.5],
    // plan final: entra a las esclusas
    [T_LOCKS - 0.1, -16.5], [T_LOCKS + 2.0, cL(0)], [T_UP2 + 0.8, cL(0)], [T_UP2 + 2.5, cL(1)], [T_UP3 + 0.8, cL(1)], [T_UP3 + 2.5, cL(2)],
    [T_UP3 + 3.5, cL(2)], [T_UP3 + 5.2, -6.0], [T_CROSS, -6.0], [T_CROSS + 2.4, 8.2], [st[0] - 0.2, 8.2], [st[0] + 1.2, cR(0)], [st[1] - 0.2, cR(0)],
    [st[1] + 1.2, cR(1)], [st[2] - 0.2, cR(1)], [st[2] + 1.2, cR(2)], [st[2] + 1.6, cR(2)], [st[2] + 3.2, 16.0],
  ];
};
const SK = shipKeys();
function shipX(t) {
  for (let i = 0; i < SK.length - 1; i++) {
    if (t >= SK[i][0] && t < SK[i + 1][0]) { const u = (t - SK[i][0]) / Math.max(1e-6, SK[i + 1][0] - SK[i][0]); return lerp(SK[i][1], SK[i + 1][1], smooth(u)); }
  }
  return t < SK[0][0] ? SK[0][1] : SK[SK.length - 1][1];
}
function updateShip(t) {
  const x = shipX(t);
  let vis = true;
  if (t < T_DIG) vis = true;
  // durante la zanja: nivel del mar; después del plan 1, el barco desaparece hasta el plan final
  const inPlan1 = t >= ev('barco') && t < ev('derrumbe', 0.6);
  const gap = t >= ev('derrumbe', 0.6) && t < T_LOCKS - 0.4;
  vis = !gap;
  const y = (inPlan1 || t < T_DIG + T_DIG_DUR) ? 0 : surfaceAt(x, t);
  ship.visible = vis;
  const bob = Math.sin(t * 2.1) * 0.015;
  ship.position.set(x, y + 0.01 + bob, -0.75);
}

// ---------------------------------------------------------------- torre de agua con casa (momento cotidiano)
const house = new THREE.Group();
{
  const slab = box(3.4, 0.3, 2.2, mat(C.soil)); slab.position.y = -0.15; house.add(slab);
  const gr = box(3.4, 0.08, 2.2, mat(C.grass)); gr.position.y = 0.04; house.add(gr);
  const body = box(1.3, 0.95, 1.2, mat(0xf3ece0)); body.position.set(0.8, 0.55, 0); house.add(body);
  const roof = box(1.45, 0.12, 1.35, mat(0x8a97ab)); roof.position.set(0.8, 1.08, 0); house.add(roof);
  const door = box(0.26, 0.5, 0.05, mat(0x6b4423)); door.position.set(0.8, 0.33, 0.61); house.add(door);
  // torre: cuatro patas y un tanque en lo alto
  for (const [dx, dz] of [[-0.18, -0.18], [0.18, -0.18], [-0.18, 0.18], [0.18, 0.18]]) { const l = box(0.06, 1.9, 0.06, mat(0x8a97ab)); l.position.set(-0.95 + dx, 0.95, dz); house.add(l); }
  const plat = box(0.62, 0.06, 0.62, mat(0x8a97ab)); plat.position.set(-0.95, 1.9, 0); house.add(plat);
  const tank = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.62, 10), mat(0x1e8ee8)); tank.position.set(-0.95, 2.24, 0); tank.castShadow = true; house.add(tank);
  const cap = new THREE.Mesh(new THREE.ConeGeometry(0.46, 0.24, 10), mat(0x8a97ab)); cap.position.set(-0.95, 2.67, 0); house.add(cap);
  const pp = box(0.07, 1.8, 0.07, mat(0xdfe4ee)); pp.position.set(-0.95, 0.98, 0.0); house.add(pp);
  const tap = box(0.34, 0.07, 0.07, mat(0xdfe4ee)); tap.position.set(-0.8, 0.22, 0.0); house.add(tap);
}
house.position.set(-10.9, -0.95, 2.2); house.visible = false; scene.add(house);
const houseWater = new Pool(C.water, 90, 0.07);
function updateHouse(t) {
  const t0 = ev('tanque'), t1 = Math.min(ev('tanque', 8.0), T_CROSS - 0.3);
  const s = smooth(prog(t, t0 - 0.3, 0.6)) * (1 - smooth(prog(t, t1, 0.6)));
  house.visible = s > 0.02; house.scale.setScalar(Math.max(0.001, s));
  houseWater.begin();
  if (s > 0.5) {
    const hp = house.position;
    for (let k = 0; k < 40; k++) {                 // el agua baja por el tubo vertical, por gravedad
      const ph = ((t - t0) * 1.2 + k / 40) % 1;
      houseWater.add(hp.x - 0.95 * s, hp.y + lerp(2.0, 0.24, ph) * s, hp.z, 1.0, k);
    }
    for (let k = 0; k < 18; k++) {                 // y sale por la llave
      const ph = ((t - t0) * 1.8 + k / 18) % 1;
      houseWater.add(hp.x + (-0.62 + 0.35 * ph) * s, hp.y + (0.2 - 0.3 * ph * ph) * s, hp.z, 1.0, k);
    }
  }
  houseWater.end();
  const a = smooth(prog(t, t0 + 0.8, 0.6)) * (1 - smooth(prog(t, t1 - 0.3, 0.5)));
  if (a > 0) setArrow(9, [house.position.x - 0.45, house.position.y + 2.0, house.position.z + 0.5], [house.position.x - 0.45, house.position.y + 0.9, house.position.z + 0.5], a * (0.9 + 0.1 * Math.sin(t * 6)));
}

// ---------------------------------------------------------------- cámara en diagonal, lenta
// Cada clave: objetivo, giro (yaw, grados desde el frente hacia la izquierda), elevación y distancia.
function camKeys() {
  const K = [];
  const add = (t, tgt, yaw, el, D) => K.push({ t, tgt, yaw, el, D });
  add(0, [-3, 1.0, -1.4], 64, 24, 47);
  add(ev('excavar', -0.4), [-6, 0.6, -1.2], 52, 24, 30);
  add(ev('excavar', 4.0), [0, 0.5, -1.2], 46, 25, 26);
  add(ev('derrumbe', -0.5), [-4.5, 0.8, -1.2], 40, 24, 21);
  add(ev('inunda', 1), [-3.5, 0.6, -1.2], 38, 24, 20);
  add(ev('plan', -0.2), [-3, 1.2, -1.2], 44, 25, 30);
  add(ev('presa', 0.2), [-6.5, 1.8, -1.2], 40, 24, 21);
  add(ev('m26', 1.0), [-8, 1.8, -1.0], 36, 22, 19);
  add(ev('esclusas', 0.5), [-10.9, 1.3, -0.8], 32, 24, 21);
  add(T_UP3 + 3.0, [-10.2, 1.5, -0.8], 34, 24, 21);
  add(ev('termino', 0.3), [-10.5, 1.4, -0.8], 34, 24, 21);
  add(ev('tanque', -0.2), [-10.2, 0.9, 0.6], 28, 19, 15.5);
  add(ev('tanque', 7.5), [-8.5, 1.6, -0.9], 38, 23, 19);
  add(T_CROSS, [-3, 1.6, -1.1], 42, 24, 27);
  add(T_CROSS + 2.8, [9.5, 1.3, -1.0], 36, 22, 17);
  add(rightSchedule()[2] + 1.5, [11.8, 0.8, -0.9], 34, 22, 16);
  add(ev('cierre'), [1, 1.2, -1.3], 55, 26, 44);
  add(TL.duracion, [1, 1.2, -1.3], 62, 28, 50);
  K.sort((a, b) => a.t - b.t);
  return K;
}
const CK = camKeys();
function updateCamera(t) {
  let i = 0;
  while (i < CK.length - 2 && t >= CK[i + 1].t) i++;
  const a = CK[i], b = CK[Math.min(i + 1, CK.length - 1)];
  const u = smooth((t - a.t) / Math.max(1e-6, b.t - a.t));
  const tgt = a.tgt.map((v, k) => lerp(v, b.tgt[k], u));
  const yaw = (lerp(a.yaw, b.yaw, u) + Math.sin(t * 0.3) * 2.0) * Math.PI / 180;     // deriva lenta
  const el = lerp(a.el, b.el, u) * Math.PI / 180, D = lerp(a.D, b.D, u);
  camera.position.set(tgt[0] - D * Math.sin(yaw) * Math.cos(el), tgt[1] + D * Math.sin(el), tgt[2] + D * Math.cos(yaw) * Math.cos(el));
  camera.lookAt(tgt[0], tgt[1], tgt[2]);
}

// ---------------------------------------------------------------- etiqueta «26 m» y subtítulos palabra por palabra
const lbl = document.getElementById('lbl26');
function updateLabel(t) {
  const t0 = ev('m26'), t1 = ev('entra', 0.5);
  const on = t >= t0 && t < t1;
  lbl.style.display = on ? 'block' : 'none';
  if (!on) return;
  const v = new THREE.Vector3(-3.0, LAKE.level + 0.9, -1.0).project(camera);
  const s = smooth(prog(t, t0, 0.4));
  lbl.style.left = ((v.x * 0.5 + 0.5) * W) + 'px';
  lbl.style.top = ((-v.y * 0.5 + 0.5) * H - 140) + 'px';
  lbl.style.opacity = s; lbl.style.transform = `translate(-50%,-50%) scale(${0.6 + 0.4 * s})`;
}
const subEl = document.getElementById('sub');
function updateSub(t) {
  const P = TL.palabras;
  let cur = null;
  for (let i = 0; i < P.length; i++) { if (t >= P[i].ini && (i === P.length - 1 || t < P[i + 1].ini)) { cur = P[i]; if (t > P[i].fin + 0.45) cur = null; break; } }
  if (!cur) { subEl.textContent = ''; subEl.className = ''; return; }
  subEl.textContent = cur.termino ? cur.w.toUpperCase() : cur.w;
  subEl.className = cur.termino ? 'term' : '';
  const L = cur.w.length;
  subEl.style.fontSize = (L > 11 ? 112 : L > 8 ? 130 : 150) + 'px';
}

// ---------------------------------------------------------------- fotograma
window.renderFrame = (t) => {
  updateTerrain(t); updateWater(t); updateGates(t); updateParticles(t); updateArrows(t);
  updateTrees(t); updateClouds(t); updateShip(t); updateHouse(t); updateCamera(t); updateLabel(t); updateSub(t);
  renderer.render(scene, camera);
  return true;
};
window.__listo = true;

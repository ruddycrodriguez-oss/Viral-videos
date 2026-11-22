// Guarda fotogramas sueltos para revisar la escena: node fotograma.js <carpeta> t1 t2 ...
const { chromium } = require('playwright');
const { iniciar } = require('./servir.js');
(async () => {
  const [out, ...ts] = process.argv.slice(2);
  const { server, port } = await iniciar();
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--enable-webgl'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', (e) => console.log('ERROR PAGINA:', e.message));
  p.on('console', (m) => { if (['error', 'warning'].includes(m.type())) console.log('CONSOLA:', m.text().slice(0, 200)); });
  await p.goto(`http://127.0.0.1:${port}/escena.html`);
  await p.waitForFunction('window.__listo === true', null, { timeout: 60000 });
  for (const t of ts) {
    const t0 = Date.now();
    await p.evaluate((x) => window.renderFrame(x), parseFloat(t));
    await p.screenshot({ path: `${out}/f_${String(parseFloat(t).toFixed(1)).padStart(5, '0')}.png` });
    console.log('t=' + t, (Date.now() - t0) + ' ms');
  }
  await b.close(); server.close();
})();

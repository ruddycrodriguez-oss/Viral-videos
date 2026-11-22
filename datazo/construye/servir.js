// Servidor estático mínimo para la escena (los módulos ES no se cargan desde file://).
const http = require('http'), fs = require('fs'), path = require('path');
const root = __dirname, types = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.json': 'application/json', '.css': 'text/css' };
function iniciar(port = 0) {
  return new Promise((res) => {
    const s = http.createServer((req, rsp) => {
      const p = path.join(root, decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '') || 'escena.html');
      if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { rsp.writeHead(404); return rsp.end('no'); }
      rsp.writeHead(200, { 'Content-Type': types[path.extname(p)] || 'application/octet-stream', 'Cache-Control': 'no-store' }); fs.createReadStream(p).pipe(rsp);
    }).listen(port, '127.0.0.1', () => res({ server: s, port: s.address().port }));
  });
}
module.exports = { iniciar };
if (require.main === module) iniciar(8123).then(({ port }) => console.log('http://127.0.0.1:' + port));

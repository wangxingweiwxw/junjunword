// node tools/shots.cjs ep01 out_dir [WxH] t1 t2 ...  -> screenshots at given lesson times
// WxH given (e.g. 390x844) -> live page layout; otherwise 1280x720 capture layout.
const {chromium} = require('playwright');
(async () => {
  let [ep, out, ...ts] = process.argv.slice(2);
  let vw = 1280, vh = 720, live = false;
  if (/^\d+x\d+$/.test(ts[0])) { [vw, vh] = ts.shift().split('x').map(Number); live = true; }
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: vw, height: vh}, deviceScaleFactor: live ? 2 : 1});
  p.on('pageerror', e => console.log('PAGEERROR', e.message));
  p.on('console', m => m.type() === 'error' && console.log('CONSOLE', m.text()));
  await p.goto(`http://127.0.0.1:8765/${ep}/index.html?capture${live ? '&layout=auto' : ''}`);
  await p.waitForFunction(() => window.__vp && window.__vp.ready);
  if (live) await p.evaluate(() => { document.body.classList.remove('capture'); window.__vp.layout(); });
  for (const t of ts) {
    await p.evaluate(t => window.__vp.render(t), +t);
    await p.screenshot({path: `${out}/s_${live ? vw + '_' : ''}${t}.png`});
  }
  await b.close();
})();

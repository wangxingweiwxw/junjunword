// node tools/capture.cjs ep01 [fps]  -> <ep>/<ep>.mp4 (1280x720, H.264 + AAC)
// Renders every frame from the deterministic render(t) and pipes JPEGs into x264,
// then muxes the lesson audio. Video-only encode first, then a stream-copy mux
// (keeps memory low on this 2 GB host).
const {chromium} = require('playwright');
const {spawn, execFileSync} = require('child_process');
const path = require('path');
(async () => {
  const ep = process.argv[2] || 'ep01', fps = +(process.argv[3] || 30);
  const root = path.resolve(__dirname, '..'), ff = path.join(__dirname, 'ffmpeg');
  const vid = path.join(root, ep, `${ep}.video.mp4`), out = path.join(root, ep, `${ep}.mp4`);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1280, height: 720}});
  p.on('pageerror', e => console.log('PAGEERROR', e.message));
  await p.goto(`http://127.0.0.1:8765/${ep}/index.html?capture`);
  await p.waitForFunction(() => window.__vp && window.__vp.ready);
  const dur = await p.evaluate(() => window.__vp.duration), n = Math.ceil(dur * fps);
  const enc = spawn(ff, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-tune', 'animation', '-pix_fmt', 'yuv420p',
    '-threads', '2', '-x264-params', 'rc-lookahead=20:lookahead-threads=1', '-g', String(fps * 4),
    '-movflags', '+faststart', vid], {stdio: ['pipe', 'inherit', 'inherit']});
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    await p.evaluate(t => window.__vp.render(t), i / fps);
    const jpg = await p.screenshot({type: 'jpeg', quality: 92});
    if (!enc.stdin.write(jpg)) await new Promise(r => enc.stdin.once('drain', r));
    if (i % 300 === 0) console.log(`frame ${i}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  }
  enc.stdin.end();
  await new Promise((res, rej) => enc.on('close', c => c ? rej(new Error('x264 exit ' + c)) : res()));
  await b.close();
  execFileSync(ff, ['-y', '-loglevel', 'error', '-i', vid, '-i', path.join(root, ep, 'audio', 'lesson.mp3'),
    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '64k', '-ac', '1',
    '-shortest', '-movflags', '+faststart', out]);
  require('fs').unlinkSync(vid);
  console.log('done', out);
})();

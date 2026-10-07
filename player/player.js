/* Vocabulary lesson player. One engine for every episode:
   <ep>/lesson.json (words, layout, script) + <ep>/timeline.json (from tools/tts.py)
   + <ep>/audio/lesson.mp3 + <ep>/audio/words.mp3.
   Everything on screen is a pure function of the audio clock (render(t)), so the
   same page plays live and can be captured frame-by-frame into an MP4 (?capture). */
(async function () {
  const root = document.getElementById('lesson');
  const base = (root.dataset.src || '.').replace(/\/$/, '') + '/';
  const qs = new URLSearchParams(location.search);
  const capture = qs.has('capture'), autoLayout = !capture || qs.get('layout') === 'auto';
  if (capture) document.body.classList.add('capture');

  const [L, T] = await Promise.all(['lesson.json', 'timeline.json'].map(f => fetch(base + f).then(r => r.json())));
  const byId = Object.fromEntries(L.nodes.map(n => [n.id, n]));

  // ---------- events derived from cues ----------
  const showT = {}, edgeT = {}, pluralT = {}, altT = {}, focusEv = [];
  let mapT = Infinity;
  for (const p of T.parts) for (const c of p.cue) {
    const [k, v] = c.split(':');
    if (k === 'map') mapT = Math.min(mapT, p.t0);
    else if (k === 'show') showT[v] ??= p.t0;
    else if (k === 'edge') edgeT[v] ??= p.t0;
    else if (k === 'plural') pluralT[v] ??= p.t0;
    else if (k === 'alt') altT[v] ??= p.t0;
    else if (k === 'focus') focusEv.push({t: p.t0, ids: v === 'none' ? [] : v.split(',')});
  }
  let line = -1;
  T.parts.forEach((p, i) => {
    if (i === 0 || p.lang === 'zh' || p.seg !== T.parts[i - 1].seg) line++;
    p.line = line;
  });
  const segStart = [...new Set(T.parts.map(p => p.seg))].map(s => T.parts.find(p => p.seg === s).t0);

  // ---------- DOM ----------
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const wrap = el('div', 'vp'), area = el('div', 'vp-area'), stage = el('div', 'vp-stage');
  const sub = el('div', 'vp-sub'), bar = el('div', 'vp-bar');
  const svgNS = 'http://www.w3.org/2000/svg';
  const edgesSvg = document.createElementNS(svgNS, 'svg');
  edgesSvg.setAttribute('class', 'vp-edges');
  stage.append(edgesSvg);
  area.append(stage); wrap.append(area, sub, bar); root.replaceWith(wrap);

  const KIND = {noun: {tag: 'n.', hex: '#FF7A59', rgb: '255,122,89'},
                adj: {tag: 'adj.', hex: '#2FA36B', rgb: '47,163,107'},
                verb: {tag: 'v.', hex: '#3D8BFD', rgb: '61,139,253'},
                num: {tag: 'num.', hex: '#9B5DE5', rgb: '155,93,229'},
                prep: {tag: 'prep.', hex: '#E0A100', rgb: '224,161,0'}};
  const kindOf = n => KIND[n.kind] ? n.kind : 'noun';
  const colorOf = n => `var(--${kindOf(n)})`;
  const hex = Object.fromEntries(Object.entries(KIND).map(([k, v]) => [k, v.hex]));
  edgesSvg.innerHTML = '<defs>' + Object.entries(hex).map(([k, c]) =>
    `<marker id="vp-ah-${k}" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto">
       <path d="M0 0L10 5L0 10z" fill="${c}"/></marker>`).join('') + '</defs>';

  function pluralHTML(a, b) {           // highlight the letters that changed: man->m<b>e</b>n
    let p = 0; while (p < a.length && p < b.length && a[p] === b[p]) p++;
    let s = 0; while (s < a.length - p && s < b.length - p && a[a.length - 1 - s] === b[b.length - 1 - s]) s++;
    return b.slice(0, p) + '<b>' + b.slice(p, b.length - s) + '</b>' + b.slice(b.length - s);
  }

  const cards = {};
  for (const n of L.nodes) {
    const c = el('div', 'vp-node ' + kindOf(n));
    c.innerHTML = `<span class="vp-pos">${KIND[kindOf(n)].tag}</span>
      <div class="vp-icon"></div><div class="vp-word"></div><div class="vp-ipa"></div><div class="vp-zh">${n.zh}</div>`
      + (n.alt ? `<div class="vp-alt">${n.altLabel ?? '也叫'} <b>${n.alt}</b></div>` : '');
    c.addEventListener('click', () => sayWord(n));
    stage.append(c);
    cards[n.id] = {n, c, icon: c.querySelector('.vp-icon'), word: c.querySelector('.vp-word'),
                   ipa: c.querySelector('.vp-ipa'), alt: c.querySelector('.vp-alt'), pl: null};
  }
  function setForm(k, plural) {
    const n = k.n; k.pl = plural;
    const w = plural ? n.plural : n.word;
    k.word.innerHTML = plural ? pluralHTML(n.word, n.plural) : n.word;
    let fs = w.length <= 6 ? 44 : w.length === 7 ? 41 : w.length === 8 ? 38 : 34;   // then shrink until it fits
    do k.word.style.fontSize = fs + 'px'; while (k.word.scrollWidth > k.word.clientWidth + 1 && (fs -= 2) > 24);
    k.ipa.textContent = plural ? n.pluralIpa : n.ipa;
    k.icon.innerHTML = plural && n.pluralIcon ? VP_ICONS.svg(n.pluralIcon) : VP_ICONS.svg(n.icon, plural);
  }
  for (const id in cards) setForm(cards[id], false);

  const edges = L.edges.map(e => {
    const line = document.createElementNS(svgNS, 'line');
    const kind = kindOf(byId[e.from]);
    line.setAttribute('stroke', hex[kind]);
    line.setAttribute('marker-end', `url(#vp-ah-${kind})`);
    if (e.dashed) line.setAttribute('stroke-dasharray', '2 12');
    edgesSvg.append(line);
    let label = null;
    if (e.label) { label = el('div', 'vp-label', e.label); label.style.color = colorOf(byId[e.from]); stage.append(label); }
    return {...e, key: e.from + '>' + e.to, line, label};
  });

  const title = el('div', 'vp-title', `<div class="ep">${L.episode || ''}</div>
    <div class="art">${VP_ICONS.svg(L.titleIcon || 'group')}</div>
    <div class="w">${[...L.title].map(ch => `<span>${ch}</span>`).join('')}</div><div class="z">${L.titleZh}</div>`);
  if (!L.episode) title.querySelector('.ep').remove();
  stage.append(title);

  let now = () => 0;   // audio clock; replaced once playback is wired up

  // ---------- layout (landscape / portrait) ----------
  let orient = null, W = 0, H = 0, geo = {};
  function layout() {
    const aw = area.clientWidth, ah = area.clientHeight;
    const o = (autoLayout && L.stage.portrait && aw / ah < 0.95) ? 'portrait' : 'landscape';
    if (o !== orient) {
      orient = o; [W, H] = L.stage[o];
      stage.style.width = W + 'px'; stage.style.height = H + 'px';
      edgesSvg.setAttribute('viewBox', `0 0 ${W} ${H}`);
      for (const id in cards) {
        const {n, c} = cards[id], [x, y] = (o === 'portrait' && n.atP) || n.at;
        geo[id] = {x, y, w: c.offsetWidth, h: c.offsetHeight};
      }
      for (const e of edges) {
        const a = geo[e.from], b = geo[e.to], dx = b.x - a.x, dy = b.y - a.y;
        const cut = (g, pad) => Math.min((g.w / 2 + pad) / Math.abs(dx || 1e-9), (g.h / 2 + pad) / Math.abs(dy || 1e-9));
        const ta = cut(a, 6), tb = cut(b, 16);
        e.p0 = [a.x + dx * ta, a.y + dy * ta]; e.p1 = [b.x - dx * tb, b.y - dy * tb];
        if (e.label) {                   // sit beside the line (above / to the right), not on it
          const len = Math.hypot(dx, dy); let nx = dy / len, ny = -dx / len;
          if (ny > 0.01 || (Math.abs(ny) <= 0.01 && nx < 0)) { nx = -nx; ny = -ny; }
          const off = 24 + 10 * Math.abs(nx);
          e.label.style.left = (e.p0[0] + e.p1[0]) / 2 + nx * off + 'px';
          e.label.style.top = (e.p0[1] + e.p1[1]) / 2 + ny * off + 'px';
        }
      }
    }
    const s = Math.min(aw / W, ah / H);
    stage.style.transform = `translate(${(aw - W * s) / 2}px, ${(ah - H * s) / 2}px) scale(${s})`;
    render(now());
  }

  // ---------- render(t) ----------
  const clamp = x => Math.max(0, Math.min(1, x));
  const ease = x => 1 - Math.pow(1 - clamp(x), 3);
  const back = x => { x = clamp(x); const c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
  let curSeg = -1;

  function render(t) {
    // title card
    const tOut = ease((t - mapT) / 0.6);
    title.style.opacity = 1 - tOut;
    title.style.transform = `scale(${1 - 0.1 * tOut})`;
    title.style.visibility = tOut >= 1 ? 'hidden' : 'visible';
    title.querySelectorAll('.w span').forEach((s, i) => {
      const k = back((t - 0.5 - i * 0.08) / 0.5);
      s.style.transform = `translateY(${(1 - k) * 60}px)`; s.style.opacity = clamp((t - 0.5 - i * 0.08) / 0.25);
    });

    // focus: the latest focus event, faded in over 0.3s
    let fe = null; for (const f of focusEv) if (f.t <= t) fe = f;
    const fset = fe ? fe.ids : [], fk = fe ? ease((t - fe.t) / 0.3) : 0;

    for (const id in cards) {
      const k = cards[id], g = geo[id], a = (t - (showT[id] ?? Infinity)) / 0.6;
      const vis = clamp(a), sc = 0.4 + 0.6 * back(a);
      const plural = t >= (pluralT[id] ?? Infinity);
      if (k.pl !== plural) setForm(k, plural);   // swap word / icon only when state changes
      const pop = plural ? Math.sin(Math.PI * clamp((t - pluralT[id]) / 0.45)) * 0.12 : 0;
      const on = fset.includes(id) ? fk : 0;
      const dim = fset.length && !fset.includes(id) ? 0.3 * fk : 0;
      const bob = on * 0.025 * Math.sin(t * 5);
      const s = sc * (1 + 0.1 * on + bob + pop);
      const col = KIND[kindOf(k.n)].rgb;
      if (k.alt) {
        const ak = (t - (altT[id] ?? Infinity)) / 0.5;
        k.alt.style.opacity = clamp(ak * 2);
        k.alt.style.transform = `translateX(-50%) scale(${0.3 + 0.7 * back(ak)})`;
      }
      k.c.style.opacity = vis * (1 - dim);
      k.c.style.visibility = vis > 0 ? 'visible' : 'hidden';
      k.c.style.transform = `translate(${g.x - g.w / 2}px, ${g.y - g.h / 2}px) scale(${s})`;
      k.c.style.borderColor = on > 0.01 ? `rgba(${col},${on})` : '';
      k.c.style.boxShadow = `0 0 0 ${8 * on}px rgba(${col},${0.22 * on}), 0 ${6 + 10 * on}px ${18 + 14 * on}px rgba(43,45,66,${0.1 + 0.08 * on})`;
      k.c.style.zIndex = on > 0 ? 3 : 2;
    }

    for (const e of edges) {
      const p = ease((t - (edgeT[e.key] ?? Infinity)) / 0.6);
      const x1 = e.p0[0] + (e.p1[0] - e.p0[0]) * p, y1 = e.p0[1] + (e.p1[1] - e.p0[1]) * p;
      e.line.setAttribute('x1', e.p0[0]); e.line.setAttribute('y1', e.p0[1]);
      e.line.setAttribute('x2', x1); e.line.setAttribute('y2', y1);
      e.line.style.opacity = p > 0.02 ? 1 : 0;
      const dim = fset.length && !(fset.includes(e.from) || fset.includes(e.to)) ? 0.55 * fk : 0;
      e.line.style.strokeOpacity = 1 - dim;
      if (e.label) e.label.style.opacity = clamp((t - (edgeT[e.key] ?? Infinity) - 0.4) / 0.3) * (1 - dim);
    }

    // subtitles: the whole sentence group, current part highlighted
    let pi = -1; for (let i = 0; i < T.parts.length; i++) if (T.parts[i].t0 <= t + 0.05) pi = i;
    const seg = pi < 0 ? -1 : T.parts[pi].line;
    if (seg !== curSeg) {
      curSeg = seg;
      sub.innerHTML = seg < 0 ? '' : '<div>' + T.parts.map((p, i) => p.line === seg
        ? `<span class="p ${p.lang}" data-i="${i}">${p.text}</span>` : '').join(' ') + '</div>';
    }
    sub.querySelectorAll('.p').forEach(s => s.classList.toggle('on', +s.dataset.i <= pi));
  }

  // ---------- capture hook ----------
  if (capture) {
    window.__vp = {duration: T.duration, render: t => render(t), layout: () => { orient = null; layout(); }};
    await document.fonts.ready;
    layout(); window.__vp.ready = true;
    return;
  }

  // ---------- playback ----------
  const audio = new Audio(base + 'audio/lesson.mp3'); audio.preload = 'auto';
  const words = new Audio(base + 'audio/words.mp3'); words.preload = 'auto';
  now = () => audio.currentTime;
  const fmt = s => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

  const ico = d => `<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="${d}"/></svg>`;
  const I = {play: ico('M7 4.5v15l12-7.5z'), pause: ico('M6 4h4v16H6zM14 4h4v16h-4z'),
             prev: ico('M6 5h2.5v14H6zM20 5v14L9.5 12z'), next: ico('M15.5 5H18v14h-2.5zM4 5v14l10.5-7z'),
             again: ico('M12 5V2L7 6l5 4V7a5 5 0 1 1-5 5H5a7 7 0 1 0 7-7z')};
  bar.innerHTML = `<button class="play" aria-label="播放">${I.play}</button>
    <button class="ghost prev" aria-label="上一句">${I.prev}</button><button class="ghost next" aria-label="下一句">${I.next}</button>
    <input type="range" min="0" max="${T.duration}" step="0.01" value="0" aria-label="进度">
    <span class="vp-time">0:00 / ${fmt(T.duration)}</span><button class="ghost speed">1×</button>`;
  const [bPlay, bPrev, bNext] = ['.play', '.prev', '.next'].map(s => bar.querySelector(s));
  const range = bar.querySelector('input'), time = bar.querySelector('.vp-time'), bSpeed = bar.querySelector('.speed');
  const start = el('button', 'vp-start', '<span>▶ 开始学习</span>');
  area.append(start);

  const syncUI = () => {
    bPlay.innerHTML = audio.ended ? I.again : audio.paused ? I.play : I.pause;
    range.value = audio.currentTime;
    time.textContent = `${fmt(audio.currentTime)} / ${fmt(T.duration)}`;
  };
  const play = () => { start.remove(); audio.play(); };
  start.onclick = play;
  bPlay.onclick = () => audio.paused ? play() : audio.pause();
  range.oninput = () => { audio.currentTime = +range.value; render(audio.currentTime); syncUI(); };
  const jump = d => {
    const t = audio.currentTime; let i = segStart.findLastIndex(s => s <= t + 0.3);
    if (d < 0 && t - segStart[Math.max(i, 0)] < 1.5) i--;
    audio.currentTime = segStart[Math.max(0, Math.min(segStart.length - 1, i + (d > 0 ? 1 : 0)))];
    render(audio.currentTime); syncUI();
  };
  bPrev.onclick = () => jump(-1); bNext.onclick = () => jump(1);
  const speeds = [1, 0.8, 1.2];
  bSpeed.onclick = () => {
    const s = speeds[(speeds.indexOf(audio.playbackRate) + 1) % speeds.length];
    audio.playbackRate = words.playbackRate = s; bSpeed.textContent = s + '×';
  };
  audio.addEventListener('play', syncUI); audio.addEventListener('pause', syncUI);
  audio.addEventListener('ended', syncUI);
  document.addEventListener('keydown', e => {
    if (e.code === 'Space') { e.preventDefault(); bPlay.click(); }
    if (e.code === 'ArrowLeft') jump(-1); if (e.code === 'ArrowRight') jump(1);
  });

  let wordTimer = null, resume = false;
  function sayWord(n) {
    const t = audio.currentTime;
    if ((showT[n.id] ?? Infinity) > t && !audio.ended) return;    // not on screen yet
    const key = n.plural && t >= (pluralT[n.id] ?? Infinity) ? n.id + ':pl' : n.id;
    let [a, b] = T.words[key];
    if (key === n.id && n.alt && t >= (altT[n.id] ?? Infinity)) b = T.words[n.id + ':alt'][1];  // "mother … mom" 
    if (!wordTimer) resume = !audio.paused;
    audio.pause(); clearTimeout(wordTimer);
    words.currentTime = a; words.play();
    wordTimer = setTimeout(() => {
      words.pause(); wordTimer = null;
      if (resume) audio.play();
    }, (b - a) / words.playbackRate * 1000 + 120);
  }

  layout();
  new ResizeObserver(layout).observe(area);
  (function loop() { render(audio.currentTime); if (!audio.paused) syncUI(); requestAnimationFrame(loop); })();
})();

/* Original flat illustrations, drawn in code. All icons live in a 120x120 box.
   VP_ICONS.svg(name, plural) -> full <svg> string. Unknown names fall back to
   rendering the name itself as text (so a lesson can use an emoji as its icon). */
(function () {
  const INK = '#3A2E2A', BLUSH = '#F49B9B';
  const SKIN = ['#F7CFAE', '#E9B48C', '#C98F68'];

  function face(cx, hy, r, o) {
    let s = `<circle cx="${cx}" cy="${hy}" r="${r}" fill="${o.skin}"/>`;
    const ey = hy + r * 0.08, ex = r * 0.38;
    if (o.glasses) {
      s += `<g fill="none" stroke="${INK}" stroke-width="2.2">
        <circle cx="${cx - ex}" cy="${ey}" r="${r * 0.27}"/><circle cx="${cx + ex}" cy="${ey}" r="${r * 0.27}"/>
        <path d="M${cx - ex + r * 0.27} ${ey}h${2 * ex - r * 0.54}"/></g>`;
    }
    s += `<circle cx="${cx - ex}" cy="${ey}" r="${r * 0.12}" fill="${INK}"/>
          <circle cx="${cx + ex}" cy="${ey}" r="${r * 0.12}" fill="${INK}"/>
          <ellipse cx="${cx - r * 0.6}" cy="${hy + r * 0.42}" rx="${r * 0.2}" ry="${r * 0.12}" fill="${BLUSH}" opacity=".7"/>
          <ellipse cx="${cx + r * 0.6}" cy="${hy + r * 0.42}" rx="${r * 0.2}" ry="${r * 0.12}" fill="${BLUSH}" opacity=".7"/>
          <path d="M${cx - r * 0.3} ${hy + r * 0.45} Q${cx} ${hy + r * 0.75} ${cx + r * 0.3} ${hy + r * 0.45}"
                fill="none" stroke="${INK}" stroke-width="2.4" stroke-linecap="round"/>`;
    return s;
  }

  function cap(cx, hy, r, color) {  // short hair covering the top of the head
    return `<path d="M${cx - r - 1} ${hy + 2} C${cx - r - 2} ${hy - r - 9} ${cx + r + 2} ${hy - r - 9} ${cx + r + 1} ${hy + 2}
      C${cx + r - 4} ${hy - r * 0.45} ${cx + r * 0.2} ${hy - r * 0.65} ${cx - r * 0.25} ${hy - r * 0.35}
      C${cx - r * 0.5} ${hy - r * 0.2} ${cx - r + 2} ${hy - r * 0.3} ${cx - r - 1} ${hy + 2}Z" fill="${color}"/>`;
  }

  function figure(kind, o = {}) {
    const adult = kind === 'man' || kind === 'woman' || kind === 'elder';
    const cx = 60, r = adult ? 19 : 22, hy = adult ? 40 : 46;
    const skin = o.skin || SKIN[0];
    const w = adult ? 38 : 31, sy = hy + r + 3;
    const shirt = o.shirt || {boy: '#3D8BFD', girl: '#FF6FA5', man: '#2E5AAC', woman: '#9B5DE5',
                              elder: '#8D7B68', person: '#2BB3A3', child: '#FFB703'}[kind];
    const hair = o.hair || (kind === 'elder' ? '#ECECF2' : kind === 'woman' ? '#5A3825' : '#3B2A20');
    let back = '', front = '';
    if (kind === 'woman')
      back += `<rect x="${cx - r - 7}" y="${hy - r - 2}" width="${2 * r + 14}" height="${2 * r + 22}" rx="${r + 6}" fill="${hair}"/>`;
    if (kind === 'girl')
      back += [-1, 1].map(s => `<circle cx="${cx + s * (r + 7)}" cy="${hy + 3}" r="9.5" fill="${hair}"/>
        <circle cx="${cx + s * (r + 1)}" cy="${hy - 1}" r="3.6" fill="#FFD23F"/>`).join('');
    const body = `<path d="M${cx - w} 118 C${cx - w} ${sy + 14} ${cx - w * 0.6} ${sy} ${cx} ${sy}
      C${cx + w * 0.6} ${sy} ${cx + w} ${sy + 14} ${cx + w} 118Z" fill="${shirt}"/>
      <rect x="${cx - 6}" y="${hy + r - 6}" width="12" height="10" rx="4" fill="${skin}"/>`;
    if (kind === 'man')
      front += `<path d="M${cx - 9} ${sy} L${cx} ${sy + 9} L${cx + 9} ${sy}Z" fill="#fff"/>
        <path d="M${cx} ${sy + 8} l-4 6 l4 22 l4 -22z" fill="#E63946"/>`;
    if (kind === 'woman')
      front += `<path d="M${cx - 8} ${sy} L${cx} ${sy + 10} L${cx + 8} ${sy}Z" fill="${skin}"/>
        <circle cx="${cx - r + 1}" cy="${hy + r * 0.55}" r="2.6" fill="#FFD23F"/>
        <circle cx="${cx + r - 1}" cy="${hy + r * 0.55}" r="2.6" fill="#FFD23F"/>`;
    if (kind === 'elder')
      front += `<path d="M${cx} ${sy + 2} V118" stroke="#6B5B4B" stroke-width="2"/>
        <circle cx="${cx + 6}" cy="${sy + 16}" r="2" fill="#F1E3C8"/><circle cx="${cx + 6}" cy="${sy + 30}" r="2" fill="#F1E3C8"/>`;
    let hairTop = '';
    if (kind === 'elder')
      hairTop = [-1, 1].map(s => `<circle cx="${cx + s * (r - 3)}" cy="${hy - r * 0.45}" r="8" fill="${hair}"/>`).join('')
        + `<path d="M${cx - 6} ${hy - r + 1} q6 -6 12 0" stroke="${hair}" stroke-width="3" fill="none" stroke-linecap="round"/>`;
    else if (kind === 'girl')
      hairTop = `<path d="M${cx - r - 1} ${hy + 2} C${cx - r - 3} ${hy - r - 10} ${cx + r + 3} ${hy - r - 10} ${cx + r + 1} ${hy + 2}
        C${cx + r - 2} ${hy - r * 0.35} ${cx - r + 2} ${hy - r * 0.35} ${cx - r - 1} ${hy + 2}Z" fill="${hair}"/>`;
    else if (kind === 'woman')
      hairTop = `<path d="M${cx - r - 1} ${hy + 4} C${cx - r - 2} ${hy - r - 8} ${cx + r + 2} ${hy - r - 8} ${cx + r + 1} ${hy + 4}
        C${cx + r - 6} ${hy - r * 0.3} ${cx} ${hy - r * 0.55} ${cx - r - 1} ${hy + 4}Z" fill="${hair}"/>`;
    else if (kind === 'child')     // curly top
      hairTop = [[-17, -6], [-10, -15], [0, -19], [10, -15], [17, -6], [-5, -11], [6, -10]]
        .map(([dx, dy]) => `<circle cx="${cx + dx}" cy="${hy + dy}" r="8.5" fill="${hair}"/>`).join('');
    else {
      hairTop = cap(cx, hy, r, hair);
      if (kind === 'boy') hairTop += `<path d="M${cx + 2} ${hy - r - 4} q5 -9 11 -6 q-6 1 -6 8z" fill="${hair}"/>`;
    }
    if (o.mustache)
      hairTop += `<path d="M${cx - 10} ${hy + r * 0.38} q5 -6 10 -1 q5 -5 10 1 q-5 4 -10 1 q-5 3 -10 -1z" fill="${hair}"/>`;
    if (o.bow)
      hairTop += `<path d="M${cx} ${hy - r - 3} l-13 -8 v16z M${cx} ${hy - r - 3} l13 -8 v16z" fill="${o.bow}"/>
        <circle cx="${cx}" cy="${hy - r - 3}" r="4" fill="${o.bow}"/>`;
    if (o.cap)
      hairTop += `<path d="M${cx - r - 2} ${hy - 4} C${cx - r - 2} ${hy - r - 12} ${cx + r + 2} ${hy - r - 12} ${cx + r + 2} ${hy - 4}Z" fill="${o.cap}"/>
        <path d="M${cx + r - 4} ${hy - 7} h20 q5 3 0 7 h-20z" fill="#B5172B"/>
        <circle cx="${cx}" cy="${hy - r - 6}" r="3" fill="#fff" opacity=".8"/>`;
    if (o.heart)
      front += `<path d="M${cx + 14} ${sy + 22} c-4 -6 -12 -2 -8 4 l8 7 l8 -7 c4 -6 -4 -10 -8 -4z" fill="${o.heart}"/>`;
    return back + body + front + face(cx, hy, r, {skin, glasses: kind === 'elder'}) + hairTop;
  }

  const heart = (x, y, k, c) =>
    `<path transform="translate(${x} ${y}) scale(${k})" d="M0 -3 c-5 -8 -16 -3 -11 6 l11 10 l11 -10 c5 -9 -6 -14 -11 -6z" fill="${c}"/>`;
  const mother = (heartOn = true) => figure('woman', {shirt: '#FF6FA5', heart: heartOn && '#fff'});
  const father = () => figure('man', {skin: SKIN[1], shirt: '#2BB3A3', mustache: true});
  const daughter = () => figure('girl', {skin: SKIN[0], shirt: '#F15BB5', bow: '#FF4D6D'});
  const son = () => figure('boy', {skin: SKIN[1], shirt: '#00A6ED'});

  // numbers: a big digit + that many dots, five to a row (so 6-10 read as "a full hand + more")
  const NUMC = ['#E63946', '#FF7A59', '#FF9F1C', '#2FA36B', '#2BB3A3', '#3D8BFD', '#5A67D8', '#9B5DE5', '#E056A0', '#C9653D'];
  const FONT = 'font-family="Nunito,Arial Rounded MT Bold,Arial,sans-serif" font-weight="900"';
  const digit = k => {
    const c = NUMC[k - 1];
    let s = `<text x="60" y="${k > 5 ? 66 : 72}" text-anchor="middle" font-size="${k === 10 ? 64 : 74}" ${FONT} fill="${c}"
      stroke="#fff" stroke-width="5" paint-order="stroke" letter-spacing="-3">${k}</text>`;
    for (let i = 0; i < k; i++) {
      const row = Math.floor(i / 5), col = i % 5;
      s += `<circle cx="${28 + col * 16}" cy="${(k > 5 ? 86 : 98) + row * 17}" r="6.5" fill="${c}" opacity="${row ? 0.6 : 1}"/>`;
    }
    return s;
  };
  const tile = (x, y, r, t, c) => `<g transform="translate(${x} ${y}) rotate(${r})">
      <rect x="-19" y="-21" width="38" height="42" rx="9" fill="${c}"/>
      <text y="13" text-anchor="middle" font-size="36" ${FONT} fill="#fff">${t}</text></g>`;

  const ART = {
    number: () => tile(26, 62, -10, 1, NUMC[0]) + tile(60, 52, 4, 2, NUMC[5]) + tile(94, 64, 12, 3, NUMC[3])
      + `<path d="M22 98 h76" stroke="#2B2D42" stroke-width="5" stroke-linecap="round" opacity=".15"/>`,
    numbers: () => [[-10, 0, 20, 46], [6, 1, 60, 36], [12, 2, 100, 48], [-6, 3, 38, 86], [8, 4, 82, 86]]
      .map(([r, i, x, y]) => `<g transform="translate(${x} ${y}) scale(.86)">${tile(0, 0, r, i + 1, NUMC[i * 2])}</g>`).join(''),
    ...Object.fromEntries(Array.from({length: 10}, (_, i) => ['n' + (i + 1), () => digit(i + 1)])),
    mother, father, daughter, son,
    child: () => figure('child', {skin: SKIN[0]}),
    kid: () => figure('person', {skin: SKIN[2], shirt: '#06D6A0', cap: '#E63946'}),
    parents: () =>
      `<g transform="translate(-8 16) scale(.8)">${father()}</g>
       <g transform="translate(32 16) scale(.8)">${mother()}</g>${heart(60, 14, 0.7, '#FF4D6D')}`,
    family: () =>
      `<path d="M10 34 L60 4 L110 34" stroke="#E63946" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <g transform="translate(-2 12) scale(.66)">${father()}</g>
       <g transform="translate(43 12) scale(.66)">${mother(false)}</g>
       <g transform="translate(14 61) scale(.5)">${son()}</g>
       <g transform="translate(48 61) scale(.5)">${daughter()}</g>`,
    depend: () =>      // a little one holding a grown-up's hand
      `<g transform="translate(-14 0) scale(1)">${figure('woman', {shirt: '#9B5DE5'})}</g>
       <g transform="translate(50 42) scale(.64)">${figure('child', {shirt: '#FFB703'})}</g>
       <path d="M74 86 C82 92 82 100 80 104" stroke="${SKIN[0]}" stroke-width="7" fill="none" stroke-linecap="round"/>
       <circle cx="80" cy="104" r="6" fill="${SKIN[0]}"/>${heart(98, 22, 0.75, '#FF4D6D')}`,
    kiss: () =>
      `<path d="M16 62 C30 40 48 44 60 54 C72 44 90 40 104 62 C90 92 30 92 16 62Z" fill="#E63946"/>
       <path d="M20 62 C40 70 80 70 100 62" stroke="#9D0208" stroke-width="3.5" fill="none" stroke-linecap="round"/>
       <path d="M34 56 q8 -6 16 -2" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".6"/>
       ${heart(94, 22, 0.8, '#FF6FA5')}${heart(22, 24, 0.55, '#FF9F1C')}${heart(104, 98, 0.5, '#FF6FA5')}`,
    call: () =>
      `<rect x="36" y="10" width="48" height="100" rx="11" fill="#2B2D42"/>
       <rect x="41" y="20" width="38" height="74" rx="4" fill="#BDE7FF"/>
       <circle cx="60" cy="40" r="10" fill="#FFD7B5"/><path d="M48 62 q12 -14 24 0z" fill="#2BB3A3"/>
       <circle cx="60" cy="80" r="9" fill="#2FA36B"/>
       <path d="M55 77 q1 -2 3 -1 l1 3 q-1 1 0 2 l2 2 q1 1 2 0 l3 1 q1 2 -1 3 q-6 2 -10 -10z" fill="#fff"/>
       <rect x="54" y="100" width="12" height="4" rx="2" fill="#8A8FA3"/>
       ${[10, 20].map(d => `<path d="M${84 + d} ${44 - d * .6} a${18 + d} ${18 + d} 0 0 1 0 ${30 + d * 1.2}" stroke="#3D8BFD" stroke-width="5" fill="none" stroke-linecap="round"/>
       <path d="M${36 - d} ${44 - d * .6} a${18 + d} ${18 + d} 0 0 0 0 ${30 + d * 1.2}" stroke="#3D8BFD" stroke-width="5" fill="none" stroke-linecap="round"/>`).join('')}`,
    person: () => figure('person'),
    boy: () => figure('boy'),
    girl: () => figure('girl', {skin: SKIN[1]}),
    man: () => figure('man', {skin: SKIN[1]}),
    woman: () => figure('woman'),
    elder: () => figure('elder'),
    group: () =>
      `<g transform="translate(-8 4) scale(.7)">${figure('person', {shirt: '#FF9F1C', skin: SKIN[2]})}</g>
       <g transform="translate(44 4) scale(.7)">${figure('person', {shirt: '#9B5DE5', skin: SKIN[1], hair: '#6B3E26'})}</g>
       <g transform="translate(17 30) scale(.74)">${figure('person')}</g>`,
    nametag: () =>
      `<g transform="rotate(-7 60 62)">
        <rect x="14" y="28" width="92" height="66" rx="12" fill="#fff" stroke="#E63946" stroke-width="4"/>
        <path d="M14 40 a12 12 0 0 1 12 -12 h68 a12 12 0 0 1 12 12 v10 h-92z" fill="#E63946"/>
        <text x="60" y="47" text-anchor="middle" font-size="15" font-weight="800" fill="#fff"
              font-family="Arial Rounded MT Bold,Arial,sans-serif" letter-spacing="1">HELLO</text>
        <text x="60" y="64" text-anchor="middle" font-size="9.5" fill="#8A7F7A" font-family="Arial,sans-serif">my name is</text>
        <path d="M30 82 c6 -10 10 -10 12 -2 s6 6 10 -4 s8 -6 10 2 s8 4 14 -4 s6 2 10 4"
              fill="none" stroke="#3D8BFD" stroke-width="3" stroke-linecap="round"/>
       </g>`,
    sprout: () =>
      `<path d="M60 86 C60 70 60 60 61 46" stroke="#3FA34D" stroke-width="5" fill="none" stroke-linecap="round"/>
       <path d="M61 52 C46 52 34 42 32 28 C48 26 60 36 61 52Z" fill="#6CCB5F"/>
       <path d="M61 46 C70 34 84 30 96 34 C92 48 78 54 61 46Z" fill="#8EDB6E"/>
       <path d="M36 84 h48 l-6 30 h-36z" fill="#E07A4F"/><rect x="32" y="80" width="56" height="10" rx="4" fill="#C9653D"/>
       <path d="M92 16 l2.5 6 l6 2.5 l-6 2.5 l-2.5 6 l-2.5 -6 l-6 -2.5 l6 -2.5z" fill="#FFD23F"/>`,
  };

  // ---------- shared bits for ep04+ ----------
  const star = (cx, cy, R, r, c, rot = -90) => `<path d="${Array.from({length: 10}, (_, i) => {
      const a = (rot + i * 36) * Math.PI / 180, k = i % 2 ? r : R;
      return (i ? 'L' : 'M') + (cx + k * Math.cos(a)).toFixed(1) + ' ' + (cy + k * Math.sin(a)).toFixed(1); }).join('')}Z" fill="${c}"/>`;
  const flame = (x, y, k = 1) => `<g transform="translate(${x} ${y}) scale(${k})">
      <path d="M0 -16 C8 -6 9 2 0 7 C-9 2 -8 -6 0 -16Z" fill="#FF9F1C"/><path d="M0 -8 C4 -3 4 2 0 4 C-4 2 -4 -3 0 -8Z" fill="#FFD23F"/></g>`;
  const gift = (x, y, w, h, c, rib = '#FFD23F') => `<rect x="${x}" y="${y + h * .22}" width="${w}" height="${h * .78}" rx="${w * .07}" fill="${c}"/>
      <rect x="${x - w * .06}" y="${y + h * .08}" width="${w * 1.12}" height="${h * .22}" rx="${w * .06}" fill="${c}"/>
      <rect x="${x - w * .06}" y="${y + h * .08}" width="${w * 1.12}" height="${h * .22}" rx="${w * .06}" fill="#fff" opacity=".22"/>
      <rect x="${x + w * .42}" y="${y + h * .08}" width="${w * .16}" height="${h * .92}" fill="${rib}"/>
      <path d="M${x + w / 2} ${y + h * .08} C${x + w * .25} ${y - h * .25} ${x + w * .05} ${y} ${x + w / 2} ${y + h * .08}
               C${x + w * .95} ${y} ${x + w * .75} ${y - h * .25} ${x + w / 2} ${y + h * .08}Z" fill="${rib}"/>`;
  const hand = (x, y, k = 1, rot = 0, skin = SKIN[0]) => `<g transform="translate(${x} ${y}) rotate(${rot}) scale(${k})">
      <path d="M-14 10 C-16 -2 -14 -10 -10 -12 L-10 -26 a3.5 3.5 0 0 1 7 0 L-3 -14 L-3 -30 a3.5 3.5 0 0 1 7 0 L4 -14 L4 -28
        a3.5 3.5 0 0 1 7 0 L11 -12 L11 -22 a3.5 3.5 0 0 1 7 0 L18 -2 C18 10 12 18 2 18 C-6 18 -12 15 -14 10Z" fill="${skin}"/>
      <path d="M-14 4 C-20 0 -24 -6 -22 -10 C-20 -13 -16 -10 -12 -4" fill="${skin}"/></g>`;

  Object.assign(ART, {
    // ---------- ep04 birthday ----------
    birthday: () =>
      `<rect x="16" y="22" width="88" height="84" rx="12" fill="#fff" stroke="#E63946" stroke-width="4"/>
       <path d="M16 34 a12 12 0 0 1 12 -12 h64 a12 12 0 0 1 12 12 v10 h-88z" fill="#E63946"/>
       <rect x="36" y="14" width="7" height="16" rx="3.5" fill="#2B2D42"/><rect x="77" y="14" width="7" height="16" rx="3.5" fill="#2B2D42"/>
       <path d="M42 80 h36 l-5 18 h-26z" fill="#FF9F1C"/><path d="M40 81 q0 -15 20 -15 q20 0 20 15z" fill="#FF6FA5"/>
       <rect x="58" y="54" width="4" height="13" rx="2" fill="#3D8BFD"/>${flame(60, 50, .55)}
       ${star(30, 62, 6, 2.6, '#FFD23F')}${star(92, 66, 5, 2.2, '#2BB3A3')}`,
    party: () =>
      `<path d="M60 16 L88 96 Q60 106 32 96Z" fill="#9B5DE5"/>
       <path d="M50 46 L70 46 M44 64 L76 64 M38 82 L82 82" stroke="#FFD23F" stroke-width="6" stroke-linecap="round"/>
       <circle cx="60" cy="15" r="9" fill="#FF6FA5"/>
       ${[[16, 30, '#E63946', 20], [100, 24, '#3D8BFD', -30], [18, 80, '#2FA36B', 40], [104, 74, '#FF9F1C', 15], [28, 52, '#FFD23F', -15], [96, 50, '#FF6FA5', 60]]
         .map(([x, y, c, r]) => `<rect x="${x - 5}" y="${y - 2.5}" width="10" height="5" rx="1.5" fill="${c}" transform="rotate(${r} ${x} ${y})"/>`).join('')}`,
    present: () => gift(24, 34, 72, 72, '#3D8BFD'),
    give: () =>
      `<rect x="-2" y="78" width="26" height="22" rx="6" fill="#2BB3A3"/>
       <path d="M22 80 h40 q9 0 9 8 q0 8 -9 8 h-40z" fill="${SKIN[0]}"/>
       ${gift(30, 42, 32, 38, '#FF6FA5')}
       <path d="M80 60 h26 m-10 -10 l10 10 l-10 10" stroke="#2FA36B" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    get: () =>
      `${gift(42, 22, 36, 40, '#FF9F1C', '#fff')}
       <path d="M20 28 v26 m-8 -9 l8 9 l8 -9" stroke="#2FA36B" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       ${hand(40, 92, 1.05, -28, SKIN[1])}<g transform="translate(120 0) scale(-1 1)">${hand(40, 92, 1.05, -28, SKIN[1])}</g>`,
    for: () =>
      `<path d="M34 28 h58 a8 8 0 0 1 8 8 v48 a8 8 0 0 1 -8 8 h-58 l-22 -32z" fill="#FFF3C4" stroke="#E0A100" stroke-width="4" stroke-linejoin="round"/>
       <circle cx="28" cy="60" r="5" fill="#fff" stroke="#E0A100" stroke-width="3"/>
       <path d="M24 57 C10 44 12 24 26 14" stroke="#E63946" stroke-width="3" fill="none" stroke-linecap="round"/>
       <text x="66" y="62" text-anchor="middle" font-size="27" ${FONT} fill="#C77800">for</text>
       ${heart(66, 76, .6, '#E63946')}`,
    cake: () =>
      `<ellipse cx="60" cy="106" rx="50" ry="7" fill="#E6DCCF"/>
       <rect x="16" y="68" width="88" height="36" rx="9" fill="#F4A261"/>
       <path d="M16 78 q0 -10 9 -10 h70 q9 0 9 10 c-6 0 -6 8 -12 8 s-6 -8 -12 -8 s-6 8 -12 8 s-6 -8 -12 -8 s-6 8 -12 8 s-6 -8 -12 -8 s-6 8 -12 8 s-4 -8 -4 -8z" fill="#fff"/>
       <rect x="30" y="44" width="60" height="28" rx="8" fill="#FF6FA5"/>
       <path d="M30 52 q0 -8 8 -8 h44 q8 0 8 8 c-5 0 -5 7 -10 7 s-5 -7 -10 -7 s-5 7 -10 7 s-5 -7 -10 -7 s-5 7 -10 7 s-4 -7 -4 -7z" fill="#fff"/>
       ${[[44, '#3D8BFD'], [60, '#2FA36B'], [76, '#FFD23F']].map(([x, c]) => `<rect x="${x - 2.5}" y="28" width="5" height="16" rx="2" fill="${c}"/>${flame(x, 24, .5)}`).join('')}
       ${[30, 50, 70, 90].map(x => `<circle cx="${x}" cy="92" r="3" fill="#E63946"/>`).join('')}`,
    candle: () =>
      `<circle cx="60" cy="30" r="22" fill="#FFD23F" opacity=".22"/>
       <ellipse cx="60" cy="108" rx="30" ry="6" fill="#C9B8A6"/>
       <rect x="44" y="46" width="32" height="62" rx="6" fill="#FF6FA5"/>
       <path d="M44 62 l32 -10 M44 80 l32 -10 M44 98 l32 -10" stroke="#fff" stroke-width="5" opacity=".7"/>
       <path d="M60 46 v-8" stroke="${INK}" stroke-width="3"/>${flame(60, 32, 1.1)}`,
    match: () =>
      `<g transform="rotate(28 60 60)"><rect x="55" y="42" width="10" height="72" rx="3" fill="#E9C27A"/>
       <ellipse cx="60" cy="40" rx="9" ry="12" fill="#E63946"/></g>
       ${flame(75, 28, 1.15)}`,
    wish: () =>
      `<path d="M14 104 L66 52" stroke="#FF9F1C" stroke-width="6" stroke-linecap="round" opacity=".55"/>
       <path d="M24 112 L70 64" stroke="#FF6FA5" stroke-width="5" stroke-linecap="round" opacity=".45"/>
       <path d="M8 90 L62 44" stroke="#3D8BFD" stroke-width="4" stroke-linecap="round" opacity=".35"/>
       ${star(78, 40, 28, 12, '#FFD23F', -70)}
       ${star(30, 30, 7, 3, '#FFD23F')}${star(104, 88, 6, 2.5, '#FFB703')}`,
    blow: () =>
      `<circle cx="44" cy="62" r="30" fill="${SKIN[0]}"/>
       <path d="M14 58 C12 30 42 22 66 38 C54 34 34 38 24 56Z" fill="#3B2A20"/>
       <circle cx="64" cy="70" r="13" fill="${SKIN[0]}"/><ellipse cx="62" cy="74" rx="6" ry="4" fill="${BLUSH}" opacity=".7"/>
       <circle cx="54" cy="54" r="3.4" fill="${INK}"/>
       <circle cx="78" cy="68" r="4.5" fill="#E63946"/>
       <path d="M88 52 q10 -4 20 2 M88 68 q12 0 24 0 M88 84 q10 4 20 -2" stroke="#7FC8F8" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    balloon: () =>
      `<path d="M44 72 C40 84 54 92 50 104 S54 114 56 116" stroke="#8A8FA3" stroke-width="2.5" fill="none"/>
       <path d="M80 76 C82 88 70 96 74 106 S68 114 66 116" stroke="#8A8FA3" stroke-width="2.5" fill="none"/>
       <ellipse cx="80" cy="50" rx="22" ry="27" fill="#3D8BFD"/><path d="M80 77 l-4 6 h8z" fill="#3D8BFD"/>
       <ellipse cx="72" cy="40" rx="5" ry="9" fill="#fff" opacity=".35" transform="rotate(25 72 40)"/>
       <ellipse cx="44" cy="44" rx="24" ry="29" fill="#E63946"/><path d="M44 73 l-4 6 h8z" fill="#E63946"/>
       <ellipse cx="35" cy="33" rx="5" ry="10" fill="#fff" opacity=".35" transform="rotate(25 35 33)"/>`,
  });

  const houseArt = (inside) =>
      `<rect x="80" y="26" width="11" height="24" fill="#8D5A3B"/>
       <rect x="24" y="56" width="72" height="52" rx="4" fill="#FFD8A8"/>
       <path d="M12 62 L60 20 L108 62" fill="#E63946" stroke="#E63946" stroke-width="6" stroke-linejoin="round"/>${inside}`;
  const sneaker = (x, y, k = 1, c = '#3D8BFD') => `<g transform="translate(${x} ${y}) scale(${k})">
      <path d="M-26 6 C-26 -6 -20 -14 -12 -14 C-6 -14 -4 -8 4 -6 C14 -4 24 -2 26 6 Z" fill="${c}"/>
      <rect x="-28" y="4" width="56" height="8" rx="4" fill="#fff" stroke="#D9DCE6" stroke-width="2"/>
      <path d="M-10 -10 l6 4 M-6 -12 l6 4" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/></g>`;
  Object.assign(ART, {
    // ---------- ep05 home / house ----------
    house: () => houseArt(`<rect x="51" y="78" width="18" height="30" rx="3" fill="#8D5A3B"/><circle cx="65" cy="94" r="2" fill="#FFD23F"/>
       <rect x="30" y="66" width="16" height="15" rx="2" fill="#BDE7FF"/><rect x="74" y="66" width="16" height="15" rx="2" fill="#BDE7FF"/>`),
    home: () => `<circle cx="60" cy="66" r="52" fill="#FFD23F" opacity=".22"/>` + houseArt(
       `${heart(60, 80, 1.15, '#FF4D6D')}<rect x="30" y="66" width="14" height="13" rx="2" fill="#FFE08A"/><rect x="76" y="66" width="14" height="13" rx="2" fill="#FFE08A"/>`)
       + `<path d="M86 22 q-6 -6 0 -12 q6 -6 0 -12" stroke="#C9C9D3" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    address: () =>
      `<rect x="10" y="44" width="84" height="58" rx="6" fill="#fff" stroke="#3D8BFD" stroke-width="4"/>
       <path d="M12 48 L52 76 L92 48" stroke="#3D8BFD" stroke-width="4" fill="none" stroke-linejoin="round"/>
       <path d="M22 90 h26 M22 82 h16" stroke="#8A8FA3" stroke-width="3" stroke-linecap="round"/>
       <path d="M92 10 C78 10 70 20 70 31 C70 46 92 64 92 64 C92 64 114 46 114 31 C114 20 106 10 92 10Z" fill="#E63946"/>
       <circle cx="92" cy="31" r="8" fill="#fff"/>`,
    key: () =>
      `<g transform="rotate(-30 60 60)"><circle cx="34" cy="60" r="18" fill="none" stroke="#FFB703" stroke-width="11"/>
       <rect x="50" y="55" width="58" height="10" rx="3" fill="#FFB703"/>
       <rect x="86" y="62" width="8" height="14" rx="2" fill="#FFB703"/><rect x="99" y="62" width="8" height="10" rx="2" fill="#FFB703"/>
       <circle cx="34" cy="60" r="18" fill="none" stroke="#fff" stroke-width="3" opacity=".35" stroke-dasharray="20 120"/></g>`,
    door: () =>
      `<rect x="28" y="10" width="64" height="102" rx="6" fill="#6B4A36"/>
       <rect x="34" y="16" width="52" height="96" rx="4" fill="#B5703F"/>
       <rect x="41" y="24" width="38" height="30" rx="3" fill="#9C5E33"/><rect x="41" y="62" width="38" height="40" rx="3" fill="#9C5E33"/>
       <circle cx="78" cy="62" r="4.5" fill="#FFD23F"/>`,
    lock: () =>
      `<path d="M40 56 V40 a20 20 0 0 1 40 0 V56" stroke="#8A8FA3" stroke-width="10" fill="none"/>
       <rect x="26" y="52" width="68" height="56" rx="12" fill="#FFB703"/>
       <rect x="26" y="52" width="68" height="12" rx="6" fill="#fff" opacity=".25"/>
       <circle cx="60" cy="76" r="7" fill="${INK}"/><path d="M57 78 h6 l2 16 h-10z" fill="${INK}"/>`,
    window: () =>
      `<rect x="16" y="14" width="88" height="86" rx="6" fill="#fff" stroke="#8D5A3B" stroke-width="6"/>
       <rect x="24" y="22" width="72" height="70" fill="#BDE7FF"/>
       <path d="M60 22 v70 M24 57 h72" stroke="#fff" stroke-width="6"/>
       <path d="M24 22 h20 c-4 22 -4 46 -12 70 h-8z" fill="#FF8FAB"/><path d="M96 22 h-20 c4 22 4 46 12 70 h8z" fill="#FF8FAB"/>
       <path d="M74 32 l10 10 M70 42 l6 6" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
       <rect x="10" y="98" width="100" height="10" rx="4" fill="#8D5A3B"/>`,
    gate: () =>
      `<rect x="10" y="30" width="14" height="80" rx="3" fill="#8D7B68"/><rect x="96" y="30" width="14" height="80" rx="3" fill="#8D7B68"/>
       <circle cx="17" cy="26" r="8" fill="#8D7B68"/><circle cx="103" cy="26" r="8" fill="#8D7B68"/>
       ${[32, 42, 52, 62, 72, 82].map(x => `<path d="M${x} 108 V${46 - Math.abs(x - 57) * .4} l3 -6 l3 6 V108" fill="#2B2D42"/>`).join('')}
       <rect x="28" y="56" width="64" height="5" fill="#2B2D42"/><rect x="28" y="92" width="64" height="5" fill="#2B2D42"/>
       <circle cx="60" cy="74" r="7" fill="none" stroke="#FFB703" stroke-width="4"/>`,
    yard: () =>
      `<rect x="10" y="78" width="100" height="32" rx="12" fill="#8EDB6E"/>
       ${[18, 34, 50, 66].map(x => `<path d="M${x} 84 V54 l6 -7 l6 7 V84z" fill="#fff" stroke="#D9C7AE" stroke-width="2"/>`).join('')}
       <rect x="14" y="60" width="68" height="6" fill="#fff" stroke="#D9C7AE" stroke-width="2"/>
       <rect x="90" y="56" width="8" height="28" fill="#8D5A3B"/><circle cx="94" cy="44" r="18" fill="#3FA34D"/><circle cx="86" cy="38" r="9" fill="#6CCB5F"/>
       <path d="M24 100 l3 -6 l3 6 M60 98 l3 -6 l3 6" stroke="#3FA34D" stroke-width="2.5" fill="none"/>`,
    flower: () =>
      `<path d="M60 112 V58" stroke="#3FA34D" stroke-width="6" stroke-linecap="round"/>
       <path d="M60 92 C44 92 34 82 32 72 C46 70 58 78 60 92Z" fill="#6CCB5F"/><path d="M60 84 C74 82 84 72 88 62 C74 62 62 70 60 84Z" fill="#8EDB6E"/>
       ${Array.from({length: 6}, (_, i) => { const a = i * 60 * Math.PI / 180;
         return `<ellipse cx="${60 + 17 * Math.cos(a)}" cy="${40 + 17 * Math.sin(a)}" rx="12" ry="9" fill="#FF6FA5" transform="rotate(${i * 60} ${60 + 17 * Math.cos(a)} ${40 + 17 * Math.sin(a)})"/>`; }).join('')}
       <circle cx="60" cy="40" r="11" fill="#FFD23F"/>`,
    stairs: () =>
      `<path d="M10 108 V90 H34 V72 H58 V54 H82 V36 H106 V108Z" fill="#E9A66B"/>
       <path d="M10 90 H34 V72 H58 V54 H82 V36 H106" stroke="#C9653D" stroke-width="5" fill="none" stroke-linejoin="round"/>
       <path d="M22 74 L94 18" stroke="#8D5A3B" stroke-width="5" stroke-linecap="round"/>
       ${[[22, 74], [46, 56], [70, 37], [94, 18]].map(([x, y]) => `<path d="M${x} ${y} V${y + 16}" stroke="#8D5A3B" stroke-width="4"/>`).join('')}`,
    step: () =>
      `<rect x="14" y="98" width="92" height="12" rx="4" fill="#C9C1B5"/>
       <rect x="44" y="70" width="62" height="30" rx="5" fill="#E9A66B"/><rect x="44" y="70" width="62" height="7" rx="3" fill="#C9653D"/>
       ${sneaker(70, 52, .95, '#FF7A59')}
       <path d="M22 84 q8 -26 30 -34" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="1 9"/>
       <path d="M44 44 l8 6 l-9 4" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    pool: () =>
      `<rect x="10" y="44" width="100" height="62" rx="16" fill="#fff" stroke="#9AD1E8" stroke-width="5"/>
       <rect x="18" y="52" width="84" height="46" rx="10" fill="#4CC9F0"/>
       <path d="M24 66 q8 -6 16 0 t16 0 t16 0 t16 0 M28 84 q8 -6 16 0 t16 0 t16 0" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round" opacity=".8"/>
       <path d="M88 30 V64 M100 30 V64 M88 40 h12 M88 52 h12" stroke="#8A8FA3" stroke-width="4" stroke-linecap="round"/>
       <circle cx="38" cy="30" r="10" fill="#FF6FA5"/><circle cx="38" cy="30" r="4" fill="#4CC9F0"/>`,
  });

  const notebook = (x, y, k = 1, c = '#3D8BFD') => `<g transform="translate(${x} ${y}) scale(${k})">
      <rect x="-24" y="-30" width="48" height="60" rx="5" fill="#fff" stroke="${c}" stroke-width="4"/>
      <rect x="-24" y="-30" width="10" height="60" rx="4" fill="${c}"/>
      <path d="M-8 -16 h24 M-8 -6 h24 M-8 4 h24 M-8 14 h16" stroke="#C5CBE0" stroke-width="3" stroke-linecap="round"/></g>`;
  const pencil = (x, y, k = 1, r = 0) => `<g transform="translate(${x} ${y}) rotate(${r}) scale(${k})">
      <rect x="-5" y="-30" width="10" height="46" fill="#FFB703"/><rect x="-5" y="-36" width="10" height="7" rx="2" fill="#FF8FAB"/>
      <path d="M-5 16 L0 28 L5 16Z" fill="#F4D3A8"/><path d="M-1.8 23 L0 28 L1.8 23Z" fill="${INK}"/></g>`;
  const check = (x, y, k = 1, c = '#2FA36B') => `<path transform="translate(${x} ${y}) scale(${k})" d="M-10 0 L-3 7 L10 -8" stroke="${c}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
  const shirt = (c, collar = '#fff') => `<path d="M38 22 L22 30 L10 50 L26 58 L30 50 V104 H90 V50 L94 58 L110 50 L98 30 L82 22 Q60 34 38 22Z" fill="${c}"/>
      <path d="M38 22 Q60 34 82 22 L74 18 Q60 28 46 18Z" fill="${collar}"/>`;
  Object.assign(ART, {
    // ---------- ep06 school / class ----------
    school: () =>
      `<rect x="10" y="54" width="100" height="54" rx="3" fill="#F4D35E"/>
       <rect x="42" y="30" width="36" height="78" fill="#EE964B"/><path d="M38 34 L60 14 L82 34Z" fill="#E63946"/>
       <path d="M60 14 V2" stroke="#8A8FA3" stroke-width="2.5"/><path d="M60 2 h14 l-4 4 l4 4 h-14z" fill="#E63946"/>
       <circle cx="60" cy="46" r="9" fill="#fff"/><path d="M60 40 v6 h5" stroke="${INK}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
       <rect x="52" y="82" width="16" height="26" rx="2" fill="#8D5A3B"/>
       ${[18, 30, 84, 96].map(x => `<rect x="${x - 4}" y="64" width="9" height="11" rx="1.5" fill="#BDE7FF"/><rect x="${x - 4}" y="84" width="9" height="11" rx="1.5" fill="#BDE7FF"/>`).join('')}`,
    class: () =>
      `<rect x="10" y="12" width="100" height="58" rx="5" fill="#8D5A3B"/><rect x="15" y="17" width="90" height="48" rx="3" fill="#2F6B4F"/>
       <text x="40" y="50" text-anchor="middle" font-size="22" ${FONT} fill="#fff" opacity=".9">ABC</text>
       <path d="M70 34 h22 M70 46 h16" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
       ${[30, 90].map(x => `<rect x="${x - 18}" y="84" width="36" height="7" rx="2" fill="#E9A66B"/><path d="M${x - 14} 91 v18 M${x + 14} 91 v18" stroke="#C9653D" stroke-width="4"/>`).join('')}
       <rect x="50" y="94" width="20" height="6" rx="2" fill="#E9A66B"/><path d="M53 100 v10 M67 100 v10" stroke="#C9653D" stroke-width="4"/>`,
    work: () =>
      `<g transform="translate(14 0) scale(.78)">${figure('man', {skin: SKIN[1], shirt: '#5A67D8'})}</g>
       <rect x="6" y="84" width="108" height="10" rx="3" fill="#C9653D"/>
       <path d="M30 84 L36 58 H84 L90 84Z" fill="#8A8FA3"/><rect x="39" y="61" width="42" height="20" rx="2" fill="#BDE7FF"/>
       <circle cx="60" cy="71" r="3" fill="#fff"/><path d="M26 84 h68" stroke="#6B7085" stroke-width="3"/>`,
    schoolwork: () =>
      `${notebook(46, 64, 1.25, '#2FA36B')}${pencil(92, 66, 1, 25)}
       <g transform="translate(70 4) scale(.34)">${'<rect x="10" y="54" width="100" height="54" rx="3" fill="#F4D35E"/><rect x="42" y="30" width="36" height="78" fill="#EE964B"/><path d="M38 34 L60 14 L82 34Z" fill="#E63946"/>'}</g>`,
    homework: () =>
      `${notebook(46, 64, 1.25, '#FF7A59')}${pencil(92, 66, 1, 25)}
       <g transform="translate(70 2) scale(.36)">${houseArt('<rect x="51" y="78" width="18" height="30" rx="3" fill="#8D5A3B"/>')}</g>`,
    complete: () =>
      `<rect x="22" y="16" width="76" height="96" rx="8" fill="#E9A66B"/><rect x="29" y="26" width="62" height="80" rx="4" fill="#fff"/>
       <rect x="44" y="10" width="32" height="14" rx="5" fill="#8A8FA3"/>
       ${[42, 62, 82].map(y => `<rect x="35" y="${y - 7}" width="14" height="14" rx="3" fill="none" stroke="#2FA36B" stroke-width="3"/>${check(42, y, .7)}
         <path d="M56 ${y} h28" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>`).join('')}
       <circle cx="92" cy="96" r="18" fill="#2FA36B"/>${check(92, 96, 1.1, '#fff')}`,
    teach: () =>
      `<rect x="50" y="14" width="64" height="44" rx="4" fill="#2F6B4F" stroke="#8D5A3B" stroke-width="4"/>
       <text x="82" y="44" text-anchor="middle" font-size="18" ${FONT} fill="#fff">1+1</text>
       <g transform="translate(-16 14) scale(.92)">${figure('woman', {shirt: '#E63946'})}</g>
       <path d="M58 82 L92 50" stroke="#8D5A3B" stroke-width="4" stroke-linecap="round"/><circle cx="58" cy="82" r="5" fill="${SKIN[0]}"/>`,
    grade: () =>
      `${[[14, 78, 1, '#FFB703'], [44, 58, 2, '#FF7A59'], [74, 38, 3, '#E63946']].map(([x, y, n, c]) =>
         `<rect x="${x}" y="${y}" width="32" height="${110 - y}" rx="5" fill="${c}"/>
          <text x="${x + 16}" y="${y + 26}" text-anchor="middle" font-size="22" ${FONT} fill="#fff">${n}</text>`).join('')}
       ${star(90, 22, 13, 5.5, '#FFD23F')}`,
    term: () =>
      `<rect x="12" y="20" width="96" height="88" rx="10" fill="#fff" stroke="#5A67D8" stroke-width="4"/>
       <path d="M12 32 a10 10 0 0 1 10 -12 h76 a10 10 0 0 1 10 12 v6 h-96z" fill="#5A67D8"/>
       ${[0, 1, 2, 3, 4, 5].map(i => { const x = 22 + (i % 3) * 28, y = 48 + Math.floor(i / 3) * 28;
         return `<rect x="${x}" y="${y}" width="20" height="20" rx="4" fill="${i < 3 ? '#FFB703' : '#E3E6F5'}"/>`; }).join('')}
       <path d="M18 82 h84" stroke="#5A67D8" stroke-width="3" stroke-dasharray="6 5"/>
       <path d="M22 98 h40" stroke="#FFB703" stroke-width="6" stroke-linecap="round"/>`,
    classmate: () =>
      `<g transform="translate(-14 6) scale(.86)">${figure('child', {shirt: '#3D8BFD', skin: SKIN[0]})}</g>
       <g transform="translate(30 6) scale(.86)">${figure('girl', {shirt: '#3D8BFD', skin: SKIN[1]})}</g>
       <rect x="6" y="100" width="108" height="10" rx="3" fill="#E9A66B"/>`,
    uniform: () =>
      `<path d="M60 4 v8 M50 16 L60 10 L70 16" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-linecap="round"/>
       ${shirt('#3D8BFD')}<path d="M60 30 l-6 8 l6 34 l6 -34z" fill="#E63946"/>
       <path d="M74 54 h12 v12 q-6 4 -12 0z" fill="#FFD23F"/>
       <path d="M30 76 H90" stroke="#fff" stroke-width="3" opacity=".5"/>`,
  });

  // posable full-body kid. Limb angles in degrees: 0 = straight down, +90 = pointing right (forward).
  // o = {la, ra, ll, rl: [upper, lower], rot, dx, dy, s, shirt, pants, skin, hair, hl: 'arm'|'leg'|'knee'|'body'|'neck'|'shoulder'|'head'|'foot'}
  function kid(o = {}) {
    const skin = o.skin || SKIN[0], shirt = o.shirt || '#FF7A59', pants = o.pants || '#3D8BFD', hair = o.hair || '#3B2A20';
    const r = Math.PI / 180, P = ([x, y], a, L) => [x + L * Math.sin(a * r), y + L * Math.cos(a * r)];
    const limb = (st, [a1, a2], L1, L2) => { const m = P(st, a1, L1); return [st, m, P(m, a2, L2)]; };
    const la = limb([52, 44], o.la || [-10, -4], 15, 14), ra = limb([68, 44], o.ra || [10, 4], 15, 14);
    const ll = limb([55, 72], o.ll || [-3, -3], 18, 17), rl = limb([65, 72], o.rl || [3, 3], 18, 17);
    const pl = pts => 'M' + pts.map(p => p.map(v => v.toFixed(1)).join(' ')).join(' L');
    const G = '#FFD23F', glow = (d, w) => `<path d="${d}" stroke="${G}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/>`;
    let s = '';
    if (o.hl === 'leg') s += glow(pl(rl), 22);
    if (o.hl === 'arm') s += glow(pl(ra), 19);
    if (o.hl === 'body') s += `<rect x="40" y="32" width="40" height="50" rx="14" fill="${G}" opacity=".9"/>`;
    if (o.hl === 'head') s += `<circle cx="60" cy="22" r="22" fill="${G}" opacity=".9"/>`;
    if (o.hl === 'neck') s += `<rect x="51" y="30" width="18" height="14" rx="6" fill="${G}"/>`;
    if (o.hl === 'shoulder') s += glow('M44 48 Q48 38 58 40 M62 40 Q72 38 76 48', 12);
    const leg = (L, back) => `<path d="${pl(L)}" stroke="${pants}" stroke-width="9.5" fill="none" stroke-linecap="round" stroke-linejoin="round" ${back ? 'opacity=".85"' : ''}/>
      <ellipse cx="${L[2][0] + 3}" cy="${L[2][1] + 1}" rx="7" ry="4.2" fill="#2B2D42"/>`;
    const arm = (A, back) => `<path d="${pl(A.slice(0, 2))}" stroke="${shirt}" stroke-width="8" stroke-linecap="round" ${back ? 'opacity=".85"' : ''}/>
      <path d="${pl(A.slice(1))}" stroke="${skin}" stroke-width="6.5" stroke-linecap="round"/><circle cx="${A[2][0]}" cy="${A[2][1]}" r="4.2" fill="${skin}"/>`;
    s += leg(ll, 1) + arm(la, 1) + leg(rl);
    s += `<rect x="56" y="32" width="8" height="10" rx="3" fill="${skin}"/>
          <rect x="47" y="38" width="26" height="38" rx="10" fill="${shirt}"/><rect x="47" y="64" width="26" height="12" rx="5" fill="${pants}"/>`;
    s += arm(ra) + face(60, 22, 13, {skin}) + cap(60, 22, 13, hair);
    if (o.hl === 'knee') s += `<circle cx="${rl[1][0]}" cy="${rl[1][1]}" r="9" fill="none" stroke="${G}" stroke-width="5"/>`;
    const t = `translate(${o.dx || 0} ${o.dy || 0}) rotate(${o.rot || 0} 60 64)` + (o.s ? ` translate(60 64) scale(${o.s}) translate(-60 -64)` : '');
    return `<g transform="${t}">${s}</g>`;
  }
  const bubble = (x, y, w, h, c, tail = 'l', inner = '') => `<g transform="translate(${x} ${y})">
      <rect x="0" y="0" width="${w}" height="${h}" rx="${h / 2.6}" fill="${c}"/>
      <path d="${tail === 'l' ? `M${w * .2} ${h - 2} l-8 12 l18 -10z` : `M${w * .8} ${h - 2} l8 12 l-18 -10z`}" fill="${c}"/>${inner}</g>`;
  const dots3 = (w, h) => [0.3, 0.5, 0.7].map(f => `<circle cx="${w * f}" cy="${h / 2}" r="3.5" fill="#fff"/>`).join('');
  const motion = (x, y) => `<path d="M${x} ${y} h-16 M${x + 4} ${y + 12} h-20 M${x} ${y + 24} h-14" stroke="#8A8FA3" stroke-width="3.5" stroke-linecap="round" opacity=".6"/>`;
  Object.assign(ART, {
    // ---------- ep07 action ----------
    action: () =>
      `<rect x="14" y="44" width="92" height="62" rx="6" fill="#2B2D42"/>
       <text x="60" y="84" text-anchor="middle" font-size="19" ${FONT} fill="#fff">ACTION!</text>
       <g transform="rotate(-14 14 42)"><rect x="14" y="26" width="92" height="16" rx="3" fill="#2B2D42"/>
       ${[0, 1, 2, 3, 4].map(i => `<path d="M${22 + i * 18} 26 l10 0 l-8 16 l-10 0z" fill="#fff"/>`).join('')}</g>
       <circle cx="14" cy="44" r="5" fill="#8A8FA3"/>${star(98, 18, 10, 4.2, '#FFD23F')}`,
    stand: () => kid({la: [-8, -4], ra: [8, 4], shirt: '#2BB3A3'}),
    walk: () => kid({la: [-24, -8], ra: [26, 48], ll: [20, 8], rl: [-20, -36], shirt: '#FF9F1C'}),
    run: () => kid({rot: 10, la: [-60, 30], ra: [55, 140], ll: [-40, -95], rl: [62, -4], shirt: '#E63946'}) + motion(26, 44),
    sit: () =>
      `<rect x="30" y="40" width="9" height="66" rx="3" fill="#C9653D"/><rect x="30" y="80" width="56" height="9" rx="3" fill="#E9A66B"/>
       <path d="M36 89 v22 M80 89 v22" stroke="#C9653D" stroke-width="6" stroke-linecap="round"/>`
       + kid({dy: 4, la: [10, 75], ra: [18, 80], ll: [88, 2], rl: [92, 0], shirt: '#9B5DE5'}),
    wait: () => kid({dx: -14, la: [-8, -4], ra: [8, 4], shirt: '#5A67D8'})
       + `<circle cx="92" cy="34" r="20" fill="#fff" stroke="#FF7A59" stroke-width="5"/>
          <path d="M92 22 v12 l8 5" stroke="${INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
          ${[84, 92, 100].map(x => `<circle cx="${x}" cy="72" r="3.5" fill="#8A8FA3"/>`).join('')}`,
    look: () => kid({dx: -12, la: [-8, -4], ra: [175, -120], shirt: '#06D6A0'})
       + `<path d="M66 20 L110 8 M66 24 L112 28" stroke="#FFB703" stroke-width="3" stroke-dasharray="5 5" stroke-linecap="round"/>`,
    see: () =>
      `<path d="M8 60 Q60 4 112 60 Q60 116 8 60Z" fill="#fff" stroke="${INK}" stroke-width="5"/>
       <circle cx="60" cy="60" r="24" fill="#3D8BFD"/><circle cx="60" cy="60" r="11" fill="${INK}"/><circle cx="68" cy="52" r="5" fill="#fff"/>
       ${[[30, 26, -30], [48, 16, -12], [72, 16, 12], [90, 26, 30]].map(([x, y, a]) => `<path d="M${x} ${y + 8} l0 -12" transform="rotate(${a} ${x} ${y + 8})" stroke="${INK}" stroke-width="4" stroke-linecap="round"/>`).join('')}`,
    talk: () => bubble(6, 14, 64, 40, '#3D8BFD', 'l', dots3(64, 40)) + bubble(48, 58, 66, 40, '#FF6FA5', 'r', dots3(66, 40)),
    say: () => `<g transform="translate(-10 26) scale(.85)">${figure('girl', {skin: SKIN[1]})}</g>`
       + bubble(50, 10, 64, 44, '#FF9F1C', 'l', `<text x="32" y="30" text-anchor="middle" font-size="22" ${FONT} fill="#fff">Hi!</text>`),
    speak: () => `<g transform="translate(-10 26) scale(.85)">${figure('boy')}</g>`
       + bubble(46, 8, 70, 46, '#2FA36B', 'l', `<text x="35" y="31" text-anchor="middle" font-size="20" ${FONT} fill="#fff">ABC</text>`),
    tell: () => `<g transform="translate(-10 26) scale(.85)">${figure('woman', {shirt: '#9B5DE5'})}</g>`
       + bubble(48, 8, 66, 48, '#5A67D8', 'l', `<path d="M14 16 q9 -4 19 0 v20 q-10 -4 -19 0z M33 16 q10 -4 19 0 v20 q-9 -4 -19 0z" fill="#fff"/>
          <path d="M33 16 v20" stroke="#5A67D8" stroke-width="2"/>`),
  });

  const GL = '#FFD23F';
  const footSide = (skin = SKIN[0]) => `<path d="M34 18 C36 40 34 62 30 76 C24 96 36 106 62 106 C84 106 104 104 106 94 C108 84 96 80 82 78 C66 76 58 66 56 50 C55 38 56 26 56 18Z" fill="${skin}"/>
      <path d="M34 18 h22" stroke="${SKIN[1]}" stroke-width="4" stroke-linecap="round"/>
      ${[[100, 92, 6], [91, 94, 4.5], [83, 96, 4], [76, 98, 3.5]].map(([x, y, r]) => `<circle cx="${x}" cy="${y - 6}" r="${r}" fill="${SKIN[1]}" opacity=".7"/>`).join('')}`;
  Object.assign(ART, {
    // ---------- ep08 body ----------
    body: () => kid({hl: 'body', shirt: '#FF7A59', s: 1.04}),
    head: () => `<circle cx="60" cy="44" r="34" fill="${GL}" opacity=".9"/>` + figure('boy', {skin: SKIN[0]}),
    hair: () => `<ellipse cx="60" cy="28" rx="36" ry="22" fill="${GL}" opacity=".9"/>` + figure('child', {skin: SKIN[1], hair: '#6B3E26'})
       + `<g transform="rotate(-25 98 26)"><rect x="86" y="18" width="26" height="8" rx="3" fill="#FF6FA5"/>
          ${[0, 1, 2, 3, 4].map(i => `<rect x="${88 + i * 5}" y="25" width="2.5" height="8" fill="#FF6FA5"/>`).join('')}</g>`,
    neck: () => figure('boy', {skin: SKIN[1], shirt: '#2BB3A3'}) + `<rect x="49" y="60" width="22" height="16" rx="7" fill="none" stroke="${GL}" stroke-width="5"/>`,
    shoulder: () => figure('person', {skin: SKIN[0], shirt: '#5A67D8'})
       + `<path d="M28 96 C30 82 40 74 52 72 M68 72 C80 74 90 82 92 96" stroke="${GL}" stroke-width="8" fill="none" stroke-linecap="round"/>`,
    arm: () => kid({hl: 'arm', dx: -8, la: [-12, -4], ra: [95, 175], shirt: '#E63946'}),
    hand: () => hand(60, 76, 2.3, 0, SKIN[0]),
    finger: () => `<circle cx="60" cy="24" r="14" fill="${GL}" opacity=".9"/>
       <path d="M53 66 V24 a7 7 0 0 1 14 0 V66" fill="${SKIN[0]}"/>
       <rect x="36" y="58" width="50" height="46" rx="18" fill="${SKIN[0]}"/>
       <path d="M44 72 h34 M44 84 h34" stroke="${SKIN[1]}" stroke-width="3" stroke-linecap="round"/>
       <path d="M36 74 C26 70 24 84 36 90" fill="${SKIN[0]}"/><rect x="40" y="100" width="40" height="16" rx="5" fill="#3D8BFD"/>`,
    leg: () => kid({hl: 'leg', rl: [14, 6], shirt: '#9B5DE5'}),
    knee: () => kid({hl: 'knee', ll: [-6, -4], rl: [40, -10], dx: -6, shirt: '#2FA36B'}),
    foot: () => footSide(),
    toe: () => `<ellipse cx="60" cy="74" rx="28" ry="38" fill="${SKIN[0]}"/>
       ${[[38, 34, 8], [50, 26, 7], [62, 24, 7], [74, 28, 6.5], [84, 38, 6]].map(([x, y, r], i) =>
         `<circle cx="${x}" cy="${y}" r="${r + 5}" fill="${GL}" opacity=".9"/><circle cx="${x}" cy="${y}" r="${r}" fill="${SKIN[0]}"/>
          <ellipse cx="${x}" cy="${y - 1}" rx="${r * .5}" ry="${r * .4}" fill="#fff" opacity=".6"/>`).join('')}`,
    shake: () => `<g transform="rotate(-15 60 70)">${hand(60, 74, 1.9, 0, SKIN[1])}</g>
       <path d="M18 46 q-10 14 0 28 M8 40 q-12 20 0 40 M102 46 q10 14 0 28 M112 40 q12 20 0 40" stroke="#3D8BFD" stroke-width="4.5" fill="none" stroke-linecap="round"/>`,
  });

  const pent = (cx, cy, R, rot, c) => `<path d="${Array.from({length: 5}, (_, i) => { const a = (rot + i * 72) * Math.PI / 180;
      return (i ? 'L' : 'M') + (cx + R * Math.cos(a)).toFixed(1) + ' ' + (cy + R * Math.sin(a)).toFixed(1); }).join('')}Z" fill="${c}"/>`;
  const soccerBall = (x, y, k = 1) => `<g transform="translate(${x} ${y}) scale(${k})"><circle r="40" fill="#fff" stroke="${INK}" stroke-width="4"/>
      ${pent(0, 0, 13, -90, INK)}
      ${Array.from({length: 5}, (_, i) => { const a = (-90 + i * 72) * Math.PI / 180, x2 = 31 * Math.cos(a), y2 = 31 * Math.sin(a);
        return `<path d="M${(13 * Math.cos(a)).toFixed(1)} ${(13 * Math.sin(a)).toFixed(1)} L${x2.toFixed(1)} ${y2.toFixed(1)}" stroke="${INK}" stroke-width="3"/>${pent(x2 * 1.08, y2 * 1.08, 9, -90 + i * 72 + 36, INK)}`; }).join('')}</g>`;
  Object.assign(ART, {
    // ---------- ep09 sports ----------
    sports: () =>
      `<path d="M30 18 h60 v18 c0 22 -14 36 -30 36 c-16 0 -30 -14 -30 -36z" fill="#FFB703"/>
       <path d="M30 26 c-18 0 -20 26 2 30 M90 26 c18 0 20 26 -2 30" stroke="#FFB703" stroke-width="6" fill="none"/>
       <rect x="54" y="70" width="12" height="16" fill="#E0A100"/><rect x="36" y="86" width="48" height="12" rx="3" fill="#E0A100"/>
       <rect x="30" y="98" width="60" height="12" rx="3" fill="#8D5A3B"/>${star(60, 40, 13, 5.5, '#fff')}`,
    race: () =>
      `<path d="M98 16 V112" stroke="#8A8FA3" stroke-width="4"/>
       ${[0, 1, 2, 3].map(r => [0, 1, 2].map(c => `<rect x="${100 + c * 6}" y="${16 + r * 6}" width="6" height="6" fill="${(r + c) % 2 ? '#fff' : INK}"/>`).join('')).join('')}
       <rect x="100" y="16" width="18" height="24" fill="none" stroke="${INK}" stroke-width="1.5"/>`
       + kid({s: .7, dx: -26, dy: 6, rot: 10, la: [-60, 30], ra: [55, 140], ll: [-40, -95], rl: [62, -4], shirt: '#3D8BFD'})
       + kid({s: .7, dx: 10, dy: 14, rot: 10, la: [-55, 35], ra: [60, 145], ll: [-30, -90], rl: [55, 0], shirt: '#E63946', skin: SKIN[1]}),
    jump: () => `<ellipse cx="60" cy="112" rx="26" ry="5" fill="#2B2D42" opacity=".15"/>`
       + kid({dy: -6, s: .92, la: [-160, -170], ra: [160, 170], ll: [-30, 20], rl: [30, -20], shirt: '#FF9F1C'})
       + `<path d="M40 104 v-8 M60 106 v-10 M80 104 v-8" stroke="#8A8FA3" stroke-width="3" stroke-linecap="round" opacity=".6"/>`,
    fall: () => `<path d="M8 108 H112" stroke="#C9C1B5" stroke-width="5" stroke-linecap="round"/>`
       + kid({rot: 78, dx: 6, dy: 22, s: .9, la: [-130, -160], ra: [130, 160], ll: [-25, -10], rl: [20, 40], shirt: '#5A67D8'})
       + star(28, 30, 8, 3.4, '#FFD23F') + star(46, 18, 6, 2.6, '#FFB703')
       + `<text x="98" y="38" text-anchor="middle" font-size="30" ${FONT} fill="#E63946">!</text>`,
    ball: () =>
      `<circle cx="60" cy="60" r="44" fill="#fff"/>
       <path d="M60 16 C40 30 36 90 60 104 C30 100 16 80 16 60 C16 36 36 18 60 16Z" fill="#E63946"/>
       <path d="M60 16 C84 30 84 90 60 104 C90 98 104 80 104 60 C104 36 84 18 60 16Z" fill="#3D8BFD"/>
       <path d="M60 16 C50 40 50 80 60 104 C70 80 70 40 60 16Z" fill="#FFD23F"/>
       <circle cx="60" cy="60" r="44" fill="none" stroke="${INK}" stroke-width="3" opacity=".25"/>
       <ellipse cx="44" cy="36" rx="10" ry="6" fill="#fff" opacity=".45" transform="rotate(-30 44 36)"/>`,
    football: () => soccerBall(60, 60, 1.1),
    soccer: () => kid({dx: -20, la: [-50, -20], ra: [40, 20], ll: [-4, -4], rl: [70, 40], shirt: '#2FA36B'}) + soccerBall(94, 98, .3),
    basketball: () =>
      `<circle cx="60" cy="60" r="44" fill="#F77F00"/>
       <path d="M16 60 H104 M60 16 V104 M30 28 C46 44 46 76 30 92 M90 28 C74 44 74 76 90 92" stroke="${INK}" stroke-width="3.5" fill="none"/>
       <ellipse cx="44" cy="36" rx="9" ry="5" fill="#fff" opacity=".3" transform="rotate(-30 44 36)"/>`,
    volleyball: () => { const c = ['M60 60 C60 38 72 22 94 28', 'M60 60 C42 72 22 70 16 52', 'M60 60 C78 72 84 92 70 104'];
      return `<circle cx="60" cy="60" r="44" fill="#fff"/>
       ${c.map((d, i) => `<path d="${d}" stroke="${['#3D8BFD', '#FFD23F', '#3D8BFD'][i]}" stroke-width="14" fill="none"/>`).join('')}
       ${c.map(d => `<path d="${d}" stroke="${INK}" stroke-width="3" fill="none"/>`).join('')}
       <circle cx="60" cy="60" r="44" fill="none" stroke="${INK}" stroke-width="3.5"/>`; },
    tabletennis: () =>
      `<g transform="rotate(-35 54 54)"><rect x="47" y="76" width="14" height="38" rx="5" fill="#C9653D"/>
       <circle cx="54" cy="50" r="32" fill="#E63946"/><circle cx="54" cy="50" r="32" fill="none" stroke="#9D0208" stroke-width="4"/></g>
       <circle cx="96" cy="26" r="11" fill="#FF9F1C"/><circle cx="92" cy="22" r="3.5" fill="#fff" opacity=".6"/>
       <path d="M80 40 q-6 6 -14 6" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-dasharray="3 4"/>`,
    net: () =>
      `<rect x="10" y="20" width="7" height="90" rx="3" fill="#8A8FA3"/><rect x="103" y="20" width="7" height="90" rx="3" fill="#8A8FA3"/>
       <rect x="17" y="26" width="86" height="8" fill="#fff" stroke="#C5CBE0" stroke-width="2"/>
       ${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `<path d="M${22 + i * 11} 34 V82" stroke="${INK}" stroke-width="1.6" opacity=".6"/>`).join('')}
       ${[0, 1, 2, 3, 4].map(i => `<path d="M17 ${40 + i * 10} H103" stroke="${INK}" stroke-width="1.6" opacity=".6"/>`).join('')}
       <rect x="17" y="82" width="86" height="5" fill="#fff" stroke="#C5CBE0" stroke-width="1.5"/>`,
  });

  const sockArt = (x, y, k, c, c2) => `<g transform="translate(${x} ${y}) scale(${k})">
      <path d="M-12 -44 h24 v46 c0 6 4 8 12 10 c12 3 14 22 0 24 h-22 c-12 0 -14 -10 -14 -22z" fill="${c}"/>
      <rect x="-14" y="-48" width="28" height="10" rx="3" fill="${c2}"/>
      <path d="M-12 -24 h24 M-12 -12 h24" stroke="${c2}" stroke-width="5"/>
      <path d="M12 28 c10 0 12 -8 10 -14" fill="none" stroke="${c2}" stroke-width="0"/></g>`;
  const tee = (c) => `<path d="M40 18 L16 30 L8 50 L28 58 L32 50 V106 H88 V50 L92 58 L112 50 L104 30 L80 18 Q60 30 40 18Z" fill="${c}"/>
      <path d="M40 18 Q60 30 80 18" stroke="#fff" stroke-width="4" fill="none" opacity=".6"/>`;
  Object.assign(ART, {
    // ---------- ep10 clothes ----------
    clothes: () =>
      `<path d="M60 8 a6 6 0 1 1 6 6 v6" stroke="#8A8FA3" stroke-width="3.5" fill="none" stroke-linecap="round"/>
       <path d="M60 22 L20 40 h80z" stroke="#8A8FA3" stroke-width="4" fill="none" stroke-linejoin="round"/>
       <g transform="translate(6 24) scale(.9)">${tee('#FF6FA5')}</g>
       <path d="M74 70 h34 l4 42 h-14 l-5 -28 l-5 28 h-14z" fill="#3D8BFD"/>`,
    wear: () => figure('boy', {shirt: '#2FA36B'})
       + `<path d="M14 88 C8 70 14 56 26 52 M106 88 C112 70 106 56 94 52" stroke="#FF7A59" stroke-width="5" fill="none" stroke-linecap="round"/>
          <path d="M26 52 l-10 0 M26 52 l-4 9 M94 52 l10 0 M94 52 l4 9" stroke="#FF7A59" stroke-width="5" stroke-linecap="round"/>
          ${star(18, 22, 8, 3.4, '#FFD23F')}${star(102, 18, 7, 3, '#FFD23F')}`,
    hat: () =>
      `<ellipse cx="60" cy="74" rx="54" ry="16" fill="#E9C27A"/>
       <path d="M30 72 C30 38 44 26 60 26 C76 26 90 38 90 72Z" fill="#F4D58D"/>
       <path d="M31 62 C46 68 74 68 89 62 L90 72 C74 78 46 78 30 72Z" fill="#E63946"/>
       <ellipse cx="60" cy="74" rx="54" ry="16" fill="none" stroke="#C9A35A" stroke-width="2.5"/>`,
    cap: () =>
      `<path d="M18 74 C18 40 38 26 62 26 C86 26 98 44 98 74Z" fill="#3D8BFD"/>
       <path d="M58 26 C52 40 52 60 54 74" stroke="#2A6FD6" stroke-width="3" fill="none"/>
       <path d="M90 66 C104 66 116 70 116 78 C116 84 98 84 86 80Z" fill="#2A6FD6"/>
       <rect x="16" y="70" width="84" height="10" rx="5" fill="#2A6FD6"/><circle cx="62" cy="26" r="5" fill="#2A6FD6"/>`,
    tshirt: () => tee('#FF9F1C') + star(60, 66, 15, 6.5, '#fff'),
    trousers: () =>
      `<path d="M30 12 h60 l8 98 h-26 l-12 -66 l-12 66 h-26z" fill="#3D5A80"/>
       <rect x="30" y="12" width="60" height="12" fill="#2C4363"/><path d="M60 24 v22" stroke="#2C4363" stroke-width="3"/>
       <path d="M40 24 q4 12 14 12 M80 24 q-4 12 -14 12" stroke="#5B7DB1" stroke-width="3" fill="none"/>`,
    pair: () => sockArt(38, 64, .95, '#FF6FA5', '#fff') + sockArt(78, 64, .95, '#FF6FA5', '#fff')
       + `<rect x="50" y="12" width="20" height="26" rx="4" fill="#FFB703"/><path d="M56 12 v-6 M64 12 v-6" stroke="#E0A100" stroke-width="4"/>
          <circle cx="98" cy="22" r="14" fill="#2FA36B"/><text x="98" y="30" text-anchor="middle" font-size="22" ${FONT} fill="#fff">2</text>`,
    underwear: () =>
      `<path d="M14 30 H106 V44 C92 50 80 66 74 92 H46 C40 66 28 50 14 44Z" fill="#7FC8F8"/>
       <rect x="14" y="28" width="92" height="12" rx="4" fill="#3D8BFD"/>
       ${[30, 50, 70, 90].map(x => `<circle cx="${x}" cy="60" r="3.5" fill="#fff" opacity=".8"/>`).join('')}`,
    sock: () => sockArt(54, 62, 1.15, '#2FA36B', '#FFD23F'),
    shoe: () => sneaker(60, 70, 1.9, '#E63946'),
  });

  Object.assign(ART, Object.fromEntries(Array.from({length: 9}, (_, i) => {
    // ---------- ep11 teens: big number + a ten-bar + extra dots ----------
    const k = i + 11, c = NUMC[i];
    return ['n' + k, () => `<text x="60" y="56" text-anchor="middle" font-size="58" ${FONT} fill="${c}" stroke="#fff" stroke-width="5" paint-order="stroke" letter-spacing="-3">${k}</text>
      <rect x="13" y="66" width="94" height="14" rx="4" fill="${c}" opacity=".28"/>
      ${Array.from({length: 10}, (_, j) => `<rect x="${15.5 + j * 9}" y="68.5" width="7" height="9" rx="2" fill="${c}" opacity=".75"/>`).join('')}
      ${Array.from({length: k - 10}, (_, j) => `<circle cx="${60 + (j - (k - 11) / 2) * 11}" cy="96" r="4.6" fill="${c}"/>`).join('')}`];
  })));

  function svg(name, plural) {
    const art = ART[name];
    if (!art) return `<div class="vp-emoji">${name}</div>`;
    const inner = plural
      ? `<g transform="translate(34 14) scale(.76)" opacity=".92">${art()}</g><g transform="translate(-4 20) scale(.8)">${art()}</g>`
      : art();
    return `<svg viewBox="0 0 120 120" aria-hidden="true">${inner}</svg>`;
  }

  window.VP_ICONS = {svg, names: Object.keys(ART)};
})();

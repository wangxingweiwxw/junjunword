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

  const thought = (x, y, w, h, inner) => `<g transform="translate(${x} ${y})">
      <circle cx="${-w * .42}" cy="${h * .78}" r="3.5" fill="#fff" stroke="#C5CBE0" stroke-width="2"/><circle cx="${-w * .3}" cy="${h * .6}" r="5.5" fill="#fff" stroke="#C5CBE0" stroke-width="2"/>
      <ellipse cx="0" cy="0" rx="${w / 2}" ry="${h / 2}" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>${inner}</g>`;
  const envelope = (x, y, k = 1, c = '#FF6FA5') => `<g transform="translate(${x} ${y}) scale(${k})">
      <rect x="-22" y="-15" width="44" height="30" rx="4" fill="#fff" stroke="${c}" stroke-width="3"/>
      <path d="M-21 -13 L0 3 L21 -13" stroke="${c}" stroke-width="3" fill="none" stroke-linejoin="round"/>${heart(0, 8, .45, c)}</g>`;
  const nope = (x, y, r) => `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="#E63946" stroke-width="7"/><path d="M${x - r * .7} ${y - r * .7} L${x + r * .7} ${y + r * .7}" stroke="#E63946" stroke-width="7"/>`;
  Object.assign(ART, {
    // ---------- ep12 birthday (2) ----------
    please: () => figure('girl', {shirt: '#2BB3A3'}) + `<ellipse cx="54" cy="96" rx="8" ry="11" fill="${SKIN[0]}"/><ellipse cx="66" cy="96" rx="8" ry="11" fill="${SKIN[0]}"/>
       <path d="M60 86 v20" stroke="${SKIN[1]}" stroke-width="2"/>${heart(98, 22, .8, '#FF4D6D')}${heart(22, 30, .55, '#FF9F1C')}`,
    invite: () => `<g transform="translate(-14 0)">${figure('boy', {shirt: '#3D8BFD'})}</g>${envelope(86, 82, 1.1)}
       <path d="M96 30 q8 8 0 16 M104 24 q12 14 0 28" stroke="#FF9F1C" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    invitation: () => `<g transform="rotate(-8 60 60)"><rect x="18" y="18" width="84" height="86" rx="8" fill="#FFF3C4" stroke="#E0A100" stroke-width="4"/>
       <text x="60" y="52" text-anchor="middle" font-size="17" ${FONT} fill="#E63946">PARTY!</text>
       <path d="M32 66 h56 M32 78 h40" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>
       <circle cx="84" cy="88" r="10" fill="#E63946"/>${star(84, 88, 6, 2.6, '#fff')}</g>${star(18, 16, 8, 3.4, '#FFB703')}`,
    guest: () => `<rect x="70" y="10" width="44" height="102" rx="4" fill="#B5703F"/><rect x="76" y="16" width="32" height="96" fill="#5A3825" opacity=".85"/>
       <circle cx="102" cy="64" r="3" fill="#FFD23F"/>
       <g transform="translate(-16 22) scale(.8)">${figure('woman', {shirt: '#9B5DE5'})}</g>
       <g transform="translate(22 34) scale(.7)">${figure('person', {shirt: '#FF9F1C', skin: SKIN[2]})}</g>`,
    celebrate: () => `<g transform="rotate(35 40 84)"><path d="M28 112 L40 52 L52 112Z" fill="#9B5DE5"/><path d="M33 90 h14 M36 74 h8" stroke="#FFD23F" stroke-width="5"/></g>
       ${[[70, 20, '#E63946', 20], [92, 36, '#3D8BFD', -30], [104, 62, '#2FA36B', 50], [80, 54, '#FFB703', 10], [58, 34, '#FF6FA5', -40], [100, 14, '#FF9F1C', 70]]
         .map(([x, y, c, r]) => `<rect x="${x - 6}" y="${y - 3}" width="12" height="6" rx="2" fill="${c}" transform="rotate(${r} ${x} ${y})"/>`).join('')}
       <path d="M56 58 q10 -24 30 -30 M62 66 q24 -8 40 4" stroke="#FF6FA5" stroke-width="3.5" fill="none" stroke-linecap="round"/>
       ${star(70, 88, 9, 4, '#FFD23F')}${star(32, 26, 7, 3, '#FFD23F')}`,
    among: () => [[30, 34], [90, 34], [30, 88], [90, 88], [60, 18], [60, 104], [16, 61], [104, 61]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="11" fill="#C5CBE0"/>`).join('')
       + `<circle cx="60" cy="61" r="24" fill="#FFD23F" opacity=".35"/>` + star(60, 61, 20, 8.5, '#FF9F1C'),
    without: () => `<g opacity=".35">${gift(30, 34, 60, 66, '#8A8FA3', '#C5CBE0')}</g>${nope(60, 66, 42)}`,
    age: () => `<rect x="16" y="8" width="26" height="104" rx="4" fill="#FFF3C4" stroke="#E0A100" stroke-width="3"/>
       ${[0, 1, 2, 3, 4, 5, 6, 7, 8].map(i => `<path d="M16 ${18 + i * 11} h${i % 2 ? 7 : 13}" stroke="#E0A100" stroke-width="2.5"/>`).join('')}
       ${kid({s: .78, dx: 22, dy: 14, shirt: '#3D8BFD'})}
       <circle cx="98" cy="24" r="17" fill="#E63946"/><text x="98" y="32" text-anchor="middle" font-size="22" ${FONT} fill="#fff">8</text>`,
    forget: () => `<g transform="translate(-18 20) scale(.85)">${figure('boy', {shirt: '#8A8FA3'})}</g>`
       + thought(84, 30, 54, 44, `<text x="0" y="12" text-anchor="middle" font-size="32" ${FONT} fill="#8A8FA3">?</text>`),
    remember: () => `<g transform="translate(-18 20) scale(.85)">${figure('girl', {shirt: '#2FA36B'})}</g>`
       + thought(84, 30, 54, 44, `<circle cx="0" cy="-2" r="11" fill="#FFD23F"/><rect x="-5" y="8" width="10" height="7" rx="2" fill="#8A8FA3"/>
          <path d="M-18 -16 l5 5 M18 -16 l-5 5 M0 -22 v6" stroke="#FFB703" stroke-width="3" stroke-linecap="round"/>`),
    remind: () => `<g transform="rotate(-6 50 64)"><rect x="12" y="24" width="68" height="70" rx="4" fill="#FFE66D"/>
       <path d="M12 82 l20 12 h-20z" fill="#E9C46A"/><circle cx="46" cy="26" r="6" fill="#E63946"/>
       <text x="46" y="76" text-anchor="middle" font-size="46" ${FONT} fill="#E63946">!</text></g>
       <g transform="translate(92 34)"><path d="M-14 8 a14 14 0 0 1 28 0 v6 l4 5 h-36 l4 -5z" fill="#FF9F1C"/><circle cy="22" r="4" fill="#FF9F1C"/>
       <path d="M-22 -6 q-4 8 0 16 M22 -6 q4 8 0 16" stroke="#FF9F1C" stroke-width="3" fill="none" stroke-linecap="round"/></g>`,
    excuse: () => kid({dx: -10, la: [-10, -4], ra: [170, 180], shirt: '#5A67D8'})
       + bubble(66, 44, 48, 32, '#FF9F1C', 'l', `<text x="24" y="22" text-anchor="middle" font-size="16" ${FONT} fill="#fff">...</text>`),

    // ---------- ep13 schoolbag ----------
    schoolbag: () => `<path d="M44 22 a16 14 0 0 1 32 0" stroke="#2A6FD6" stroke-width="6" fill="none"/>
       <rect x="22" y="24" width="76" height="88" rx="22" fill="#3D8BFD"/>
       <path d="M22 54 Q60 40 98 54" stroke="#2A6FD6" stroke-width="4" fill="none"/>
       <rect x="34" y="66" width="52" height="34" rx="10" fill="#7FB5FF"/><path d="M34 76 h52" stroke="#2A6FD6" stroke-width="3"/>
       <circle cx="60" cy="86" r="4" fill="#FFD23F"/>`,
    book: () => `<rect x="16" y="66" width="88" height="20" rx="4" fill="#E63946"/><rect x="22" y="70" width="76" height="12" fill="#fff" opacity=".85"/>
       <rect x="20" y="44" width="80" height="22" rx="4" fill="#2FA36B"/><rect x="26" y="48" width="68" height="14" fill="#fff" opacity=".85"/>
       <rect x="12" y="86" width="96" height="22" rx="4" fill="#3D8BFD"/><rect x="18" y="90" width="84" height="14" fill="#fff" opacity=".85"/>
       <rect x="30" y="20" width="60" height="24" rx="4" fill="#FF9F1C"/><rect x="36" y="24" width="48" height="16" fill="#fff" opacity=".85"/>`,
    dictionary: () => `<rect x="24" y="14" width="74" height="96" rx="6" fill="#5A67D8"/><rect x="24" y="14" width="14" height="96" rx="5" fill="#434FB8"/>
       <rect x="92" y="18" width="8" height="88" fill="#F1E3C8"/>
       <text x="66" y="62" text-anchor="middle" font-size="24" ${FONT} fill="#fff">A–Z</text>
       <path d="M48 76 h36 M52 86 h28" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/>`,
    notebook: () => `<rect x="24" y="12" width="76" height="98" rx="6" fill="#fff" stroke="#FF6FA5" stroke-width="4"/>
       ${[24, 40, 56, 72, 88].map(y => `<circle cx="24" cy="${y + 4}" r="6" fill="none" stroke="#8A8FA3" stroke-width="3"/>`).join('')}
       ${[34, 50, 66, 82, 98].map(y => `<path d="M40 ${y} h48" stroke="#C5CBE0" stroke-width="3" stroke-linecap="round"/>`).join('')}`,
    pen: () => `<g transform="rotate(40 60 60)"><rect x="52" y="6" width="16" height="84" rx="7" fill="#3D8BFD"/>
       <rect x="52" y="6" width="16" height="20" rx="7" fill="#2A6FD6"/><rect x="66" y="10" width="4" height="34" rx="2" fill="#8A8FA3"/>
       <path d="M52 88 L60 112 L68 88Z" fill="#C5CBE0"/><circle cx="60" cy="110" r="2.5" fill="#2A6FD6"/></g>`,
    pencil: () => pencil(60, 56, 1.5, 40),
    ruler: () => `<g transform="rotate(-30 60 60)"><rect x="4" y="44" width="112" height="30" rx="4" fill="#FFD23F" stroke="#E0A100" stroke-width="2"/>
       ${Array.from({length: 13}, (_, i) => `<path d="M${12 + i * 8} 44 v${i % 2 ? 7 : 12}" stroke="#8D5A3B" stroke-width="2"/>`).join('')}
       ${[0, 1, 2, 3].map(i => `<text x="${12 + i * 32}" y="68" text-anchor="middle" font-size="10" ${FONT} fill="#8D5A3B">${i}</text>`).join('')}</g>`,
    crayon: () => `<path d="M14 104 q16 -20 30 -6 t30 -8" stroke="#9B5DE5" stroke-width="6" fill="none" stroke-linecap="round"/>
       <g transform="rotate(40 66 50)"><rect x="56" y="18" width="20" height="70" rx="4" fill="#9B5DE5"/>
       <rect x="56" y="34" width="20" height="36" fill="#fff" opacity=".85"/><path d="M60 44 h12 M60 60 h12" stroke="#9B5DE5" stroke-width="3"/>
       <path d="M56 18 L66 0 L76 18Z" fill="#9B5DE5"/></g>`,
    paper: () => `<path d="M24 10 H80 L100 30 V112 H24Z" fill="#fff" stroke="#C5CBE0" stroke-width="4" stroke-linejoin="round"/>
       <path d="M80 10 V30 H100" fill="#E3E6F5" stroke="#C5CBE0" stroke-width="4" stroke-linejoin="round"/>
       ${[48, 62, 76, 90].map(y => `<path d="M36 ${y} h52" stroke="#E3E6F5" stroke-width="4" stroke-linecap="round"/>`).join('')}`,
    eraser: () => `<g transform="rotate(-20 60 64)"><rect x="18" y="44" width="84" height="40" rx="8" fill="#FF8FAB"/>
       <rect x="18" y="44" width="36" height="40" rx="8" fill="#3D8BFD"/><rect x="40" y="44" width="16" height="40" fill="#3D8BFD"/></g>
       <path d="M24 102 q20 -8 40 0" stroke="#C5CBE0" stroke-width="4" fill="none" stroke-dasharray="2 7" stroke-linecap="round"/>
       ${[[78, 100], [86, 108], [94, 98]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#FF8FAB"/>`).join('')}`,
  });

  const waves = (y, c = '#4CC9F0') => `<path d="M0 ${y} q10 -7 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 V120 H0Z" fill="${c}"/>
      <path d="M0 ${y + 14} q10 -7 20 0 t20 0 t20 0 t20 0 t20 0 t20 0" stroke="#fff" stroke-width="3" fill="none" opacity=".6"/>`;
  const bigFace = (skin = SKIN[0], hair = '#3B2A20') => `<circle cx="60" cy="64" r="42" fill="${skin}"/>` + cap(60, 64, 42, hair).replace(/fill=/, 'fill=');
  Object.assign(ART, {
    // ---------- ep15 sports (2) ----------
    coach: () => figure('man', {skin: SKIN[1], shirt: '#2BB3A3', cap: '#E63946'})
       + `<path d="M50 62 L60 86 L70 62" stroke="#8A8FA3" stroke-width="2" fill="none"/>
          <rect x="54" y="84" width="16" height="10" rx="4" fill="#8A8FA3"/><circle cx="70" cy="89" r="3" fill="#C5CBE0"/>`,
    encourage: () => `<g transform="translate(-20 4) scale(.92)">${figure('woman', {shirt: '#FF9F1C'})}</g>
       <g transform="translate(46 42) scale(.62)">${figure('child', {shirt: '#3D8BFD'})}</g>
       <path d="M52 86 Q66 70 78 70" stroke="${SKIN[0]}" stroke-width="8" fill="none" stroke-linecap="round"/>`
       + bubble(66, 4, 50, 32, '#2FA36B', 'l', `<text x="25" y="22" text-anchor="middle" font-size="16" ${FONT} fill="#fff">Go!</text>`),
    spirit: () => `<path d="M60 112 C30 112 16 90 22 66 C26 50 38 44 36 24 C50 34 52 46 50 54 C58 40 64 22 60 6 C82 22 98 46 98 72 C98 96 84 112 60 112Z" fill="#FF7A59"/>
       <path d="M60 110 C42 110 34 96 38 82 C42 72 50 70 50 60 C60 68 62 76 60 82 C68 76 72 66 70 56 C82 66 86 80 84 90 C82 102 74 110 60 110Z" fill="#FFD23F"/>
       ${heart(60, 92, .7, '#E63946')}`,
    choose: () => `<rect x="8" y="22" width="30" height="30" rx="8" fill="#C5CBE0"/><circle cx="60" cy="37" r="17" fill="#FF9F1C"/>
       <path d="M82 52 L97 22 L112 52Z" fill="#C5CBE0"/>
       <circle cx="60" cy="37" r="24" fill="none" stroke="#2FA36B" stroke-width="4"/>
       <g transform="translate(60 92) rotate(0)">${hand(0, 0, .95, 0, SKIN[0])}</g>${check(88, 88, 1.2)}`,
    throw: () => kid({dx: -18, rot: -6, la: [-40, -20], ra: [120, 150], ll: [-14, -4], rl: [18, 6], shirt: '#E63946'})
       + `<path d="M64 26 Q86 6 104 22" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-dasharray="4 5"/>
          <circle cx="104" cy="28" r="9" fill="#fff" stroke="#E63946" stroke-width="2.5"/>`,
    baseball: () => `<circle cx="60" cy="60" r="44" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <path d="M30 26 C44 44 44 76 30 94 M90 26 C76 44 76 76 90 94" stroke="#E63946" stroke-width="3" fill="none"/>
       ${[0, 1, 2, 3, 4, 5].map(i => { const y = 36 + i * 9.5; const x1 = 38 - Math.abs(y - 60) * .15, x2 = 82 + Math.abs(y - 60) * .15;
         return `<path d="M${x1 - 4} ${y - 3} l8 6 M${x2 + 4} ${y - 3} l-8 6" stroke="#E63946" stroke-width="2.4"/>`; }).join('')}`,
    hit: () => `<g transform="rotate(-40 40 80)"><path d="M34 112 L40 30 Q44 14 50 30 L54 112Z" fill="#C9653D"/><rect x="34" y="96" width="20" height="16" rx="3" fill="#2B2D42"/></g>
       ${star(86, 34, 22, 10, '#FFD23F', -20)}<circle cx="86" cy="34" r="11" fill="#fff" stroke="#E63946" stroke-width="2.5"/>
       <path d="M104 18 l8 -6 M108 34 h10 M104 50 l8 6" stroke="#FF9F1C" stroke-width="3.5" stroke-linecap="round"/>`,
    training: () => kid({la: [-160, -172], ra: [160, 172], shirt: '#FF7A59', dy: 6})
       + `<rect x="24" y="18" width="72" height="6" rx="3" fill="#6B7085"/>
          <rect x="16" y="8" width="10" height="26" rx="3" fill="#2B2D42"/><rect x="94" y="8" width="10" height="26" rx="3" fill="#2B2D42"/>
          <path d="M30 60 q-4 6 0 10 M90 60 q4 6 0 10" stroke="#7FC8F8" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    strong: () => `<path d="M14 104 L14 76 Q16 60 40 58 L62 56 Q70 30 78 22 Q92 14 98 26 Q104 40 92 50 Q84 74 70 82 L44 92 Q34 100 30 104Z" fill="${SKIN[1]}"/>
       <path d="M44 62 Q60 46 74 56" stroke="#C98F68" stroke-width="3" fill="none"/><rect x="8" y="90" width="26" height="22" rx="4" fill="#E63946"/>
       ${star(104, 72, 9, 4, '#FFD23F')}${star(26, 30, 7, 3, '#FFD23F')}`,
    weak: () => `<rect x="14" y="32" width="84" height="56" rx="10" fill="#fff" stroke="#8A8FA3" stroke-width="5"/>
       <rect x="98" y="48" width="10" height="24" rx="3" fill="#8A8FA3"/><rect x="21" y="39" width="16" height="42" rx="4" fill="#E63946"/>
       <circle cx="58" cy="56" r="3.5" fill="${INK}"/><circle cx="76" cy="56" r="3.5" fill="${INK}"/>
       <path d="M58 74 q9 -7 18 0" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
       <path d="M86 26 q4 8 0 12 q-4 -4 0 -12z" fill="#7FC8F8"/>`,
    quick: () => `${sneaker(70, 78, 1.5, '#FF9F1C')}<path d="M8 64 h28 M2 80 h30 M10 96 h24" stroke="#8A8FA3" stroke-width="5" stroke-linecap="round" opacity=".6"/>
       <path d="M78 6 L60 40 H76 L64 62 L96 26 H80 L90 6Z" fill="#FFD23F" stroke="#E0A100" stroke-width="2" stroke-linejoin="round"/>`,
    swim: () => `${waves(70)}<circle cx="48" cy="62" r="17" fill="${SKIN[0]}"/>${cap(48, 62, 17, '#E63946')}
       <rect x="34" y="58" width="28" height="9" rx="4.5" fill="#3D8BFD"/><circle cx="41" cy="62" r="4" fill="#BDE7FF"/><circle cx="55" cy="62" r="4" fill="#BDE7FF"/>
       <path d="M64 70 Q78 30 102 46" stroke="${SKIN[0]}" stroke-width="8" fill="none" stroke-linecap="round"/>
       <path d="M20 54 q-6 -6 -2 -12 M100 66 q6 -4 4 -10" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    swimming: () => `${waves(46)}${[66, 90, 112].map(y => `<path d="M0 ${y} H120" stroke="#E63946" stroke-width="4" stroke-dasharray="8 6"/>`).join('')}
       <g transform="translate(60 26)"><path d="M-44 0 H44" stroke="#2B2D42" stroke-width="4"/>
       <ellipse cx="-17" cy="0" rx="16" ry="13" fill="#3D8BFD"/><ellipse cx="17" cy="0" rx="16" ry="13" fill="#3D8BFD"/>
       <ellipse cx="-17" cy="0" rx="10" ry="8" fill="#BDE7FF"/><ellipse cx="17" cy="0" rx="10" ry="8" fill="#BDE7FF"/>
       <path d="M-3 0 h6" stroke="#2B2D42" stroke-width="4"/></g>`,

    // ---------- ep16 body (2) ----------
    face: () => `<circle cx="60" cy="62" r="44" fill="${SKIN[0]}"/>` + cap(60, 62, 44, '#3B2A20')
       + `<circle cx="44" cy="66" r="5" fill="${INK}"/><circle cx="76" cy="66" r="5" fill="${INK}"/>
          <path d="M58 70 q2 8 -2 10" stroke="#C98F68" stroke-width="3" fill="none" stroke-linecap="round"/>
          <path d="M46 86 q14 12 28 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
          <ellipse cx="34" cy="80" rx="7" ry="4" fill="${BLUSH}" opacity=".7"/><ellipse cx="86" cy="80" rx="7" ry="4" fill="${BLUSH}" opacity=".7"/>`,
    eye: () => `<path d="M22 36 Q60 18 98 36" stroke="#3B2A20" stroke-width="7" fill="none" stroke-linecap="round"/>
       <path d="M12 68 Q60 26 108 68 Q60 106 12 68Z" fill="#fff" stroke="${INK}" stroke-width="4"/>
       <circle cx="60" cy="68" r="22" fill="#8D5A3B"/><circle cx="60" cy="68" r="10" fill="${INK}"/><circle cx="67" cy="61" r="5" fill="#fff"/>`,
    nose: () => `<circle cx="60" cy="60" r="50" fill="${SKIN[0]}" opacity=".5"/>
       <path d="M56 18 C56 46 40 64 36 78 C32 92 46 98 60 98 C74 98 88 92 84 78 C80 64 64 46 64 18Z" fill="${SKIN[0]}" stroke="#C98F68" stroke-width="3"/>
       <ellipse cx="50" cy="86" rx="6" ry="4" fill="#C98F68"/><ellipse cx="70" cy="86" rx="6" ry="4" fill="#C98F68"/>`,
    ear: () => `<path d="M40 30 C40 6 92 2 94 40 C96 62 80 66 76 80 C72 96 62 110 48 106 C36 102 38 90 42 84" fill="${SKIN[0]}" stroke="#C98F68" stroke-width="3"/>
       <path d="M54 38 C56 22 82 22 82 42 C82 54 70 58 66 66 C62 74 66 82 58 86" stroke="#C98F68" stroke-width="4" fill="none" stroke-linecap="round"/>
       <path d="M100 28 q8 10 0 20 M108 20 q14 18 0 36" stroke="#3D8BFD" stroke-width="3.5" fill="none" stroke-linecap="round"/>`,
    mouth: () => `<path d="M14 52 Q60 40 106 52 Q96 104 60 104 Q24 104 14 52Z" fill="#9D0208"/>
       <path d="M22 54 Q60 46 98 54 L96 64 Q60 58 24 64Z" fill="#fff"/>
       <path d="M36 92 Q60 72 84 92 Q72 102 60 102 Q48 102 36 92Z" fill="#FF6FA5"/>
       <path d="M10 52 Q60 30 110 52 Q60 44 10 52Z M12 54 Q24 108 60 108 Q96 108 108 54 Q98 100 60 100 Q22 100 12 54Z" fill="#E63946"/>`,
    tooth: () => `<path d="M26 30 C26 12 46 12 60 20 C74 12 94 12 94 30 C94 52 86 60 84 80 C82 100 76 110 70 108 C64 106 64 84 60 84 C56 84 56 106 50 108 C44 110 38 100 36 80 C34 60 26 52 26 30Z"
         fill="#fff" stroke="#C5CBE0" stroke-width="4"/>
       <circle cx="48" cy="44" r="3.5" fill="${INK}"/><circle cx="72" cy="44" r="3.5" fill="${INK}"/>
       <path d="M52 56 q8 6 16 0" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
       <path d="M36 28 q4 -8 12 -8" stroke="#BDE7FF" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    tongue: () => `<circle cx="60" cy="56" r="44" fill="${SKIN[1]}"/>` + cap(60, 56, 44, '#3B2A20')
       + `<path d="M44 52 q6 -6 12 0 M64 52 q6 -6 12 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
          <path d="M38 76 Q60 88 82 76" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
          <path d="M48 78 Q48 110 60 110 Q72 110 72 78Z" fill="#FF6FA5" stroke="#E63946" stroke-width="2.5"/><path d="M60 82 v18" stroke="#E63946" stroke-width="2.5"/>`,
    chin: () => `<circle cx="60" cy="54" r="44" fill="${SKIN[0]}"/>` + cap(60, 54, 44, '#6B3E26')
       + `<circle cx="44" cy="58" r="4.5" fill="${INK}"/><circle cx="76" cy="58" r="4.5" fill="${INK}"/>
          <path d="M48 76 q12 8 24 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
          <path d="M34 92 Q60 112 86 92" stroke="#FFD23F" stroke-width="9" fill="none" stroke-linecap="round"/>`,
    throat: () => figure('boy', {skin: SKIN[0], shirt: '#5A67D8'})
       + `<path d="M54 66 v10 M66 66 v10" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/><circle cx="60" cy="72" r="4" fill="#FFD23F"/>
          <path d="M86 58 q8 6 0 12 M94 52 q14 12 0 24" stroke="#FF9F1C" stroke-width="3.5" fill="none" stroke-linecap="round"/>`,
    chest: () => `<rect x="30" y="76" width="60" height="34" rx="14" fill="#FFD23F" opacity=".9"/>` + figure('person', {skin: SKIN[1], shirt: '#2BB3A3'})
       + heart(60, 92, .75, '#E63946'),
    mind: () => `<path d="M30 112 V84 C14 76 12 52 20 36 C30 14 60 6 80 14 C100 22 108 44 102 62 L110 76 L100 80 V96 Q100 104 90 104 H78 V112Z" fill="#C5CBE0"/>
       <circle cx="62" cy="48" r="20" fill="#FFD23F"/><rect x="55" y="66" width="14" height="10" rx="3" fill="#8A8FA3"/>
       <path d="M62 18 v-8 M38 26 l-6 -6 M86 26 l6 -6" stroke="#FFB703" stroke-width="4" stroke-linecap="round"/>`,
    brain: () => `<path d="M24 60 C14 44 26 24 42 26 C46 12 70 10 76 22 C92 18 106 34 98 48 C110 58 104 82 88 82 C86 96 66 100 58 92 C46 100 28 92 30 80 C18 76 16 66 24 60Z" fill="#FF8FAB" stroke="#E56B8A" stroke-width="3"/>
       <path d="M60 24 C54 40 66 50 58 62 C52 72 62 82 58 92 M36 44 q10 0 12 10 M84 40 q-10 4 -8 14 M36 70 q10 -4 16 4 M80 66 q-6 8 4 14" stroke="#E56B8A" stroke-width="3.5" fill="none" stroke-linecap="round"/>
       <path d="M60 92 v18" stroke="#E56B8A" stroke-width="6" stroke-linecap="round"/>`,
  });

  const mini = (name, x, y, k) => `<g transform="translate(${x - 60 * k} ${y - 60 * k}) scale(${k})">${ART[name]()}</g>`;
  const note = (x, y, c) => `<g transform="translate(${x} ${y})"><path d="M0 0 V-18 l10 -3 V-4" stroke="${c}" stroke-width="3" fill="none"/>
      <ellipse cx="-3" cy="0" rx="5" ry="4" fill="${c}"/><ellipse cx="7" cy="-3" rx="5" ry="4" fill="${c}"/></g>`;
  const badge = (x, y, kind) => {
    const b = {pig: `<circle r="15" fill="#FFB3C6"/><ellipse cy="4" rx="8" ry="6" fill="#FF8FAB"/><circle cx="-3" cy="4" r="1.6" fill="${INK}"/><circle cx="3" cy="4" r="1.6" fill="${INK}"/>
                     <circle cx="-6" cy="-5" r="1.8" fill="${INK}"/><circle cx="6" cy="-5" r="1.8" fill="${INK}"/><path d="M-14 -10 l4 -8 l4 6z M14 -10 l-4 -8 l-4 6z" fill="#FF8FAB"/>`,
               cow: `<path d="M-14 -12 q-6 -6 -2 -10 M14 -12 q6 -6 2 -10" stroke="#C9B8A6" stroke-width="4" fill="none" stroke-linecap="round"/>
                     <circle r="15" fill="#fff" stroke="#C5CBE0" stroke-width="2"/><ellipse cx="-6" cy="-6" rx="5" ry="4" fill="${INK}"/>
                     <ellipse cy="6" rx="9" ry="6" fill="#FFB3C6"/><circle cx="-3" cy="6" r="1.5" fill="${INK}"/><circle cx="3" cy="6" r="1.5" fill="${INK}"/><circle cx="6" cy="-4" r="1.8" fill="${INK}"/>`,
               sheep: `${[[-10, -8], [0, -13], [10, -8], [-12, 2], [12, 2]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="7" fill="#fff" stroke="#E3E6F5" stroke-width="1.5"/>`).join('')}
                     <ellipse cy="3" rx="9" ry="10" fill="#5A4636"/><circle cx="-3.5" cy="1" r="1.6" fill="#fff"/><circle cx="3.5" cy="1" r="1.6" fill="#fff"/>`}[kind];
    return `<g transform="translate(${x} ${y})"><circle r="18" fill="#fff" opacity=".9"/>${b}</g>`;
  };
  Object.assign(ART, {
    // ---------- ep17 senses ----------
    sense: () => `<circle cx="60" cy="60" r="18" fill="#FFD23F"/>${star(60, 60, 12, 5, '#fff')}`
       + [['eye', 0], ['ear', 72], ['nose', 144], ['tongue', 216], ['hand', 288]].map(([n, a]) => {
           const r = (a - 90) * Math.PI / 180, x = 60 + 40 * Math.cos(r), y = 60 + 40 * Math.sin(r);
           return `<circle cx="${x}" cy="${y}" r="19" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>` + (n === 'hand' ? hand(x, y + 3, .55) : mini(n, x, y, .3)); }).join(''),
    sight: () => `<rect x="22" y="8" width="76" height="104" rx="6" fill="#fff" stroke="#C5CBE0" stroke-width="4"/>
       ${[[30, 36, 0], [20, 64, 1], [14, 84, 2], [10, 100, 3]].map(([fs, y, i]) => `<text x="60" y="${y}" text-anchor="middle" font-size="${fs}" ${FONT} fill="${INK}" letter-spacing="${i * 2}">${['E', 'F P', 'T O Z', 'L P E D'][i]}</text>`).join('')}`,
    hear: () => mini('ear', 48, 62, .9).replace(/stroke="#3D8BFD"[^/]*\/>/g, '/>') + note(96, 40, '#9B5DE5') + note(98, 86, '#FF6FA5'),
    listen: () => `<path d="M22 70 V58 a38 38 0 0 1 76 0 V70" stroke="#2B2D42" stroke-width="8" fill="none"/>
       <rect x="12" y="62" width="24" height="40" rx="10" fill="#E63946"/><rect x="84" y="62" width="24" height="40" rx="10" fill="#E63946"/>
       ${note(64, 96, '#3D8BFD')}`,
    hearing: () => `${[30, 42, 54].map((r, i) => `<circle cx="60" cy="60" r="${r}" fill="none" stroke="#3D8BFD" stroke-width="3" opacity="${.6 - i * .18}"/>`).join('')}`
       + mini('ear', 58, 62, .48).replace(/stroke="#3D8BFD"[^/]*\/>/g, '/>'),
    smell: () => mini('nose', 40, 70, .62)
       + `<path d="M58 54 q8 -8 0 -16 t0 -16 M70 58 q8 -8 0 -16 t0 -16" stroke="#9B5DE5" stroke-width="3.5" fill="none" stroke-linecap="round" opacity=".7"/>`
       + mini('flower', 94, 70, .45),
    taste: () => `<path d="M76 66 L92 112 L108 66Z" fill="#E9A66B"/><path d="M80 74 l24 0 M84 86 l16 0" stroke="#C9653D" stroke-width="2"/>
       <circle cx="84" cy="56" r="14" fill="#FF8FAB"/><circle cx="100" cy="58" r="13" fill="#BDE7FF"/><circle cx="92" cy="44" r="13" fill="#FFE08A"/>`
       + mini('tongue', 40, 60, .62),
    salty: () => `<path d="M38 50 h44 l6 60 h-56z" fill="#fff" stroke="#C5CBE0" stroke-width="4"/>
       <path d="M40 26 h40 l2 24 h-44z" fill="#8A8FA3"/>${[[50, 34], [60, 31], [70, 34], [55, 42], [65, 42]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="2" fill="#fff"/>`).join('')}
       <text x="60" y="90" text-anchor="middle" font-size="20" ${FONT} fill="#3D8BFD">SALT</text>
       ${[[24, 14], [94, 18], [100, 34], [18, 30]].map(([x, y]) => `<rect x="${x}" y="${y}" width="4" height="4" fill="#C5CBE0" transform="rotate(30 ${x} ${y})"/>`).join('')}`,
    sweet: () => `<path d="M26 60 L6 44 L10 76Z M94 60 L114 44 L110 76Z" fill="#FF6FA5"/>
       <ellipse cx="60" cy="60" rx="36" ry="26" fill="#FF6FA5"/>
       <path d="M36 44 Q48 60 36 76 M52 36 Q64 60 52 84 M68 36 Q80 60 68 84 M84 44 Q96 60 84 76" stroke="#fff" stroke-width="5" fill="none" opacity=".7"/>`,
    sour: () => `<ellipse cx="54" cy="64" rx="40" ry="32" fill="#FFE066" transform="rotate(-20 54 64)"/>
       <path d="M90 46 q12 -6 14 -18" stroke="#FFE066" stroke-width="8" stroke-linecap="round"/>
       <path d="M90 36 q12 -18 26 -14 q-6 14 -26 14z" fill="#6CCB5F"/>
       <circle cx="40" cy="58" r="3.5" fill="${INK}"/><circle cx="62" cy="52" r="3.5" fill="${INK}"/>
       <path d="M34 50 l10 4 M68 44 l-10 5" stroke="${INK}" stroke-width="2.6" stroke-linecap="round"/>
       <circle cx="54" cy="74" r="5" fill="none" stroke="${INK}" stroke-width="2.6"/>`,
    bitter: () => `<rect x="70" y="30" width="34" height="62" rx="8" fill="#8D5A3B"/><rect x="74" y="20" width="26" height="12" rx="3" fill="#fff" stroke="#C5CBE0" stroke-width="2"/>
       <rect x="74" y="50" width="26" height="22" rx="3" fill="#fff"/><path d="M87 54 v14 M80 61 h14" stroke="#E63946" stroke-width="3.5"/>
       <path d="M8 84 q22 10 44 0 l14 -6" stroke="#8A8FA3" stroke-width="5" fill="none" stroke-linecap="round"/>
       <ellipse cx="30" cy="82" rx="22" ry="8" fill="#C5CBE0"/><ellipse cx="30" cy="81" rx="16" ry="5" fill="#5A3825"/>
       <circle cx="32" cy="38" r="22" fill="${SKIN[0]}"/>
       <path d="M20 32 l7 3 M44 32 l-7 3" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
       <path d="M22 48 q5 -5 10 0 t10 0" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    touch: () => `${[18, 30, 42].map((r, i) => `<ellipse cx="60" cy="96" rx="${r * 1.3}" ry="${r * .4}" fill="none" stroke="#3D8BFD" stroke-width="3" opacity="${.7 - i * .2}"/>`).join('')}
       <rect x="8" y="94" width="104" height="4" rx="2" fill="#C5CBE0" opacity=".6"/>
       <g transform="rotate(180 60 56)">${ART.finger().replace(/<circle cx="60" cy="24" r="14"[^>]*>/, '')}</g>`,
    feel: () => hand(48, 76, 1.5, -15, SKIN[0]) + heart(94, 38, 1, '#FF4D6D') + star(92, 82, 8, 3.4, '#FFD23F') + star(24, 26, 7, 3, '#FFD23F'),

    // ---------- ep18 food ----------
    food: () => `<ellipse cx="60" cy="72" rx="44" ry="30" fill="#fff" stroke="#C5CBE0" stroke-width="4"/>
       <circle cx="46" cy="64" r="12" fill="#E63946"/><path d="M46 52 q2 -6 6 -6" stroke="#3FA34D" stroke-width="3" fill="none"/>
       <rect x="58" y="58" width="24" height="18" rx="6" fill="#E9A66B"/><circle cx="64" cy="82" r="7" fill="#6CCB5F"/>
       <path d="M8 40 v28 M4 40 v12 M12 40 v12 M4 52 h8" stroke="#8A8FA3" stroke-width="3" stroke-linecap="round"/>
       <path d="M112 40 v34 M112 40 q-8 10 0 22" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    eat: () => `<g transform="translate(-14 0)">${figure('boy', {shirt: '#FF9F1C'})}</g>
       <path d="M42 86 Q70 104 98 86Z" fill="#fff" stroke="#3D8BFD" stroke-width="3"/><ellipse cx="70" cy="86" rx="28" ry="5" fill="#F4F1E8"/>
       <path d="M88 82 L58 60" stroke="#8A8FA3" stroke-width="4" stroke-linecap="round"/><ellipse cx="56" cy="58" rx="6" ry="4" fill="#8A8FA3"/>`,
    hungry: () => figure('child', {shirt: '#9B5DE5'}) + `<path d="M46 94 q4 -4 8 0 t8 0 t8 0" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>
       <path d="M52 66 q4 6 0 12" stroke="#7FC8F8" stroke-width="3" fill="none" stroke-linecap="round"/>
       <ellipse cx="96" cy="96" rx="20" ry="6" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <text x="96" y="80" text-anchor="middle" font-size="26" ${FONT} fill="#8A8FA3">?</text>`,
    full: () => figure('person', {shirt: '#2FA36B'}) + `<ellipse cx="60" cy="102" rx="30" ry="18" fill="#2FA36B"/><ellipse cx="60" cy="100" rx="22" ry="12" fill="#45C17E"/>
       <path d="M52 47 q4 3 8 0 M64 47 q4 3 8 0" stroke="${INK}" stroke-width="0"/>
       ${heart(98, 30, .6, '#FF6FA5')}<circle cx="98" cy="52" r="4" fill="#C5CBE0"/><circle cx="104" cy="62" r="2.5" fill="#C5CBE0"/>`,
    meal: () => `<rect x="6" y="40" width="108" height="66" rx="12" fill="#E9A66B"/><rect x="12" y="46" width="96" height="54" rx="8" fill="#F4C99B"/>
       <path d="M18 74 a18 14 0 0 0 36 0z" fill="#fff" stroke="#3D8BFD" stroke-width="2.5"/><ellipse cx="36" cy="72" rx="16" ry="5" fill="#fff"/>
       <circle cx="78" cy="70" r="18" fill="#fff" stroke="#C5CBE0" stroke-width="2.5"/><circle cx="74" cy="66" r="6" fill="#6CCB5F"/><rect x="78" y="68" width="10" height="8" rx="3" fill="#C9653D"/>
       <rect x="24" y="86" width="2" height="0"/><path d="M58 50 L102 50 M58 56 L102 54" stroke="#C9653D" stroke-width="3" stroke-linecap="round"/>`,
    rice: () => `<path d="M58 34 L96 6 M66 36 L102 12" stroke="#C9653D" stroke-width="4" stroke-linecap="round"/>
       <path d="M18 60 h84 a42 46 0 0 1 -84 0z" fill="#fff" stroke="#3D8BFD" stroke-width="4"/>
       <path d="M22 62 Q22 34 60 32 Q98 34 98 62Z" fill="#fff"/>${[[40, 50], [52, 42], [64, 44], [76, 50], [48, 56], [70, 56], [60, 52]].map(([x, y]) =>
         `<ellipse cx="${x}" cy="${y}" rx="3" ry="1.8" fill="#E3E6F5"/>`).join('')}
       <path d="M30 80 h60" stroke="#3D8BFD" stroke-width="3" opacity=".4"/>`,
    meat: () => `<rect x="70" y="72" width="34" height="12" rx="6" fill="#F4EBD9" transform="rotate(35 70 72)"/>
       <circle cx="102" cy="98" r="8" fill="#F4EBD9"/><circle cx="96" cy="104" r="8" fill="#F4EBD9"/>
       <ellipse cx="50" cy="52" rx="38" ry="32" fill="#C1440E"/><ellipse cx="46" cy="48" rx="28" ry="22" fill="#E07A4F"/>
       <path d="M30 40 q10 -6 22 0" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" opacity=".5"/>`,
    chicken: () => `<ellipse cx="58" cy="94" rx="50" ry="10" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <ellipse cx="56" cy="66" rx="40" ry="28" fill="#E9A66B"/><ellipse cx="50" cy="60" rx="28" ry="18" fill="#F4C99B"/>
       <path d="M86 62 l18 -16" stroke="#E9A66B" stroke-width="12" stroke-linecap="round"/><circle cx="106" cy="42" r="6" fill="#fff"/><circle cx="110" cy="48" r="6" fill="#fff"/>
       <path d="M26 66 l-14 -12" stroke="#E9A66B" stroke-width="12" stroke-linecap="round"/><circle cx="10" cy="50" r="6" fill="#fff"/>`,
    pork: () => `<path d="M14 70 C14 44 40 34 66 38 C94 42 108 62 98 82 C88 102 30 104 14 70Z" fill="#FF8FAB"/>
       <path d="M24 70 C24 52 44 46 64 48 C86 50 94 64 88 78 C80 92 36 92 24 70Z" fill="#FFC2D1"/>
       <path d="M30 66 C46 62 60 74 78 68" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/>${badge(96, 26, 'pig')}`,
    beef: () => `<path d="M12 64 C10 40 40 30 64 34 C92 38 110 56 104 78 C98 100 40 104 22 88 C14 82 12 74 12 64Z" fill="#9D0208"/>
       <path d="M22 64 C22 46 44 42 62 44 C86 46 96 60 92 74 C86 90 42 92 30 82 C24 78 22 72 22 64Z" fill="#C1121F"/>
       <path d="M36 58 C50 70 70 52 86 64 M40 76 C56 72 66 82 82 76" stroke="#FFB3C6" stroke-width="4" fill="none" stroke-linecap="round"/>${badge(96, 26, 'cow')}`,
    mutton: () => `<path d="M12 104 L84 32" stroke="#C9653D" stroke-width="5" stroke-linecap="round"/>
       ${[[34, 82], [52, 64], [70, 46]].map(([x, y]) => `<rect x="${x - 12}" y="${y - 10}" width="24" height="20" rx="7" fill="#B5703F" transform="rotate(-45 ${x} ${y})"/>
         <rect x="${x - 8}" y="${y - 6}" width="16" height="12" rx="5" fill="#D99058" transform="rotate(-45 ${x} ${y})"/>`).join('')}${badge(96, 26, 'sheep')}`,
    oil: () => `<path d="M48 12 h24 v14 h-24z" fill="#E0A100"/><path d="M50 26 h20 q20 10 20 30 v46 q0 10 -10 10 h-40 q-10 0 -10 -10 v-46 q0 -20 20 -30z" fill="#FFD23F" opacity=".9"/>
       <rect x="36" y="58" width="48" height="30" rx="6" fill="#fff"/><path d="M60 64 C66 72 68 76 60 82 C52 76 54 72 60 64Z" fill="#FFB703"/>
       <path d="M42 40 q-4 20 0 40" stroke="#fff" stroke-width="4" fill="none" opacity=".6" stroke-linecap="round"/>`,
    spicy: () => `<path d="M30 30 C20 60 40 100 90 108 C110 110 112 98 96 92 C62 80 54 56 52 34Z" fill="#E63946"/>
       <path d="M30 30 C34 22 48 22 52 34 C46 30 38 30 30 30Z" fill="#3FA34D"/><path d="M42 26 q0 -12 8 -16" stroke="#3FA34D" stroke-width="5" fill="none" stroke-linecap="round"/>
       <path d="M40 46 C42 64 52 80 70 90" stroke="#fff" stroke-width="4" fill="none" opacity=".5" stroke-linecap="round"/>
       ${flame(90, 50, 1.1)}${flame(108, 66, .7)}`,
  });

  const cloud = (x, y, k = 1, c = '#fff', st = '#C5CBE0') => `<g transform="translate(${x} ${y}) scale(${k})">
      <path d="M-30 14 a14 14 0 0 1 2 -28 a20 20 0 0 1 38 -6 a16 16 0 0 1 20 20 a12 12 0 0 1 0 14z" fill="${c}" stroke="${st}" stroke-width="${3 / k}" stroke-linejoin="round"/></g>`;
  const sun = (x, y, r, face = false) => `<g transform="translate(${x} ${y})">
      ${Array.from({length: 8}, (_, i) => `<path d="M0 ${-r - 6} v-10" stroke="#FFB703" stroke-width="${r / 5}" stroke-linecap="round" transform="rotate(${i * 45})"/>`).join('')}
      <circle r="${r}" fill="#FFD23F"/>${face ? `<circle cx="${-r * .35}" cy="${-r * .1}" r="${r * .1}" fill="${INK}"/><circle cx="${r * .35}" cy="${-r * .1}" r="${r * .1}" fill="${INK}"/>
      <path d="M${-r * .3} ${r * .25} q${r * .3} ${r * .3} ${r * .6} 0" stroke="${INK}" stroke-width="2.5" fill="none" stroke-linecap="round"/>` : ''}</g>`;
  const drops = (pts, c = '#3D8BFD') => pts.map(([x, y]) => `<path d="M${x} ${y} q-5 8 0 11 q5 -3 0 -11z" fill="${c}"/>`).join('');
  const flake = (x, y, r, c = '#7FC8F8') => `<g transform="translate(${x} ${y})" stroke="${c}" stroke-width="${r / 4}" stroke-linecap="round">
      ${[0, 60, 120].map(a => `<path d="M0 ${-r} V${r} M-${r * .3} ${-r * .7} L0 ${-r * .4} L${r * .3} ${-r * .7} M-${r * .3} ${r * .7} L0 ${r * .4} L${r * .3} ${r * .7}" transform="rotate(${a})" fill="none"/>`).join('')}</g>`;
  const bolt = (x, y, k = 1) => `<path transform="translate(${x} ${y}) scale(${k})" d="M4 -16 L-10 4 H0 L-6 20 L12 -2 H2 L8 -16Z" fill="#FFD23F" stroke="#E0A100" stroke-width="1.5" stroke-linejoin="round"/>`;
  const tree = (x, y, k, leaf) => `<g transform="translate(${x} ${y}) scale(${k})"><rect x="-5" y="0" width="10" height="30" fill="#8D5A3B"/>${leaf}</g>`;
  const garment = (d, c, extra = '') => `<path d="${d}" fill="${c}" stroke="#fff" stroke-width="0"/>${extra}`;
  Object.assign(ART, {
    // ---------- ep19 weather ----------
    weather: () => sun(42, 44, 18) + cloud(68, 66, 1.2) + drops([[54, 92], [72, 98], [90, 92]]),
    air: () => `<path d="M10 40 H70 a14 14 0 1 0 -14 -14 M10 62 H92 a14 14 0 1 1 -14 14 M18 84 H56" stroke="#7FC8F8" stroke-width="7" fill="none" stroke-linecap="round"/>
       <circle cx="96" cy="32" r="5" fill="#BDE7FF"/><circle cx="104" cy="50" r="3.5" fill="#BDE7FF"/>`,
    sunny: () => sun(60, 60, 30, true),
    sunshine: () => `<path d="M0 120 L56 40 L120 82 V120Z" fill="#FFE08A" opacity=".55"/><path d="M0 120 L56 40 L40 120Z" fill="#FFD23F" opacity=".45"/>`
       + sun(28, 26, 16) + `<path d="M10 112 h100" stroke="#6CCB5F" stroke-width="8" stroke-linecap="round"/>` + mini('flower', 86, 92, .38),
    cloudy: () => sun(36, 38, 16) + cloud(64, 64, 1.5) + cloud(30, 86, .9, '#E3E6F5', '#C5CBE0'),
    windy: () => tree(36, 70, 1.1, `<path d="M0 0 C-30 -4 -36 -40 -6 -48 C14 -54 30 -26 0 0Z" fill="#6CCB5F" transform="rotate(25)"/>`)
       + `<path d="M58 40 H98 a10 10 0 1 0 -10 -10 M64 60 H108 M58 80 H96 a10 10 0 1 1 -10 10" stroke="#7FC8F8" stroke-width="6" fill="none" stroke-linecap="round"/>
          <path d="M96 104 q6 -8 12 -2" stroke="#6CCB5F" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    rainy: () => cloud(62, 48, 1.25, '#C5CBE0', '#8A8FA3') + drops([[34, 74], [52, 86], [70, 74], [88, 86], [44, 100], [80, 102]]),
    shower: () => cloud(62, 46, 1.25, '#8A8FA3', '#6B7085') + [[30, 66], [44, 66], [58, 66], [72, 66], [86, 66]].map(([x, y]) =>
         `<path d="M${x} ${y} l-8 40" stroke="#3D8BFD" stroke-width="4.5" stroke-linecap="round"/>`).join(''),
    storm: () => cloud(62, 46, 1.25, '#6B7085', '#2B2D42') + bolt(58, 84, 1.7) + drops([[28, 72], [92, 74], [36, 96]], '#7FC8F8'),
    snowy: () => cloud(62, 46, 1.25, '#fff', '#C5CBE0') + flake(36, 82, 9) + flake(62, 96, 11) + flake(90, 80, 9),
    foggy: () => cloud(60, 40, 1.1, '#E3E6F5', '#C5CBE0') + [60, 76, 92, 108].map((y, i) => `<path d="M${14 + i * 6} ${y} H${106 - i * 4}" stroke="#C5CBE0" stroke-width="7" stroke-linecap="round"/>`).join(''),
    hot: () => `<rect x="52" y="10" width="16" height="74" rx="8" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><rect x="56" y="30" width="8" height="58" rx="4" fill="#E63946"/>
       <circle cx="60" cy="96" r="16" fill="#E63946"/>${[24, 36, 48, 60].map(y => `<path d="M70 ${y} h7" stroke="#C5CBE0" stroke-width="2.5"/>`).join('')}
       <path d="M22 70 q-8 -12 0 -24 t0 -24 M98 70 q-8 -12 0 -24 t0 -24" stroke="#FF7A59" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    cold: () => `<rect x="52" y="10" width="16" height="74" rx="8" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><rect x="56" y="66" width="8" height="22" rx="4" fill="#3D8BFD"/>
       <circle cx="60" cy="96" r="16" fill="#3D8BFD"/>${[24, 36, 48, 60].map(y => `<path d="M70 ${y} h7" stroke="#C5CBE0" stroke-width="2.5"/>`).join('')}`
       + flake(24, 40, 13) + flake(98, 58, 11),

    // ---------- ep20 seasons ----------
    season: () => `<circle cx="60" cy="60" r="50" fill="#fff" stroke="#E3E6F5" stroke-width="3"/>
       <path d="M60 60 V10 A50 50 0 0 1 110 60Z" fill="#B7E4A8"/><path d="M60 60 H110 A50 50 0 0 1 60 110Z" fill="#FFE08A"/>
       <path d="M60 60 V110 A50 50 0 0 1 10 60Z" fill="#FFC09F"/><path d="M60 60 H10 A50 50 0 0 1 60 10Z" fill="#CFE8FF"/>
       ${mini('flower', 82, 36, .24)}${sun(82, 84, 7)}
       <path d="M38 76 c-8 0 -10 10 -2 14 c8 -2 8 -10 2 -14z" fill="#E07A4F"/>${flake(38, 38, 8, '#3D8BFD')}
       <circle cx="60" cy="60" r="6" fill="${INK}"/>`,
    spring: () => tree(60, 66, 1.2, `<circle cx="0" cy="-12" r="26" fill="#B7E4A8"/>${[[-14, -20], [8, -26], [14, -6], [-6, -2], [-18, -6], [2, -14]].map(([x, y]) =>
         `<circle cx="${x}" cy="${y}" r="4.5" fill="#FF8FAB"/>`).join('')}`) + `<path d="M8 110 h104" stroke="#6CCB5F" stroke-width="7" stroke-linecap="round"/>`
       + drops([[18, 30], [100, 26], [106, 52]], '#7FC8F8'),
    summer: () => sun(92, 26, 15) + `<path d="M0 86 q15 -8 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/>
       <path d="M0 98 h120 V120 H0Z" fill="#FFE08A"/><path d="M30 94 L30 40" stroke="#8D5A3B" stroke-width="3"/>
       <path d="M30 40 L4 58 Q30 30 56 58Z" fill="#E63946"/><path d="M30 40 L17 58 Q30 44 43 58Z" fill="#fff" opacity=".7"/>`,
    autumn: () => `<path d="M60 14 C86 26 98 54 84 84 C74 104 46 104 36 84 C22 54 34 26 60 14Z" fill="#E07A4F"/>
       <path d="M60 18 V108 M60 50 L80 36 M60 66 L40 50 M60 82 L80 70" stroke="#B5482A" stroke-width="3.5" fill="none" stroke-linecap="round"/>
       <path d="M18 92 c-10 0 -12 12 -2 16 c10 -2 10 -12 2 -16z" fill="#FFB703"/><path d="M100 24 c-10 0 -12 12 -2 16 c10 -2 10 -12 2 -16z" fill="#C1440E"/>`,
    winter: () => `<path d="M0 100 Q60 86 120 100 V120 H0Z" fill="#fff"/>
       <circle cx="60" cy="84" r="24" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><circle cx="60" cy="46" r="18" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <path d="M42 30 h36 v-6 h-6 v-14 h-24 v14 h-6z" fill="#2B2D42"/><circle cx="54" cy="44" r="2.6" fill="${INK}"/><circle cx="66" cy="44" r="2.6" fill="${INK}"/>
       <path d="M60 50 l10 3 l-10 2z" fill="#FF9F1C"/><path d="M44 62 q16 8 32 0" stroke="#E63946" stroke-width="7" fill="none" stroke-linecap="round"/>
       <circle cx="60" cy="78" r="2.6" fill="${INK}"/><circle cx="60" cy="90" r="2.6" fill="${INK}"/>${flake(18, 26, 8)}${flake(104, 40, 7)}`,
    dress: () => garment('M44 10 h32 l2 22 q-2 10 -6 14 L104 108 H16 L48 46 q-4 -4 -6 -14z', '#FF6FA5',
       `<path d="M44 10 l-6 -4 M76 10 l6 -4" stroke="#FF6FA5" stroke-width="4" stroke-linecap="round"/><path d="M42 46 h36" stroke="#fff" stroke-width="5"/>
        ${[[40, 80], [60, 70], [80, 84], [50, 98], [72, 98]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3.5" fill="#fff"/>`).join('')}`),
    skirt: () => garment('M34 26 h52 l24 78 H10z', '#9B5DE5', `<rect x="32" y="20" width="56" height="12" rx="3" fill="#7B3FC4"/>
       ${[28, 44, 60, 76, 92].map(x => `<path d="M${60 + (x - 60) * .6} 34 L${x} 104" stroke="#7B3FC4" stroke-width="2.5"/>`).join('')}`),
    shorts: () => garment('M20 22 h80 l10 66 h-40 l-10 -36 l-10 36 h-40z', '#2BB3A3', `<rect x="20" y="16" width="80" height="12" rx="3" fill="#1E8C7F"/>
       <path d="M56 28 l-4 10 M64 28 l4 10" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>
       <path d="M26 30 q4 14 16 14" stroke="#1E8C7F" stroke-width="3" fill="none"/>`),
    pocket: () => `<rect x="14" y="14" width="92" height="92" rx="6" fill="#3D5A80"/>
       <path d="M32 40 h56 v38 q-28 18 -56 0z" fill="#5B7DB1" stroke="#FFD23F" stroke-width="3" stroke-dasharray="5 4"/>
       <path d="M32 40 h56" stroke="#FFD23F" stroke-width="3"/><rect x="50" y="22" width="9" height="30" rx="3" fill="#FFB703" transform="rotate(-8 54 36)"/>
       <circle cx="72" cy="34" r="8" fill="#E63946"/>`,
    jacket: () => garment('M38 14 L14 30 L8 104 H34 V54 L40 108 H80 L86 54 V104 H112 L106 30 L82 14 L60 30Z', '#2FA36B',
       `<path d="M60 30 V108" stroke="#1E7A4E" stroke-width="3"/>${[48, 64, 80, 96].map(y => `<circle cx="66" cy="${y}" r="2.6" fill="#FFD23F"/>`).join('')}
        <path d="M38 14 L50 34 L60 30 L70 34 L82 14" fill="#1E7A4E"/><rect x="40" y="70" width="14" height="10" rx="2" fill="#1E7A4E"/><rect x="66" y="70" width="14" height="10" rx="2" fill="#1E7A4E"/>`),
    jeans: () => ART.trousers().replace(/#3D5A80/g, '#4A78C2').replace(/#2C4363/g, '#2F5A9E')
       + `<path d="M36 100 h20 M64 100 h20" stroke="#FFB703" stroke-width="2.5" stroke-dasharray="4 3"/><circle cx="60" cy="18" r="3" fill="#FFB703"/>`,
    sweater: () => garment('M36 16 L12 32 L6 104 H30 V56 V110 H90 V56 V104 H114 L108 32 L84 16 Q60 30 36 16Z', '#E63946',
       `<path d="M36 16 Q60 30 84 16 L80 12 Q60 24 40 12Z" fill="#B5172B"/>
        ${[50, 68].map(y => `<path d="M30 ${y} ${[0, 1, 2, 3, 4, 5].map(i => `l5 -6 l5 6`).join(' ')}" stroke="#fff" stroke-width="3" fill="none"/>`).join('')}
        <path d="M30 100 H90" stroke="#B5172B" stroke-width="6"/>`),
    coat: () => garment('M38 10 L14 28 L8 92 H30 V48 L34 114 H86 L90 48 V92 H112 L106 28 L82 10 L60 26Z', '#8D5A3B',
       `<path d="M38 10 L52 44 L60 26 L68 44 L82 10" fill="#6B4A36"/>
        ${[50, 70, 90].map(y => `<circle cx="52" cy="${y}" r="3.2" fill="#FFD23F"/><circle cx="68" cy="${y}" r="3.2" fill="#FFD23F"/>`).join('')}
        <path d="M34 112 L44 110 M86 112 L76 110" stroke="#6B4A36" stroke-width="3"/>`),
    also: () => `<circle cx="60" cy="60" r="44" fill="#FFF3C4" stroke="#E0A100" stroke-width="4"/>
       <path d="M60 36 v48 M36 60 h48" stroke="#E0A100" stroke-width="12" stroke-linecap="round"/>`,
  });

  // ---------- ep14 time / day ----------
  const clockF = (cx, cy, r, h, m, o = {}) => {
    const ang = (v, n) => (v / n) * 360;
    const hand = (a, len, w, c) => `<path d="M${cx} ${cy} L${cx + len * Math.sin(a * Math.PI / 180)} ${cy - len * Math.cos(a * Math.PI / 180)}" stroke="${c}" stroke-width="${w}" stroke-linecap="round"/>`;
    return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#fff" stroke="${o.rim || '#3D8BFD'}" stroke-width="${r / 7}"/>
      ${Array.from({length: 12}, (_, i) => `<path d="M${cx} ${cy - r * .78} v${i % 3 ? r * .08 : r * .16}" stroke="#8A8FA3" stroke-width="${i % 3 ? 2 : 3.5}" transform="rotate(${i * 30} ${cx} ${cy})"/>`).join('')}
      ${o.glow ? `<path d="M${cx} ${cy} L${cx + r * .7 * Math.sin(ang(o.glow[0], o.glow[1]) * Math.PI / 180)} ${cy - r * .7 * Math.cos(ang(o.glow[0], o.glow[1]) * Math.PI / 180)}" stroke="#FFD23F" stroke-width="${r / 3.2}" stroke-linecap="round" opacity=".85"/>` : ''}
      ${hand(ang(h + m / 60, 12), r * .45, r / 9, o.hc || INK)}${hand(ang(m, 60), r * .68, r / 13, o.mc || INK)}
      ${o.sec != null ? hand(ang(o.sec, 60), r * .74, r / 26, '#E63946') : ''}<circle cx="${cx}" cy="${cy}" r="${r / 12}" fill="${INK}"/>`;
  };
  const sky = (top, ground = '#8EDB6E') => `<rect x="4" y="4" width="112" height="112" rx="18" fill="${top}"/>
      <path d="M4 86 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="${ground}"/>`;
  const moon = (x, y, r, c = '#FFE08A', bg = '#2B2D6E') => `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}"/><circle cx="${x + r * .45}" cy="${y - r * .3}" r="${r * .85}" fill="${bg}"/>`;
  const twinkles = (pts) => pts.map(([x, y, k]) => star(x, y, k, k * .42, '#FFF3C4')).join('');
  Object.assign(ART, {
    day: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/>` + sun(60, 54, 24, true)
       + cloud(26, 96, .6) + cloud(96, 100, .55),
    morning: () => sky('#FFE3C2') + sun(30, 82, 16, true).replace('<g transform', '<g opacity="1" transform')
       + `<path d="M4 86 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#8EDB6E"/>` + cloud(86, 36, .5),
    noon: () => sky('#7FC8F8') + sun(60, 42, 14, true) + `<path d="M60 70 v14" stroke="#3B2A20" stroke-width="5"/><ellipse cx="60" cy="88" rx="10" ry="3" fill="#3FA34D"/>`,
    afternoon: () => sky('#A8DAFF') + sun(82, 56, 13, true) + cloud(36, 40, .55),
    evening: () => sky('#FF9F6B', '#6B4A6E') + `<rect x="4" y="44" width="112" height="44" fill="#FFC09F"/>`
       + `<path d="M24 86 a36 30 0 0 1 72 0z" fill="#FF7A59"/>`
       + `<path d="M4 86 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#6B4A6E"/>`
       + `<path d="M30 30 l6 3 l6 -3 M70 22 l5 2.5 l5 -2.5" stroke="#5A3825" stroke-width="2.5" fill="none" stroke-linecap="round"/>`,
    night: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#2B2D6E"/>` + moon(70, 50, 24)
       + twinkles([[24, 28, 7], [36, 74, 5], [96, 92, 6], [100, 22, 5], [20, 98, 4]]),
    midnight: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#1B1D4A"/>` + moon(34, 34, 16, '#FFE08A', '#1B1D4A')
       + clockF(70, 72, 32, 12, 0, {rim: '#9B5DE5'}) + twinkles([[96, 22, 5], [18, 92, 5]]),
    time: () => `<rect x="30" y="8" width="60" height="10" rx="4" fill="#8D5A3B"/><rect x="30" y="102" width="60" height="10" rx="4" fill="#8D5A3B"/>
       <path d="M36 18 H84 C84 44 64 52 64 60 C64 68 84 76 84 102 H36 C36 76 56 68 56 60 C56 52 36 44 36 18Z" fill="#E3F4FF" stroke="#8A8FA3" stroke-width="3"/>
       <path d="M44 30 H76 C74 42 62 48 60 56 C58 48 46 42 44 30Z" fill="#FFB703"/><path d="M40 100 C44 86 54 82 60 80 C66 82 76 86 80 100Z" fill="#FFB703"/>
       <path d="M60 58 v22" stroke="#FFB703" stroke-width="2" stroke-dasharray="2 3"/>`,
    clock: () => `<path d="M30 20 l-14 -10 M90 20 l14 -10" stroke="#E63946" stroke-width="6" stroke-linecap="round"/>
       <circle cx="22" cy="18" r="12" fill="#E63946"/><circle cx="98" cy="18" r="12" fill="#E63946"/>
       <path d="M36 102 l-8 12 M84 102 l8 12" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>` + clockF(60, 64, 44, 10, 10, {rim: '#E63946'}),
    oclock: () => clockF(60, 52, 40, 3, 0, {rim: '#2FA36B'})
       + `<rect x="26" y="96" width="68" height="22" rx="8" fill="#2B2D42"/><text x="60" y="113" text-anchor="middle" font-size="17" ${FONT} fill="#6CFF8F" letter-spacing="1">3:00</text>`,
    at: () => `<path d="M8 84 H112" stroke="#C5CBE0" stroke-width="6" stroke-linecap="round"/>
       ${[16, 38, 60, 82, 104].map((x, i) => `<path d="M${x} 78 v12" stroke="#8A8FA3" stroke-width="3"/><text x="${x}" y="108" text-anchor="middle" font-size="12" ${FONT} fill="#8A8FA3">${i + 1}</text>`).join('')}
       <path d="M60 76 C60 64 42 56 42 40 a18 18 0 0 1 36 0 C78 56 60 64 60 76Z" fill="#E0A100"/><circle cx="60" cy="40" r="8" fill="#fff"/>
       <circle cx="60" cy="84" r="6" fill="#E0A100"/>`,
    hour: () => clockF(60, 60, 48, 4, 0, {rim: '#FF7A59', glow: [4, 12], hc: '#E63946'}),
    minute: () => clockF(60, 60, 48, 2, 40, {rim: '#3D8BFD', glow: [40, 60], mc: '#2A6FD6'}),
    second: () => `<rect x="52" y="4" width="16" height="12" rx="3" fill="#8A8FA3"/><path d="M92 26 l8 -8" stroke="#8A8FA3" stroke-width="6" stroke-linecap="round"/>`
       + clockF(60, 66, 44, 0, 0, {rim: '#2BB3A3', sec: 20}) + `<path d="M60 66 L60 26 A40 40 0 0 1 94.6 86Z" fill="#E63946" opacity=".15"/>`,
  });

  const plate = (cx, cy, rx, ry, c = '#fff') => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${c}" stroke="#C5CBE0" stroke-width="3"/>
      <ellipse cx="${cx}" cy="${cy - 1}" rx="${rx * .72}" ry="${ry * .62}" fill="none" stroke="#E3E6F5" stroke-width="2"/>`;
  const steam = (x, y) => `<path d="M${x} ${y} q-6 -8 0 -14 t0 -14 M${x + 14} ${y + 2} q-6 -8 0 -14 t0 -14" stroke="#C5CBE0" stroke-width="3.5" fill="none" stroke-linecap="round"/>`;
  const bowl = (c = '#fff', rim = '#3D8BFD') => `<path d="M14 58 h92 a46 44 0 0 1 -92 0z" fill="${c}" stroke="${rim}" stroke-width="4"/><path d="M40 108 h40" stroke="${rim}" stroke-width="6" stroke-linecap="round"/>`;
  Object.assign(ART, {
    // ---------- ep21 meals ----------
    breakfast: () => plate(60, 78, 52, 22) + `<ellipse cx="44" cy="74" rx="22" ry="13" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><circle cx="44" cy="74" r="8" fill="#FFB703"/>
       <rect x="68" y="58" width="30" height="26" rx="6" fill="#E9A66B"/><rect x="72" y="62" width="22" height="18" rx="4" fill="#F4D3A8"/>` + sun(96, 26, 11),
    porridge: () => bowl('#fff') + `<ellipse cx="60" cy="58" rx="44" ry="10" fill="#F4EBD9"/>${[[44, 56], [62, 60], [76, 55]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#C1440E"/>`).join('')}
       <path d="M78 54 L104 20" stroke="#8A8FA3" stroke-width="5" stroke-linecap="round"/>` + steam(40, 40),
    pancake: () => plate(60, 96, 50, 14) + [82, 70, 58, 46].map(y => `<ellipse cx="60" cy="${y}" rx="40" ry="11" fill="#E9A66B"/><ellipse cx="60" cy="${y - 3}" rx="40" ry="10" fill="#F4C27A"/>`).join('')
       + `<path d="M34 44 q26 -8 52 0 q2 14 -6 24 q-2 -10 -8 -12 q-4 14 -10 14 q-2 -12 -10 -12 q-6 10 -12 6 q2 -10 -6 -20z" fill="#B5482A" opacity=".9"/>
          <rect x="52" y="32" width="16" height="10" rx="2" fill="#FFE066"/>`,
    butter: () => plate(60, 86, 52, 18) + `<path d="M24 76 L40 54 H96 L84 76Z" fill="#FFE066"/><path d="M24 76 H84 V88 H24Z" fill="#FFD23F"/><path d="M84 76 L96 54 V66 L84 88Z" fill="#E0B400"/>
       <path d="M98 30 L66 58" stroke="#C5CBE0" stroke-width="6" stroke-linecap="round"/><path d="M66 58 l-10 6 l4 -10z" fill="#C5CBE0"/>`,
    prefer: () => `<g opacity=".45">${mini('porridge', 30, 74, .42)}</g>${mini('pancake', 88, 74, .5)}
       <path d="M58 24 v50" stroke="#C5CBE0" stroke-width="3" stroke-dasharray="4 5"/>${heart(88, 26, .9, '#E63946')}`
       + `<text x="30" y="34" text-anchor="middle" font-size="22" ${FONT} fill="#C5CBE0">&gt;</text>`.replace('&gt;', '?'),
    lunch: () => `<rect x="10" y="34" width="100" height="70" rx="10" fill="#3D8BFD"/><rect x="16" y="40" width="88" height="58" rx="6" fill="#fff"/>
       <path d="M60 40 v58 M60 70 h44" stroke="#3D8BFD" stroke-width="4"/>
       <path d="M20 56 h36 a18 18 0 0 1 -36 0z" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><ellipse cx="38" cy="56" rx="18" ry="6" fill="#F4F1E8"/>
       <circle cx="74" cy="56" r="7" fill="#6CCB5F"/><circle cx="90" cy="54" r="7" fill="#E63946"/><rect x="68" y="76" width="30" height="16" rx="6" fill="#E9A66B"/>
       <circle cx="60" cy="22" r="10" fill="#fff" stroke="#8A8FA3" stroke-width="2.5"/><path d="M60 16 v6 h5" stroke="${INK}" stroke-width="2" fill="none"/>`,
    sandwich: () => `<path d="M14 92 L60 24 L106 92Z" fill="#F4D3A8" stroke="#C9934A" stroke-width="5" stroke-linejoin="round"/>
       <path d="M24 82 L60 30 L96 82" fill="none" stroke="#6CCB5F" stroke-width="7" stroke-linejoin="round"/>
       <path d="M30 76 L60 34 L90 76" fill="none" stroke="#E63946" stroke-width="5" stroke-linejoin="round"/>
       <path d="M36 72 L60 38 L84 72" fill="none" stroke="#FFD23F" stroke-width="5" stroke-linejoin="round"/>
       <path d="M12 96 L60 28 L108 96 Z" fill="none"/><rect x="12" y="90" width="96" height="12" rx="6" fill="#E9A66B"/>`,
    bread: () => `<path d="M10 70 C10 40 40 28 60 28 C80 28 110 40 110 70 C110 92 96 100 60 100 C24 100 10 92 10 70Z" fill="#D99058"/>
       <path d="M18 70 C18 46 42 36 60 36 C78 36 102 46 102 70" fill="#E9A66B"/>
       ${[38, 56, 74].map(x => `<path d="M${x} 46 q8 8 4 20" stroke="#B5703F" stroke-width="5" fill="none" stroke-linecap="round"/>`).join('')}`,
    salad: () => bowl('#fff', '#2FA36B') + `<path d="M18 58 C20 34 40 30 50 40 C56 24 76 24 80 40 C92 32 106 42 102 58Z" fill="#6CCB5F"/>
       <circle cx="40" cy="48" r="8" fill="#E63946"/><circle cx="74" cy="46" r="7" fill="#E63946"/><circle cx="58" cy="52" r="6" fill="#FFD23F"/>
       <path d="M86 48 a8 8 0 1 1 -1 0" stroke="#9B5DE5" stroke-width="3.5" fill="none"/>`,
    sausage: () => `<path d="M100 40 C108 52 100 82 70 92 C40 102 18 92 16 82" stroke="#B5482A" stroke-width="22" fill="none" stroke-linecap="round"/>
       <path d="M96 46 C100 58 92 78 68 86" stroke="#E07A4F" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/>
       <path d="M10 82 l-6 -4 M106 34 l4 -6" stroke="#B5482A" stroke-width="4" stroke-linecap="round"/>
       <path d="M40 80 l6 -8 M56 78 l6 -8 M72 70 l6 -8" stroke="#8D2E0A" stroke-width="2.5" stroke-linecap="round"/>`,
    noodles: () => bowl('#fff', '#E63946') + `<ellipse cx="60" cy="58" rx="44" ry="10" fill="#FFE8A8"/>
       ${[0, 1, 2, 3].map(i => `<path d="M${30 + i * 14} 60 q4 -10 0 -18 t2 -18" stroke="#F4C27A" stroke-width="4" fill="none"/>`).join('')}
       <path d="M44 6 L76 66 M58 4 L84 64" stroke="#8D5A3B" stroke-width="4.5" stroke-linecap="round"/>
       ${[0, 1, 2].map(i => `<path d="M${42 + i * 10} 88 h8" stroke="#E63946" stroke-width="3"/>`).join('')}`,
    dinner: () => `<rect x="4" y="4" width="112" height="70" rx="16" fill="#2B2D6E"/>${moon(94, 26, 10, '#FFE08A', '#2B2D6E')}`
       + plate(56, 88, 46, 18) + `<ellipse cx="56" cy="84" rx="22" ry="9" fill="#C1440E"/><circle cx="42" cy="82" r="5" fill="#6CCB5F"/><circle cx="70" cy="80" r="4" fill="#FFB703"/>
       <rect x="16" y="34" width="10" height="34" rx="3" fill="#fff"/>${flame(21, 28, .7)}`,
    hamburger: () => `<path d="M16 54 C16 26 104 26 104 54Z" fill="#E9A66B"/>${[[40, 40], [58, 34], [76, 40], [52, 46], [68, 46]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="2.5" ry="1.5" fill="#fff"/>`).join('')}
       <path d="M12 60 q12 8 24 0 t24 0 t24 0 t24 0 v-6 h-96z" fill="#6CCB5F"/><rect x="14" y="62" width="92" height="8" fill="#FFD23F"/>
       <rect x="12" y="70" width="96" height="16" rx="8" fill="#8D4A2B"/><path d="M16 86 h88 v6 a8 8 0 0 1 -8 8 h-72 a8 8 0 0 1 -8 -8z" fill="#E9A66B"/>`,
    spaghetti: () => plate(60, 86, 54, 20) + `<path d="M24 82 C24 60 96 60 96 82Z" fill="#FFE08A"/>
       ${[0, 1, 2, 3, 4].map(i => `<path d="M${30 + i * 13} 80 q6 -12 12 -2" stroke="#F4C27A" stroke-width="3.5" fill="none"/>`).join('')}
       <path d="M40 66 C46 56 74 56 80 66 C70 74 50 74 40 66Z" fill="#E63946"/><circle cx="52" cy="64" r="5" fill="#B5172B"/><circle cx="68" cy="63" r="5" fill="#B5172B"/>
       <path d="M86 12 L74 60 M80 10 l-4 16 M92 14 l-4 16" stroke="#8A8FA3" stroke-width="4" stroke-linecap="round"/>`,

    // ---------- ep22 friends ----------
    let: () => `<rect x="70" y="10" width="44" height="100" rx="4" fill="#B5703F"/><rect x="76" y="16" width="32" height="94" fill="#FFF3C4"/>
       <path d="M76 16 L96 22 V104 L76 110Z" fill="#9C5E33"/>` + `<g transform="translate(-22 10) scale(.9)">${figure('woman', {shirt: '#FF6FA5'})}</g>`
       + `<path d="M58 84 C70 78 76 72 84 70" stroke="${SKIN[0]}" stroke-width="7" stroke-linecap="round" fill="none"/>${check(26, 20, 1.2)}`,
    play: () => kid({s: .82, dx: -24, dy: 8, la: [-50, -20], ra: [120, 140], ll: [-14, -4], rl: [24, 10], shirt: '#FF9F1C'})
       + kid({s: .82, dx: 26, dy: 8, la: [-130, -150], ra: [40, 20], ll: [-20, -6], rl: [10, 4], shirt: '#3D8BFD', skin: SKIN[1]})
       + mini('ball', 60, 18, .2),
    with: () => `<circle cx="42" cy="60" r="30" fill="#FF7A59" opacity=".85"/><circle cx="78" cy="60" r="30" fill="#3D8BFD" opacity=".85"/>
       <path d="M60 36 a30 30 0 0 1 0 48 a30 30 0 0 1 0 -48z" fill="#9B5DE5"/>${heart(60, 60, .55, '#fff')}`,
    friend: () => `<g transform="translate(-16 14) scale(.86)">${figure('boy', {shirt: '#2FA36B'})}</g><g transform="translate(32 14) scale(.86)">${figure('girl', {shirt: '#FF9F1C', skin: SKIN[1]})}</g>
       <path d="M44 92 Q60 82 76 92" stroke="#2FA36B" stroke-width="8" fill="none" stroke-linecap="round"/>${heart(60, 20, .7, '#FF4D6D')}`,
    share: () => `<circle cx="60" cy="54" r="30" fill="#D99058"/><path d="M60 22 l-6 14 l8 10 l-6 12 l8 10 l-6 16" stroke="#FFF6EA" stroke-width="5" fill="none"/>
       ${[[44, 44], [48, 66], [72, 46], [76, 66]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="4" fill="#5A3825"/>`).join('')}`
       + hand(30, 100, .9, 30, SKIN[0]) + `<g transform="translate(120 0) scale(-1 1)">${hand(30, 100, .9, 30, SKIN[1])}</g>`,
    toy: () => `<circle cx="36" cy="30" r="12" fill="#B5703F"/><circle cx="84" cy="30" r="12" fill="#B5703F"/><circle cx="36" cy="30" r="6" fill="#E9A66B"/><circle cx="84" cy="30" r="6" fill="#E9A66B"/>
       <ellipse cx="60" cy="88" rx="30" ry="26" fill="#B5703F"/><ellipse cx="60" cy="92" rx="16" ry="14" fill="#E9A66B"/>
       <circle cx="60" cy="48" r="26" fill="#B5703F"/><ellipse cx="60" cy="56" rx="12" ry="9" fill="#E9A66B"/>
       <circle cx="50" cy="44" r="3.5" fill="${INK}"/><circle cx="70" cy="44" r="3.5" fill="${INK}"/><ellipse cx="60" cy="52" rx="4" ry="3" fill="${INK}"/>
       <path d="M44 70 l16 8 l16 -8 l-16 -2z" fill="#E63946"/>`,
    game: () => `<path d="M14 54 C14 38 30 34 44 38 H76 C90 34 106 38 106 54 L110 84 C112 98 96 104 88 92 L80 80 H40 L32 92 C24 104 8 98 10 84Z" fill="#5A67D8"/>
       <path d="M30 52 v20 M20 62 h20" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
       <circle cx="84" cy="54" r="5" fill="#FFD23F"/><circle cx="94" cy="64" r="5" fill="#E63946"/><circle cx="74" cy="64" r="5" fill="#2FA36B"/><circle cx="84" cy="74" r="5" fill="#3D8BFD"/>`,
    greet: () => `<g transform="translate(-18 18) scale(.8)">${figure('boy', {shirt: '#3D8BFD'})}</g><g transform="translate(42 18) scale(.8)">${figure('girl', {shirt: '#FF6FA5', skin: SKIN[1]})}</g>`
       + bubble(26, 2, 68, 30, '#2FA36B', 'l', `<text x="34" y="21" text-anchor="middle" font-size="16" ${FONT} fill="#fff">Hello!</text>`),
    wave: () => kid({la: [-10, -4], ra: [150, 170], shirt: '#2BB3A3'}) + `<path d="M96 6 q10 6 10 18 M104 2 q14 10 12 26 M74 6 q-6 4 -8 12" stroke="#FFB703" stroke-width="3.5" fill="none" stroke-linecap="round"/>`,
    shy: () => `<circle cx="60" cy="58" r="40" fill="${SKIN[0]}"/>` + cap(60, 58, 40, '#5A3825')
       + `<path d="M40 60 q6 -4 12 0 M68 60 q6 -4 12 0" stroke="${INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
          <ellipse cx="36" cy="74" rx="10" ry="6" fill="#FF6F91"/><ellipse cx="84" cy="74" rx="10" ry="6" fill="#FF6F91"/>
          <path d="M52 82 q8 4 16 0" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>` + hand(24, 106, .7, 20, SKIN[0]) + heart(100, 22, .5, '#FF6F91'),
    nervous: () => `<circle cx="60" cy="60" r="40" fill="${SKIN[1]}"/>` + cap(60, 60, 40, '#3B2A20')
       + `<circle cx="46" cy="62" r="5" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="74" cy="62" r="5" fill="#fff" stroke="${INK}" stroke-width="2"/>
          <circle cx="46" cy="62" r="2" fill="${INK}"/><circle cx="74" cy="62" r="2" fill="${INK}"/>
          <path d="M44 84 q4 -4 8 0 t8 0 t8 0 t8 0" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
          <path d="M96 40 q6 10 0 14 q-6 -4 0 -14z" fill="#7FC8F8"/><path d="M104 60 q4 7 0 10 q-4 -3 0 -10z" fill="#7FC8F8"/>`,
    promise: () => `<path d="M8 96 C16 74 32 66 46 66 L54 52 a5 5 0 0 1 9 4 L58 68 C60 80 50 92 34 98Z" fill="${SKIN[0]}"/>
       <path d="M112 96 C104 74 88 66 74 66 L66 52 a5 5 0 0 0 -9 4 L62 68 C60 80 70 92 86 98Z" fill="${SKIN[1]}"/>
       <path d="M54 50 q6 -10 12 0" stroke="#C98F68" stroke-width="7" fill="none" stroke-linecap="round"/>${star(60, 22, 12, 5, '#FFD23F')}`,
  });
  // ---------- ep23 tens: number + that many ten-bars ----------
  Object.assign(ART, Object.fromEntries([0, 20, 30, 40, 50, 60, 70, 80, 90, 100].map((k, i) => {
    const c = NUMC[i % 10], t = k / 10;
    const bars = Array.from({length: t}, (_, j) => `<rect x="${60 - (Math.min(t, 5) * 15) / 2 + (j % 5) * 15 + 2}" y="${66 + Math.floor(j / 5) * 22}" width="10" height="18" rx="3" fill="${c}" opacity="${j % 5 === 4 ? 1 : .75}"/>`).join('');
    return ['n' + k, () => `<text x="60" y="58" text-anchor="middle" font-size="${k === 100 ? 48 : 58}" ${FONT} fill="${c}" stroke="#fff" stroke-width="5" paint-order="stroke" letter-spacing="-3">${k}</text>`
      + (k ? bars : `<ellipse cx="60" cy="88" rx="22" ry="14" fill="none" stroke="${c}" stroke-width="4" stroke-dasharray="6 5"/>`)];
  })));

  const splat = (x, y, r, c) => `<path transform="translate(${x} ${y}) scale(${r / 30})" d="M0 -30 C10 -30 12 -20 20 -22 C30 -24 32 -12 26 -4 C34 2 32 16 22 16 C22 28 8 32 0 24 C-8 32 -24 28 -22 16 C-34 16 -34 0 -26 -6 C-32 -16 -22 -26 -14 -22 C-10 -30 -6 -30 0 -30Z" fill="${c}"/>`;
  const wheel = (x, y, r) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#2B2D42"/><circle cx="${x}" cy="${y}" r="${r * .45}" fill="#C5CBE0"/>`;
  const road = `<rect x="4" y="96" width="112" height="8" rx="4" fill="#C5CBE0"/>`;
  const colourArt = (c, obj) => `${splat(46, 50, 36, c)}<circle cx="86" cy="86" r="26" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>${obj}`;
  Object.assign(ART, {
    // ---------- ep24 colours ----------
    colour: () => `<path d="M60 12 C28 12 8 36 10 62 C12 92 36 110 58 108 C70 106 70 96 64 90 C58 84 62 74 74 76 C94 78 112 70 110 50 C108 28 88 12 60 12Z" fill="#F4D3A8"/>
       ${[[34, 40, '#E63946'], [56, 28, '#FF9F1C'], [80, 34, '#FFD23F'], [92, 54, '#2FA36B'], [30, 66, '#3D8BFD'], [42, 88, '#9B5DE5']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="9" fill="${c}"/>`).join('')}
       <path d="M96 96 L116 116" stroke="#8D5A3B" stroke-width="5" stroke-linecap="round"/><path d="M90 90 l8 8 l-4 4 q-8 -2 -8 -8z" fill="#2B2D42"/>`,
    red: () => colourArt('#E63946', `<circle cx="86" cy="90" r="15" fill="#E63946"/><path d="M86 76 q2 -6 6 -8" stroke="#3FA34D" stroke-width="3" fill="none"/>`),
    orange: () => colourArt('#FF9F1C', `<circle cx="86" cy="88" r="15" fill="#FF9F1C"/><path d="M86 73 q6 -6 12 -2 q-6 4 -12 2z" fill="#3FA34D"/><circle cx="82" cy="84" r="2" fill="#FFC970"/>`),
    yellow: () => colourArt('#FFD23F', `<path d="M70 80 C72 98 92 104 104 92 C94 96 80 94 76 80Z" fill="#FFD23F" stroke="#E0B400" stroke-width="2"/>`),
    green: () => colourArt('#2FA36B', `<path d="M74 100 C70 82 84 70 102 74 C104 92 90 104 74 100Z" fill="#2FA36B"/><path d="M74 100 L98 78" stroke="#1E7A4E" stroke-width="2"/>`),
    blue: () => colourArt('#3D8BFD', `<path d="M86 70 C80 82 74 88 74 94 a12 12 0 0 0 24 0 C98 88 92 82 86 70Z" fill="#3D8BFD"/>`),
    purple: () => colourArt('#9B5DE5', [[80, 80], [92, 80], [86, 90], [74, 90], [98, 90], [86, 100], [80, 98], [92, 98]].slice(0, 7).map(([x, y]) => `<circle cx="${x}" cy="${y}" r="5.5" fill="#9B5DE5"/>`).join('') + `<path d="M86 74 v-6" stroke="#3FA34D" stroke-width="3"/>`),
    pink: () => colourArt('#FF6FA5', mini('flower', 86, 88, .32).replace(/#FF6FA5/g, '#FF6FA5')),
    white: () => `<path transform="translate(46 50) scale(1.2)" d="M0 -30 C10 -30 12 -20 20 -22 C30 -24 32 -12 26 -4 C34 2 32 16 22 16 C22 28 8 32 0 24 C-8 32 -24 28 -22 16 C-34 16 -34 0 -26 -6 C-32 -16 -22 -26 -14 -22 C-10 -30 -6 -30 0 -30Z" fill="#fff" stroke="#C5CBE0" stroke-width="2"/>
       <circle cx="86" cy="86" r="26" fill="#BDE7FF"/>` + cloud(88, 90, .55),
    gold: () => colourArt('#F4B400', `<path d="M76 66 l10 14 l10 -14" stroke="#E63946" stroke-width="5" fill="none"/><circle cx="86" cy="92" r="13" fill="#F4B400" stroke="#C99700" stroke-width="2.5"/>${star(86, 92, 7, 3, '#FFF3C4')}`),
    silver: () => colourArt('#B8BFCC', `<circle cx="86" cy="88" r="15" fill="#D9DEE7" stroke="#8A8FA3" stroke-width="2.5"/><circle cx="86" cy="88" r="9" fill="none" stroke="#fff" stroke-width="2"/><path d="M80 82 l4 -4" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>`),
    black: () => colourArt('#2B2D42', `<path d="M74 102 C72 88 76 80 86 80 C96 80 100 88 98 102Z" fill="#2B2D42"/><path d="M76 82 l2 -10 l6 7 M96 82 l-2 -10 l-6 7" fill="#2B2D42"/>
       <circle cx="81" cy="88" r="2" fill="#FFD23F"/><circle cx="91" cy="88" r="2" fill="#FFD23F"/>`),
    brown: () => colourArt('#8D5A3B', `<circle cx="78" cy="78" r="5" fill="#8D5A3B"/><circle cx="94" cy="78" r="5" fill="#8D5A3B"/><circle cx="86" cy="90" r="13" fill="#8D5A3B"/>
       <ellipse cx="86" cy="94" rx="5" ry="4" fill="#D99058"/><circle cx="81" cy="87" r="1.8" fill="${INK}"/><circle cx="91" cy="87" r="1.8" fill="${INK}"/>`),
    bright: () => `<rect x="10" y="20" width="44" height="80" rx="8" fill="#FFD23F"/><rect x="66" y="20" width="44" height="80" rx="8" fill="#FFF3A3"/>`
       + sun(88, 30, 9) + `<path d="M20 34 l8 -8 M20 48 l20 -20" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>`,
    dark: () => `<rect x="10" y="20" width="44" height="80" rx="8" fill="#3D8BFD"/><rect x="66" y="20" width="44" height="80" rx="8" fill="#1F3E7A"/>`
       + moon(88, 34, 10, '#FFE08A', '#1F3E7A'),

    // ---------- ep25 transportation ----------
    transportation: () => `<path d="M8 100 C30 70 50 90 64 60 C76 34 98 44 112 18" stroke="#8A8FA3" stroke-width="14" fill="none" stroke-linecap="round"/>
       <path d="M8 100 C30 70 50 90 64 60 C76 34 98 44 112 18" stroke="#fff" stroke-width="2.5" fill="none" stroke-dasharray="6 6"/>`
       + mini('car', 30, 66, .32) + mini('bus', 86, 74, .32) + mini('plane', 40, 22, .32),
    car: () => road + `<path d="M14 82 V68 Q16 60 26 58 L36 40 Q40 34 50 34 H76 Q84 34 90 42 L100 58 Q110 60 110 70 V82Z" fill="#E63946"/>
       <path d="M42 44 Q44 40 50 40 H60 V58 H36Z M66 40 H76 Q82 40 86 46 L92 58 H66Z" fill="#BDE7FF"/>` + wheel(36, 84, 11) + wheel(88, 84, 11)
       + `<rect x="104" y="64" width="6" height="6" rx="2" fill="#FFD23F"/>`,
    truck: () => road + `<rect x="8" y="34" width="66" height="48" rx="4" fill="#3D8BFD"/><path d="M74 48 H96 L110 64 V82 H74Z" fill="#FFB703"/>
       <path d="M80 54 H94 L102 64 H80Z" fill="#BDE7FF"/>` + wheel(28, 86, 10) + wheel(56, 86, 10) + wheel(94, 86, 10),
    motorbike: () => road + wheel(26, 82, 14) + wheel(96, 82, 14) + `<path d="M26 82 L50 62 H78 L96 82 M50 62 L42 50 H30" stroke="#2B2D42" stroke-width="5" fill="none" stroke-linejoin="round"/>
       <path d="M46 58 Q60 46 82 56 L78 66 H50Z" fill="#E63946"/><path d="M82 48 L90 40 h8" stroke="#2B2D42" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    bicycle: () => road + `<circle cx="28" cy="78" r="18" fill="none" stroke="#2B2D42" stroke-width="5"/><circle cx="92" cy="78" r="18" fill="none" stroke="#2B2D42" stroke-width="5"/>
       <path d="M28 78 L48 50 H80 L92 78 M48 50 L62 78 L80 50 M62 78 H28 M44 40 h12 M80 50 L76 36 h10" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>`,
    ride: () => `<circle cx="28" cy="84" r="17" fill="none" stroke="#2B2D42" stroke-width="5"/><circle cx="92" cy="84" r="17" fill="none" stroke="#2B2D42" stroke-width="5"/>
       <path d="M28 84 L48 60 H80 L92 84 M48 60 L62 84 L80 60 M80 60 L76 48" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linejoin="round"/>`
       + kid({s: .7, dx: 2, dy: -14, rot: 10, la: [140, 120], ra: [130, 110], ll: [60, -30], rl: [100, 10], shirt: '#FF9F1C'}),
    bus: () => road + `<rect x="8" y="30" width="104" height="56" rx="10" fill="#FFB703"/>
       ${[16, 40, 64].map(x => `<rect x="${x}" y="38" width="20" height="18" rx="3" fill="#BDE7FF"/>`).join('')}<rect x="88" y="38" width="16" height="36" rx="3" fill="#BDE7FF"/>
       <rect x="8" y="64" width="80" height="5" fill="#E63946"/>` + wheel(30, 88, 10) + wheel(86, 88, 10),
    train: () => `<path d="M4 104 H116" stroke="#8D5A3B" stroke-width="4"/>${[12, 32, 52, 72, 92, 112].map(x => `<rect x="${x - 3}" y="100" width="6" height="10" fill="#8D5A3B"/>`).join('')}
       <rect x="10" y="44" width="62" height="46" rx="6" fill="#2FA36B"/><rect x="72" y="28" width="38" height="62" rx="6" fill="#E63946"/>
       <rect x="80" y="36" width="22" height="18" rx="3" fill="#BDE7FF"/><rect x="18" y="52" width="16" height="14" rx="2" fill="#BDE7FF"/><rect x="42" y="52" width="16" height="14" rx="2" fill="#BDE7FF"/>
       <rect x="20" y="30" width="12" height="16" fill="#2B2D42"/><circle cx="26" cy="22" r="7" fill="#E3E6F5"/><circle cx="36" cy="14" r="5" fill="#E3E6F5"/>` + wheel(26, 94, 8) + wheel(56, 94, 8) + wheel(90, 94, 8),
    subway: () => `<path d="M4 116 V60 a56 50 0 0 1 112 0 V116Z" fill="#6B7085"/><path d="M14 116 V64 a46 42 0 0 1 92 0 V116Z" fill="#2B2D42"/>
       <path d="M24 108 V66 Q24 46 60 46 Q96 46 96 66 V108Z" fill="#E3E6F5"/><rect x="34" y="58" width="52" height="20" rx="4" fill="#5A67D8"/>
       <circle cx="38" cy="94" r="5" fill="#FFD23F"/><circle cx="82" cy="94" r="5" fill="#FFD23F"/><rect x="24" y="82" width="72" height="5" fill="#E63946"/>
       <text x="60" y="38" text-anchor="middle" font-size="14" ${FONT} fill="#fff">M</text>`,
    plane: () => cloud(30, 96, .5) + `<g transform="rotate(-20 60 60)"><path d="M10 60 Q10 50 24 50 H96 Q112 52 114 60 Q112 68 96 70 H24 Q10 70 10 60Z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <path d="M50 52 L70 20 H80 L70 52Z M50 68 L70 100 H80 L70 68Z" fill="#3D8BFD"/><path d="M14 54 L8 36 H18 L28 52Z" fill="#3D8BFD"/>
       ${[78, 88, 98].map(x => `<circle cx="${x}" cy="58" r="3" fill="#7FC8F8"/>`).join('')}</g>`,
    ship: () => `<path d="M0 98 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 V120 H0Z" fill="#4CC9F0"/>
       <path d="M8 74 H112 L98 98 H22Z" fill="#E63946"/><rect x="26" y="52" width="64" height="22" rx="3" fill="#fff"/>
       ${[34, 50, 66].map(x => `<circle cx="${x + 4}" cy="63" r="4" fill="#7FC8F8"/>`).join('')}<rect x="70" y="32" width="14" height="20" fill="#2B2D42"/><rect x="70" y="32" width="14" height="6" fill="#E63946"/>
       <circle cx="80" cy="22" r="6" fill="#E3E6F5"/>`,
    boat: () => `<path d="M0 96 q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 V120 H0Z" fill="#4CC9F0"/>
       <path d="M18 82 H102 L90 98 H30Z" fill="#B5703F"/><path d="M58 14 V82" stroke="#6B4A36" stroke-width="4"/>
       <path d="M62 18 L96 74 H62Z" fill="#fff" stroke="#C5CBE0" stroke-width="2"/><path d="M54 30 L28 74 H54Z" fill="#FF9F1C"/>`,
    fast: () => `<path d="M2 50 h26 M8 64 h22 M2 78 h28" stroke="#8A8FA3" stroke-width="4.5" stroke-linecap="round" opacity=".6"/>
       <path d="M30 86 V72 Q32 62 46 60 L60 46 Q64 42 72 42 H90 Q104 44 112 62 Q116 70 114 86Z" fill="#FF9F1C"/>
       <path d="M64 50 Q66 48 72 48 H86 Q96 50 100 62 H58Z" fill="#BDE7FF"/><text x="80" y="80" text-anchor="middle" font-size="16" ${FONT} fill="#fff">1</text>`
       + wheel(48, 88, 11) + wheel(98, 88, 11) + bolt(26, 22, 1),
    slow: () => `<path d="M10 96 H112" stroke="#8EDB6E" stroke-width="6" stroke-linecap="round"/>
       <path d="M18 92 C18 84 26 80 40 80 H96 C106 80 108 92 100 92Z" fill="#C9E4A8"/><circle cx="60" cy="64" r="26" fill="#E9A66B"/>
       <path d="M60 64 m-16 0 a16 16 0 1 1 16 16 a10 10 0 1 1 -10 -10 a5 5 0 1 1 5 5" stroke="#B5703F" stroke-width="4" fill="none"/>
       <path d="M96 84 L104 58 M104 84 L112 62" stroke="#C9E4A8" stroke-width="4" stroke-linecap="round"/><circle cx="104" cy="56" r="4" fill="${INK}"/><circle cx="112" cy="60" r="4" fill="${INK}"/>
       <text x="22" y="40" font-size="16" ${FONT} fill="#8A8FA3">z z</text>`,
    ticket: () => `<g transform="rotate(-12 60 60)"><path d="M10 36 H110 V52 a8 8 0 0 0 0 16 V84 H10 V68 a8 8 0 0 0 0 -16Z" fill="#FFB703"/>
       <path d="M80 36 V84" stroke="#fff" stroke-width="3" stroke-dasharray="4 4"/>
       <text x="44" y="66" text-anchor="middle" font-size="13" ${FONT} fill="#fff">TICKET</text>${star(96, 60, 9, 4, '#fff')}</g>`,

    // ---------- ep26 family (2) ----------
    grandmother: () => figure('woman', {hair: '#D9DCE6', shirt: '#9B5DE5'}) + `<g fill="none" stroke="${INK}" stroke-width="2.2"><circle cx="53" cy="42" r="5"/><circle cx="67" cy="42" r="5"/><path d="M58 42h4"/></g>
       <circle cx="60" cy="16" r="9" fill="#D9DCE6"/>`,
    grandfather: () => figure('elder', {shirt: '#2BB3A3', mustache: true, hair: '#D9DCE6'}),
    grandparents: () => `<g transform="translate(-10 16) scale(.82)">${ART.grandfather()}</g><g transform="translate(32 16) scale(.82)">${ART.grandmother()}</g>${heart(60, 14, .6, '#FF4D6D')}`,
    granddaughter: () => `<g transform="translate(-24 26) scale(.8)">${ART.grandmother()}</g><g transform="translate(42 44) scale(.62)">${figure('girl', {shirt: '#FF6FA5', skin: SKIN[0]})}</g>${heart(96, 24, .6, '#FF4D6D')}`,
    grandson: () => `<g transform="translate(-24 26) scale(.8)">${ART.grandfather()}</g><g transform="translate(42 44) scale(.62)">${figure('boy', {shirt: '#3D8BFD', skin: SKIN[1]})}</g>${heart(96, 24, .6, '#FF4D6D')}`,
    aunt: () => figure('woman', {shirt: '#FF9F1C', hair: '#8D4A2B', skin: SKIN[1]}),
    uncle: () => figure('man', {shirt: '#5A67D8', mustache: true}),
    cousin: () => `<g transform="translate(-16 14) scale(.86)">${figure('child', {shirt: '#FFB703'})}</g><g transform="translate(32 14) scale(.86)">${figure('boy', {shirt: '#06D6A0', skin: SKIN[2]})}</g>`,
    relative: () => `<path d="M60 112 V70 M60 80 L34 56 M60 72 L86 50 M60 92 L92 82" stroke="#8D5A3B" stroke-width="7" stroke-linecap="round"/>
       <circle cx="60" cy="44" r="40" fill="#8EDB6E" opacity=".55"/>
       ${[[60, 22, '#FF9F1C'], [30, 50, '#3D8BFD'], [90, 44, '#FF6FA5'], [50, 74, '#2FA36B'], [94, 80, '#9B5DE5'], [22, 84, '#E63946']].map(([x, y, c]) =>
         `<circle cx="${x}" cy="${y}" r="11" fill="#fff" stroke="${c}" stroke-width="3"/><circle cx="${x}" cy="${y - 2}" r="4" fill="${c}"/><path d="M${x - 6} ${y + 7} a6 5 0 0 1 12 0" fill="${c}"/>`).join('')}`,
  });

  const board = (x, y, w, h, c = '#2F6B4F', inner = '') => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="4" fill="#8D5A3B"/><rect x="${x + 5}" y="${y + 5}" width="${w - 10}" height="${h - 10}" rx="2" fill="${c}"/>${inner}`;
  const deskA = (x, y, k = 1) => `<g transform="translate(${x} ${y}) scale(${k})"><rect x="-26" y="-4" width="52" height="8" rx="2" fill="#E9A66B"/><path d="M-22 4 v22 M22 4 v22" stroke="#C9653D" stroke-width="4"/></g>`;
  const pizza = (cut) => `<circle cx="60" cy="60" r="48" fill="#E9A66B"/><circle cx="60" cy="60" r="40" fill="#FFD166"/>
      ${[[44, 44], [74, 40], [80, 70], [50, 78], [62, 58], [36, 62]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="5" fill="#E63946"/>`).join('')}${cut}`;
  Object.assign(ART, {
    // ---------- ep27 classroom ----------
    classroom: () => board(18, 8, 84, 40, '#2F6B4F', `<text x="60" y="35" text-anchor="middle" font-size="14" ${FONT} fill="#fff">ABC</text>`)
       + [[30, 70], [90, 70], [30, 98], [90, 98], [60, 84]].map(([x, y]) => deskA(x, y, .55)).join(''),
    board: () => `<rect x="10" y="30" width="100" height="62" rx="4" fill="#E9A66B"/><path d="M14 44 H106 M14 60 H106 M14 76 H106" stroke="#C9934A" stroke-width="2.5"/>
       <path d="M24 34 q10 4 20 0 M70 66 q10 4 22 0" stroke="#B5703F" stroke-width="2" fill="none"/>`,
    blackboard: () => board(8, 18, 104, 70, '#2B2D42', `<text x="36" y="56" text-anchor="middle" font-size="18" ${FONT} fill="#fff">1+1</text>
       <path d="M64 46 h30 M64 60 h20" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>`) + `<rect x="18" y="88" width="84" height="6" rx="2" fill="#8D5A3B"/><path d="M40 94 l-6 20 M80 94 l6 20" stroke="#8D5A3B" stroke-width="5"/>`,
    chalk: () => `<path d="M14 92 q20 -24 46 -10 t48 -12" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".0"/>
       <rect x="20" y="70" width="80" height="40" rx="6" fill="#3D8BFD"/>${[[36, '#fff'], [52, '#FFD23F'], [68, '#FF8FAB'], [84, '#7FC8F8']].map(([x, c], i) =>
         `<rect x="${x - 5}" y="${30 + (i % 2) * 8}" width="10" height="46" rx="4" fill="${c}" transform="rotate(${(i - 1.5) * 8} ${x} 70)"/>`).join('')}
       <rect x="20" y="70" width="80" height="12" rx="4" fill="#2A6FD6"/>`,
    lesson: () => `<rect x="18" y="14" width="84" height="96" rx="8" fill="#fff" stroke="#5A67D8" stroke-width="4"/>
       <rect x="18" y="14" width="84" height="20" rx="8" fill="#5A67D8"/><text x="60" y="29" text-anchor="middle" font-size="12" ${FONT} fill="#fff">LESSON 1</text>
       ${[46, 62, 78, 94].map(y => `<path d="M30 ${y} h${y === 94 ? 34 : 60}" stroke="#C5CBE0" stroke-width="5" stroke-linecap="round"/>`).join('')}`,
    monitor: () => figure('boy', {shirt: '#2FA36B'}) + `<rect x="66" y="86" width="22" height="14" rx="3" fill="#E63946"/><path d="M70 93 h14" stroke="#fff" stroke-width="2.5"/>${star(100, 22, 10, 4, '#FFD23F')}`,
    student: () => figure('child', {shirt: '#3D8BFD'}) + `<path d="M34 84 v30 M86 84 v30" stroke="#FF7A59" stroke-width="7" stroke-linecap="round"/>` + `<g transform="translate(86 26) scale(.6)">${notebook(0, 0, 1, '#FF7A59')}</g>`,
    desk: () => `<rect x="12" y="50" width="96" height="14" rx="3" fill="#E9A66B"/><rect x="18" y="64" width="84" height="18" fill="#C9934A"/>
       <path d="M22 82 v28 M98 82 v28" stroke="#B5703F" stroke-width="7" stroke-linecap="round"/>` + `<g transform="translate(44 30) scale(.4)">${ART.book()}</g>`,
    seat: () => `<rect x="34" y="14" width="10" height="96" rx="4" fill="#B5703F"/><rect x="34" y="14" width="52" height="34" rx="6" fill="#E9A66B"/>
       <rect x="34" y="62" width="58" height="12" rx="4" fill="#E9A66B"/><path d="M86 74 v36 M42 74 v36" stroke="#B5703F" stroke-width="7" stroke-linecap="round"/>`,
    row: () => [30, 60, 90].map(x => `<g transform="translate(${x - 18} 28) scale(.3)">${ART.seat()}</g>`).join('')
       + [30, 60, 90].map(x => `<g transform="translate(${x - 18} 68) scale(.3)">${ART.seat()}</g>`).join('')
       + `<rect x="8" y="24" width="104" height="44" rx="10" fill="none" stroke="#FFB703" stroke-width="4" stroke-dasharray="6 5"/>`,
    group: () => `<circle cx="60" cy="64" r="48" fill="#FFF3C4"/>` + [[60, 38, '#E63946'], [34, 72, '#3D8BFD'], [86, 72, '#2FA36B'], [60, 92, '#9B5DE5']].map(([x, y, c]) =>
         `<circle cx="${x}" cy="${y - 6}" r="9" fill="${SKIN[0]}"/><path d="M${x - 13} ${y + 16} a13 12 0 0 1 26 0z" fill="${c}"/>`).join('')
       + `<rect x="46" y="58" width="28" height="12" rx="3" fill="#E9A66B"/>`,

    // ---------- ep28 measures ----------
    tall: () => `<path d="M14 112 H106" stroke="#C5CBE0" stroke-width="4"/>` + `<g transform="translate(-10 -6) scale(1.05)">${figure('man', {shirt: '#3D8BFD'})}</g>`.replace('<g transform="translate(-10 -6) scale(1.05)">', '<g transform="translate(-16 -2) scale(1)">')
       + `<path d="M98 10 V110 M90 18 l8 -8 l8 8 M90 102 l8 8 l8 -8" stroke="#2FA36B" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    short: () => `<path d="M14 112 H106" stroke="#C5CBE0" stroke-width="4"/><g transform="translate(-4 40) scale(.62)">${figure('boy', {shirt: '#FF9F1C'})}</g>
       <path d="M98 66 V110 M90 74 l8 -8 l8 8 M90 102 l8 8 l8 -8" stroke="#E63946" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    long: () => `<path d="M14 54 C14 34 30 28 46 34 L96 52 C112 58 110 82 94 82 L30 76 C18 74 14 64 14 54Z" fill="#6CCB5F"/>
       <path d="M30 60 C50 56 70 64 92 64" stroke="#3FA34D" stroke-width="3" fill="none"/><circle cx="26" cy="48" r="4" fill="${INK}"/>
       <path d="M8 96 H112 M16 88 l-8 8 l8 8 M104 88 l8 8 l-8 8" stroke="#3D8BFD" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    straight: () => `<path d="M10 40 H110" stroke="#2FA36B" stroke-width="7" stroke-linecap="round"/>${check(104, 22, 1)}
       <path d="M10 84 q12 -16 25 0 t25 0 t25 0 t25 0" stroke="#C5CBE0" stroke-width="7" fill="none" stroke-linecap="round"/>`
       + `<path d="M98 72 l12 12 M110 72 l-12 12" stroke="#E63946" stroke-width="4" stroke-linecap="round"/>`,
    inch: () => `<rect x="6" y="40" width="108" height="40" rx="4" fill="#FFD23F" stroke="#E0A100" stroke-width="2"/>
       ${Array.from({length: 17}, (_, i) => `<path d="M${12 + i * 6} 40 v${i % 4 ? (i % 2 ? 6 : 10) : 16}" stroke="#8D5A3B" stroke-width="2"/>`).join('')}
       <text x="12" y="74" font-size="12" ${FONT} fill="#8D5A3B">0</text><text x="108" y="74" text-anchor="end" font-size="12" ${FONT} fill="#8D5A3B">4</text>
       <path d="M12 96 H36 M12 90 v12 M36 90 v12" stroke="#E63946" stroke-width="3"/><text x="44" y="102" font-size="14" ${FONT} fill="#E63946">1 inch</text>`,
    thick: () => `<g transform="translate(0 6)">${[0, 1, 2, 3, 4].map(i => `<rect x="20" y="${76 - i * 12}" width="80" height="12" rx="2" fill="${['#E63946', '#3D8BFD', '#2FA36B', '#FF9F1C', '#9B5DE5'][i]}"/><rect x="26" y="${78 - i * 12}" width="68" height="8" fill="#fff" opacity=".85"/>`).join('')}</g>
       <path d="M108 30 V94 M102 36 l6 -6 l6 6 M102 88 l6 6 l6 -6" stroke="#2B2D42" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    thin: () => `<rect x="20" y="62" width="80" height="6" rx="2" fill="#3D8BFD"/><rect x="26" y="63" width="68" height="4" fill="#fff" opacity=".85"/>
       <path d="M108 56 V74" stroke="#2B2D42" stroke-width="3.5" stroke-linecap="round"/><path d="M60 22 v28 M54 44 l6 6 l6 -6" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    lot: () => `<path d="M24 36 H96 L88 110 H32Z" fill="#E63946"/><path d="M40 36 V110 M60 36 V110 M80 36 V110" stroke="#fff" stroke-width="7" opacity=".9"/>
       ${[[34, 30], [48, 22], [62, 26], [76, 20], [90, 30], [42, 12], [70, 10], [56, 14], [84, 16]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="9" fill="#FFF3C4" stroke="#F4D58D" stroke-width="2"/>`).join('')}`,
    much: () => `<path d="M30 30 h22 v8 q10 8 10 20 v48 h-42 v-48 q0 -12 10 -20z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><path d="M22 60 h38 v46 h-38z" fill="#7FC8F8"/>
       <path d="M70 30 h22 v8 q10 8 10 20 v48 h-42 v-48 q0 -12 10 -20z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><path d="M62 92 h38 v14 h-38z" fill="#7FC8F8"/>
       ${check(42, 18, 1)}`,
    weigh: () => `<rect x="20" y="40" width="80" height="70" rx="14" fill="#E63946"/><circle cx="60" cy="76" r="24" fill="#fff"/>
       ${Array.from({length: 9}, (_, i) => `<path d="M60 56 v5" stroke="#8A8FA3" stroke-width="2" transform="rotate(${-80 + i * 20} 60 76)"/>`).join('')}
       <path d="M60 76 L72 62" stroke="${INK}" stroke-width="3" stroke-linecap="round"/><rect x="14" y="26" width="92" height="12" rx="4" fill="#8A8FA3"/>
       <path d="M24 26 q36 -24 72 0" fill="#FF9F1C"/><circle cx="46" cy="16" r="8" fill="#E63946"/><circle cx="72" cy="14" r="9" fill="#2FA36B"/>`,
    half: () => pizza(`<path d="M60 12 V108" stroke="#fff" stroke-width="5"/><path d="M60 12 A48 48 0 0 1 60 108Z" fill="#fff" opacity=".55"/>`),
    quarter: () => pizza(`<path d="M60 12 V108 M12 60 H108" stroke="#fff" stroke-width="5"/><path d="M60 60 V12 A48 48 0 0 1 108 60Z" fill="#fff" opacity="0"/>
       <path d="M60 60 V12 A48 48 0 0 1 108 60Z" fill="none" stroke="#2FA36B" stroke-width="5"/>`).replace('<circle cx="60" cy="60" r="40" fill="#FFD166"/>', '<circle cx="60" cy="60" r="40" fill="#FFD166"/>')
       + `<path d="M12 60 A48 48 0 0 1 60 12 V60Z M12 60 A48 48 0 0 0 60 108 V60Z M60 108 A48 48 0 0 0 108 60 H60Z" fill="#fff" opacity=".55"/>`,
  });

  const sheet = (inner, c = '#fff', st = '#C5CBE0') => `<rect x="22" y="10" width="76" height="100" rx="6" fill="${c}" stroke="${st}" stroke-width="3"/>${inner}`;
  Object.assign(ART, {
    // ---------- ep29 clubs ----------
    club: () => `<path d="M14 30 L60 10 L106 30Z" fill="#E63946"/><rect x="20" y="30" width="80" height="78" rx="4" fill="#FFF3C4"/>
       <rect x="30" y="40" width="60" height="20" rx="4" fill="#5A67D8"/><text x="60" y="55" text-anchor="middle" font-size="14" ${FONT} fill="#fff">CLUB</text>
       <rect x="48" y="74" width="24" height="34" rx="3" fill="#B5703F"/>${star(32, 82, 7, 3, '#FFB703')}${star(88, 82, 7, 3, '#FFB703')}`,
    join: () => `<circle cx="74" cy="60" r="32" fill="#2FA36B" opacity=".25"/>` + [[64, 48], [86, 48], [74, 74]].map(([x, y]) => `<circle cx="${x}" cy="${y - 6}" r="7" fill="${SKIN[0]}"/><path d="M${x - 10} ${y + 12} a10 9 0 0 1 20 0z" fill="#2FA36B"/>`).join('')
       + `<circle cx="22" cy="58" r="8" fill="${SKIN[1]}"/><path d="M11 78 a11 10 0 0 1 22 0z" fill="#FF9F1C"/>
          <path d="M34 50 h14 m-6 -6 l6 6 l-6 6" stroke="#FF9F1C" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    chess: () => `<rect x="10" y="78" width="100" height="32" rx="4" fill="#8D5A3B"/>${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `<rect x="${14 + i * 11.5}" y="82" width="11.5" height="11" fill="${i % 2 ? '#F4D3A8' : '#5A3825'}"/><rect x="${14 + i * 11.5}" y="93" width="11.5" height="11" fill="${i % 2 ? '#5A3825' : '#F4D3A8'}"/>`).join('')}
       <path d="M36 76 h28 l-4 -8 h-20z M40 68 C38 56 44 50 40 42 C48 30 62 30 62 44 C62 50 58 52 60 68Z" fill="#2B2D42"/><circle cx="50" cy="40" r="2.5" fill="#fff"/>
       <path d="M72 76 h24 l-3 -8 h-18z M77 68 C76 58 80 52 76 46 h16 c-4 6 0 12 -1 22z M80 46 l4 -10 l4 10z" fill="#fff" stroke="#2B2D42" stroke-width="2"/>`,
    painting: () => `<path d="M30 112 L46 20 M90 112 L74 20 M60 112 V60" stroke="#B5703F" stroke-width="5" stroke-linecap="round"/>
       <rect x="24" y="14" width="72" height="56" rx="3" fill="#fff" stroke="#E9A66B" stroke-width="4"/>
       <path d="M30 64 L48 40 L60 54 L72 36 L90 64Z" fill="#6CCB5F"/>${sun(78, 28, 6)}`,
    imagine: () => `<g transform="translate(-26 26) scale(.85)">${figure('girl', {shirt: '#9B5DE5'})}</g>`
       + thought(80, 32, 64, 50, `<path d="M-14 6 q-4 -14 8 -16 q2 -10 12 -6 q10 -4 12 6 q8 6 0 16z" fill="#FF8FAB"/>${star(14, -12, 6, 2.5, '#FFD23F')}<path d="M-6 6 l-4 10 M6 6 l4 10" stroke="#9B5DE5" stroke-width="2.5"/>`),
    camera: () => `<rect x="10" y="34" width="100" height="70" rx="12" fill="#2B2D42"/><rect x="38" y="24" width="30" height="14" rx="4" fill="#2B2D42"/>
       <circle cx="60" cy="69" r="24" fill="#6B7085"/><circle cx="60" cy="69" r="16" fill="#3D8BFD"/><circle cx="54" cy="63" r="5" fill="#fff" opacity=".7"/>
       <rect x="88" y="42" width="14" height="8" rx="2" fill="#FFD23F"/><circle cx="22" cy="44" r="4" fill="#E63946"/>`,
    photo: () => `<g transform="rotate(-6 60 60)"><rect x="14" y="16" width="92" height="86" rx="4" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <rect x="22" y="24" width="76" height="58" fill="#BDE7FF"/><path d="M22 82 L44 58 L58 72 L74 52 L98 82Z" fill="#6CCB5F"/>${sun(84, 36, 6)}</g>`,
    background: () => `<rect x="10" y="14" width="100" height="92" rx="8" fill="#BDE7FF"/><path d="M10 80 L36 50 L56 70 L78 42 L110 80 V98 a8 8 0 0 1 -8 8 H18 a8 8 0 0 1 -8 -8Z" fill="#8EDB6E"/>`
       + sun(88, 32, 9) + `<g transform="translate(26 40) scale(.6)">${figure('child', {shirt: '#E63946'})}</g>`
       + `<rect x="10" y="14" width="100" height="92" rx="8" fill="none" stroke="#FFB703" stroke-width="4" stroke-dasharray="7 5"/>`,
    tent: () => `<path d="M8 104 H112" stroke="#6CCB5F" stroke-width="6" stroke-linecap="round"/>
       <path d="M14 100 L60 22 L106 100Z" fill="#FF9F1C"/><path d="M60 22 L72 100 H48Z" fill="#B5482A"/><path d="M60 22 L56 10 M60 22 L64 10" stroke="#8D5A3B" stroke-width="3"/>
       <path d="M60 22 L86 100" stroke="#E07A4F" stroke-width="2"/>`,
    camping: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#2B2D6E"/>` + twinkles([[22, 22, 5], [96, 18, 5], [70, 30, 4]])
       + `<path d="M4 90 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#3FA34D"/>
          <path d="M14 92 L44 40 L74 92Z" fill="#FF9F1C"/><path d="M44 40 L52 92 H36Z" fill="#B5482A"/>
          <path d="M84 94 l10 -12 l10 12z" fill="#8D5A3B"/>${flame(94, 82, 1.3)}`,
    magazine: () => `<g transform="rotate(8 60 60)">${sheet(`<rect x="22" y="10" width="76" height="40" rx="6" fill="#FF6FA5"/><text x="60" y="30" text-anchor="middle" font-size="14" ${FONT} fill="#fff">KIDS</text>
       <text x="60" y="44" text-anchor="middle" font-size="9" ${FONT} fill="#fff">MAGAZINE</text><circle cx="44" cy="74" r="12" fill="#FFD23F"/>
       <path d="M62 66 h28 M62 76 h28 M32 96 h56" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>`)}</g>`,
    article: () => sheet(`<path d="M32 24 h56" stroke="#2B2D42" stroke-width="7" stroke-linecap="round"/><rect x="32" y="36" width="24" height="22" rx="2" fill="#7FC8F8"/>
       ${[38, 46, 54].map(y => `<path d="M62 ${y} h26" stroke="#C5CBE0" stroke-width="3.5" stroke-linecap="round"/>`).join('')}
       ${[68, 78, 88, 98].map(y => `<path d="M32 ${y} h${y === 98 ? 34 : 56}" stroke="#C5CBE0" stroke-width="3.5" stroke-linecap="round"/>`).join('')}`),
    poem: () => sheet(`<text x="60" y="34" text-anchor="middle" font-size="14" ${FONT} fill="#9B5DE5">Poem</text>
       ${[50, 64, 78, 92].map((y, i) => `<path d="M${36 + (i % 2) * 8} ${y} h${40 - (i % 2) * 8}" stroke="#C5CBE0" stroke-width="3.5" stroke-linecap="round"/>`).join('')}`, '#FFF8EE', '#E3C8A0')
       + `<path d="M88 104 C96 82 108 74 116 72 C112 86 102 98 88 104Z" fill="#9B5DE5"/><path d="M88 104 L110 78" stroke="#fff" stroke-width="1.5"/>`,
    inspiration: () => `<circle cx="60" cy="50" r="30" fill="#FFD23F"/><path d="M46 74 h28 v14 a6 6 0 0 1 -6 6 h-16 a6 6 0 0 1 -6 -6z" fill="#8A8FA3"/>
       <path d="M48 80 h24 M48 86 h24" stroke="#C5CBE0" stroke-width="2"/><path d="M52 52 q8 -12 16 0 M60 46 v24" stroke="#E0A100" stroke-width="3" fill="none"/>
       ${[0, 45, 90, 135, 180, 225, 315].map(a => `<path d="M60 ${50 - 38} v-8" stroke="#FFB703" stroke-width="4" stroke-linecap="round" transform="rotate(${a - 90} 60 50)"/>`).join('')}`,

    // ---------- ep30 music ----------
    music: () => `<path d="M42 92 V30 L96 18 V80" stroke="#9B5DE5" stroke-width="7" fill="none" stroke-linejoin="round"/><path d="M42 40 L96 28" stroke="#9B5DE5" stroke-width="10"/>
       <ellipse cx="32" cy="92" rx="13" ry="10" fill="#9B5DE5"/><ellipse cx="86" cy="80" rx="13" ry="10" fill="#9B5DE5"/>${note(104, 100, '#FF6FA5')}`,
    sound: () => `<rect x="20" y="16" width="52" height="92" rx="8" fill="#2B2D42"/><circle cx="46" cy="40" r="11" fill="#6B7085"/><circle cx="46" cy="40" r="5" fill="#2B2D42"/>
       <circle cx="46" cy="80" r="19" fill="#6B7085"/><circle cx="46" cy="80" r="9" fill="#2B2D42"/>
       <path d="M82 60 q8 12 0 24 M92 52 q14 20 0 40 M102 44 q20 28 0 56" stroke="#3D8BFD" stroke-width="4" fill="none" stroke-linecap="round" transform="translate(0 -12)"/>`,
    noise: () => `<g transform="translate(-6 18) scale(.86)">${figure('boy', {shirt: '#8A8FA3'})}</g>`
       + `<path d="M30 58 l-6 -14 M90 58 l6 -14" stroke="#fff" stroke-width="0"/>` + hand(34, 62, .55, -60, SKIN[0]) + `<g transform="translate(120 0) scale(-1 1)">${hand(34, 62, .55, -60, SKIN[0])}</g>`
       + `<path d="M8 20 l10 6 l-8 4 l10 6 M112 20 l-10 6 l8 4 l-10 6" stroke="#E63946" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`
       + `<text x="60" y="18" text-anchor="middle" font-size="16" ${FONT} fill="#E63946">!!</text>`,
    concert: () => `<path d="M4 84 H116 V116 H4Z" fill="#8D5A3B"/><path d="M4 8 Q30 30 30 84 H4Z M116 8 Q90 30 90 84 H116Z" fill="#E63946"/>
       <path d="M40 8 L28 84 M80 8 L92 84" stroke="#FFD23F" stroke-width="0"/><path d="M60 0 L30 84 H90Z" fill="#FFF3C4" opacity=".45"/>
       <g transform="translate(24 30) scale(.6)">${figure('woman', {shirt: '#9B5DE5'})}</g>${note(36, 40, '#FFD23F')}${note(90, 34, '#FFD23F')}`,
    song: () => `<path d="M10 60 C30 30 50 90 70 60 S100 40 112 52" stroke="#C5CBE0" stroke-width="3" fill="none"/>` + note(30, 64, '#FF6FA5') + note(64, 48, '#3D8BFD') + note(98, 62, '#2FA36B')
       + `<text x="60" y="104" text-anchor="middle" font-size="20" ${FONT} fill="#9B5DE5">la la la</text>`,
    sing: () => figure('girl', {shirt: '#FF6FA5'}) + `<ellipse cx="60" cy="58" rx="4" ry="5" fill="#9D0208"/>
       <rect x="78" y="62" width="8" height="30" rx="3" fill="#2B2D42" transform="rotate(-25 82 77)"/><circle cx="88" cy="56" r="8" fill="#6B7085"/>` + note(100, 30, '#9B5DE5') + note(20, 34, '#3D8BFD'),
    voice: () => `<path d="M30 16 C58 16 74 34 74 56 L84 72 L74 76 V88 Q74 98 64 98 H56 V112 H22 V88 C10 78 8 60 12 44 C16 28 22 16 30 16Z" fill="${SKIN[0]}"/>
       <path d="M74 84 h-10" stroke="#C98F68" stroke-width="3" stroke-linecap="round"/>
       <path d="M90 64 q8 10 0 20 M98 56 q14 18 0 36 M106 48 q20 26 0 52" stroke="#9B5DE5" stroke-width="4" fill="none" stroke-linecap="round" transform="translate(-4 -8)"/>`,
    terrible: () => `<circle cx="60" cy="60" r="44" fill="#B9E28C"/><path d="M38 48 l14 6 M82 48 l-14 6" stroke="${INK}" stroke-width="4" stroke-linecap="round"/>
       <circle cx="46" cy="60" r="4" fill="${INK}"/><circle cx="74" cy="60" r="4" fill="${INK}"/>
       <path d="M40 88 q5 -8 10 0 t10 0 t10 0 t10 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>
       <path d="M96 30 q8 -6 8 -16 M24 30 q-8 -6 -8 -16" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    piano: () => `<rect x="8" y="30" width="104" height="60" rx="6" fill="#2B2D42"/><rect x="14" y="54" width="92" height="32" fill="#fff"/>
       ${Array.from({length: 9}, (_, i) => `<path d="M${14 + (i + 1) * 9.2} 54 V86" stroke="#C5CBE0" stroke-width="1.5"/>`).join('')}
       ${[0, 1, 3, 4, 5, 7, 8].map(i => `<rect x="${14 + (i + 1) * 9.2 - 3}" y="54" width="6" height="18" fill="#2B2D42"/>`).join('')}
       <path d="M22 90 v20 M98 90 v20" stroke="#2B2D42" stroke-width="6" stroke-linecap="round"/>${note(96, 22, '#FF6FA5')}`,
    violin: () => `<g transform="rotate(30 60 60)"><path d="M60 4 V30" stroke="#5A3825" stroke-width="7"/><path d="M54 8 h12" stroke="#5A3825" stroke-width="4"/>
       <path d="M60 30 C42 30 40 46 48 56 C38 62 38 92 60 98 C82 92 82 62 72 56 C80 46 78 30 60 30Z" fill="#C1440E"/>
       <path d="M54 50 q-4 6 0 12 M66 50 q4 6 0 12" stroke="#5A3825" stroke-width="2.5" fill="none"/><path d="M60 34 V86" stroke="#F4D3A8" stroke-width="1.5"/>
       <rect x="54" y="84" width="12" height="5" fill="#2B2D42"/></g><path d="M14 30 L106 96" stroke="#8D5A3B" stroke-width="3" stroke-linecap="round"/>`,
    drum: () => `<ellipse cx="60" cy="50" rx="44" ry="14" fill="#F4F1E8" stroke="#C5CBE0" stroke-width="3"/><path d="M16 50 V90 Q60 110 104 90 V50 Q60 66 16 50Z" fill="#E63946"/>
       <path d="M16 56 L40 94 L60 66 L80 94 L104 56" stroke="#FFD23F" stroke-width="3" fill="none"/>
       <path d="M40 30 L74 4 M80 30 L104 10" stroke="#B5703F" stroke-width="5" stroke-linecap="round"/><circle cx="74" cy="4" r="5" fill="#F4D3A8"/><circle cx="104" cy="10" r="5" fill="#F4D3A8"/>`,
    guitar: () => `<g transform="rotate(-35 60 64)"><rect x="54" y="4" width="12" height="54" fill="#8D5A3B"/><rect x="50" y="0" width="20" height="12" rx="3" fill="#5A3825"/>
       <path d="M60 52 C40 52 36 66 42 76 C30 82 30 108 60 112 C90 108 90 82 78 76 C84 66 80 52 60 52Z" fill="#FF9F1C"/>
       <circle cx="60" cy="80" r="8" fill="#5A3825"/><rect x="50" y="96" width="20" height="5" fill="#5A3825"/>
       <path d="M57 6 V98 M63 6 V98" stroke="#fff" stroke-width="1" opacity=".8"/></g>`,
  });

  const dog = (x, y, k, c = '#E9A66B', ear = '#B5703F', spot = false) => `<g transform="translate(${x} ${y}) scale(${k})">
      <ellipse cx="0" cy="34" rx="18" ry="20" fill="${c}"/><circle cx="0" cy="0" r="20" fill="${c}"/>
      <ellipse cx="-17" cy="2" rx="7" ry="13" fill="${ear}" transform="rotate(15 -17 2)"/><ellipse cx="17" cy="2" rx="7" ry="13" fill="${ear}" transform="rotate(-15 17 2)"/>
      ${spot ? `<circle cx="7" cy="-6" r="7" fill="${ear}"/>` : ''}<circle cx="-7" cy="-2" r="2.6" fill="${INK}"/><circle cx="7" cy="-2" r="2.6" fill="${INK}"/>
      <ellipse cx="0" cy="7" rx="4.5" ry="3.2" fill="${INK}"/><path d="M-4 12 q4 3 8 0" stroke="${INK}" stroke-width="1.8" fill="none"/></g>`;
  const thumb = (x, y, k, up = true, c = SKIN[0]) => `<g transform="translate(${x} ${y}) scale(${k}) rotate(${up ? 0 : 180})">
      <rect x="-14" y="-4" width="34" height="32" rx="9" fill="${c}"/><rect x="-20" y="-28" width="14" height="34" rx="7" fill="${c}" transform="rotate(-8 -13 -10)"/>
      <path d="M-2 4 h20 M-2 12 h20 M-2 20 h20" stroke="${SKIN[1]}" stroke-width="2.4" stroke-linecap="round"/></g>`;
  const calPage = (top, big, c = '#E63946', sub = '') => `<rect x="16" y="14" width="88" height="94" rx="10" fill="#fff" stroke="#E3E6F5" stroke-width="3"/>
      <path d="M16 24 a10 10 0 0 1 10 -10 h68 a10 10 0 0 1 10 10 v14 h-88z" fill="${c}"/>
      <rect x="36" y="6" width="6" height="16" rx="3" fill="#8A8FA3"/><rect x="78" y="6" width="6" height="16" rx="3" fill="#8A8FA3"/>
      <text x="60" y="33" text-anchor="middle" font-size="14" ${FONT} fill="#fff">${top}</text>
      <text x="60" y="${sub ? 80 : 88}" text-anchor="middle" font-size="${big.length > 2 ? 30 : 44}" ${FONT} fill="${INK}">${big}</text>
      ${sub ? `<text x="60" y="100" text-anchor="middle" font-size="12" ${FONT} fill="#8A8FA3">${sub}</text>` : ''}`;
  const arrowR = (x1, y, x2, c = '#8A8FA3', w = 5) => `<path d="M${x1} ${y} H${x2} m-9 -8 l9 8 l-9 8" stroke="${c}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
  const person = (kind, o, x, y, k) => `<g transform="translate(${x} ${y}) scale(${k})">${figure(kind, o)}</g>`;
  Object.assign(ART, {
    // ---------- ep31 compare ----------
    compare: () => `<path d="M60 22 V100 M30 104 h60" stroke="#8D5A3B" stroke-width="5" stroke-linecap="round"/><path d="M18 40 L102 30" stroke="#8D5A3B" stroke-width="5" stroke-linecap="round"/>
       <path d="M18 40 l-10 26 h20z M102 30 l-10 26 h20z" fill="none" stroke="#8A8FA3" stroke-width="2.5"/>
       <path d="M4 66 a14 6 0 0 0 28 0z" fill="#FF9F1C"/><path d="M88 56 a14 6 0 0 0 28 0z" fill="#3D8BFD"/><circle cx="60" cy="22" r="6" fill="#FFD23F"/>`,
    same: () => dog(34, 40, 1.05) + dog(88, 40, 1.05) + `<text x="61" y="112" text-anchor="middle" font-size="26" ${FONT} fill="#2FA36B">=</text>`,
    different: () => dog(34, 40, 1.05) + dog(88, 40, 1.05, '#fff', '#2B2D42', true) + `<text x="61" y="112" text-anchor="middle" font-size="26" ${FONT} fill="#E63946">≠</text>`,
    as: () => `<rect x="10" y="34" width="38" height="52" rx="8" fill="#3D8BFD"/><rect x="72" y="34" width="38" height="52" rx="8" fill="#3D8BFD"/>
       <path d="M10 26 H110" stroke="#FFB703" stroke-width="4" stroke-dasharray="6 5"/><path d="M10 94 H110" stroke="#FFB703" stroke-width="4" stroke-dasharray="6 5"/>
       <path d="M52 60 h16" stroke="#8A8FA3" stroke-width="4"/>`,
    good: () => `<circle cx="60" cy="60" r="48" fill="#E8F7EE"/>` + thumb(60, 70, 1.5),
    well: () => `<circle cx="60" cy="60" r="46" fill="#2FA36B"/>` + check(60, 62, 3, '#fff'),
    bad: () => `<circle cx="60" cy="60" r="48" fill="#FDECEC"/>` + thumb(60, 50, 1.5, false, SKIN[1]),
    badly: () => `<circle cx="60" cy="60" r="46" fill="#E63946"/><path d="M40 40 L80 80 M80 40 L40 80" stroke="#fff" stroke-width="12" stroke-linecap="round"/>`,
    quite: () => `<rect x="14" y="48" width="92" height="24" rx="12" fill="#E3E6F5"/><rect x="14" y="48" width="70" height="24" rx="12" fill="#FF9F1C"/>
       <text x="60" y="34" text-anchor="middle" font-size="18" ${FONT} fill="#8A8FA3">75%</text>`,
    cool: () => `<circle cx="60" cy="62" r="44" fill="#FFD23F"/><path d="M22 52 h76 l-4 16 q-12 8 -24 0 l-4 -10 h-12 l-4 10 q-12 8 -24 0z" fill="#2B2D42"/>
       <path d="M42 84 q18 14 36 0" stroke="${INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M30 58 l8 -4" stroke="#fff" stroke-width="3" stroke-linecap="round"/>`,
    great: () => star(60, 62, 46, 20, '#FFB703') + star(60, 62, 26, 11, '#FFD23F') + star(18, 22, 7, 3, '#FF6FA5') + star(102, 26, 8, 3.4, '#3D8BFD'),

    // ---------- ep32 time line ----------
    yesterday: () => calPage('昨天', '←', '#8A8FA3', 'yesterday'),
    today: () => calPage('今天', '★', '#E63946', 'today'),
    tomorrow: () => calPage('明天', '→', '#3D8BFD', 'tomorrow'),
    past: () => `<path d="M14 60 H106" stroke="#C5CBE0" stroke-width="5"/>${[[24, 0], [48, 1], [72, 2]].map(([x, i]) => `<circle cx="${x}" cy="60" r="8" fill="#8A8FA3" opacity="${.4 + i * .2}"/>`).join('')}
       <circle cx="98" cy="60" r="11" fill="#E63946"/><path d="M60 34 H20 m10 -8 l-10 8 l10 8" stroke="#8D5A3B" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <text x="40" y="96" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">过去</text>`,
    future: () => `<path d="M14 60 H106" stroke="#C5CBE0" stroke-width="5"/><circle cx="22" cy="60" r="11" fill="#E63946"/>${[[48, 0], [72, 1], [96, 2]].map(([x, i]) => `<circle cx="${x}" cy="60" r="8" fill="#3D8BFD" opacity="${.8 - i * .2}"/>`).join('')}
       <path d="M60 34 H100 m-10 -8 l10 8 l-10 8" stroke="#3D8BFD" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>${star(96, 92, 8, 3.4, '#FFD23F')}`,
    daily: () => [0, 1, 2, 3, 4, 5, 6].map(i => `<rect x="${12 + (i % 4) * 26}" y="${22 + Math.floor(i / 4) * 40}" width="22" height="32" rx="4" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>
         <rect x="${12 + (i % 4) * 26}" y="${22 + Math.floor(i / 4) * 40}" width="22" height="8" rx="3" fill="#FF9F1C"/>${check(23 + (i % 4) * 26, 44 + Math.floor(i / 4) * 40, .55)}`).join('')
       + `<path d="M94 74 a12 12 0 1 1 -4 -9" stroke="#2FA36B" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M86 60 l6 4 l-6 4z" fill="#2FA36B"/>`,
    tonight: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#2B2D6E"/>` + moon(60, 48, 24) + twinkles([[24, 30, 6], [96, 26, 5], [92, 84, 6]])
       + `<path d="M4 88 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#3B3F8F"/>${[22, 46, 74, 98].map(x => `<rect x="${x - 6}" y="76" width="12" height="20" fill="#5A5FA8"/><rect x="${x - 3}" y="82" width="6" height="6" fill="#FFE08A"/>`).join('')}`,
    allday: () => `<path d="M10 92 A50 50 0 0 1 110 92" fill="#BDE7FF"/>${sun(60, 44, 12)}<path d="M10 92 H110" stroke="#2BB3A3" stroke-width="5"/>
       <path d="M16 92 A44 44 0 0 1 104 92" stroke="#FF9F1C" stroke-width="4" fill="none" stroke-dasharray="6 5"/>
       <text x="60" y="114" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">早 → 晚</text>`,
    since: () => `<path d="M24 40 V80 M24 60 H106 m-10 -8 l10 8 l-10 8" stroke="#E63946" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <circle cx="24" cy="60" r="10" fill="#E63946"/><text x="64" y="44" text-anchor="middle" font-size="16" ${FONT} fill="#8A8FA3">从…起</text>`,
    until: () => `<path d="M14 60 H86 m-10 -8 l10 8 l-10 8 M96 40 V80" stroke="#3D8BFD" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <text x="52" y="44" text-anchor="middle" font-size="16" ${FONT} fill="#8A8FA3">直到…</text>`,

    // ---------- ep33 learning ----------
    learn: () => person('child', {shirt: '#3D8BFD'}, 0, 0, 1) + `<g transform="translate(34 70) scale(.44)">${ART.book()}</g>` + mini('inspiration', 100, 22, .3),
    read: () => `<path d="M60 36 C44 26 22 26 10 32 V96 C22 90 44 90 60 100 C76 90 98 90 110 96 V32 C98 26 76 26 60 36Z" fill="#fff" stroke="#3D8BFD" stroke-width="4"/>
       <path d="M60 36 V100" stroke="#3D8BFD" stroke-width="3"/>${[48, 60, 72].map(y => `<path d="M20 ${y} q16 -4 32 2 M68 ${y + 2} q16 -6 32 -2" stroke="#C5CBE0" stroke-width="3" fill="none"/>`).join('')}
       <circle cx="44" cy="20" r="6" fill="${INK}"/><circle cx="76" cy="20" r="6" fill="${INK}"/>`,
    story: () => `<path d="M60 30 C44 20 22 20 10 26 V100 C22 94 44 94 60 104 C76 94 98 94 110 100 V26 C98 20 76 20 60 30Z" fill="#FFF3C4" stroke="#E0A100" stroke-width="4"/>
       <path d="M60 30 V104" stroke="#E0A100" stroke-width="3"/>` + mini('toy', 34, 64, .3) + `<path d="M74 76 l10 -26 l10 26z" fill="#2FA36B"/>${star(86, 40, 7, 3, '#FF9F1C')}`,
    write: () => `<rect x="14" y="20" width="76" height="90" rx="6" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <path d="M24 44 q8 -10 14 0 t14 0 M24 62 q10 -8 18 0 t18 0 M24 80 h28" stroke="#3D8BFD" stroke-width="3.5" fill="none" stroke-linecap="round"/>` + pencil(92, 56, 1.1, 35),
    spell: () => ['C', 'A', 'T'].map((c, i) => `<rect x="${10 + i * 36}" y="${40 + (i % 2) * 8}" width="30" height="34" rx="6" fill="${['#E63946', '#FF9F1C', '#2FA36B'][i]}"/>
         <text x="${25 + i * 36}" y="${66 + (i % 2) * 8}" text-anchor="middle" font-size="24" ${FONT} fill="#fff">${c}</text>`).join('')
       + `<text x="60" y="108" text-anchor="middle" font-size="16" ${FONT} fill="#8A8FA3">C-A-T</text>`,
    spelling: () => `<rect x="16" y="14" width="88" height="94" rx="8" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       ${['apple', 'book', 'cat'].map((w, i) => `<text x="28" y="${44 + i * 26}" font-size="15" ${FONT} fill="${INK}">${i + 1}. ${w}</text>${check(96, 38 + i * 26, .6)}`).join('')}`,
    speech: () => `<rect x="38" y="64" width="44" height="46" rx="4" fill="#B5703F"/><rect x="34" y="60" width="52" height="8" rx="3" fill="#8D5A3B"/>`
       + person('boy', {shirt: '#2FA36B'}, 22, -2, .64) + `<path d="M68 56 L76 40" stroke="#2B2D42" stroke-width="3"/><circle cx="77" cy="38" r="4" fill="#2B2D42"/>`
       + `<path d="M90 30 q6 6 0 12 M98 24 q10 12 0 24" stroke="#FF9F1C" stroke-width="3" fill="none" stroke-linecap="round"/>`,
    explain: () => board(40, 14, 76, 54, '#2F6B4F', `<text x="78" y="48" text-anchor="middle" font-size="16" ${FONT} fill="#fff">A→B</text>`)
       + person('man', {shirt: '#5A67D8', skin: SKIN[1]}, -22, 24, .8) + `<path d="M48 80 L64 56" stroke="#8D5A3B" stroke-width="3.5" stroke-linecap="round"/>`,
    clear: () => `<circle cx="50" cy="50" r="30" fill="#E3F4FF" stroke="#3D8BFD" stroke-width="7"/><path d="M72 72 L100 100" stroke="#3D8BFD" stroke-width="10" stroke-linecap="round"/>
       <text x="50" y="58" text-anchor="middle" font-size="22" ${FONT} fill="${INK}">abc</text><path d="M34 36 q6 -6 14 -6" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    example: () => `<rect x="14" y="20" width="92" height="80" rx="8" fill="#FFF3C4" stroke="#E0A100" stroke-width="3"/>
       <text x="32" y="48" font-size="15" ${FONT} fill="#E0A100">e.g.</text><path d="M30 64 h60 M30 80 h44" stroke="#C9934A" stroke-width="4" stroke-linecap="round"/>${star(92, 36, 8, 3.4, '#FF9F1C')}`,
    understand: () => person('child', {shirt: '#FF9F1C'}, 0, 4, .96) + `<circle cx="98" cy="24" r="16" fill="#FFD23F"/><rect x="92" y="38" width="12" height="7" rx="2" fill="#8A8FA3"/>
       <path d="M98 0 v6 M80 8 l4 4 M116 8 l-4 4" stroke="#FFB703" stroke-width="3" stroke-linecap="round"/>${check(98, 24, .8, '#E0A100')}`,
    repeat: () => `<path d="M30 56 a30 26 0 0 1 58 -8" stroke="#2BB3A3" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M92 30 l-2 22 l-20 -8z" fill="#2BB3A3"/>
       <path d="M90 66 a30 26 0 0 1 -58 8" stroke="#FF9F1C" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M28 92 l2 -22 l20 8z" fill="#FF9F1C"/>
       <text x="60" y="68" text-anchor="middle" font-size="20" ${FONT} fill="${INK}">×2</text>`,

    // ---------- ep34 family tree ----------
    brother: () => person('boy', {shirt: '#3D8BFD'}, -16, 14, .86) + person('boy', {shirt: '#2FA36B', skin: SKIN[1]}, 30, 26, .74),
    sister: () => person('girl', {shirt: '#FF6FA5'}, -16, 14, .86) + person('girl', {shirt: '#9B5DE5', skin: SKIN[1], bow: '#FFD23F'}, 30, 26, .74),
    husband: () => figure('man', {shirt: '#2E5AAC'}) + `<circle cx="96" cy="88" r="9" fill="none" stroke="#FFD23F" stroke-width="4"/>`,
    wife: () => figure('woman', {shirt: '#E63946'}) + `<circle cx="96" cy="88" r="9" fill="none" stroke="#FFD23F" stroke-width="4"/><circle cx="96" cy="78" r="3.5" fill="#BDE7FF"/>`,
    couple: () => person('man', {shirt: '#2E5AAC'}, -14, 16, .84) + person('woman', {shirt: '#E63946'}, 32, 16, .84) + heart(60, 18, .8, '#FF4D6D')
       + `<circle cx="52" cy="22" r="7" fill="none" stroke="#FFD23F" stroke-width="3"/><circle cx="68" cy="22" r="7" fill="none" stroke="#FFD23F" stroke-width="3"/>`.replace(/<circle cx="52"[\s\S]*$/, ''),
    twins: () => person('girl', {shirt: '#FFB703', bow: '#E63946'}, -16, 14, .86) + person('girl', {shirt: '#FFB703', bow: '#E63946'}, 32, 14, .86)
       + `<text x="60" y="22" text-anchor="middle" font-size="18" ${FONT} fill="#E63946">×2</text>`,
    ancestor: () => `<rect x="18" y="10" width="84" height="100" rx="6" fill="#8D5A3B"/><rect x="26" y="18" width="68" height="84" rx="3" fill="#F4E4C1"/>`
       + `<g transform="translate(20 24) scale(.68)">${figure('elder', {shirt: '#6B4A36', mustache: true})}</g>`,
    relation: () => `<circle cx="34" cy="50" r="22" fill="#FF7A59"/><circle cx="86" cy="50" r="22" fill="#3D8BFD"/>
       <path d="M52 50 H68" stroke="#8A8FA3" stroke-width="6" stroke-linecap="round"/><path d="M34 76 v14 h52 v-14" stroke="#8A8FA3" stroke-width="4" fill="none" stroke-dasharray="5 4"/>
       <circle cx="34" cy="46" r="7" fill="#fff"/><path d="M24 62 a10 8 0 0 1 20 0z" fill="#fff"/><circle cx="86" cy="46" r="7" fill="#fff"/><path d="M76 62 a10 8 0 0 1 20 0z" fill="#fff"/>`,
    relationship: () => `<path d="M60 112 V64 M60 76 L32 52 M60 70 L88 46" stroke="#8D5A3B" stroke-width="7" stroke-linecap="round"/>
       ${[[60, 26, '#FF9F1C'], [26, 44, '#3D8BFD'], [94, 40, '#FF6FA5']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="16" fill="#fff" stroke="${c}" stroke-width="4"/><circle cx="${x}" cy="${y - 3}" r="5" fill="${c}"/><path d="M${x - 8} ${y + 9} a8 7 0 0 1 16 0z" fill="${c}"/>`).join('')}
       ${heart(60, 90, .6, '#E63946')}`,
    blood: () => `<path d="M60 12 C46 36 30 54 30 76 a30 30 0 0 0 60 0 C90 54 74 36 60 12Z" fill="#E63946"/>
       <path d="M44 76 a16 16 0 0 0 12 16" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".7"/>`,
    although: () => `<path d="M14 60 C30 30 46 30 60 60 C74 90 90 90 106 60" stroke="#8A8FA3" stroke-width="6" fill="none" stroke-linecap="round"/>
       <circle cx="22" cy="30" r="14" fill="#7FC8F8"/>${drops([[16, 50], [28, 54]])}` + sun(98, 30, 12)
       + `<text x="60" y="108" text-anchor="middle" font-size="16" ${FONT} fill="#8A8FA3">虽然…但…</text>`,

    // ---------- ep35 jobs ----------
    job: () => `<rect x="14" y="40" width="92" height="66" rx="10" fill="#8D5A3B"/><path d="M44 40 V28 a6 6 0 0 1 6 -6 h20 a6 6 0 0 1 6 6 V40" stroke="#6B4A36" stroke-width="7" fill="none"/>
       <rect x="14" y="62" width="92" height="8" fill="#6B4A36"/><rect x="52" y="58" width="16" height="16" rx="3" fill="#FFD23F"/>`,
    become: () => person('child', {shirt: '#FFB703'}, -20, 34, .66) + arrowR(42, 70, 70, '#2FA36B') + person('man', {shirt: '#2E5AAC'}, 34, 8, .9)
       + star(100, 18, 8, 3.4, '#FFD23F'),
    artist: () => figure('woman', {shirt: '#9B5DE5'}) + `<path d="M36 34 C36 18 84 18 84 34 C70 26 50 26 36 34Z" fill="#E63946"/><circle cx="60" cy="18" r="4" fill="#E63946"/>
       <ellipse cx="94" cy="94" rx="20" ry="14" fill="#F4D3A8"/>${[[86, 88, '#E63946'], [96, 86, '#3D8BFD'], [104, 94, '#FFD23F'], [92, 100, '#2FA36B']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="3.5" fill="${c}"/>`).join('')}`,
    scientist: () => figure('man', {shirt: '#fff', skin: SKIN[0], hair: '#6B3E26'}) + `<path d="M36 84 v34 M84 84 v34" stroke="#C5CBE0" stroke-width="2"/>
       <g fill="none" stroke="${INK}" stroke-width="2.2"><circle cx="53" cy="42" r="5"/><circle cx="67" cy="42" r="5"/></g>
       <path d="M92 70 h12 M95 70 v14 l-8 18 a4 4 0 0 0 4 6 h22 a4 4 0 0 0 4 -6 l-8 -18 v-14" fill="#fff" stroke="#8A8FA3" stroke-width="2.5"/><path d="M90 100 l6 -12 h12 l6 12z" fill="#2FA36B"/>`,
    cook: () => figure('man', {shirt: '#fff', skin: SKIN[1]}) + `<path d="M42 30 C30 30 30 12 44 14 C46 2 74 2 76 14 C90 12 90 30 78 30 V36 H42Z" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>
       <path d="M44 84 h32" stroke="#E63946" stroke-width="4"/>`,
    engineer: () => figure('man', {shirt: '#FF9F1C', skin: SKIN[1]}) + `<path d="M38 32 C38 14 82 14 82 32Z" fill="#FFD23F"/><rect x="34" y="30" width="52" height="6" rx="3" fill="#E0B400"/>
       <path d="M60 14 v18" stroke="#E0B400" stroke-width="3"/><path d="M90 76 l18 18 m-4 -22 a8 8 0 0 0 -10 10" stroke="#8A8FA3" stroke-width="5" fill="none" stroke-linecap="round"/>`,
    dentist: () => figure('woman', {shirt: '#7FC8F8'}) + `<rect x="48" y="48" width="24" height="12" rx="5" fill="#BDE7FF" stroke="#7FC8F8" stroke-width="1.5"/>`
       + `<g transform="translate(78 64) scale(.32)">${ART.tooth()}</g>`,
    nurse: () => figure('woman', {shirt: '#FF8FAB'}) + `<path d="M44 22 h32 l-4 -12 h-24z" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><path d="M60 11 v8 M56 15 h8" stroke="#E63946" stroke-width="3"/>`,
    doctor: () => figure('man', {shirt: '#fff', skin: SKIN[0]}) + `<path d="M48 82 q-8 18 10 22 q16 0 12 -18" stroke="#2B2D42" stroke-width="3" fill="none"/><circle cx="70" cy="86" r="5" fill="#8A8FA3"/>
       <rect x="80" y="86" width="14" height="14" rx="2" fill="#E63946"/><path d="M87 89 v8 M83 93 h8" stroke="#fff" stroke-width="2.5"/>`,
    pilot: () => figure('man', {shirt: '#2E5AAC', skin: SKIN[1]}) + `<path d="M38 30 C38 14 82 14 82 30Z" fill="#2B2D42"/><rect x="34" y="28" width="52" height="7" rx="3" fill="#1B1D4A"/>
       <path d="M48 22 h24 M52 22 l-6 -4 M68 22 l6 -4" stroke="#FFD23F" stroke-width="2.5" stroke-linecap="round"/><path d="M40 92 h14" stroke="#FFD23F" stroke-width="3"/>`,
    driver: () => figure('man', {shirt: '#2FA36B', skin: SKIN[2]}) + `<circle cx="60" cy="98" r="22" fill="none" stroke="#2B2D42" stroke-width="7"/><circle cx="60" cy="98" r="5" fill="#2B2D42"/>
       <path d="M38 98 h44 M60 98 v22" stroke="#2B2D42" stroke-width="5"/>`,
  });

  const emo = (bg, eyes, mouth, extra = '') => `<circle cx="60" cy="60" r="46" fill="${bg}"/>${eyes}${mouth}${extra}`;
  const dotEyes = (r = 5) => `<circle cx="44" cy="52" r="${r}" fill="${INK}"/><circle cx="76" cy="52" r="${r}" fill="${INK}"/>`;
  const glass = (fill, h, extra = '') => `<path d="M34 24 H86 L80 106 H40Z" fill="#EAF6FF" stroke="#C5CBE0" stroke-width="3"/>
      <path d="M${34 + (1 - h) * 6 + 1} ${24 + (1 - h) * 82} H${86 - (1 - h) * 6 - 1} L80 104 H40Z" fill="${fill}"/>${extra}`;
  const animal = {
    pig: () => `<ellipse cx="60" cy="66" rx="44" ry="38" fill="#FFB3C6"/><path d="M24 40 l6 -22 l16 14z M96 40 l-6 -22 l-16 14z" fill="#FF8FAB"/>
       <ellipse cx="60" cy="78" rx="18" ry="13" fill="#FF8FAB"/><circle cx="53" cy="78" r="3.5" fill="${INK}"/><circle cx="67" cy="78" r="3.5" fill="${INK}"/>${dotEyes(4.5).replace(/cy="52"/g, 'cy="56"')}`,
    sheep: () => `${[[30, 46], [46, 32], [66, 30], [84, 40], [92, 60], [28, 66], [86, 80], [34, 84]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="16" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>`).join('')}
       <ellipse cx="60" cy="66" rx="22" ry="26" fill="#5A4636"/><circle cx="51" cy="62" r="3.5" fill="#fff"/><circle cx="69" cy="62" r="3.5" fill="#fff"/><path d="M54 78 q6 4 12 0" stroke="#fff" stroke-width="2.5" fill="none"/>`,
    horse: () => `<path d="M30 64 h56 a14 14 0 0 1 0 28 h-56 a14 14 0 0 1 0 -28z" fill="#B5703F"/>
       ${[34, 46, 78, 90].map(x => `<rect x="${x - 4}" y="84" width="8" height="28" rx="3" fill="#B5703F"/><rect x="${x - 5}" y="106" width="10" height="6" rx="2" fill="#5A3825"/>`).join('')}
       <path d="M80 70 L96 30 C98 24 106 22 110 28 L116 42 C118 48 112 52 106 48 L100 46 L94 72Z" fill="#B5703F"/>
       <path d="M96 30 C90 34 86 46 84 60 L92 62 C94 50 96 40 100 34Z" fill="#5A3825"/><path d="M98 26 l2 -10 l6 10z" fill="#B5703F"/>
       <circle cx="104" cy="34" r="2.6" fill="${INK}"/><path d="M18 70 C6 76 6 92 14 98 C14 88 16 80 22 74Z" fill="#5A3825"/>`,
    cow: () => `<path d="M24 34 q-12 -8 -12 -20 M96 34 q12 -8 12 -20" stroke="#C9B8A6" stroke-width="7" fill="none" stroke-linecap="round"/>
       <ellipse cx="60" cy="58" rx="38" ry="40" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><path d="M30 34 q14 -4 18 16 q-16 8 -22 -6z" fill="#2B2D42"/><circle cx="84" cy="48" r="9" fill="#2B2D42"/>
       <ellipse cx="60" cy="84" rx="24" ry="16" fill="#FFB3C6"/><circle cx="52" cy="84" r="3.5" fill="${INK}"/><circle cx="68" cy="84" r="3.5" fill="${INK}"/>
       <circle cx="46" cy="56" r="4" fill="${INK}"/><circle cx="74" cy="56" r="4" fill="${INK}"/>`,
    hen: () => `<ellipse cx="58" cy="72" rx="38" ry="32" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><circle cx="84" cy="40" r="20" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>
       <path d="M78 22 q4 -12 10 -4 q6 -8 8 4 q8 0 2 10" fill="#E63946"/><path d="M102 40 l12 4 l-12 4z" fill="#FFB703"/><path d="M96 52 q4 8 -2 10 q-4 -4 2 -10z" fill="#E63946"/>
       <circle cx="88" cy="38" r="3.5" fill="${INK}"/><path d="M30 64 q14 -10 26 4 q-14 14 -26 -4z" fill="#F4F1E8"/>
       <path d="M50 104 v10 M66 104 v10" stroke="#FFB703" stroke-width="4"/>`,
    fox: () => `<path d="M14 18 L40 44 L60 40 L80 44 L106 18 L100 62 C96 88 78 104 60 104 C42 104 24 88 20 62Z" fill="#FF7A3D"/>
       <path d="M30 70 C40 72 50 80 60 104 C70 80 80 72 90 70 C86 92 74 104 60 104 C46 104 34 92 30 70Z" fill="#fff"/>
       <circle cx="44" cy="62" r="4" fill="${INK}"/><circle cx="76" cy="62" r="4" fill="${INK}"/><ellipse cx="60" cy="96" rx="5" ry="4" fill="${INK}"/>
       <path d="M24 26 L36 42 M96 26 L84 42" stroke="#2B2D42" stroke-width="5"/>`,
  };
  Object.assign(ART, animal, {
    // ---------- ep36 week ----------
    week: () => `<rect x="8" y="22" width="104" height="82" rx="10" fill="#fff" stroke="#E3E6F5" stroke-width="3"/><path d="M8 32 a10 10 0 0 1 10 -10 h84 a10 10 0 0 1 10 10 v10 h-104z" fill="#5A67D8"/>
       ${'一二三四五六日'.split('').map((d, i) => `<rect x="${14 + i * 14}" y="54" width="12" height="40" rx="3" fill="${i > 4 ? '#FFB703' : '#BDE7FF'}"/>
         <text x="${20 + i * 14}" y="80" text-anchor="middle" font-size="10" ${FONT} fill="${INK}">${d}</text>`).join('')}`,
    ...Object.fromEntries(['Monday 周一', 'Tuesday 周二', 'Wednesday 周三', 'Thursday 周四', 'Friday 周五', 'Saturday 周六', 'Sunday 周日'].map((x, i) => {
      const [en, zh] = x.split(' ');
      return [en.toLowerCase(), () => calPage(en.slice(0, 3).toUpperCase(), zh, i > 4 ? '#FF9F1C' : ['#E63946', '#FF7A59', '#2FA36B', '#3D8BFD', '#9B5DE5'][i])];
    })),
    weekday: () => `<g transform="translate(20 6) scale(.66)">${ART.job()}</g>` + [0, 1, 2, 3, 4].map(i => `<rect x="${14 + i * 19}" y="88" width="16" height="16" rx="3" fill="#BDE7FF"/>`).join(''),
    weekend: () => `<g transform="translate(0 -4)">${sun(84, 30, 13)}</g><path d="M14 92 C30 60 50 60 66 92Z" fill="#6CCB5F"/><path d="M50 92 C70 50 96 50 112 92Z" fill="#8EDB6E"/>`
       + [0, 1].map(i => `<rect x="${36 + i * 30}" y="98" width="24" height="16" rx="3" fill="#FFB703"/>`).join('') + heart(30, 34, .6, '#FF6FA5'),
    before: () => `<path d="M10 70 H110" stroke="#C5CBE0" stroke-width="5"/><circle cx="76" cy="70" r="12" fill="#E63946"/>
       <circle cx="36" cy="70" r="12" fill="#2FA36B"/><path d="M48 44 H22 m8 -8 l-8 8 l8 8" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <text x="60" y="104" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">在…之前</text>`,
    after: () => `<path d="M10 70 H110" stroke="#C5CBE0" stroke-width="5"/><circle cx="44" cy="70" r="12" fill="#E63946"/>
       <circle cx="84" cy="70" r="12" fill="#3D8BFD"/><path d="M72 44 H98 m-8 -8 l8 8 l-8 8" stroke="#3D8BFD" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <text x="60" y="104" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">在…之后</text>`,
    from: () => `<circle cx="24" cy="60" r="14" fill="#E63946"/><path d="M42 60 H104 m-10 -10 l10 10 l-10 10" stroke="#E63946" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <text x="70" y="44" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">从…</text>`,
    on: () => calPage('ON', '📌'.length > 1 ? 'MON' : '', '#E63946') + `<circle cx="88" cy="88" r="10" fill="none" stroke="#2FA36B" stroke-width="4"/>`,

    // ---------- ep37 farm ----------
    farm: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/><path d="M4 76 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#8EDB6E"/>
       <rect x="22" y="44" width="48" height="40" fill="#E63946"/><path d="M16 46 L46 22 L76 46Z" fill="#9D0208"/><rect x="38" y="60" width="16" height="24" fill="#fff"/>
       <path d="M38 60 L54 84 M54 60 L38 84" stroke="#E63946" stroke-width="2.5"/><rect x="80" y="36" width="20" height="48" rx="10" fill="#C5CBE0"/>` + sun(98, 18, 7),
    field: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/><path d="M4 50 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#E9C46A"/>
       ${[60, 74, 90, 108].map((y, i) => `<path d="M4 ${y} Q60 ${y - 12 + i * 3} 116 ${y}" stroke="#B5893A" stroke-width="3" fill="none"/>`).join('')}
       <path d="M4 50 Q40 40 70 50 T116 46" stroke="#6CCB5F" stroke-width="6" fill="none"/>`,
    grass: () => `<path d="M8 108 H112" stroke="#6CCB5F" stroke-width="6" stroke-linecap="round"/>${[16, 30, 44, 58, 72, 86, 100].map((x, i) =>
         `<path d="M${x - 8} 108 Q${x - 4} ${70 - (i % 3) * 14} ${x + 2} ${46 - (i % 3) * 10} Q${x + 2} ${74 - (i % 3) * 10} ${x + 8} 108Z" fill="${i % 2 ? '#3FA34D' : '#6CCB5F'}"/>`).join('')}`,
    plant: () => `<path d="M38 84 h44 l-6 28 h-32z" fill="#E07A4F"/><rect x="34" y="78" width="52" height="10" rx="4" fill="#C9653D"/>
       <path d="M60 80 V36" stroke="#3FA34D" stroke-width="5" stroke-linecap="round"/><path d="M60 60 C42 60 32 48 30 34 C46 34 58 44 60 60Z" fill="#6CCB5F"/>
       <path d="M60 46 C74 44 86 32 90 18 C74 18 62 30 60 46Z" fill="#8EDB6E"/>`,
    tree: () => tree(60, 74, 1.4, `<circle cx="0" cy="-22" r="30" fill="#6CCB5F"/><circle cx="-18" cy="-8" r="18" fill="#3FA34D"/><circle cx="18" cy="-10" r="20" fill="#8EDB6E"/>`),
    leaf: () => `<path d="M24 98 C20 50 50 18 102 16 C104 70 72 102 24 98Z" fill="#6CCB5F"/><path d="M24 98 C50 74 74 46 96 22" stroke="#3FA34D" stroke-width="4" fill="none"/>
       ${[[44, 76, 36, 56], [58, 60, 54, 38], [70, 46, 72, 28], [46, 74, 64, 82], [62, 58, 80, 64]].map(([a, b, c, d]) => `<path d="M${a} ${b} L${c} ${d}" stroke="#3FA34D" stroke-width="2.5"/>`).join('')}`,
    lay: () => `<g transform="translate(-2 -12) scale(.82)">${animal.hen()}</g><ellipse cx="40" cy="100" rx="12" ry="15" fill="#FFF3C4" stroke="#E9C46A" stroke-width="2"/>
       <path d="M14 112 h70" stroke="#E9C46A" stroke-width="5" stroke-linecap="round"/>${star(18, 86, 6, 2.5, '#FFD23F')}`,
    egg: () => `<ellipse cx="60" cy="62" rx="34" ry="44" fill="#FFF3C4" stroke="#E9C46A" stroke-width="3"/><ellipse cx="48" cy="44" rx="8" ry="12" fill="#fff" opacity=".8"/>`,
    eat2: () => '',

    // ---------- ep38 rooms ----------
    room: () => `<path d="M10 30 L60 10 L110 30 V106 H10Z" fill="#FFE8C2"/><path d="M10 106 L30 86 H90 L110 106Z" fill="#E9A66B"/><path d="M30 86 V40 H90 V86" fill="#FFF3DD" stroke="#E9C8A0" stroke-width="2"/>
       <rect x="40" y="62" width="40" height="18" rx="4" fill="#3D8BFD"/><rect x="40" y="54" width="10" height="12" rx="3" fill="#3D8BFD"/><rect x="70" y="54" width="10" height="12" rx="3" fill="#3D8BFD"/>
       <rect x="52" y="44" width="16" height="12" fill="#BDE7FF" stroke="#8D5A3B" stroke-width="2"/>`,
    bedroom: () => `<rect x="10" y="60" width="100" height="30" rx="6" fill="#3D8BFD"/><rect x="10" y="40" width="14" height="66" rx="4" fill="#8D5A3B"/><rect x="96" y="54" width="14" height="52" rx="4" fill="#8D5A3B"/>
       <rect x="26" y="48" width="30" height="16" rx="8" fill="#fff"/><path d="M50 60 h46 v30 h-46z" fill="#7FB5FF"/>` + `<text x="96" y="30" font-size="16" ${FONT} fill="#8A8FA3">z</text><text x="106" y="20" font-size="12" ${FONT} fill="#8A8FA3">z</text>`,
    bathroom: () => `<path d="M14 62 H106 V74 Q106 98 82 98 H38 Q14 98 14 74Z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><path d="M30 98 l-4 12 M90 98 l4 12" stroke="#C5CBE0" stroke-width="5" stroke-linecap="round"/>
       <path d="M96 62 V24 a10 10 0 0 0 -20 0" stroke="#8A8FA3" stroke-width="5" fill="none"/>${drops([[70, 34], [62, 44], [78, 46]], '#7FC8F8')}
       ${[[30, 56], [44, 50], [56, 56]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="7" fill="#EAF6FF" stroke="#BDE7FF" stroke-width="2"/>`).join('')}`,
    toilet: () => `<rect x="30" y="12" width="60" height="30" rx="6" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><path d="M22 52 H98 Q98 80 70 84 L74 108 H46 L50 84 Q22 80 22 52Z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <ellipse cx="60" cy="52" rx="38" ry="8" fill="#EAF6FF" stroke="#C5CBE0" stroke-width="3"/><rect x="72" y="20" width="12" height="5" rx="2" fill="#8A8FA3"/>`,
    washroom: () => `<rect x="34" y="12" width="52" height="40" rx="20" fill="#BDE7FF" stroke="#8A8FA3" stroke-width="3"/><path d="M20 66 H100 Q100 92 60 92 Q20 92 20 66Z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <rect x="52" y="92" width="16" height="20" fill="#E3E6F5"/><path d="M60 66 V56 h10" stroke="#8A8FA3" stroke-width="4" fill="none"/>${drops([[68, 62]], '#7FC8F8')}`,
    restroom: () => `<rect x="10" y="14" width="100" height="92" rx="12" fill="#2B2D42"/><path d="M60 24 V96" stroke="#fff" stroke-width="3"/>
       <circle cx="35" cy="36" r="8" fill="#7FC8F8"/><path d="M25 50 h20 v24 h-4 v18 h-12 v-18 h-4z" fill="#7FC8F8"/>
       <circle cx="85" cy="36" r="8" fill="#FF8FAB"/><path d="M85 48 L99 76 H71Z M79 76 v16 M91 76 v16" fill="#FF8FAB" stroke="#FF8FAB" stroke-width="5"/>`,
    kitchen: () => `<rect x="8" y="58" width="104" height="52" rx="4" fill="#E9A66B"/><rect x="8" y="52" width="104" height="10" rx="3" fill="#C9C1B5"/>
       <rect x="14" y="68" width="40" height="34" rx="3" fill="#2B2D42"/><rect x="18" y="72" width="32" height="20" rx="2" fill="#6B7085"/>
       <rect x="62" y="68" width="22" height="36" rx="2" fill="#D99058"/><rect x="88" y="68" width="18" height="36" rx="2" fill="#D99058"/>
       <path d="M30 52 v-6 h12 v6" fill="#8A8FA3"/><rect x="62" y="16" width="44" height="22" rx="4" fill="#C5CBE0"/><path d="M76 38 h16 l4 10 h-24z" fill="#8A8FA3"/>` + steam(30, 40),
    livingroom: () => `<rect x="8" y="60" width="104" height="38" rx="12" fill="#2BB3A3"/><rect x="18" y="48" width="84" height="26" rx="10" fill="#45C9B8"/>
       <rect x="8" y="58" width="16" height="40" rx="8" fill="#1E8C7F"/><rect x="96" y="58" width="16" height="40" rx="8" fill="#1E8C7F"/><path d="M20 98 v12 M100 98 v12" stroke="#8D5A3B" stroke-width="5"/>
       <rect x="40" y="14" width="40" height="26" rx="3" fill="#2B2D42"/><rect x="44" y="18" width="32" height="18" fill="#7FC8F8"/>`,
    ceiling: () => `<path d="M4 8 H116 L96 40 H24Z" fill="#F4F1E8" stroke="#C5CBE0" stroke-width="3"/><path d="M60 40 V54" stroke="#8A8FA3" stroke-width="3"/>
       <path d="M40 72 a20 18 0 0 1 40 0z" fill="#FFD23F"/><path d="M42 72 h36" stroke="#E0B400" stroke-width="3"/><path d="M60 54 L60 54" /><circle cx="60" cy="56" r="4" fill="#8A8FA3"/>
       <path d="M36 84 l-8 16 M60 86 v18 M84 84 l8 16" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/>`,
    toothbrush: () => `<g transform="rotate(-35 60 60)"><rect x="54" y="40" width="12" height="74" rx="6" fill="#3D8BFD"/><rect x="52" y="8" width="16" height="36" rx="5" fill="#fff" stroke="#C5CBE0" stroke-width="2"/>
       ${[12, 18, 24, 30, 36].map(y => `<path d="M46 ${y} h8" stroke="#7FC8F8" stroke-width="3"/>`).join('')}</g>`
       + `<path d="M22 22 q8 -10 16 0 q8 -10 16 0 v6 h-32z" fill="#fff" stroke="#BDE7FF" stroke-width="2"/>`,
    soap: () => `<ellipse cx="60" cy="80" rx="44" ry="22" fill="#FF8FAB"/><ellipse cx="60" cy="70" rx="44" ry="22" fill="#FFB3C6"/>
       ${[[30, 34, 10], [52, 22, 8], [74, 30, 12], [94, 18, 7]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#EAF6FF" stroke="#BDE7FF" stroke-width="2"/>`).join('')}`,
    towel: () => `<path d="M24 20 H96" stroke="#8D5A3B" stroke-width="6" stroke-linecap="round"/><rect x="30" y="20" width="60" height="88" rx="4" fill="#2BB3A3"/>
       <rect x="30" y="86" width="60" height="8" fill="#fff" opacity=".7"/><rect x="30" y="20" width="60" height="14" fill="#1E8C7F"/>`,

    // ---------- ep39 feelings ----------
    feeling: () => `${[[30, 34, '#FFD23F'], [90, 34, '#7FC8F8'], [30, 88, '#FF8FAB'], [90, 88, '#B9E28C']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="24" fill="${c}"/>`).join('')}
       <path d="M22 38 q8 8 16 0 M82 42 q8 -8 16 0 M22 92 q8 -6 16 0 M84 92 h12" stroke="${INK}" stroke-width="3" fill="none" stroke-linecap="round"/>${heart(60, 62, .8, '#E63946')}`,
    like: () => emo('#FFD23F', heart(44, 52, .5, '#E63946') + heart(76, 52, .5, '#E63946'), `<path d="M40 76 q20 18 40 0" stroke="${INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>`),
    smile: () => emo('#FFD23F', `<path d="M36 54 q8 -8 16 0 M68 54 q8 -8 16 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
       `<path d="M38 72 q22 22 44 0" stroke="${INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>`, `<ellipse cx="32" cy="70" rx="7" ry="4" fill="${BLUSH}"/><ellipse cx="88" cy="70" rx="7" ry="4" fill="${BLUSH}"/>`),
    happy: () => emo('#FFD23F', dotEyes(5.5), `<path d="M36 70 h48 q-4 24 -24 24 q-20 0 -24 -24z" fill="#9D0208"/><path d="M44 84 q16 10 32 0" fill="#FF6FA5"/>`),
    surprised: () => emo('#FFD23F', `<circle cx="44" cy="50" r="8" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="76" cy="50" r="8" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="44" cy="50" r="3" fill="${INK}"/><circle cx="76" cy="50" r="3" fill="${INK}"/>`,
       `<ellipse cx="60" cy="84" rx="9" ry="12" fill="#9D0208"/>`, `<path d="M36 34 q8 -6 16 0 M68 34 q8 -6 16 0" stroke="${INK}" stroke-width="3" fill="none"/>`),
    sudden: () => bolt(60, 60, 3) + `<text x="98" y="30" font-size="28" ${FONT} fill="#E63946">!</text>`,
    excited: () => emo('#FF9F1C', star(44, 52, 9, 4, '#fff') + star(76, 52, 9, 4, '#fff'), `<path d="M38 70 h44 q-4 26 -22 26 q-18 0 -22 -26z" fill="#9D0208"/>`,
       `<path d="M8 30 l10 8 M112 30 l-10 8 M10 70 h12 M98 70 h12" stroke="#FFB703" stroke-width="4" stroke-linecap="round"/>`),
    mad: () => emo('#E63946', `<path d="M34 42 l18 8 M86 42 l-18 8" stroke="${INK}" stroke-width="5" stroke-linecap="round"/>` + dotEyes(5).replace(/cy="52"/g, 'cy="58"'),
       `<path d="M42 88 q18 -14 36 0" stroke="${INK}" stroke-width="5" fill="none" stroke-linecap="round"/>`, `<path d="M94 14 l-6 10 l10 -2 l-6 10" stroke="#9D0208" stroke-width="4" fill="none"/>`),
    sad: () => emo('#7FC8F8', `<path d="M36 50 q8 4 16 -2 M68 48 q8 6 16 2" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>` + dotEyes(4).replace(/cy="52"/g, 'cy="58"'),
       `<path d="M42 88 q18 -12 36 0" stroke="${INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>`),
    cry: () => emo('#7FC8F8', `<path d="M34 54 q10 -8 18 0 M68 54 q10 -8 18 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
       `<path d="M40 84 q20 -16 40 0 q-20 10 -40 0z" fill="#9D0208"/>`, `<path d="M38 60 v34 M82 60 v34" stroke="#3D8BFD" stroke-width="7" stroke-linecap="round" opacity=".8"/>`),
    tears: () => drops([[40, 30], [60, 50], [80, 34]], '#3D8BFD').replace(/scale/g, 'scale') + `<path d="M28 74 q-10 16 0 26 q10 -10 0 -26z M60 86 q-10 16 0 26 q10 -10 0 -26z M92 74 q-10 16 0 26 q10 -10 0 -26z" fill="#7FC8F8"/>`,
    afraid: () => emo('#E3E6F5', dotEyes(6), `<path d="M44 86 q4 -6 8 0 t8 0 t8 0 t8 0" stroke="${INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>`,
       `<path d="M14 40 l6 6 M106 40 l-6 6 M10 60 h8 M102 60 h8" stroke="#8A8FA3" stroke-width="3.5" stroke-linecap="round"/><path d="M90 28 q6 10 0 14 q-6 -4 0 -14z" fill="#7FC8F8"/>`),
    scared: () => emo('#B9E28C', `<circle cx="44" cy="50" r="9" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="76" cy="50" r="9" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="44" cy="52" r="3" fill="${INK}"/><circle cx="76" cy="52" r="3" fill="${INK}"/>`,
       `<path d="M38 74 h44 v14 a8 8 0 0 1 -8 8 h-28 a8 8 0 0 1 -8 -8z" fill="#9D0208"/><path d="M38 74 h44 v6 h-44z" fill="#fff"/>`),
    fear: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#2B2D42"/><path d="M60 16 C34 16 26 40 26 60 V104 l10 -8 l8 8 l8 -8 l8 8 l8 -8 l8 8 l8 -8 l10 8 V60 C94 40 86 16 60 16Z" fill="#fff"/>
       <ellipse cx="48" cy="54" rx="6" ry="9" fill="#2B2D42"/><ellipse cx="72" cy="54" rx="6" ry="9" fill="#2B2D42"/><ellipse cx="60" cy="78" rx="7" ry="9" fill="#2B2D42"/>`,

    // ---------- ep40 drinks ----------
    drink: () => glass('#FF9F1C', .7, `<path d="M70 4 L62 60" stroke="#E63946" stroke-width="5" stroke-linecap="round"/><circle cx="76" cy="40" r="10" fill="#FFD23F" stroke="#E0B400" stroke-width="2"/>`),
    thirsty: () => figure('boy', {shirt: '#FF9F1C'}) + `<path d="M52 66 q8 -6 16 0" stroke="${INK}" stroke-width="0"/>` + `<ellipse cx="60" cy="62" rx="5" ry="7" fill="#9D0208"/>`
       + sun(100, 20, 10) + `<path d="M24 40 q-6 8 0 12 q6 -4 0 -12z" fill="#7FC8F8"/>`,
    water: () => glass('#7FC8F8', .75, `<path d="M42 50 q6 4 12 0" stroke="#fff" stroke-width="3" fill="none" opacity=".7"/>`),
    milk: () => `<path d="M30 40 L44 18 H76 L90 40 V110 H30Z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/><path d="M44 18 L60 8 L76 18" fill="#E3E6F5" stroke="#C5CBE0" stroke-width="3"/>
       <rect x="30" y="56" width="60" height="34" fill="#3D8BFD"/><text x="60" y="80" text-anchor="middle" font-size="17" ${FONT} fill="#fff">MILK</text>`,
    juice: () => glass('#FF9F1C', .8, `<circle cx="80" cy="26" r="14" fill="#FFB703"/><circle cx="80" cy="26" r="9" fill="#FFD23F"/><path d="M80 17 v18 M71 26 h18" stroke="#FFB703" stroke-width="1.5"/>
       <path d="M56 4 L62 60" stroke="#2FA36B" stroke-width="5" stroke-linecap="round"/>`),
    coffee: () => `<path d="M20 50 H88 V84 a24 24 0 0 1 -24 24 H44 a24 24 0 0 1 -24 -24Z" fill="#fff" stroke="#C5CBE0" stroke-width="3"/>
       <path d="M88 60 h8 a12 12 0 0 1 0 24 h-10" stroke="#C5CBE0" stroke-width="5" fill="none"/><ellipse cx="54" cy="52" rx="32" ry="6" fill="#6B4A36"/>
       <path d="M40 40 q-6 -8 0 -14 t0 -14 M58 38 q-6 -8 0 -14 t0 -14" stroke="#C5CBE0" stroke-width="3.5" fill="none" stroke-linecap="round"/>`,
    cup: () => `<path d="M20 44 H88 V80 a24 24 0 0 1 -24 24 H44 a24 24 0 0 1 -24 -24Z" fill="#FF6FA5"/>
       <path d="M88 54 h8 a12 12 0 0 1 0 24 h-10" stroke="#FF6FA5" stroke-width="6" fill="none"/>${heart(54, 72, .7, '#fff')}<ellipse cx="54" cy="110" rx="40" ry="5" fill="#E3E6F5"/>`,
    soup: () => bowl('#fff', '#FF9F1C') + `<ellipse cx="60" cy="58" rx="44" ry="10" fill="#FFB703"/>${[[40, 56, '#2FA36B'], [62, 60, '#E63946'], [80, 55, '#2FA36B']].map(([x, y, c]) => `<circle cx="${x}" cy="${y}" r="4" fill="${c}"/>`).join('')}` + steam(48, 40),
    beer: () => `<path d="M26 36 H82 V104 a6 6 0 0 1 -6 6 H32 a6 6 0 0 1 -6 -6Z" fill="#FFB703" opacity=".9"/><path d="M82 50 h10 a10 10 0 0 1 10 10 v20 a10 10 0 0 1 -10 10 h-10" stroke="#C5CBE0" stroke-width="6" fill="none"/>
       <path d="M22 36 q4 -16 18 -10 q8 -12 20 -4 q10 -10 22 0 q8 0 6 14z" fill="#fff"/><path d="M40 60 v36 M54 60 v36 M68 60 v36" stroke="#fff" stroke-width="3" opacity=".5"/>
       <text x="98" y="22" text-anchor="middle" font-size="13" ${FONT} fill="#E63946">18+</text>`,
    enough: () => glass('#7FC8F8', 1, '') + check(98, 30, 1.2) + `<path d="M24 24 h72" stroke="#2FA36B" stroke-width="3" stroke-dasharray="5 4"/>`,
    satisfy: () => emo('#FFD23F', `<path d="M36 52 q8 -8 16 0 M68 52 q8 -8 16 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
       `<path d="M40 72 q20 16 40 0" stroke="${INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>`, hand(96, 100, .55, -10, SKIN[0]) + `<circle cx="96" cy="86" r="6" fill="none" stroke="${INK}" stroke-width="0"/>`),
  });
  delete ART.eat2;

  const building = (x, y, w, h, c, roof, sign = '', sc = '#fff') => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${c}"/>
      <rect x="${x - 4}" y="${y - 10}" width="${w + 8}" height="12" rx="3" fill="${roof}"/>
      ${sign ? `<text x="${x + w / 2}" y="${y - 1}" text-anchor="middle" font-size="9" ${FONT} fill="${sc}">${sign}</text>` : ''}
      <rect x="${x + w / 2 - 7}" y="${y + h - 22}" width="14" height="22" fill="#8D5A3B"/>
      ${[0, 1].map(i => `<rect x="${x + 5 + i * (w - 21)}" y="${y + 8}" width="11" height="11" rx="1.5" fill="#BDE7FF"/>`).join('')}`;
  const broom = (x, y, k = 1, r = 20) => `<g transform="translate(${x} ${y}) rotate(${r}) scale(${k})"><rect x="-3" y="-50" width="6" height="56" rx="3" fill="#B5703F"/>
      <path d="M-16 6 h32 l6 26 h-44z" fill="#FFB703"/>${[-12, -4, 4, 12].map(d => `<path d="M${d} 10 l${d / 3} 20" stroke="#E0A100" stroke-width="2"/>`).join('')}</g>`;
  const bellA = (x, y, k = 1, c = '#FFB703') => `<g transform="translate(${x} ${y}) scale(${k})"><path d="M-22 18 C-22 -14 -14 -26 0 -26 C14 -26 22 -14 22 18 l6 6 h-56z" fill="${c}"/>
      <circle cy="30" r="6" fill="#C9934A"/><rect x="-4" y="-34" width="8" height="10" rx="3" fill="#C9934A"/></g>`;
  const catA = (x, y, k, c = '#FF9F1C') => `<g transform="translate(${x} ${y}) scale(${k})"><ellipse cx="0" cy="30" rx="22" ry="20" fill="${c}"/>
      <path d="M-22 -10 L-18 -34 L-4 -20 Z M22 -10 L18 -34 L4 -20Z" fill="${c}"/><circle cx="0" cy="-4" r="22" fill="${c}"/>
      <circle cx="-8" cy="-6" r="3" fill="${INK}"/><circle cx="8" cy="-6" r="3" fill="${INK}"/><path d="M-3 2 h6 l-3 3z" fill="#FF6F91"/>
      <path d="M-24 0 h12 M-24 6 h12 M24 0 h-12 M24 6 h-12" stroke="${INK}" stroke-width="1.4"/><path d="M20 40 q18 -4 14 -24" stroke="${c}" stroke-width="6" fill="none" stroke-linecap="round"/></g>`;
  const birdA = (x, y, k, c = '#3D8BFD') => `<g transform="translate(${x} ${y}) scale(${k})"><ellipse cx="0" cy="0" rx="26" ry="20" fill="${c}"/><circle cx="20" cy="-14" r="14" fill="${c}"/>
      <path d="M32 -16 l12 4 l-12 4z" fill="#FFB703"/><circle cx="23" cy="-17" r="2.6" fill="${INK}"/><path d="M-8 -6 C-4 -26 14 -22 10 -2Z" fill="#fff" opacity=".45"/>
      <path d="M-24 2 L-42 -6 L-36 10Z" fill="${c}"/><path d="M-4 18 v10 M6 18 v10" stroke="#FFB703" stroke-width="3"/></g>`;
  Object.assign(ART, {
    // ---------- ep41 chores ----------
    chore: () => `<path d="M24 60 h58 l-8 48 h-42z" fill="#7FC8F8"/><path d="M24 60 Q53 50 82 60" fill="#BDE7FF"/><path d="M28 60 q4 -24 25 -24 q21 0 25 24" stroke="#8A8FA3" stroke-width="4" fill="none"/>`
       + broom(92, 66, .9, 20) + `<circle cx="40" cy="54" r="6" fill="#fff" opacity=".8"/><circle cx="52" cy="50" r="4" fill="#fff" opacity=".8"/>`,
    rubbish: () => `<path d="M28 44 h64 l-6 66 h-52z" fill="#8A8FA3"/>${[40, 52, 64, 76].map(x => `<path d="M${x} 52 v50" stroke="#6B7085" stroke-width="3"/>`).join('')}
       <path d="M40 44 l6 -18 l12 8 l8 -16 l10 14 l6 -6 l4 18z" fill="#C9934A"/><path d="M60 30 l10 -6 l4 8z" fill="#E63946"/><circle cx="48" cy="28" r="5" fill="#2FA36B"/>`,
    bin: () => `<path d="M30 40 h60 l-6 70 h-48z" fill="#2FA36B"/><rect x="24" y="30" width="72" height="12" rx="4" fill="#1E7A4E"/><rect x="50" y="22" width="20" height="10" rx="3" fill="#1E7A4E"/>
       <path d="M52 64 l8 -12 l8 12 M48 80 h24 l-4 -8 M60 52 l-14 24" stroke="#fff" stroke-width="3.5" fill="none" stroke-linejoin="round"/>`,
    basket: () => `<path d="M30 52 Q60 10 90 52" stroke="#B5703F" stroke-width="7" fill="none"/><path d="M14 52 h92 l-10 54 h-72z" fill="#E9A66B"/>
       ${[0, 1, 2].map(i => `<path d="M${18 + i * 2} ${64 + i * 14} H${102 - i * 2}" stroke="#B5703F" stroke-width="3"/>`).join('')}${[32, 46, 60, 74, 88].map(x => `<path d="M${x} 54 V104" stroke="#C9934A" stroke-width="2.5"/>`).join('')}`,
    brush: () => `<g transform="rotate(-30 60 60)"><rect x="54" y="4" width="12" height="54" rx="5" fill="#B5703F"/><rect x="44" y="56" width="32" height="14" rx="3" fill="#8A8FA3"/>
       <path d="M44 70 h32 v26 q-16 8 -32 0z" fill="#2B2D42"/>${[48, 54, 60, 66, 72].map(x => `<path d="M${x} 74 v18" stroke="#6B7085" stroke-width="2"/>`).join('')}</g>`,
    tidy: () => `<rect x="14" y="16" width="92" height="94" rx="6" fill="#E9A66B"/><rect x="20" y="22" width="80" height="40" fill="#FFF3DD"/><rect x="20" y="66" width="80" height="38" fill="#FFF3DD"/>
       ${[[26, '#E63946'], [36, '#3D8BFD'], [46, '#2FA36B'], [56, '#FFB703']].map(([x, c]) => `<rect x="${x}" y="30" width="8" height="32" fill="${c}"/>`).join('')}
       <rect x="70" y="40" width="22" height="22" rx="3" fill="#9B5DE5"/><rect x="28" y="84" width="60" height="20" rx="3" fill="#7FC8F8"/>${star(96, 14, 8, 3.4, '#FFD23F')}`,
    mess: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#FFF3DD"/><path d="M22 84 l20 -8 l6 18 l-20 8z" fill="#E63946"/><path d="M60 92 C70 80 86 84 90 96" stroke="#3D8BFD" stroke-width="8" fill="none" stroke-linecap="round"/>
       <rect x="66" y="28" width="26" height="20" rx="3" fill="#2FA36B" transform="rotate(25 79 38)"/><circle cx="34" cy="40" r="10" fill="#FFB703"/>
       <path d="M44 56 l14 4 l-4 12z" fill="#9B5DE5"/>${[[96, 70], [20, 64], [78, 62]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#8A8FA3"/>`).join('')}`,
    dirty: () => tee('#fff') + `<path d="M40 18 Q60 30 80 18" stroke="#C5CBE0" stroke-width="3" fill="none"/>${[[44, 56, 9], [70, 74, 12], [52, 90, 7], [80, 46, 6]].map(([x, y, r]) =>
         `<path d="M${x - r} ${y} q${r / 2} -${r} ${r} -${r / 2} q${r} -${r / 2} ${r} ${r / 2} q${r / 2} ${r} -${r / 2} ${r} q-${r} ${r / 2} -${r * 1.5} -${r}z" fill="#8D5A3B" opacity=".8"/>`).join('')}`,
    wash: () => `<path d="M14 62 H106 Q102 104 60 104 Q18 104 14 62Z" fill="#7FC8F8"/><ellipse cx="60" cy="62" rx="46" ry="10" fill="#BDE7FF"/>`
       + hand(40, 58, .9, -30, SKIN[0]) + `<g transform="translate(120 0) scale(-1 1)">${hand(40, 58, .9, -30, SKIN[0])}</g>`
       + [[30, 34, 8], [50, 22, 6], [74, 28, 9], [92, 40, 6]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#EAF6FF" stroke="#BDE7FF" stroke-width="2"/>`).join(''),
    clean: () => tee('#7FC8F8') + star(42, 50, 10, 4, '#fff') + star(80, 76, 8, 3.4, '#fff') + star(98, 22, 7, 3, '#FFD23F') + star(20, 30, 6, 2.5, '#FFD23F'),
    sweep: () => broom(60, 58, 1.1, 30) + `<path d="M8 108 H112" stroke="#C5CBE0" stroke-width="5" stroke-linecap="round"/>
       ${[[14, 100], [22, 96], [30, 102], [18, 92]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#8D5A3B"/>`).join('')}<path d="M40 92 q-10 -4 -16 -2" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-dasharray="3 4"/>`,
    floor: () => `<path d="M4 50 L60 30 L116 50 L60 74Z" fill="#E9A66B"/><path d="M4 50 L60 74 V110 L4 86Z" fill="#C9934A"/><path d="M116 50 L60 74 V110 L116 86Z" fill="#B5703F"/>
       ${[0, 1, 2, 3].map(i => `<path d="M${18 + i * 14} ${45 - i * 5} L${74 + i * 14 - 56} ${60 + i * 5}" stroke="#C9934A" stroke-width="2"/>`).join('')}
       ${[0, 1, 2].map(i => `<path d="M${18 + i * 18} ${56 + i * 7} L${74 + i * 18} ${36 + i * 7}" stroke="#C9934A" stroke-width="2"/>`).join('')}`,

    // ---------- ep42 school rules ----------
    each: () => [0, 1, 2, 3].map(i => `<g transform="translate(${8 + i * 26} 40)">${`<circle cx="12" cy="10" r="9" fill="${SKIN[i % 3]}"/><path d="M0 40 a12 14 0 0 1 24 0z" fill="${['#E63946', '#3D8BFD', '#2FA36B', '#FFB703'][i]}"/>`}
         ${star(12, -10, 6, 2.5, '#FFD23F')}</g>`).join('') + `<text x="60" y="104" text-anchor="middle" font-size="15" ${FONT} fill="#8A8FA3">每一个</text>`,
    pupil: () => figure('child', {shirt: '#3D8BFD'}) + `<path d="M36 84 v30 M84 84 v30" stroke="#FF7A59" stroke-width="7" stroke-linecap="round"/>${star(98, 24, 8, 3.4, '#FFD23F')}`,
    headmaster: () => figure('elder', {shirt: '#2E5AAC', mustache: true}) + `<rect x="68" y="88" width="20" height="12" rx="3" fill="#FFD23F"/><path d="M78 88 v12" stroke="#E0A100" stroke-width="2"/>`
       + `<path d="M30 6 h60 l-30 -6z" fill="#2B2D42"/>`.replace(/<path d="M30 6[^>]*>/, ''),
    educate: () => board(40, 18, 76, 52, '#2F6B4F', `<text x="78" y="50" text-anchor="middle" font-size="18" ${FONT} fill="#fff">abc</text>`)
       + person('woman', {shirt: '#E63946'}, -22, 26, .8) + person('child', {shirt: '#3D8BFD'}, 52, 54, .55),
    follow: () => [[22, '#E63946'], [52, '#3D8BFD'], [82, '#2FA36B']].map(([x, c], i) => kid({s: .55, dx: x - 60, dy: 20, la: [-20, -10], ra: [20, 10], ll: [20, 8], rl: [-20, -30], shirt: c})).join('')
       + `<path d="M8 22 H112 m-10 -8 l10 8 l-10 8" stroke="#FFB703" stroke-width="4" fill="none" stroke-linecap="round" stroke-dasharray="1 0"/>`,
    rule: () => `<rect x="20" y="10" width="80" height="100" rx="8" fill="#fff" stroke="#5A67D8" stroke-width="4"/><rect x="20" y="10" width="80" height="22" rx="8" fill="#5A67D8"/>
       <text x="60" y="27" text-anchor="middle" font-size="13" ${FONT} fill="#fff">RULES</text>
       ${[46, 64, 82, 100].map((y, i) => `<text x="32" y="${y}" font-size="12" ${FONT} fill="#5A67D8">${i + 1}.</text><path d="M46 ${y - 4} h42" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>`).join('')}`,
    attention: () => `<path d="M60 10 L112 104 H8Z" fill="#FFD23F" stroke="#E0A100" stroke-width="5" stroke-linejoin="round"/><rect x="54" y="40" width="12" height="38" rx="5" fill="${INK}"/><circle cx="60" cy="90" r="7" fill="${INK}"/>`,
    late: () => clockF(60, 58, 42, 8, 20, {rim: '#E63946'}) + kid({s: .4, dx: 24, dy: 54, rot: 10, la: [-60, 30], ra: [55, 140], ll: [-40, -95], rl: [62, -4], shirt: '#3D8BFD'})
       + `<text x="24" y="26" font-size="26" ${FONT} fill="#E63946">!</text>`,
    alarm: () => ART.clock() + `<path d="M8 50 l-6 -4 M10 66 h-8 M112 50 l6 -4 M110 66 h8" stroke="#FFB703" stroke-width="4" stroke-linecap="round"/>`,
    bell: () => bellA(60, 60, 1.6) + `<path d="M14 40 q-8 14 0 28 M106 40 q8 14 0 28" stroke="#FFB703" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    fight: () => kid({s: .8, dx: -24, dy: 10, la: [-40, -20], ra: [100, 90], ll: [-14, -4], rl: [18, 6], shirt: '#E63946'})
       + kid({s: .8, dx: 24, dy: 10, la: [-100, -90], ra: [40, 20], ll: [-18, -6], rl: [14, 4], shirt: '#3D8BFD', skin: SKIN[1]})
       + star(60, 30, 14, 6, '#FFD23F') + `<path d="M60 8 v-6 M46 14 l-6 -6 M74 14 l6 -6" stroke="#FFB703" stroke-width="3" stroke-linecap="round"/>`,
    attend: () => `<rect x="18" y="10" width="84" height="100" rx="8" fill="#fff" stroke="#2FA36B" stroke-width="4"/>
       ${[0, 1, 2, 3].map(i => `<circle cx="34" cy="${32 + i * 22}" r="6" fill="${SKIN[i % 3]}"/><path d="M46 ${32 + i * 22} h30" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>${check(88, 32 + i * 22, .55)}`).join('')}`,
    absent: () => `<rect x="18" y="10" width="84" height="100" rx="8" fill="#fff" stroke="#E63946" stroke-width="4"/>
       <path d="M40 40 h40 v50 h-40z" fill="none" stroke="#C5CBE0" stroke-width="4" stroke-dasharray="6 5"/><text x="60" y="76" text-anchor="middle" font-size="28" ${FONT} fill="#C5CBE0">?</text>
       <path d="M74 22 l16 16 M90 22 l-16 16" stroke="#E63946" stroke-width="4" stroke-linecap="round"/>`,
    punish: () => kid({la: [-170, -175], ra: [170, 175], shirt: '#8A8FA3'}) + `<rect x="36" y="-2" width="48" height="14" rx="3" fill="#E9A66B"/>`
       + `<path d="M98 50 q6 10 0 14 q-6 -4 0 -14z" fill="#7FC8F8"/>`,

    // ---------- ep43 town ----------
    town: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/>` + building(14, 50, 28, 60, '#FF9F1C', '#E63946') + building(46, 30, 30, 80, '#5A67D8', '#2B2D42')
       + building(80, 58, 28, 52, '#2FA36B', '#1E7A4E') + `<rect x="4" y="104" width="112" height="12" fill="#8A8FA3"/>`,
    village: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/><path d="M4 70 Q60 50 116 70 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#8EDB6E"/>`
       + [[30, 66], [74, 60]].map(([x, y]) => `<rect x="${x - 14}" y="${y}" width="28" height="22" fill="#FFE8C2"/><path d="M${x - 18} ${y + 2} L${x} ${y - 16} L${x + 18} ${y + 2}Z" fill="#C1440E"/><rect x="${x - 4}" y="${y + 10}" width="8" height="12" fill="#8D5A3B"/>`).join('')
       + tree(100, 70, .6, `<circle cx="0" cy="-14" r="16" fill="#3FA34D"/>`),
    square: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/><ellipse cx="60" cy="88" rx="54" ry="22" fill="#E3E6F5"/>
       <ellipse cx="60" cy="84" rx="26" ry="9" fill="#7FC8F8" stroke="#C5CBE0" stroke-width="3"/><path d="M60 82 V58" stroke="#7FC8F8" stroke-width="4"/>
       <path d="M60 58 q-12 6 -14 20 M60 58 q12 6 14 20" stroke="#7FC8F8" stroke-width="3" fill="none"/>${[[24, 76], [96, 76]].map(([x, y]) => `<circle cx="${x}" cy="${y - 10}" r="5" fill="${SKIN[0]}"/><path d="M${x - 6} ${y + 6} a6 8 0 0 1 12 0z" fill="#FF9F1C"/>`).join('')}`,
    cinema: () => `<rect x="10" y="20" width="100" height="62" rx="4" fill="#2B2D42"/><rect x="16" y="26" width="88" height="50" fill="#5A67D8"/>`
       + star(60, 50, 14, 6, '#FFD23F') + [20, 44, 68, 92].map(x => `<path d="M${x} 108 v-12 a8 8 0 0 1 16 0 v12z" fill="#E63946"/>`).join(''),
    show: () => `<path d="M4 8 Q30 30 30 96 H4Z M116 8 Q90 30 90 96 H116Z" fill="#E63946"/><path d="M4 96 H116 V112 H4Z" fill="#8D5A3B"/>`
       + kid({s: .6, dy: 28, la: [-150, -160], ra: [150, 160], shirt: '#FFB703'}) + star(36, 30, 6, 2.5, '#FFD23F') + star(86, 26, 6, 2.5, '#FFD23F'),
    restaurant: () => building(20, 44, 80, 64, '#FFF3DD', '#E63946', 'RESTAURANT') + `<path d="M20 44 h80 v8 q-10 6 -20 0 q-10 6 -20 0 q-10 6 -20 0 q-10 6 -20 0z" fill="#E63946" opacity=".6"/>`
       + `<path d="M36 74 v12 M32 74 v6 M40 74 v6 M84 74 v14 M84 74 q-6 6 0 10" stroke="#8A8FA3" stroke-width="2.5" fill="none"/>`,
    bookstore: () => building(18, 40, 84, 68, '#E9A66B', '#5A67D8', 'BOOKS')
       + [[28, '#E63946'], [36, '#3D8BFD'], [44, '#2FA36B'], [76, '#FFB703'], [84, '#9B5DE5']].map(([x, c]) => `<rect x="${x}" y="76" width="6" height="22" fill="${c}"/>`).join(''),
    supermarket: () => building(10, 40, 100, 68, '#fff', '#2FA36B', 'SUPERMARKET') + `<rect x="10" y="40" width="100" height="68" fill="none" stroke="#E3E6F5" stroke-width="2"/>
       <path d="M74 84 h22 l-4 12 h-16z M74 84 l-4 -8" stroke="#E63946" stroke-width="3" fill="none"/><circle cx="78" cy="100" r="3" fill="#E63946"/><circle cx="90" cy="100" r="3" fill="#E63946"/>`,
    mall: () => `<rect x="6" y="36" width="108" height="72" rx="4" fill="#C5CBE0"/><path d="M6 36 Q60 4 114 36Z" fill="#7FC8F8"/>
       ${[0, 1, 2].map(r => [0, 1, 2, 3, 4].map(c => `<rect x="${14 + c * 20}" y="${44 + r * 18}" width="14" height="12" rx="2" fill="${(r + c) % 3 ? '#fff' : '#FFD23F'}"/>`).join('')).join('')}
       <rect x="48" y="92" width="24" height="16" fill="#2B2D42"/>`,
    zoo: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#8EDB6E"/><path d="M14 48 Q60 14 106 48" stroke="#8D5A3B" stroke-width="8" fill="none"/>
       <rect x="14" y="44" width="8" height="66" fill="#8D5A3B"/><rect x="98" y="44" width="8" height="66" fill="#8D5A3B"/><text x="60" y="44" text-anchor="middle" font-size="16" ${FONT} fill="#fff">ZOO</text>`
       + `<g transform="translate(26 50) scale(.55)">${ART.giraffe ? '' : ''}</g>` + `<circle cx="50" cy="80" r="14" fill="#fff"/><circle cx="42" cy="68" r="6" fill="${INK}"/><circle cx="58" cy="68" r="6" fill="${INK}"/>
       <ellipse cx="45" cy="78" rx="4" ry="5" fill="${INK}"/><ellipse cx="55" cy="78" rx="4" ry="5" fill="${INK}"/><path d="M76 108 V70 l8 -6 l6 6 V108" fill="#FFB703"/>`,
    street: () => `<path d="M40 4 H80 L116 116 H4Z" fill="#6B7085"/><path d="M60 10 V26 M60 40 V60 M60 76 V100" stroke="#fff" stroke-width="5"/>
       <path d="M40 4 L4 116 M80 4 L116 116" stroke="#C5CBE0" stroke-width="5"/>`,
    crossing: () => `<rect x="4" y="30" width="112" height="60" fill="#6B7085"/>${[0, 1, 2, 3, 4, 5].map(i => `<rect x="${12 + i * 17}" y="38" width="10" height="44" fill="#fff"/>`).join('')}`,
    cross: () => `<rect x="4" y="70" width="112" height="42" fill="#6B7085"/>${[0, 1, 2, 3, 4, 5].map(i => `<rect x="${12 + i * 17}" y="76" width="10" height="30" fill="#fff"/>`).join('')}`
       + kid({s: .62, dy: -4, la: [-24, -8], ra: [26, 48], ll: [20, 8], rl: [-20, -36], shirt: '#E63946'}),
    open: () => `<rect x="20" y="24" width="80" height="50" rx="8" fill="#2FA36B"/><text x="60" y="58" text-anchor="middle" font-size="22" ${FONT} fill="#fff">OPEN</text>
       <path d="M40 24 L60 8 L80 24" stroke="#8A8FA3" stroke-width="3" fill="none"/><path d="M30 96 h60" stroke="#C5CBE0" stroke-width="4"/>`,
    closed: () => `<rect x="14" y="24" width="92" height="50" rx="8" fill="#E63946"/><text x="60" y="58" text-anchor="middle" font-size="20" ${FONT} fill="#fff">CLOSED</text>
       <path d="M40 24 L60 8 L80 24" stroke="#8A8FA3" stroke-width="3" fill="none"/>`,

    // ---------- ep44 restaurant ----------
    service: () => figure('man', {shirt: '#2B2D42', skin: SKIN[1]}) + `<path d="M50 70 l10 6 l10 -6 l-10 -4z" fill="#E63946"/>`
       + `<path d="M76 70 h40" stroke="#C5CBE0" stroke-width="4"/><path d="M80 70 a16 12 0 0 1 32 0z" fill="#C5CBE0"/><circle cx="96" cy="56" r="3" fill="#8A8FA3"/>`,
    menu: () => `<rect x="22" y="10" width="76" height="100" rx="6" fill="#8D5A3B"/><rect x="28" y="16" width="64" height="88" rx="3" fill="#FFF3DD"/>
       <text x="60" y="36" text-anchor="middle" font-size="14" ${FONT} fill="#8D5A3B">MENU</text>${[50, 64, 78, 92].map(y => `<path d="M36 ${y} h30" stroke="#C9934A" stroke-width="3"/><text x="84" y="${y + 4}" text-anchor="middle" font-size="10" ${FONT} fill="#C9934A">$</text>`).join('')}`,
    dish: () => plate(60, 72, 52, 26) + `<path d="M34 70 C34 50 86 50 86 70Z" fill="#E07A4F"/><circle cx="46" cy="60" r="5" fill="#6CCB5F"/><circle cx="72" cy="58" r="5" fill="#6CCB5F"/>` + steam(52, 40),
    make: () => `<path d="M24 64 h72 v20 a16 16 0 0 1 -16 16 h-40 a16 16 0 0 1 -16 -16z" fill="#2B2D42"/><path d="M96 70 h18" stroke="#2B2D42" stroke-width="7" stroke-linecap="round"/>
       <ellipse cx="60" cy="64" rx="36" ry="7" fill="#6B7085"/>${flame(44, 112, .7)}${flame(60, 114, .8)}${flame(76, 112, .7)}
       <path d="M60 58 L84 18" stroke="#B5703F" stroke-width="5" stroke-linecap="round"/><ellipse cx="58" cy="60" rx="10" ry="4" fill="#E07A4F"/>`,
    delicious: () => emo('#FFD23F', `<path d="M36 52 q8 -8 16 0 M68 52 q8 -8 16 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
       `<path d="M40 72 q20 18 40 0" stroke="${INK}" stroke-width="4.5" fill="none" stroke-linecap="round"/><path d="M66 80 q6 8 12 0" fill="#FF6FA5"/>`, star(100, 22, 8, 3.4, '#E63946') + star(18, 30, 6, 2.5, '#E63946')),
    dumpling: () => plate(60, 86, 52, 20) + [[38, 74], [60, 66], [82, 74]].map(([x, y]) => `<path d="M${x - 18} ${y} C${x - 18} ${y - 22} ${x + 18} ${y - 22} ${x + 18} ${y}Z" fill="#FBE3B8" stroke="#C9934A" stroke-width="2.5"/>
         ${[-10, -3, 4, 11].map(d => `<path d="M${x + d} ${y - 14} q2 -4 4 0" stroke="#C9934A" stroke-width="2" fill="none"/>`).join('')}`).join(''),
    common: () => [0, 1, 2, 3, 4, 5].map(i => `<circle cx="${22 + (i % 3) * 38}" cy="${40 + Math.floor(i / 3) * 40}" r="15" fill="#7FC8F8"/>`).join('')
       + `<text x="60" y="114" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">到处都有</text>`,
    plenty: () => `<path d="M14 58 H106 Q102 104 60 104 Q18 104 14 58Z" fill="#fff" stroke="#3D8BFD" stroke-width="4"/>`
       + [[30, 50], [48, 40], [66, 42], [84, 50], [40, 30], [58, 24], [76, 30]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="11" fill="#E63946"/>`).join(''),
    piece: () => pizza(`<path d="M60 60 L60 12 A48 48 0 0 1 101 36Z" fill="#fff" opacity=".0"/>`).replace('<circle cx="60" cy="60" r="48" fill="#E9A66B"/>', '<path d="M60 60 L60 12 A48 48 0 1 0 101 36Z" fill="#E9A66B"/>')
       + `<path d="M70 52 L74 6 A48 48 0 0 1 112 32Z" fill="#E9A66B"/><path d="M74 46 L77 14 A40 40 0 0 1 106 32Z" fill="#FFD166"/><circle cx="88" cy="28" r="4" fill="#E63946"/>`,
    bit: () => `<circle cx="60" cy="60" r="44" fill="#F4D3A8" opacity=".5"/><circle cx="60" cy="60" r="8" fill="#B5703F"/>${[[46, 44], [76, 50], [52, 78]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#B5703F"/>`).join('')}
       <text x="60" y="110" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">一点点</text>`,
    normal: () => `<rect x="10" y="40" width="100" height="40" rx="20" fill="#E3E6F5"/><circle cx="60" cy="60" r="16" fill="#2FA36B"/>${check(60, 62, .8, '#fff')}`,
    treat: () => person('woman', {shirt: '#FF6FA5'}, -18, 14, .85) + `<path d="M58 84 h40" stroke="${SKIN[0]}" stroke-width="6" stroke-linecap="round"/>`
       + `<g transform="translate(70 56) scale(.4)">${ART.cake()}</g>` + heart(98, 26, .6, '#E63946'),
    pardon: () => `<g transform="translate(-14 14) scale(.86)">${figure('boy', {shirt: '#5A67D8'})}</g>` + hand(26, 70, .5, -40, SKIN[0])
       + bubble(62, 10, 54, 40, '#FF9F1C', 'l', `<text x="27" y="29" text-anchor="middle" font-size="26" ${FONT} fill="#fff">?</text>`),

    // ---------- ep45 animals ----------
    animal: () => dog(30, 60, .8) + catA(64, 48, .7) + birdA(96, 30, .55),
    wild: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#8EDB6E"/>${[12, 30, 88, 104].map((x, i) => `<path d="M${x - 10} 116 Q${x} ${40 + i * 6} ${x + 10} 116Z" fill="#3FA34D"/>`).join('')}`
       + `<circle cx="60" cy="56" r="26" fill="#FFB703"/><circle cx="60" cy="56" r="34" fill="none" stroke="#C1440E" stroke-width="10" stroke-dasharray="6 4"/>
          <circle cx="51" cy="52" r="3.5" fill="${INK}"/><circle cx="69" cy="52" r="3.5" fill="${INK}"/><path d="M54 64 q6 6 12 0" stroke="${INK}" stroke-width="3" fill="none"/>`,
    pet: () => dog(44, 56, 1.05) + `<path d="M64 88 h40 v20 h-40z" fill="#E63946"/><circle cx="84" cy="74" r="8" fill="#FFD23F"/>` + heart(96, 26, .7, '#FF4D6D'),
    care: () => `<path d="M14 92 C30 74 50 70 64 76 L92 70 C102 68 104 80 96 84 L64 98 C46 104 28 104 14 100Z" fill="${SKIN[0]}"/>` + catA(60, 50, .7) + heart(98, 20, .7, '#FF4D6D'),
    usual: () => `<rect x="14" y="20" width="92" height="84" rx="8" fill="#fff" stroke="#E3E6F5" stroke-width="3"/>${[0, 1, 2, 3, 4, 5, 6, 7, 8].map(i =>
         `<circle cx="${32 + (i % 3) * 28}" cy="${40 + Math.floor(i / 3) * 24}" r="8" fill="#7FC8F8"/>`).join('')}`,
    unusual: () => `<rect x="14" y="20" width="92" height="84" rx="8" fill="#fff" stroke="#E3E6F5" stroke-width="3"/>${[0, 1, 2, 3, 5, 6, 7, 8].map(i =>
         `<circle cx="${32 + (i % 3) * 28}" cy="${40 + Math.floor(i / 3) * 24}" r="8" fill="#7FC8F8"/>`).join('')}${star(60, 64, 14, 6, '#E63946')}`,
    dog: () => dog(60, 44, 1.6),
    cat: () => catA(56, 52, 1.2),
    mouse: () => `<ellipse cx="60" cy="74" rx="34" ry="24" fill="#B8BFCC"/><circle cx="36" cy="44" r="16" fill="#B8BFCC"/><circle cx="72" cy="44" r="16" fill="#B8BFCC"/>
       <circle cx="36" cy="44" r="9" fill="#FFB3C6"/><circle cx="72" cy="44" r="9" fill="#FFB3C6"/><circle cx="46" cy="70" r="3.5" fill="${INK}"/><circle cx="66" cy="70" r="3.5" fill="${INK}"/>
       <circle cx="56" cy="80" r="4" fill="#FF6F91"/><path d="M92 82 C112 84 112 104 96 108" stroke="#B8BFCC" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    snake: () => `<path d="M16 96 C16 76 50 80 56 64 C62 48 30 46 34 30 C38 16 66 16 82 22" stroke="#2FA36B" stroke-width="16" fill="none" stroke-linecap="round"/>
       <circle cx="88" cy="24" r="13" fill="#2FA36B"/><circle cx="92" cy="20" r="3" fill="${INK}"/><path d="M100 26 l10 2 l-4 -6 M110 28 l-4 6" stroke="#E63946" stroke-width="2.5" fill="none"/>
       ${[[24, 88], [44, 74], [44, 46], [62, 22]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="3" fill="#FFD23F"/>`).join('')}`,
    bird: () => birdA(56, 62, 1.4),
    wing: () => `<path d="M60 70 C40 40 14 30 8 44 C4 60 30 76 60 74Z" fill="#7FC8F8"/><path d="M60 70 C80 40 106 30 112 44 C116 60 90 76 60 74Z" fill="#7FC8F8"/>
       ${[24, 36, 48].map(x => `<path d="M60 72 L${x} ${46 + (x - 24) / 3}" stroke="#3D8BFD" stroke-width="2"/><path d="M60 72 L${120 - x} ${46 + (x - 24) / 3}" stroke="#3D8BFD" stroke-width="2"/>`).join('')}
       <ellipse cx="60" cy="78" rx="6" ry="14" fill="#3D8BFD"/>`,
    fly: () => cloud(30, 92, .55) + birdA(64, 48, 1) + `<path d="M8 40 q14 -10 28 0 M10 60 q10 -8 20 0" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-linecap="round" opacity=".6"/>`,
    tail: () => `<path d="M30 96 C20 60 40 24 70 16 C100 10 112 36 96 48 C84 58 66 46 76 36" stroke="#E9A66B" stroke-width="18" fill="none" stroke-linecap="round"/>
       <path d="M30 96 C20 60 40 24 70 16" stroke="#C9934A" stroke-width="4" fill="none" stroke-dasharray="5 7"/>`,
  });

  const crop = (c, head, x = 60) => `<path d="M${x} 112 V40" stroke="#3FA34D" stroke-width="5" stroke-linecap="round"/>
      <path d="M${x} 86 C${x - 18} 84 ${x - 26} 72 ${x - 28} 60 C${x - 12} 62 ${x - 2} 72 ${x} 86Z M${x} 74 C${x + 18} 72 ${x + 26} 60 ${x + 28} 48 C${x + 12} 50 ${x + 2} 60 ${x} 74Z" fill="#6CCB5F"/>${head}`;
  const zooA = {
    panda: () => `<circle cx="60" cy="64" r="40" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><circle cx="28" cy="32" r="14" fill="#2B2D42"/><circle cx="92" cy="32" r="14" fill="#2B2D42"/>
       <ellipse cx="44" cy="60" rx="11" ry="14" fill="#2B2D42" transform="rotate(-20 44 60)"/><ellipse cx="76" cy="60" rx="11" ry="14" fill="#2B2D42" transform="rotate(20 76 60)"/>
       <circle cx="46" cy="60" r="4" fill="#fff"/><circle cx="74" cy="60" r="4" fill="#fff"/><ellipse cx="60" cy="78" rx="7" ry="5" fill="#2B2D42"/>
       <path d="M54 88 q6 5 12 0" stroke="#2B2D42" stroke-width="3" fill="none"/><ellipse cx="30" cy="80" rx="7" ry="4" fill="#FF8FAB" opacity=".7"/><ellipse cx="90" cy="80" rx="7" ry="4" fill="#FF8FAB" opacity=".7"/>`,
    bamboo: () => [36, 60, 84].map((x, i) => `<rect x="${x - 6}" y="${8 + i * 6}" width="12" height="${104 - i * 6}" rx="4" fill="${['#6CCB5F', '#3FA34D', '#8EDB6E'][i]}"/>
       ${[30, 56, 82].map(y => `<rect x="${x - 7}" y="${y + i * 4}" width="14" height="4" rx="2" fill="#2F7D32"/>`).join('')}
       <path d="M${x + 6} ${40 + i * 10} q14 -10 22 -4 q-10 10 -22 4z" fill="#6CCB5F"/>`).join(''),
    lion: () => `${Array.from({length: 14}, (_, i) => { const a = i / 14 * 6.283; return `<circle cx="${60 + 40 * Math.cos(a)}" cy="${62 + 40 * Math.sin(a)}" r="14" fill="#C1440E"/>`; }).join('')}
       <circle cx="60" cy="62" r="36" fill="#E07A4F"/><circle cx="60" cy="62" r="30" fill="#FFB703"/><circle cx="48" cy="56" r="4" fill="${INK}"/><circle cx="72" cy="56" r="4" fill="${INK}"/>
       <path d="M54 68 h12 l-6 7z" fill="#8D5A3B"/><path d="M60 75 v6 M52 82 q8 6 16 0" stroke="#8D5A3B" stroke-width="3" fill="none"/>`,
    zebra: () => `<path d="M42 112 V54 C42 32 50 16 64 14 C80 12 90 26 88 44 L94 64 C96 74 84 78 78 70 L76 112Z" fill="#fff" stroke="#2B2D42" stroke-width="3"/>
       ${[30, 44, 58, 72, 88, 102].map(y => `<path d="M44 ${y} q16 -6 32 0" stroke="#2B2D42" stroke-width="6" fill="none"/>`).join('')}
       <path d="M60 14 C56 6 62 2 66 10 M74 14 C76 4 82 6 80 14" stroke="#2B2D42" stroke-width="5" fill="none"/><circle cx="78" cy="38" r="3.5" fill="${INK}"/>`,
    giraffe: () => `<path d="M54 112 V60 L58 22 C58 12 70 8 76 16 L90 30 C96 36 90 44 84 40 L72 36 L70 112Z" fill="#FFB703"/>
       ${[[62, 50], [64, 72], [62, 94], [70, 28], [66, 62], [66, 84]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="4.5" fill="#B5703F"/>`).join('')}
       <path d="M64 12 v-8 M72 12 v-8" stroke="#B5703F" stroke-width="4" stroke-linecap="round"/><circle cx="76" cy="24" r="3" fill="${INK}"/>`,
    elephant: () => `<ellipse cx="60" cy="60" rx="36" ry="34" fill="#B8BFCC"/><ellipse cx="22" cy="58" rx="20" ry="26" fill="#C9D0DC"/><ellipse cx="98" cy="58" rx="20" ry="26" fill="#C9D0DC"/>
       <path d="M60 70 C60 90 54 104 44 106 C40 106 40 100 44 98 C50 96 50 86 50 76Z" fill="#B8BFCC"/><circle cx="48" cy="54" r="4" fill="${INK}"/><circle cx="72" cy="54" r="4" fill="${INK}"/>
       <path d="M42 74 q-6 8 -4 14 M78 74 q6 8 4 14" stroke="#fff" stroke-width="5" stroke-linecap="round"/>`,
    owl: () => `<ellipse cx="60" cy="66" rx="36" ry="42" fill="#8D5A3B"/><path d="M30 30 l6 -18 l12 14 M90 30 l-6 -18 l-12 14" fill="#8D5A3B"/>
       <circle cx="44" cy="52" r="14" fill="#fff"/><circle cx="76" cy="52" r="14" fill="#fff"/><circle cx="44" cy="52" r="7" fill="${INK}"/><circle cx="76" cy="52" r="7" fill="${INK}"/>
       <path d="M54 64 l6 10 l6 -10z" fill="#FFB703"/><ellipse cx="60" cy="88" rx="20" ry="16" fill="#E9A66B"/>`,
    monkey: () => `<circle cx="24" cy="54" r="12" fill="#B5703F"/><circle cx="96" cy="54" r="12" fill="#B5703F"/><circle cx="60" cy="56" r="36" fill="#B5703F"/>
       <path d="M36 62 C36 44 50 42 60 50 C70 42 84 44 84 62 C84 82 72 92 60 92 C48 92 36 82 36 62Z" fill="#F4D3A8"/>
       <circle cx="50" cy="58" r="4" fill="${INK}"/><circle cx="70" cy="58" r="4" fill="${INK}"/><path d="M50 76 q10 8 20 0" stroke="${INK}" stroke-width="3" fill="none"/>`,
    bear: () => `<circle cx="28" cy="28" r="14" fill="#8D5A3B"/><circle cx="92" cy="28" r="14" fill="#8D5A3B"/><circle cx="60" cy="62" r="42" fill="#8D5A3B"/>
       <ellipse cx="60" cy="76" rx="18" ry="14" fill="#D99058"/><ellipse cx="60" cy="70" rx="7" ry="5" fill="${INK}"/><circle cx="44" cy="52" r="4.5" fill="${INK}"/><circle cx="76" cy="52" r="4.5" fill="${INK}"/>`,
    wolf: () => `<path d="M20 14 L40 44 L60 38 L80 44 L100 14 L98 64 C96 90 78 108 60 108 C42 108 24 90 22 64Z" fill="#8A8FA3"/>
       <path d="M36 76 C44 74 52 82 60 108 C68 82 76 74 84 76 C80 96 70 108 60 108 C50 108 40 96 36 76Z" fill="#E3E6F5"/>
       <path d="M38 58 l12 4 M82 58 l-12 4" stroke="${INK}" stroke-width="4" stroke-linecap="round"/><ellipse cx="60" cy="98" rx="6" ry="4" fill="${INK}"/>`,
    shark: () => `<path d="M0 98 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/>
       <path d="M8 72 C30 48 74 46 104 66 L116 54 L112 76 L118 92 L104 80 C76 96 34 96 8 72Z" fill="#6B7085"/><path d="M50 54 L62 26 L70 54Z" fill="#6B7085"/>
       <path d="M12 74 C34 88 70 90 100 78 C72 92 34 92 12 74Z" fill="#fff"/><circle cx="26" cy="66" r="3" fill="${INK}"/><path d="M14 76 l6 2 l2 -4 l4 4 l2 -4" stroke="#fff" stroke-width="1.6" fill="none"/>`,
    whale: () => `<path d="M0 100 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/>
       <path d="M12 70 C12 44 44 36 70 42 C92 46 100 62 98 74 L112 62 L108 86 L96 82 C88 96 30 100 12 70Z" fill="#3D8BFD"/>
       <path d="M16 76 C30 92 70 94 92 82 C70 98 30 96 16 76Z" fill="#BDE7FF"/><circle cx="32" cy="62" r="3.5" fill="${INK}"/>
       <path d="M50 38 C48 24 42 18 36 22 M50 38 C52 22 60 16 66 22" stroke="#7FC8F8" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    duck: () => `<ellipse cx="54" cy="78" rx="38" ry="26" fill="#FFD23F"/><circle cx="82" cy="44" r="20" fill="#FFD23F"/><path d="M98 44 l18 2 q-4 10 -18 6z" fill="#FF9F1C"/>
       <circle cx="86" cy="40" r="3.5" fill="${INK}"/><path d="M28 74 q16 -14 32 0 q-16 14 -32 0z" fill="#F4B400"/><path d="M0 104 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/>`,
    rabbit: () => `<ellipse cx="44" cy="30" rx="10" ry="26" fill="#fff" stroke="#E3E6F5" stroke-width="2"/><ellipse cx="76" cy="30" rx="10" ry="26" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>
       <ellipse cx="44" cy="30" rx="5" ry="18" fill="#FFB3C6"/><ellipse cx="76" cy="30" rx="5" ry="18" fill="#FFB3C6"/><circle cx="60" cy="74" r="34" fill="#fff" stroke="#E3E6F5" stroke-width="2"/>
       <circle cx="48" cy="70" r="4" fill="${INK}"/><circle cx="72" cy="70" r="4" fill="${INK}"/><path d="M56 80 h8 l-4 4z" fill="#FF6F91"/><path d="M60 84 v4 M54 90 q6 4 12 0" stroke="${INK}" stroke-width="2" fill="none"/>`,
    spider: () => `${[-1, 1].map(sd => [0, 1, 2, 3].map(i => `<path d="M60 64 L${60 + sd * (30 + i * 4)} ${44 + i * 14} L${60 + sd * (44 + i * 2)} ${60 + i * 14}" stroke="#2B2D42" stroke-width="4" fill="none" stroke-linejoin="round"/>`).join('')).join('')}
       <ellipse cx="60" cy="72" rx="18" ry="22" fill="#2B2D42"/><circle cx="60" cy="46" r="12" fill="#2B2D42"/><circle cx="55" cy="44" r="3" fill="#fff"/><circle cx="65" cy="44" r="3" fill="#fff"/>
       <path d="M60 4 V34" stroke="#C5CBE0" stroke-width="2"/>`,
  };
  Object.assign(ART, zooA, {
    // ---------- ep46 country ----------
    plants: () => crop('', `<ellipse cx="60" cy="36" rx="10" ry="16" fill="#8EDB6E"/>`) + `<g transform="translate(-30 20) scale(.7)">${crop('', '<circle cx="60" cy="36" r="10" fill="#FFB703"/>')}</g>`,
    kind: () => [[30, '#E63946'], [60, '#FFB703'], [90, '#2FA36B']].map(([x, c], i) => `<circle cx="${x}" cy="44" r="15" fill="${c}"/><rect x="${x - 15}" y="70" width="30" height="30" rx="${i * 7}" fill="${c}" opacity=".7"/>`).join('')
       + `<text x="60" y="116" text-anchor="middle" font-size="13" ${FONT} fill="#8A8FA3">种类</text>`,
    corn: () => `<path d="M60 112 V96" stroke="#3FA34D" stroke-width="5"/><ellipse cx="60" cy="56" rx="18" ry="40" fill="#FFD23F"/>
       ${[0, 1, 2, 3, 4, 5, 6].map(r => [-1, 0, 1].map(c => `<circle cx="${60 + c * 9}" cy="${28 + r * 9}" r="3.5" fill="#F4B400"/>`).join('')).join('')}
       <path d="M60 104 C40 100 32 80 34 56 C44 70 52 84 60 96Z M60 104 C80 100 88 80 86 56 C76 70 68 84 60 96Z" fill="#6CCB5F"/>`,
    wheat: () => [44, 60, 76].map((x, i) => `<path d="M${x} 112 Q${x + (i - 1) * 4} 70 ${x + (i - 1) * 8} 40" stroke="#C9934A" stroke-width="3" fill="none"/>
       ${[0, 1, 2, 3, 4].map(k => `<ellipse cx="${x + (i - 1) * 8 - 5}" cy="${18 + k * 9}" rx="4" ry="7" fill="#E9C46A" transform="rotate(-25 ${x + (i - 1) * 8 - 5} ${18 + k * 9})"/>
         <ellipse cx="${x + (i - 1) * 8 + 5}" cy="${18 + k * 9}" rx="4" ry="7" fill="#E9C46A" transform="rotate(25 ${x + (i - 1) * 8 + 5} ${18 + k * 9})"/>`).join('')}`).join(''),
    cotton: () => `<path d="M60 112 V70 M60 86 L36 70 M60 80 L86 64" stroke="#8D5A3B" stroke-width="5" stroke-linecap="round"/>
       ${[[60, 46], [32, 60], [90, 54]].map(([x, y]) => `${[[-8, 0], [8, 0], [0, -9], [-5, 7], [5, 7]].map(([dx, dy]) => `<circle cx="${x + dx}" cy="${y + dy}" r="9" fill="#fff" stroke="#E3E6F5" stroke-width="1.5"/>`).join('')}
         <path d="M${x - 12} ${y + 10} l12 6 l12 -6" stroke="#8D5A3B" stroke-width="3" fill="none"/>`).join('')}`,
    pick: () => crop('', `<circle cx="60" cy="40" r="10" fill="#E63946"/><circle cx="74" cy="56" r="8" fill="#E63946"/>`) + hand(82, 30, .6, -150, SKIN[0]),
    wood: () => tree(28, 74, .9, `<circle cx="0" cy="-18" r="22" fill="#3FA34D"/>`) + tree(64, 70, 1.05, `<circle cx="0" cy="-20" r="26" fill="#6CCB5F"/>`) + tree(98, 76, .85, `<circle cx="0" cy="-16" r="20" fill="#2F7D32"/>`),
    live: () => `<path d="M60 112 V60" stroke="#3FA34D" stroke-width="6" stroke-linecap="round"/><path d="M60 80 C38 78 26 62 26 42 C46 44 58 58 60 80Z" fill="#6CCB5F"/>
       <path d="M60 66 C80 62 92 46 94 28 C74 30 62 44 60 66Z" fill="#8EDB6E"/>` + heart(60, 30, .7, '#E63946') + `<text x="98" y="104" text-anchor="middle" font-size="12" ${FONT} fill="#2FA36B">alive</text>`,
    die: () => `<path d="M60 112 V70 C60 60 54 52 44 50" stroke="#B5893A" stroke-width="6" fill="none" stroke-linecap="round"/>
       <path d="M44 50 C30 50 22 62 24 76 C36 72 44 62 44 50Z" fill="#C9A35A"/><path d="M60 80 C72 82 80 92 82 104 C70 102 62 94 60 80Z" fill="#C9A35A"/>
       <text x="96" y="40" text-anchor="middle" font-size="12" ${FONT} fill="#8A8FA3">dead</text>`,

    // ---------- ep47 zoo ----------
    // (animals above)

    // ---------- ep48 shopping ----------
    store: () => building(18, 40, 84, 68, '#fff', '#FF7A59', 'STORE') + `<rect x="18" y="40" width="84" height="68" fill="none" stroke="#E3E6F5" stroke-width="2"/>`,
    shopping: () => `<path d="M30 40 h60 l-6 70 h-48z" fill="#FF6FA5"/><path d="M44 40 V30 a16 16 0 0 1 32 0 V40" stroke="#E63946" stroke-width="5" fill="none"/>
       <path d="M64 40 h40 l-4 54 h-32z" fill="#3D8BFD"/><path d="M76 40 V34 a8 8 0 0 1 16 0 V40" stroke="#2A6FD6" stroke-width="4" fill="none"/>${star(48, 74, 9, 4, '#fff')}`,
    buy: () => hand(40, 80, 1.1, 20, SKIN[0]) + `<rect x="48" y="30" width="56" height="34" rx="5" fill="#2FA36B" transform="rotate(-12 76 47)"/><circle cx="76" cy="47" r="9" fill="#BCE9C9"/>
       <text x="76" y="52" text-anchor="middle" font-size="12" ${FONT} fill="#1E7A4E" transform="rotate(-12 76 47)">¥</text>`,
    sell: () => `<rect x="10" y="64" width="100" height="16" rx="3" fill="#B5703F"/><path d="M14 80 v30 M106 80 v30" stroke="#8D5A3B" stroke-width="5"/>
       ${[[30, '#E63946'], [52, '#FFB703'], [74, '#2FA36B']].map(([x, c]) => `<circle cx="${x}" cy="54" r="10" fill="${c}"/>`).join('')}
       <rect x="78" y="16" width="34" height="22" rx="3" fill="#fff" stroke="#E63946" stroke-width="2.5"/><text x="95" y="32" text-anchor="middle" font-size="12" ${FONT} fill="#E63946">SALE</text>
       <path d="M95 38 V46" stroke="#8A8FA3" stroke-width="2"/>`,
    free: () => `<g transform="rotate(-10 60 60)"><path d="M20 38 h60 l20 22 l-20 22 h-60z" fill="#2FA36B"/><circle cx="84" cy="60" r="5" fill="#fff"/>
       <text x="50" y="68" text-anchor="middle" font-size="22" ${FONT} fill="#fff">FREE</text></g>` + star(100, 20, 8, 3.4, '#FFD23F'),
    afford: () => `<rect x="14" y="40" width="72" height="54" rx="10" fill="#8D5A3B"/><rect x="14" y="40" width="72" height="16" rx="6" fill="#6B4A36"/>
       <rect x="62" y="56" width="30" height="20" rx="5" fill="#6B4A36"/><circle cx="74" cy="66" r="4" fill="#FFD23F"/>` + check(100, 30, 1.2),
    market: () => [[20, '#E63946'], [60, '#3D8BFD'], [100, '#2FA36B']].map(([x, c]) => `<path d="M${x - 18} 52 L${x} 34 L${x + 18} 52Z" fill="${c}"/>
         <rect x="${x - 16}" y="52" width="32" height="40" fill="#FFF3DD"/><path d="M${x - 16} 52 h32 v6 q-8 5 -16 0 q-8 5 -16 0z" fill="${c}" opacity=".6"/>
         <circle cx="${x - 6}" cy="${80}" r="5" fill="#FFB703"/><circle cx="${x + 6}" cy="80" r="5" fill="#E07A4F"/>`).join('') + `<path d="M0 94 H120" stroke="#C5CBE0" stroke-width="4"/>`,
    cheap: () => `<g transform="rotate(-10 60 60)"><path d="M20 38 h60 l20 22 l-20 22 h-60z" fill="#FFD23F"/><circle cx="84" cy="60" r="5" fill="#fff"/>
       <text x="50" y="69" text-anchor="middle" font-size="24" ${FONT} fill="#E63946">¥1</text></g><path d="M100 84 v24 m-8 -8 l8 8 l8 -8" stroke="#2FA36B" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    expensive: () => `<g transform="rotate(-10 60 60)"><path d="M14 38 h66 l20 22 l-20 22 h-66z" fill="#9B5DE5"/><circle cx="84" cy="60" r="5" fill="#fff"/>
       <text x="48" y="68" text-anchor="middle" font-size="18" ${FONT} fill="#fff">¥999</text></g><path d="M100 108 v-24 m-8 8 l8 -8 l8 8" stroke="#E63946" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    trade: () => `<path d="M20 44 H92 m-12 -12 l12 12 l-12 12" stroke="#3D8BFD" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
       <path d="M100 82 H28 m12 -12 l-12 12 l12 12" stroke="#FF9F1C" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>` + gift(10, 20, 22, 22, '#E63946') + `<circle cx="100" cy="100" r="11" fill="#FFD23F"/>`,
    deal: () => `<path d="M8 76 L34 60 L56 70 L64 62 L86 60 L112 76 L96 96 L70 88 L56 96 L24 94Z" fill="${SKIN[0]}"/>
       <path d="M56 70 L76 84 M64 62 L84 78 M48 76 L66 90" stroke="${SKIN[1]}" stroke-width="3"/><path d="M8 76 L20 92 M112 76 L100 92" stroke="#3D8BFD" stroke-width="10" stroke-linecap="round"/>` + star(60, 24, 12, 5, '#FFD23F'),
    steal: () => `<g transform="translate(-6 8) scale(.92)">${figure('man', {shirt: '#2B2D42', skin: SKIN[0], cap: '#2B2D42'})}</g>
       <rect x="40" y="40" width="40" height="10" rx="5" fill="#2B2D42"/><circle cx="52" cy="45" r="3" fill="#fff"/><circle cx="68" cy="45" r="3" fill="#fff"/>
       <path d="M86 80 h24 v26 h-24z" fill="#FFD23F"/><text x="98" y="98" text-anchor="middle" font-size="12" ${FONT} fill="#E0A100">$</text>
       <path d="M8 18 l14 14 M22 18 l-14 14" stroke="#E63946" stroke-width="4" stroke-linecap="round"/>`,

    // ---------- ep49 accessories ----------
    available: () => calPage('FREE', '✓', '#2FA36B'),
    bring: () => `<path d="M26 40 H82 V100 H26Z" fill="#E9A66B"/><path d="M26 40 L54 54 L82 40" stroke="#B5703F" stroke-width="3" fill="none"/>` + hand(30, 102, .7, 70, SKIN[0])
       + `<path d="M90 70 h-22 m8 -8 l-8 8 l8 8" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(28 0)"/>`,
    suit: () => `<path d="M38 14 L14 30 L10 112 H110 L106 30 L82 14 L60 40Z" fill="#2B2D42"/><path d="M38 14 L52 54 L60 40 L68 54 L82 14 L60 22Z" fill="#fff"/>
       <path d="M60 30 l-5 8 l5 24 l5 -24z" fill="#E63946"/><path d="M52 54 L60 112 L68 54" stroke="#1B1D2E" stroke-width="2" fill="none"/>
       ${[70, 84].map(y => `<circle cx="66" cy="${y}" r="2.6" fill="#8A8FA3"/>`).join('')}`,
    tie: () => `<path d="M48 14 h24 l-4 14 h-16z" fill="#C1121F"/><path d="M52 28 h16 l10 62 l-18 22 l-18 -22z" fill="#E63946"/>
       ${[44, 62, 80].map(y => `<path d="M${54 - (y - 44) / 8} ${y} L${66 + (y - 44) / 8} ${y + 8}" stroke="#FFD23F" stroke-width="4"/>`).join('')}`,
    earring: () => [36, 84].map(x => `<circle cx="${x}" cy="20" r="5" fill="none" stroke="#E0A100" stroke-width="3"/><path d="M${x} 25 v14" stroke="#E0A100" stroke-width="2.5"/>
       <path d="M${x} 40 L${x - 14} 76 L${x} 104 L${x + 14} 76Z" fill="#9B5DE5"/><circle cx="${x}" cy="72" r="5" fill="#FFD23F"/>`).join(''),
    scarf: () => `<path d="M24 36 C24 16 96 16 96 36 C96 52 24 52 24 36Z" fill="none" stroke="#E63946" stroke-width="14"/>
       <path d="M70 48 L76 110 H96 L86 46Z" fill="#E63946"/>${[78, 82, 86, 90, 94].map(x => `<path d="M${x} 110 v8" stroke="#E63946" stroke-width="2.5"/>`).join('')}
       ${[30, 46, 62].map(y => `<path d="M${74 + (y - 30) / 10} ${y + 30} h${16}" stroke="#fff" stroke-width="4" opacity=".7"/>`).join('')}`,
    bag: () => `<rect x="22" y="36" width="76" height="72" rx="16" fill="#2FA36B"/><path d="M44 36 V26 a16 12 0 0 1 32 0 V36" stroke="#1E7A4E" stroke-width="6" fill="none"/>
       <rect x="34" y="64" width="52" height="28" rx="8" fill="#45C17E"/><path d="M34 74 h52" stroke="#1E7A4E" stroke-width="3"/>`,
    handbag: () => `<path d="M24 50 h72 l10 58 h-92z" fill="#FF6FA5"/><path d="M40 50 C40 20 80 20 80 50" stroke="#C1266B" stroke-width="7" fill="none"/>
       <rect x="52" y="64" width="16" height="12" rx="3" fill="#FFD23F"/>`,
    purse: () => `<path d="M14 58 C14 40 106 40 106 58 V92 a12 12 0 0 1 -12 12 H26 a12 12 0 0 1 -12 -12Z" fill="#9B5DE5"/>
       <path d="M14 58 C30 70 90 70 106 58" stroke="#7B3FC4" stroke-width="4" fill="none"/><circle cx="52" cy="46" r="6" fill="#FFD23F"/><circle cx="68" cy="46" r="6" fill="#FFD23F"/>`,
    wallet: () => `<rect x="12" y="32" width="96" height="66" rx="10" fill="#8D5A3B"/><rect x="12" y="32" width="96" height="20" rx="8" fill="#6B4A36"/>
       <rect x="70" y="54" width="42" height="26" rx="8" fill="#6B4A36"/><circle cx="84" cy="67" r="5" fill="#FFD23F"/><rect x="22" y="22" width="44" height="18" rx="2" fill="#2FA36B"/>`,
    glove: () => `<path d="M30 112 V64 C30 56 22 48 22 40 C22 32 32 30 36 38 L40 50 V22 a7 7 0 0 1 14 0 V48 V16 a7 7 0 0 1 14 0 V48 V22 a7 7 0 0 1 14 0 V54 V36 a7 7 0 0 1 14 0 V80 C96 98 86 112 72 112Z" fill="#E63946"/>
       <rect x="30" y="98" width="66" height="14" fill="#FFF3DD"/>${[38, 52, 66, 80].map(x => `<path d="M${x} 98 v14" stroke="#E3D3B8" stroke-width="2"/>`).join('')}`,
    ring: () => `<circle cx="60" cy="74" r="32" fill="none" stroke="#FFD23F" stroke-width="10"/><circle cx="60" cy="74" r="32" fill="none" stroke="#E0B400" stroke-width="2"/>
       <path d="M46 40 L52 24 H68 L74 40 L60 54Z" fill="#7FC8F8"/><path d="M46 40 H74 M52 24 L60 54 L68 24" stroke="#fff" stroke-width="1.6" fill="none"/>${star(90, 20, 6, 2.5, '#fff')}`,

    // ---------- ep50 weather (2) ----------
    temperature: () => ART.hot().replace(/<path d="M22 70[\s\S]*$/, '`'.slice(1)) + `<text x="94" y="40" text-anchor="middle" font-size="16" ${FONT} fill="#E63946">°C</text>`,
    degree: () => `<text x="56" y="80" text-anchor="middle" font-size="58" ${FONT} fill="#3D8BFD">25</text><circle cx="96" cy="34" r="8" fill="none" stroke="#3D8BFD" stroke-width="5"/>`,
    heat: () => sun(60, 46, 24, true) + `<path d="M24 110 q-8 -12 0 -24 t0 -24 M60 112 q-8 -12 0 -24 M96 110 q-8 -12 0 -24 t0 -24" stroke="#FF7A59" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    smoke: () => `<path d="M60 112 V84" stroke="#8D5A3B" stroke-width="0"/>${flame(60, 102, 1.2)}<path d="M56 80 C40 70 64 58 50 44 C38 32 60 22 54 8" stroke="#8A8FA3" stroke-width="8" fill="none" stroke-linecap="round" opacity=".55"/>
       <path d="M70 76 C82 64 64 54 76 40" stroke="#C5CBE0" stroke-width="7" fill="none" stroke-linecap="round" opacity=".6"/>`,
    dry: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#FFE8C2"/><path d="M4 76 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#E9C46A"/>
       <path d="M20 84 l12 10 l-4 12 M58 80 l-6 14 l12 8 M90 86 l8 10" stroke="#B5893A" stroke-width="2.5" fill="none"/>` + sun(88, 30, 14)
       + `<path d="M36 76 V48 M36 58 l-10 -8 M36 54 l10 -10" stroke="#B5893A" stroke-width="4" stroke-linecap="round"/>`,
    wet: () => tee('#7FC8F8') + drops([[40, 54], [64, 70], [80, 48], [52, 88], [76, 92]], '#3D8BFD') + drops([[20, 8], [50, 4], [90, 10]], '#7FC8F8'),
    umbrella: () => `<path d="M10 58 C10 22 110 22 110 58 C100 50 88 50 80 58 C72 50 48 50 40 58 C32 50 20 50 10 58Z" fill="#E63946"/>
       <path d="M60 24 C46 34 40 46 40 58 M60 24 C74 34 80 46 80 58" stroke="#B5172B" stroke-width="2" fill="none"/>
       <path d="M60 22 V96 a8 8 0 0 1 -16 0" stroke="#2B2D42" stroke-width="5" fill="none" stroke-linecap="round"/>` + drops([[18, 76], [100, 80], [86, 100]]),
    raincoat: () => `<path d="M60 10 C40 10 32 24 34 40 L20 104 H100 L86 40 C88 24 80 10 60 10Z" fill="#FFD23F"/>
       <circle cx="60" cy="34" r="14" fill="${SKIN[0]}"/><path d="M46 30 C46 16 74 16 74 30" fill="#FFD23F"/><path d="M60 50 V104" stroke="#E0B400" stroke-width="3"/>
       ${[62, 76, 90].map(y => `<circle cx="66" cy="${y}" r="3" fill="#E0B400"/>`).join('')}` + drops([[14, 30], [104, 40], [100, 70]]),
    take: () => `<g transform="translate(18 0) scale(.7)">${ART.umbrella()}</g>` + hand(40, 96, .9, 20, SKIN[0])
       + `<path d="M16 74 V40 m-8 8 l8 -8 l8 8" stroke="#2FA36B" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
    too: () => `<circle cx="38" cy="60" r="26" fill="#3D8BFD"/><circle cx="82" cy="60" r="26" fill="#3D8BFD"/><text x="60" y="68" text-anchor="middle" font-size="22" ${FONT} fill="#fff">+</text>
       <text x="60" y="112" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">也</text>`,
    ice: () => [[36, 66, -8], [72, 52, 10], [70, 88, -4]].map(([x, y, r]) => `<g transform="rotate(${r} ${x} ${y})"><rect x="${x - 22}" y="${y - 22}" width="44" height="44" rx="8" fill="#BDE7FF" stroke="#7FC8F8" stroke-width="3"/>
         <path d="M${x - 12} ${y - 12} l10 -2" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>`).join(''),
    freeze: () => glass('#BDE7FF', .8) + flake(60, 70, 18, '#fff') + flake(96, 22, 9, '#7FC8F8'),
  });

  const flagGoal = (x, y, c = '#E63946') => `<path d="M${x} ${y} V${y + 70}" stroke="#8A8FA3" stroke-width="4"/><path d="M${x} ${y} h26 l-6 10 l6 10 h-26z" fill="${c}"/>`;
  const arrowTo = (x1, y1, x2, y2, c = '#E63946', w = 6) => { const a = Math.atan2(y2 - y1, x2 - x1), h = 10;
    return `<path d="M${x1} ${y1} L${x2} ${y2} M${x2 - h * Math.cos(a - .5)} ${y2 - h * Math.sin(a - .5)} L${x2} ${y2} L${x2 - h * Math.cos(a + .5)} ${y2 - h * Math.sin(a + .5)}" stroke="${c}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`; };
  const coin = (x, y, r = 10) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#FFD23F" stroke="#E0A100" stroke-width="2.5"/><text x="${x}" y="${y + r * .4}" text-anchor="middle" font-size="${r * 1.1}" ${FONT} fill="#C77800">¥</text>`;
  const paper = (inner, st = '#C5CBE0') => `<rect x="22" y="10" width="76" height="100" rx="6" fill="#fff" stroke="${st}" stroke-width="3"/>${inner}`;
  const lines = (ys, x = 32, w = 56) => ys.map(y => `<path d="M${x} ${y} h${w}" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>`).join('');
  Object.assign(ART, {
    // ---------- ep51 town (2) ----------
    church: () => `<rect x="30" y="54" width="60" height="56" fill="#F4F1E8" stroke="#C5CBE0" stroke-width="2"/><path d="M24 58 L60 30 L96 58Z" fill="#8D5A3B"/>
       <rect x="50" y="20" width="20" height="40" fill="#F4F1E8" stroke="#C5CBE0" stroke-width="2"/><path d="M46 22 L60 6 L74 22Z" fill="#8D5A3B"/>
       <path d="M50 82 a10 10 0 0 1 20 0 V110 H50Z" fill="#8D5A3B"/><circle cx="60" cy="40" r="6" fill="#7FC8F8"/>
       ${[38, 76].map(x => `<path d="M${x} 72 a6 6 0 0 1 12 0 v12 h-12z" fill="#7FC8F8"/>`).join('')}`,
    factory: () => `<path d="M8 110 V62 L32 48 V62 L56 48 V62 L80 48 V110Z" fill="#8A8FA3"/><rect x="84" y="20" width="14" height="90" fill="#6B7085"/><rect x="84" y="28" width="14" height="6" fill="#E63946"/>
       ${[18, 42, 66].map(x => `<rect x="${x}" y="74" width="12" height="12" fill="#FFD23F"/>`).join('')}<circle cx="96" cy="12" r="8" fill="#E3E6F5"/><circle cx="108" cy="6" r="5" fill="#E3E6F5"/>`,
    grounds: () => `<rect x="4" y="4" width="112" height="112" rx="18" fill="#BDE7FF"/><path d="M4 60 H116 V98 a18 18 0 0 1 -18 18 H22 a18 18 0 0 1 -18 -18Z" fill="#6CCB5F"/>
       <ellipse cx="60" cy="86" rx="40" ry="16" fill="none" stroke="#fff" stroke-width="4"/><path d="M60 70 V102" stroke="#fff" stroke-width="3"/>
       <rect x="12" y="40" width="96" height="20" fill="#E9A66B"/><path d="M12 40 h96" stroke="#B5703F" stroke-width="3"/>`,
    prison: () => `<rect x="14" y="16" width="92" height="94" rx="6" fill="#8A8FA3"/><rect x="24" y="26" width="72" height="74" fill="#2B2D42"/>
       ${[34, 50, 66, 82].map(x => `<rect x="${x}" y="26" width="5" height="74" fill="#C5CBE0"/>`).join('')}<rect x="24" y="58" width="72" height="5" fill="#C5CBE0"/>`,
    library: () => `<rect x="10" y="40" width="100" height="70" fill="#F4E4C1"/><path d="M4 42 L60 12 L116 42Z" fill="#B5703F"/>
       ${[22, 44, 66, 88].map(x => `<rect x="${x - 4}" y="46" width="8" height="54" fill="#E9C8A0"/>`).join('')}<rect x="6" y="100" width="108" height="10" fill="#C9934A"/>
       <text x="60" y="36" text-anchor="middle" font-size="10" ${FONT} fill="#fff">LIBRARY</text>`,
    borrow: () => `<g transform="translate(14 22) scale(.55)">${ART.book()}</g>` + arrowTo(96, 30, 96, 96, '#2FA36B') + hand(52, 102, .8, 0, SKIN[0])
       + `<text x="96" y="22" text-anchor="middle" font-size="12" ${FONT} fill="#2FA36B">借入</text>`,
    lend: () => `<g transform="translate(40 52) scale(.55)">${ART.book()}</g>` + arrowTo(24, 96, 24, 30, '#FF9F1C') + hand(70, 104, .8, 0, SKIN[1])
       + `<text x="24" y="114" text-anchor="middle" font-size="12" ${FONT} fill="#FF9F1C">借出</text>`,
    return: () => `<g transform="translate(30 30) scale(.5)">${ART.book()}</g><path d="M96 60 a36 36 0 1 1 -10 -26" stroke="#3D8BFD" stroke-width="7" fill="none" stroke-linecap="round"/>
       <path d="M92 18 l-4 18 l18 -2z" fill="#3D8BFD"/>`,
    bank: () => `<path d="M8 40 L60 10 L112 40Z" fill="#5A67D8"/><rect x="12" y="40" width="96" height="8" fill="#434FB8"/>
       ${[22, 44, 66, 88].map(x => `<rect x="${x - 5}" y="50" width="10" height="46" fill="#E3E6F5"/>`).join('')}<rect x="8" y="96" width="104" height="12" fill="#434FB8"/>${coin(60, 28, 8)}`,
    corner: () => `<path d="M10 10 H58 V58 H110 V110 H10Z" fill="#6B7085"/><path d="M34 10 V84 H110" stroke="#fff" stroke-width="4" stroke-dasharray="8 8" fill="none"/>
       <circle cx="58" cy="58" r="14" fill="#FFD23F" stroke="#E0A100" stroke-width="3"/><rect x="62" y="16" width="44" height="36" rx="4" fill="#E9A66B"/>`,
    across: () => `<path d="M0 40 H120 M0 84 H120" stroke="#C5CBE0" stroke-width="4"/><rect x="0" y="44" width="120" height="36" fill="#6B7085"/>`
       + arrowTo(30, 104, 90, 20, '#E63946', 7),

    // ---------- ep52 transport (2) ----------
    airport: () => `<rect x="8" y="76" width="104" height="34" rx="4" fill="#C5CBE0"/><rect x="14" y="82" width="92" height="14" fill="#7FC8F8"/>
       <rect x="84" y="20" width="16" height="56" fill="#8A8FA3"/><rect x="76" y="14" width="32" height="16" rx="4" fill="#5A67D8"/><path d="M80 20 h24" stroke="#BDE7FF" stroke-width="4"/>`
       + `<g transform="translate(-10 -10) scale(.55)">${ART.plane()}</g>`,
    flight: () => `<path d="M10 100 C40 96 70 70 104 26" stroke="#8A8FA3" stroke-width="3" fill="none" stroke-dasharray="6 6"/>` + `<g transform="translate(46 0) scale(.6)">${ART.plane()}</g>`
       + `<circle cx="14" cy="100" r="7" fill="#E63946"/>`,
    arrive: () => `<path d="M8 96 H112" stroke="#C5CBE0" stroke-width="5"/>` + flagGoal(96, 30) + arrowTo(14, 74, 80, 74, '#2FA36B', 7) + check(26, 40, 1.2),
    narrowly: () => `<path d="M40 10 V110 M80 10 V110" stroke="#8A8FA3" stroke-width="10"/><path d="M50 60 H70" stroke="#FFD23F" stroke-width="10" stroke-linecap="round"/>`
       + `<path d="M22 50 l-8 10 l8 10 M98 50 l8 10 l-8 10" stroke="#E63946" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    drive: () => kid({s: .62, dx: -16, dy: -8, la: [80, 60], ra: [70, 50], shirt: '#3D8BFD'}) + `<circle cx="70" cy="58" r="22" fill="none" stroke="#2B2D42" stroke-width="7"/>
       <circle cx="70" cy="58" r="5" fill="#2B2D42"/><path d="M48 58 h44 M70 58 v22" stroke="#2B2D42" stroke-width="4"/>`,
    license: () => `<rect x="8" y="26" width="104" height="68" rx="8" fill="#BDE7FF" stroke="#3D8BFD" stroke-width="3"/><rect x="18" y="38" width="30" height="40" rx="4" fill="#fff"/>
       <circle cx="33" cy="52" r="8" fill="${SKIN[0]}"/><path d="M23 74 a10 8 0 0 1 20 0z" fill="#3D8BFD"/>${lines([46, 58, 70], 58, 44)}<text x="80" y="88" text-anchor="middle" font-size="9" ${FONT} fill="#3D8BFD">DRIVER LICENSE</text>`,
    wheel: () => `<circle cx="60" cy="60" r="48" fill="#2B2D42"/><circle cx="60" cy="60" r="30" fill="#C5CBE0"/><circle cx="60" cy="60" r="10" fill="#8A8FA3"/>
       ${[0, 72, 144, 216, 288].map(a => `<path d="M60 60 L60 32" stroke="#8A8FA3" stroke-width="6" transform="rotate(${a} 60 60)"/>`).join('')}`,
    taxi: () => ART.car().replace(/#E63946/g, '#FFD23F').replace('<rect x="104" y="64" width="6" height="6" rx="2" fill="#FFD23F"/>', '') + `<rect x="46" y="24" width="28" height="12" rx="3" fill="#2B2D42"/><text x="60" y="33" text-anchor="middle" font-size="9" ${FONT} fill="#FFD23F">TAXI</text>`,
    traffic: () => `<rect x="44" y="8" width="32" height="80" rx="10" fill="#2B2D42"/>${[['#E63946', 24], ['#FFB703', 48], ['#2FA36B', 72]].map(([c, y]) => `<circle cx="60" cy="${y}" r="10" fill="${c}"/>`).join('')}
       <rect x="56" y="88" width="8" height="24" fill="#2B2D42"/>` + `<g transform="translate(-14 58) scale(.42)">${ART.car()}</g><g transform="translate(70 62) scale(.4)">${ART.bus()}</g>`,
    station: () => `<rect x="10" y="44" width="100" height="56" fill="#F4E4C1"/><path d="M4 48 L60 18 L116 48Z" fill="#C1440E"/><circle cx="60" cy="34" r="8" fill="#fff"/>
       <path d="M60 30 v4 h3" stroke="${INK}" stroke-width="1.6" fill="none"/>${[24, 48, 72, 96].map(x => `<rect x="${x - 7}" y="60" width="14" height="22" rx="2" fill="#7FC8F8"/>`).join('')}
       <rect x="4" y="100" width="112" height="10" fill="#8A8FA3"/>`,
    railway: () => `<path d="M38 4 L14 116 M82 4 L106 116" stroke="#8A8FA3" stroke-width="6"/>${[14, 32, 52, 74, 98].map((y, i) => `<path d="M${36 - i * 4.5} ${y} H${84 + i * 4.5}" stroke="#8D5A3B" stroke-width="7"/>`).join('')}`,
    tunnel: () => `<path d="M0 116 V60 C0 20 40 8 60 8 C80 8 120 20 120 60 V116Z" fill="#8D7B68"/><path d="M24 116 V70 a36 36 0 0 1 72 0 V116Z" fill="#2B2D42"/>
       <path d="M0 116 H120" stroke="#6B7085" stroke-width="6"/>${[[16, 30], [100, 36], [30, 14]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="5" fill="#6B5B4B"/>`).join('')}<circle cx="60" cy="96" r="6" fill="#FFD23F"/>`,
    bridge: () => `<path d="M0 104 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/><path d="M4 70 H116" stroke="#C1440E" stroke-width="8"/>
       <path d="M10 70 C30 30 90 30 110 70" stroke="#E63946" stroke-width="6" fill="none"/>${[22, 38, 60, 82, 98].map(x => `<path d="M${x} 70 V${70 - Math.sin((x - 10) / 100 * Math.PI) * 30}" stroke="#E63946" stroke-width="3"/>`).join('')}
       <path d="M20 70 V104 M100 70 V104" stroke="#8D5A3B" stroke-width="8"/>`,

    // ---------- ep53 directions ----------
    find: () => `<circle cx="50" cy="50" r="28" fill="#E3F4FF" stroke="#3D8BFD" stroke-width="7"/><path d="M70 70 L100 100" stroke="#3D8BFD" stroke-width="10" stroke-linecap="round"/>` + star(50, 50, 13, 5.5, '#FFB703'),
    way: () => `<path d="M60 116 C60 80 30 70 34 46 C38 22 70 24 76 6" stroke="#C9934A" stroke-width="22" fill="none"/>
       <path d="M60 116 C60 80 30 70 34 46 C38 22 70 24 76 6" stroke="#fff" stroke-width="2.5" fill="none" stroke-dasharray="6 6"/>`,
    towards: () => `<path d="M10 66 H110" stroke="#C5CBE0" stroke-width="4" stroke-dasharray="6 6"/><circle cx="96" cy="66" r="14" fill="#E63946"/><circle cx="96" cy="66" r="6" fill="#fff"/>`
       + kid({s: .5, dx: -36, dy: 14, la: [-24, -8], ra: [26, 48], ll: [20, 8], rl: [-20, -36], shirt: '#3D8BFD'}) + arrowTo(40, 40, 76, 40, '#2FA36B'),
    turn: () => `<path d="M30 110 V60 a24 24 0 0 1 24 -24 H92" stroke="#3D8BFD" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M88 22 l20 14 l-20 14z" fill="#3D8BFD"/>`,
    left: () => `<rect x="56" y="60" width="8" height="52" fill="#8A8FA3"/><path d="M104 30 V74 H40 L14 52 L40 30Z" fill="#E63946"/>
       <text x="66" y="62" text-anchor="middle" font-size="22" ${FONT} fill="#fff">LEFT</text>`,
    rightdir: () => `<rect x="56" y="60" width="8" height="52" fill="#8A8FA3"/><path d="M16 30 V74 H80 L106 52 L80 30Z" fill="#3D8BFD"/>
       <text x="54" y="62" text-anchor="middle" font-size="20" ${FONT} fill="#fff">RIGHT</text>`,
    up: () => hand(60, 74, 1.5, 0, SKIN[0]) + arrowTo(98, 96, 98, 20, '#2FA36B'),
    down: () => hand(60, 46, 1.5, 180, SKIN[0]) + arrowTo(98, 20, 98, 96, '#FF9F1C'),
    over: () => `<path d="M0 104 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/><path d="M14 80 C30 50 90 50 106 80" stroke="#B5703F" stroke-width="8" fill="none"/>`
       + `<path d="M14 54 C34 10 86 10 106 54" stroke="#E63946" stroke-width="4" fill="none" stroke-dasharray="6 5"/><path d="M98 44 l8 10 l-12 2z" fill="#E63946"/>`,
    through: () => `<path d="M0 116 V64 a40 40 0 0 1 120 0 V116Z" fill="#8D7B68"/><path d="M28 116 V74 a32 32 0 0 1 64 0 V116Z" fill="#2B2D42"/>` + arrowTo(4, 96, 116, 96, '#FFD23F', 7),
    along: () => `<rect x="0" y="70" width="120" height="30" fill="#6B7085"/><path d="M0 85 H120" stroke="#fff" stroke-width="3" stroke-dasharray="10 8"/>`
       + kid({s: .44, dx: -26, dy: 2, la: [-24, -8], ra: [26, 48], ll: [20, 8], rl: [-20, -36], shirt: '#E63946'}) + arrowTo(30, 58, 110, 58, '#2FA36B'),
    into: () => `<rect x="62" y="40" width="50" height="70" fill="#FFE8C2"/><path d="M56 44 L87 18 L118 44Z" fill="#C1440E"/><rect x="74" y="70" width="22" height="40" fill="#2B2D42"/>` + arrowTo(8, 90, 80, 90, '#2FA36B', 7),

    // ---------- ep54 animal traits ----------
    size: () => `<rect x="10" y="70" width="28" height="28" rx="4" fill="#FF9F1C"/><rect x="46" y="48" width="40" height="50" rx="5" fill="#3D8BFD"/><rect x="94" y="84" width="16" height="14" rx="3" fill="#2FA36B"/>
       <path d="M6 106 H114" stroke="#8A8FA3" stroke-width="3"/><text x="66" y="40" text-anchor="middle" font-size="13" ${FONT} fill="#8A8FA3">S M L</text>`,
    big: () => ART.elephant(),
    small: () => `<g transform="translate(26 26) scale(.55)">${ART.mouse()}</g>` + `<path d="M10 104 H110" stroke="#C5CBE0" stroke-width="3"/>`,
    brave: () => figure('boy', {shirt: '#E63946'}) + `<path d="M24 66 L10 112 L46 92Z M96 66 L110 112 L74 92Z" fill="#E63946" opacity=".75"/>` + star(60, 92, 10, 4, '#FFD23F'),
    cute: () => `<circle cx="60" cy="62" r="44" fill="#FFB3C6"/><circle cx="26" cy="28" r="14" fill="#FFB3C6"/><circle cx="94" cy="28" r="14" fill="#FFB3C6"/>
       <circle cx="44" cy="58" r="9" fill="${INK}"/><circle cx="76" cy="58" r="9" fill="${INK}"/><circle cx="47" cy="54" r="3.5" fill="#fff"/><circle cx="79" cy="54" r="3.5" fill="#fff"/>
       <path d="M52 76 q8 8 16 0" stroke="${INK}" stroke-width="3" fill="none"/><ellipse cx="32" cy="74" rx="7" ry="4" fill="#FF6F91"/><ellipse cx="88" cy="74" rx="7" ry="4" fill="#FF6F91"/>`,
    funny: () => emo('#FFD23F', `<path d="M34 50 l14 6 l-14 6 M86 50 l-14 6 l14 6" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`,
       `<path d="M34 74 h52 q-4 24 -26 24 q-22 0 -26 -24z" fill="#9D0208"/>`, `<path d="M24 40 q-8 10 0 16 q8 -6 0 -16z M96 40 q8 10 0 16 q-8 -6 0 -16z" fill="#7FC8F8"/>`),
    humorous: () => `<circle cx="60" cy="60" r="44" fill="#FFD23F"/><path d="M28 44 q10 -8 20 0 M72 44 q10 -8 20 0" stroke="${INK}" stroke-width="4" fill="none"/>
       <circle cx="60" cy="66" r="9" fill="#E63946"/><path d="M40 60 q-18 0 -22 -10 M80 60 q18 0 22 -10" stroke="#2B2D42" stroke-width="5" fill="none" stroke-linecap="round"/>
       <path d="M44 84 q16 12 32 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
    smart: () => ART.monkey() + `<path d="M28 26 h64 l-32 -16z" fill="#2B2D42"/><rect x="40" y="24" width="40" height="8" fill="#2B2D42"/><path d="M92 26 v14" stroke="#FFD23F" stroke-width="3"/>`,
    stupid: () => ART.pig() + `<path d="M88 14 q8 -6 14 0 t14 0" stroke="#8A8FA3" stroke-width="3" fill="none"/><text x="104" y="40" font-size="18" ${FONT} fill="#8A8FA3">?</text>`,
    silly: () => emo('#B9E28C', `<circle cx="44" cy="52" r="8" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="76" cy="52" r="6" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="46" cy="54" r="3" fill="${INK}"/><circle cx="74" cy="50" r="2.5" fill="${INK}"/>`,
       `<path d="M40 74 q20 14 40 0" stroke="${INK}" stroke-width="4" fill="none"/><path d="M58 80 q4 14 10 0" fill="#FF6FA5"/>`),
    though: () => `<path d="M14 60 C30 30 46 30 60 60 C74 90 90 90 106 60" stroke="#8A8FA3" stroke-width="6" fill="none" stroke-linecap="round"/>`
       + `<text x="60" y="108" text-anchor="middle" font-size="15" ${FONT} fill="#8A8FA3">不过…</text>`,

    // ---------- ep55 exams ----------
    exam: () => paper(lines([30, 44, 58, 72, 86]) + `<text x="88" y="104" text-anchor="end" font-size="20" ${FONT} fill="#E63946">95</text>`) + pencil(102, 70, .9, 30),
    examination: () => `<rect x="10" y="20" width="100" height="74" rx="4" fill="#2F6B4F" stroke="#8D5A3B" stroke-width="5"/><text x="60" y="64" text-anchor="middle" font-size="20" ${FONT} fill="#fff">EXAM</text>`
       + clockF(96, 92, 16, 10, 10, {rim: '#E63946'}),
    start: () => `<path d="M8 100 H112" stroke="#C5CBE0" stroke-width="4"/>` + flagGoal(24, 30, '#2FA36B') + arrowTo(40, 80, 104, 80, '#2FA36B', 7) + `<text x="70" y="60" text-anchor="middle" font-size="16" ${FONT} fill="#2FA36B">GO!</text>`,
    finish: () => `<path d="M8 100 H112" stroke="#C5CBE0" stroke-width="4"/>` + flagGoal(90, 30) + arrowTo(10, 80, 76, 80, '#E63946', 7),
    know: () => `<circle cx="60" cy="60" r="44" fill="#FFF3C4"/>` + mini('inspiration', 60, 54, .66) + check(96, 96, 1.2),
    test: () => paper(`<text x="60" y="34" text-anchor="middle" font-size="14" ${FONT} fill="#3D8BFD">TEST</text>
       ${[50, 68, 86].map((y, i) => `<circle cx="36" cy="${y}" r="5" fill="none" stroke="#8A8FA3" stroke-width="2"/><path d="M48 ${y} h40" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/>${i === 1 ? `<circle cx="36" cy="${y}" r="3" fill="#3D8BFD"/>` : ''}`).join('')}`),
    level: () => [0, 1, 2, 3].map(i => `<rect x="${14 + i * 24}" y="${86 - i * 20}" width="20" height="${24 + i * 20}" rx="3" fill="${['#C5CBE0', '#7FC8F8', '#3D8BFD', '#2A6FD6'][i]}"/>`).join('') + star(98, 22, 10, 4, '#FFD23F'),
    gradeA: () => `<circle cx="60" cy="60" r="46" fill="#fff" stroke="#E63946" stroke-width="6"/><text x="56" y="82" text-anchor="middle" font-size="64" ${FONT} fill="#E63946">A</text>
       <text x="88" y="52" text-anchor="middle" font-size="28" ${FONT} fill="#E63946">+</text>`,
    preparation: () => `<g transform="translate(6 30) scale(.55)">${ART.book()}</g>` + pencil(96, 60, 1, 20) + `<g transform="translate(56 54) scale(.4)">${ART.ruler()}</g>` + check(36, 22, 1),
    question: () => `<circle cx="60" cy="60" r="44" fill="#7FC8F8"/><text x="60" y="84" text-anchor="middle" font-size="68" ${FONT} fill="#fff">?</text>`,
    answer: () => `<circle cx="60" cy="60" r="44" fill="#2FA36B"/><text x="60" y="82" text-anchor="middle" font-size="64" ${FONT} fill="#fff">!</text>`,
    guess: () => `<g transform="translate(-14 22) scale(.86)">${figure('child', {shirt: '#FF9F1C'})}</g>` + thought(84, 30, 56, 44, `<text x="0" y="12" text-anchor="middle" font-size="30" ${FONT} fill="#8A8FA3">?!</text>`),
    rightok: () => `<circle cx="60" cy="60" r="46" fill="#2FA36B"/>` + check(60, 62, 3, '#fff'),
    wrong: () => `<circle cx="60" cy="60" r="46" fill="#E63946"/><path d="M40 40 L80 80 M80 40 L40 80" stroke="#fff" stroke-width="12" stroke-linecap="round"/>`,
    correct: () => paper(`<path d="M34 40 h40" stroke="#C5CBE0" stroke-width="4" stroke-linecap="round"/><path d="M30 34 l48 12" stroke="#E63946" stroke-width="4"/>
       <path d="M34 64 h40" stroke="#2FA36B" stroke-width="5" stroke-linecap="round"/>${check(84, 64, .8)}${lines([86])}`) + pencil(102, 84, .9, 30),
  });

  const face2 = (x, y, r, skin, mouth, eyes, hair = '#3B2A20') => `<circle cx="${x}" cy="${y}" r="${r}" fill="${skin}"/>` + cap(x, y, r, hair) + (eyes || `<circle cx="${x - r * .38}" cy="${y + r * .05}" r="${r * .1}" fill="${INK}"/><circle cx="${x + r * .38}" cy="${y + r * .05}" r="${r * .1}" fill="${INK}"/>`) + mouth;
  const MON = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'];
  const MONC = ['#3D8BFD', '#E63946', '#2FA36B', '#FF6FA5', '#6CCB5F', '#FFB703', '#FF7A3D', '#E0A100', '#C1440E', '#9B5DE5', '#8D5A3B', '#2BB3A3'];
  const MONART = [
    (x, y) => flake(x, y, 9, '#7FC8F8'), (x, y) => heart(x, y, .55, '#E63946'), (x, y) => `<path d="M${x} ${y + 8} v-12" stroke="#3FA34D" stroke-width="3"/><circle cx="${x}" cy="${y - 6}" r="5" fill="#FF8FAB"/>`,
    (x, y) => drops([[x - 6, y - 4], [x + 6, y]], '#3D8BFD'), (x, y) => `<circle cx="${x}" cy="${y}" r="7" fill="#FFD23F"/>${[0, 72, 144, 216, 288].map(a => `<circle cx="${x + 9 * Math.cos(a * Math.PI / 180)}" cy="${y + 9 * Math.sin(a * Math.PI / 180)}" r="5" fill="#FF6FA5"/>`).join('')}`,
    (x, y) => sun(x, y, 7), (x, y) => `<path d="M${x - 10} ${y + 6} q10 -14 20 0" fill="#FF7A3D"/><path d="M${x} ${y - 8} v8" stroke="#8A8FA3" stroke-width="2"/>`,
    (x, y) => `<path d="M${x - 12} ${y + 4} q6 -6 12 0 t12 0" stroke="#4CC9F0" stroke-width="4" fill="none"/>`, (x, y) => `<rect x="${x - 9}" y="${y - 8}" width="18" height="14" rx="2" fill="#E63946"/><path d="M${x - 5} ${y - 8} v-4 h10 v4" stroke="#E63946" stroke-width="2" fill="none"/>`,
    (x, y) => `<path d="M${x - 9} ${y + 8} C${x - 9} ${y - 4} ${x + 9} ${y - 4} ${x + 9} ${y + 8}Z" fill="#FF7A3D"/><path d="M${x} ${y - 2} v-6" stroke="#3FA34D" stroke-width="3"/>`,
    (x, y) => `<path d="M${x - 8} ${y + 8} c-6 -10 4 -18 8 -10 c4 -8 14 0 8 10z" fill="#C1440E"/>`, (x, y) => `<path d="M${x} ${y - 12} L${x - 10} ${y + 8} H${x + 10}Z" fill="#2FA36B"/>${star(x, y - 12, 4, 1.8, '#FFD23F')}`,
  ];
  const monthArt = (i) => `<rect x="16" y="14" width="88" height="94" rx="10" fill="#fff" stroke="#E3E6F5" stroke-width="3"/>
      <path d="M16 24 a10 10 0 0 1 10 -10 h68 a10 10 0 0 1 10 10 v14 h-88z" fill="${MONC[i]}"/>
      <rect x="36" y="6" width="6" height="16" rx="3" fill="#8A8FA3"/><rect x="78" y="6" width="6" height="16" rx="3" fill="#8A8FA3"/>
      <text x="60" y="33" text-anchor="middle" font-size="15" ${FONT} fill="#fff">${MON[i]}</text>
      <text x="44" y="82" text-anchor="middle" font-size="34" ${FONT} fill="${INK}">${i + 1}</text>${MONART[i](84, 70)}
      <text x="60" y="102" text-anchor="middle" font-size="12" ${FONT} fill="#8A8FA3">${i + 1}月</text>`;
  const ordArt = (k) => { const suf = k === 1 ? 'st' : k === 2 ? 'nd' : k === 3 ? 'rd' : 'th', c = NUMC[k - 1];
    return `<path d="M60 8 L72 30 H96 L78 46 L86 72 L60 56 L34 72 L42 46 L24 30 H48Z" fill="${k <= 3 ? ['#FFD23F', '#C5CBE0', '#E9A66B'][k - 1] : c}" opacity="${k <= 3 ? 1 : .25}"/>
      <text x="${k === 10 ? 52 : 56}" y="104" text-anchor="middle" font-size="${k === 10 ? 46 : 54}" ${FONT} fill="${c}" stroke="#fff" stroke-width="4" paint-order="stroke">${k}</text>
      <text x="${k === 10 ? 92 : 84}" y="80" text-anchor="middle" font-size="22" ${FONT} fill="${c}">${suf}</text>`; };
  Object.assign(ART,
    Object.fromEntries(MON.map((m, i) => [['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'][i], () => monthArt(i)])),
    Object.fromEntries(Array.from({length: 10}, (_, i) => ['ord' + (i + 1), () => ordArt(i + 1)])), {
    // ---------- ep56 holiday ----------
    holiday: () => calPage('HOLIDAY', '', '#E63946') + star(60, 74, 20, 8, '#FFD23F') + star(32, 92, 6, 2.5, '#FF6FA5') + star(90, 90, 7, 3, '#3D8BFD'),
    general: () => [0, 1, 2, 3, 4, 5, 6, 7, 8].map(i => `<circle cx="${28 + (i % 3) * 32}" cy="${30 + Math.floor(i / 3) * 30}" r="11" fill="#C5CBE0"/>`).join('')
       + `<text x="60" y="116" text-anchor="middle" font-size="13" ${FONT} fill="#8A8FA3">一般的</text>`,
    relaxing: () => `<path d="M8 96 H112" stroke="#E9C46A" stroke-width="10" stroke-linecap="round"/><path d="M24 92 L40 56 H96 L88 92" fill="#2BB3A3"/><path d="M40 56 L56 30 L104 30 L96 56" fill="#45C9B8"/>`
       + `<circle cx="66" cy="22" r="10" fill="${SKIN[0]}"/><path d="M50 18 h32" stroke="#2B2D42" stroke-width="5"/>` + sun(102, 14, 8),
    trip: () => `<rect x="30" y="34" width="60" height="68" rx="8" fill="#FF7A59"/><path d="M48 34 V24 a6 6 0 0 1 6 -6 h12 a6 6 0 0 1 6 6 V34" stroke="#C1440E" stroke-width="6" fill="none"/>
       <path d="M30 56 h60 M30 80 h60" stroke="#C1440E" stroke-width="4"/><circle cx="42" cy="106" r="5" fill="#2B2D42"/><circle cx="78" cy="106" r="5" fill="#2B2D42"/>
       <rect x="38" y="62" width="18" height="10" rx="2" fill="#FFD23F"/>`,
    away: () => `<rect x="62" y="44" width="48" height="60" fill="#FFE8C2"/><path d="M56 48 L86 22 L116 48Z" fill="#C1440E"/><rect x="78" y="72" width="16" height="32" fill="#8D5A3B"/>`
       + kid({s: .5, dx: -36, dy: 22, rot: -6, la: [24, 48], ra: [-24, -8], ll: [-20, -36], rl: [20, 8], shirt: '#3D8BFD'}) + arrowTo(52, 40, 12, 40, '#FF9F1C'),
    picnic: () => `<path d="M8 82 L60 64 L112 82 L60 104Z" fill="#E63946"/><path d="M34 73 L86 95 M86 73 L34 95" stroke="#fff" stroke-width="5"/>`
       + `<g transform="translate(38 20) scale(.4)">${ART.basket()}</g><circle cx="88" cy="68" r="7" fill="#E63946"/><circle cx="30" cy="74" r="7" fill="#FFB703"/>` + sun(100, 18, 9),
    suppose: () => `<g transform="translate(-16 22) scale(.84)">${figure('girl', {shirt: '#9B5DE5'})}</g>` + thought(84, 30, 56, 44, `<path d="M-10 10 l8 -18 l8 18z" fill="#2FA36B"/>${sun(12, -8, 5)}`)
       + `<text x="102" y="68" font-size="18" ${FONT} fill="#8A8FA3">?</text>`,
    festival: () => [[30, '#E63946'], [60, '#FFB703'], [90, '#E63946']].map(([x, c], i) => `<path d="M${x} ${10 + i % 2 * 8} V${20 + i % 2 * 8}" stroke="#8A8FA3" stroke-width="2"/>
         <ellipse cx="${x}" cy="${40 + i % 2 * 8}" rx="16" ry="20" fill="${c}"/><rect x="${x - 10}" y="${18 + i % 2 * 8}" width="20" height="4" fill="#C77800"/><rect x="${x - 10}" y="${58 + i % 2 * 8}" width="20" height="4" fill="#C77800"/>
         <path d="M${x} ${62 + i % 2 * 8} v14" stroke="#FFD23F" stroke-width="3"/>`).join('') + `<path d="M4 104 h112" stroke="#C5CBE0" stroke-width="4"/>${star(60, 96, 6, 2.5, '#FFD23F')}`,
    during: () => `<path d="M10 70 H110" stroke="#C5CBE0" stroke-width="5"/><rect x="34" y="56" width="52" height="28" rx="6" fill="#FFB703" opacity=".7"/>
       <path d="M34 50 v40 M86 50 v40" stroke="#E0A100" stroke-width="4"/>` + kid({s: .36, dy: -16, la: [-150, -160], ra: [150, 160], shirt: '#E63946'})
       + `<text x="60" y="112" text-anchor="middle" font-size="13" ${FONT} fill="#8A8FA3">在…期间</text>`,
    visit: () => `<rect x="70" y="14" width="44" height="98" rx="4" fill="#B5703F"/><rect x="76" y="20" width="32" height="92" fill="#FFF3C4"/>`
       + person('woman', {shirt: '#9B5DE5'}, 48, 20, .7) + person('man', {shirt: '#3D8BFD'}, -14, 20, .8) + `<g transform="translate(20 72) scale(.35)">${gift(0, 0, 60, 60, '#FF6FA5')}</g>`,
    visitor: () => ART.visit() + `<circle cx="20" cy="40" r="22" fill="none" stroke="#E63946" stroke-width="4"/>`,
    come: () => person('child', {shirt: '#2FA36B'}, 30, 20, .8) + arrowTo(4, 70, 34, 70, '#2FA36B') + `<text x="18" y="104" text-anchor="middle" font-size="12" ${FONT} fill="#2FA36B">came</text>`,
    together: () => [[-20, '#E63946', 0], [12, '#3D8BFD', 1], [44, '#FFB703', 2]].map(([dx, c, i]) => person(['girl', 'boy', 'child'][i], {shirt: c, skin: SKIN[i]}, dx, 20, .76)).join('')
       + heart(60, 16, .7, '#FF4D6D'),

    // ---------- ep57 travel ----------
    vacation: () => sun(90, 26, 14) + `<path d="M0 82 q15 -8 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/><path d="M0 100 H120 V120 H0Z" fill="#FFE08A"/>`
       + `<path d="M36 100 V52" stroke="#8D5A3B" stroke-width="5"/>${[[-30], [0], [30], [60], [90]].map(([a]) => `<path d="M36 52 q${24 * Math.cos(a * Math.PI / 180)} ${-6 - 10 * Math.sin(a * Math.PI / 180)} ${30 * Math.cos(a * Math.PI / 180)} ${12}" stroke="#3FA34D" stroke-width="6" fill="none" stroke-linecap="round"/>`).join('')}`,
    travel: () => `<circle cx="60" cy="60" r="44" fill="#7FC8F8"/><path d="M36 30 q14 -4 18 10 q-4 12 6 18 q10 8 0 18 q-14 4 -18 -10 q-12 -6 -8 -22z" fill="#6CCB5F"/>
       <path d="M74 26 q14 2 18 14 q-6 4 -14 0 z M82 70 q12 0 14 12 q-10 10 -18 0z" fill="#6CCB5F"/>` + `<g transform="translate(60 -6) scale(.4)">${ART.plane()}</g>`,
    agent: () => figure('man', {shirt: '#2E5AAC'}) + `<rect x="74" y="80" width="34" height="24" rx="3" fill="#fff" stroke="#C5CBE0" stroke-width="2"/>${lines([88, 96], 80, 22)}`
       + `<g transform="translate(78 10) scale(.3)">${ART.travel()}</g>`,
    tour: () => `<g transform="translate(-4 16) scale(.62)">${ART.bus()}</g>` + `<path d="M74 14 L74 70" stroke="#8A8FA3" stroke-width="3"/><path d="M74 14 h34 l-6 10 l6 10 h-34z" fill="#E63946"/>`
       + `<path d="M10 104 Q40 84 60 100 T110 96" stroke="#C9934A" stroke-width="4" fill="none" stroke-dasharray="6 5"/>`,
    guide: () => figure('woman', {shirt: '#FF9F1C', cap: '#2FA36B'}) + `<path d="M86 52 L104 42 V70 L86 60Z" fill="#E63946"/><rect x="80" y="52" width="8" height="10" rx="2" fill="#8A8FA3"/>`
       + `<path d="M108 48 q6 8 0 16" stroke="#E63946" stroke-width="3" fill="none"/>`,
    palace: () => `<rect x="8" y="64" width="104" height="44" fill="#E63946"/><path d="M2 66 Q60 40 118 66Z" fill="#FFB703"/><path d="M22 46 Q60 20 98 46 L94 54 H26Z" fill="#FFB703"/>
       <path d="M30 34 Q60 6 90 34 Z" fill="#E0A100"/>${[20, 40, 80, 100].map(x => `<rect x="${x - 4}" y="70" width="8" height="38" fill="#C1121F"/>`).join('')}<rect x="50" y="78" width="20" height="30" fill="#8D5A3B"/>
       <rect x="4" y="106" width="112" height="6" fill="#C5CBE0"/>`,
    museum: () => `<path d="M8 40 L60 12 L112 40Z" fill="#C5CBE0"/><rect x="12" y="40" width="96" height="8" fill="#8A8FA3"/>
       ${[24, 44, 64, 84, 100].map(x => `<rect x="${x - 5}" y="50" width="10" height="46" fill="#E3E6F5"/>`).join('')}<rect x="8" y="96" width="104" height="12" fill="#8A8FA3"/>
       <path d="M52 30 l8 -8 l8 8 l-8 8z" fill="#FFD23F"/>`,
    tower: () => `<path d="M48 112 L54 30 H66 L72 112Z" fill="#C9C1B5"/><rect x="46" y="30" width="28" height="10" fill="#8A8FA3"/><path d="M50 30 L60 6 L70 30Z" fill="#5A67D8"/>
       <circle cx="60" cy="54" r="8" fill="#fff" stroke="#8A8FA3" stroke-width="2"/>${[72, 90].map(y => `<rect x="56" y="${y}" width="8" height="10" rx="2" fill="#7FC8F8"/>`).join('')}
       <path d="M60 6 V0" stroke="#E63946" stroke-width="2"/>`,
    passport: () => `<rect x="24" y="10" width="72" height="100" rx="8" fill="#1F3E7A"/><circle cx="60" cy="52" r="20" fill="none" stroke="#FFD23F" stroke-width="3"/>
       <path d="M40 52 h40 M60 32 v40 M44 40 q16 8 32 0 M44 64 q16 -8 32 0" stroke="#FFD23F" stroke-width="2" fill="none"/>
       <text x="60" y="94" text-anchor="middle" font-size="12" ${FONT} fill="#FFD23F">PASSPORT</text>`,
    hotel: () => `<rect x="20" y="12" width="80" height="100" fill="#5A67D8"/><rect x="34" y="4" width="52" height="14" rx="3" fill="#E63946"/>
       <text x="60" y="15" text-anchor="middle" font-size="10" ${FONT} fill="#fff">HOTEL</text>
       ${[0, 1, 2, 3].map(r => [0, 1, 2].map(c => `<rect x="${30 + c * 22}" y="${26 + r * 18}" width="14" height="12" rx="1.5" fill="${(r + c) % 2 ? '#FFD23F' : '#BDE7FF'}"/>`).join('')).join('')}
       <rect x="50" y="96" width="20" height="16" fill="#2B2D42"/>`,
    island: () => `<path d="M0 84 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/><ellipse cx="60" cy="86" rx="42" ry="12" fill="#FFE08A"/>
       <path d="M58 86 C58 66 62 52 70 42" stroke="#8D5A3B" stroke-width="6" fill="none"/>${[[-40], [-10], [20], [60], [100]].map(([a]) => `<path d="M70 42 q${26 * Math.cos(a * Math.PI / 180)} ${-8 - 10 * Math.sin(a * Math.PI / 180)} ${32 * Math.cos(a * Math.PI / 180)} 12" stroke="#3FA34D" stroke-width="7" fill="none" stroke-linecap="round"/>`).join('')}`,
    beach: () => sun(98, 22, 11) + `<path d="M0 62 q15 -6 30 0 t30 0 t30 0 t30 0 V80 H0Z" fill="#4CC9F0"/><path d="M0 78 H120 V120 H0Z" fill="#FFE08A"/>
       <path d="M30 108 V74" stroke="#8A8FA3" stroke-width="3"/><path d="M8 78 Q30 54 52 78Z" fill="#E63946"/><path d="M19 78 Q30 62 41 78Z" fill="#fff"/>
       <path d="M80 100 l6 -10 l6 10z" fill="#FF8FAB"/><circle cx="96" cy="104" r="5" fill="#FFB703"/>`,
    map: () => `<path d="M8 22 L40 12 L80 24 L112 14 V98 L80 108 L40 96 L8 106Z" fill="#FFF3C4" stroke="#E0A100" stroke-width="3" stroke-linejoin="round"/>
       <path d="M40 12 V96 M80 24 V108" stroke="#E0A100" stroke-width="2"/><path d="M20 80 C34 60 50 74 62 56 S90 40 98 30" stroke="#E63946" stroke-width="3" fill="none" stroke-dasharray="5 4"/>
       <path d="M92 26 l12 12 M104 26 l-12 12" stroke="#E63946" stroke-width="4"/>`,

    // ---------- ep58 feelings (2) ----------
    enjoy: () => `<path d="M0 90 q15 -6 30 0 t30 0 t30 0 t30 0 V120 H0Z" fill="#4CC9F0"/><ellipse cx="60" cy="88" rx="40" ry="14" fill="#FF6FA5"/><ellipse cx="60" cy="86" rx="24" ry="7" fill="#4CC9F0"/>`
       + face2(60, 54, 18, SKIN[0], `<path d="M50 60 q10 8 20 0" stroke="${INK}" stroke-width="3" fill="none"/>`, `<rect x="44" y="48" width="32" height="8" rx="4" fill="#2B2D42"/>`) + sun(100, 18, 9),
    comfortable: () => `<rect x="10" y="56" width="100" height="44" rx="14" fill="#9B5DE5"/><rect x="18" y="40" width="84" height="30" rx="12" fill="#B07CEB"/>
       <rect x="8" y="54" width="16" height="44" rx="8" fill="#7B3FC4"/><rect x="96" y="54" width="16" height="44" rx="8" fill="#7B3FC4"/>`
       + face2(56, 46, 14, SKIN[0], `<path d="M50 52 q6 4 12 0" stroke="${INK}" stroke-width="2.5" fill="none"/>`, `<path d="M46 46 q4 -3 8 0 M58 46 q4 -3 8 0" stroke="${INK}" stroke-width="2.5" fill="none"/>`)
       + `<text x="92" y="32" font-size="14" ${FONT} fill="#8A8FA3">z</text>`,
    pleasant: () => emo('#FFD23F', `<path d="M36 52 q8 -8 16 0 M68 52 q8 -8 16 0" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
       `<path d="M40 70 q20 18 40 0" stroke="${INK}" stroke-width="4.5" fill="none"/>`, star(18, 24, 7, 3, '#FF9F1C') + star(102, 22, 8, 3.4, '#FF9F1C')),
    happiness: () => person('woman', {shirt: '#FF6FA5'}, -16, 18, .84) + person('child', {shirt: '#FFB703'}, 34, 34, .7) + heart(60, 20, .8, '#FF4D6D') + star(22, 20, 6, 2.5, '#FFD23F'),
    unhappiness: () => emo('#B8BFCC', `<path d="M36 50 q8 4 16 -2 M68 48 q8 6 16 2" stroke="${INK}" stroke-width="4" fill="none" stroke-linecap="round"/>`,
       `<path d="M42 88 q18 -12 36 0" stroke="${INK}" stroke-width="4.5" fill="none"/>`, cloud(98, 20, .4, '#8A8FA3', '#6B7085')),
    miss: () => `<g transform="translate(-16 22) scale(.84)">${figure('girl', {shirt: '#3D8BFD'})}</g>` + thought(84, 30, 56, 44, `${heart(0, 2, .7, '#FF4D6D')}`)
       + `<path d="M28 66 q-4 8 0 10 q4 -2 0 -10z" fill="#7FC8F8"/>`,
    separate: () => person('boy', {shirt: '#3D8BFD'}, -24, 20, .76) + person('girl', {shirt: '#FF6FA5'}, 48, 20, .76)
       + arrowTo(52, 50, 30, 50, '#8A8FA3', 4) + arrowTo(68, 50, 90, 50, '#8A8FA3', 4) + `<path d="M60 30 V100" stroke="#C5CBE0" stroke-width="3" stroke-dasharray="5 5"/>`,
    shame: () => face2(60, 56, 40, SKIN[0], `<path d="M50 80 q10 -4 20 0" stroke="${INK}" stroke-width="3" fill="none"/>`, `<path d="M40 58 q6 4 12 0 M68 58 q6 4 12 0" stroke="${INK}" stroke-width="3.5" fill="none"/>`)
       + `<ellipse cx="34" cy="72" rx="10" ry="6" fill="#FF6F91"/><ellipse cx="86" cy="72" rx="10" ry="6" fill="#FF6F91"/>` + hand(30, 108, .55, 30, SKIN[0]) + `<g transform="translate(120 0) scale(-1 1)">${hand(30, 108, .55, 30, SKIN[0])}</g>`,
    regret: () => face2(60, 56, 40, SKIN[1], `<path d="M46 84 q14 -10 28 0" stroke="${INK}" stroke-width="3.5" fill="none"/>`, `<path d="M38 52 l12 4 M82 52 l-12 4" stroke="${INK}" stroke-width="3.5"/>` + `<circle cx="45" cy="62" r="3.5" fill="${INK}"/><circle cx="75" cy="62" r="3.5" fill="${INK}"/>`)
       + hand(82, 40, .55, -150, SKIN[1]) + `<text x="16" y="28" font-size="20" ${FONT} fill="#8A8FA3">…</text>`,
    pity: () => person('child', {shirt: '#8A8FA3'}, -16, 20, .84) + `<g transform="translate(66 60) scale(.42)">${ART.dog()}</g>` + drops([[86, 50]], '#7FC8F8') + heart(98, 28, .5, '#FF8FAB'),
    hate: () => emo('#E63946', `<path d="M34 44 l16 8 M86 44 l-16 8" stroke="${INK}" stroke-width="5" stroke-linecap="round"/><circle cx="44" cy="60" r="4" fill="${INK}"/><circle cx="76" cy="60" r="4" fill="${INK}"/>`,
       `<path d="M40 88 h40" stroke="${INK}" stroke-width="5" stroke-linecap="round"/>`, `<path d="M96 14 l-6 10 l10 -2 l-6 10" stroke="#9D0208" stroke-width="4" fill="none"/>`),

    // ---------- ep59 order ----------
    order: () => [1, 2, 3].map((n, i) => `<rect x="${12 + i * 36}" y="${80 - i * 24}" width="30" height="${30 + i * 24}" rx="4" fill="${['#E9A66B', '#C5CBE0', '#FFD23F'][2 - i]}"/>
         <text x="${27 + i * 36}" y="${102 - i * 12}" text-anchor="middle" font-size="18" ${FONT} fill="#fff">${3 - i}</text>`).join('') + arrowTo(10, 22, 70, 22, '#3D8BFD', 4),
    next: () => [0, 1, 2].map(i => `<circle cx="${24 + i * 36}" cy="60" r="14" fill="${i === 1 ? '#2FA36B' : '#E3E6F5'}"/>`).join('') + arrowTo(24, 32, 60, 32, '#2FA36B', 4)
       + `<text x="60" y="104" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">下一个</text>`,
    last: () => [0, 1, 2, 3].map(i => `<circle cx="${18 + i * 28}" cy="60" r="11" fill="${i === 3 ? '#E63946' : '#E3E6F5'}"/>`).join('') + flagGoal(100, 22)
       + `<text x="60" y="104" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">最后</text>`,

    // ---------- ep60 months ----------
    month: () => `<rect x="12" y="14" width="96" height="94" rx="10" fill="#fff" stroke="#E3E6F5" stroke-width="3"/><path d="M12 24 a10 10 0 0 1 10 -10 h76 a10 10 0 0 1 10 10 v12 h-96z" fill="#5A67D8"/>
       ${Array.from({length: 20}, (_, i) => `<rect x="${20 + (i % 5) * 17}" y="${44 + Math.floor(i / 5) * 15}" width="12" height="10" rx="2" fill="${i === 12 ? '#E63946' : '#E3E6F5'}"/>`).join('')}`,
    date: () => calPage('DATE', '10', '#E63946') + `<circle cx="60" cy="72" r="24" fill="none" stroke="#2FA36B" stroke-width="4"/>`,
    inmonth: () => `<rect x="10" y="30" width="100" height="60" rx="10" fill="#E3E6F5"/><rect x="30" y="40" width="60" height="40" rx="6" fill="#5A67D8"/>
       <text x="60" y="66" text-anchor="middle" font-size="16" ${FONT} fill="#fff">MAY</text><text x="60" y="112" text-anchor="middle" font-size="14" ${FONT} fill="#8A8FA3">in …</text>`,
  });

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

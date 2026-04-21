// Binary clock — 6 columns (H1 H2 : M1 M2 : S1 S2)
// Each column = 4 bits (rows), MSB on top

const COLS = [
  { id: 'h1', max: 2, cls: 'col-h' },   // hours tens   (0-2)
  { id: 'h2', max: 9, cls: 'col-h' },   // hours units  (0-9)
  { id: 'm1', max: 5, cls: 'col-m' },   // minutes tens (0-5)
  { id: 'm2', max: 9, cls: 'col-m' },   // minutes units
  { id: 's1', max: 5, cls: 'col-s' },   // seconds tens
  { id: 's2', max: 9, cls: 'col-s' },   // seconds units
];
const BITS = 4;  // rows per column

const grid = document.getElementById('clock-grid');
const timeText = document.getElementById('time-text');

// Build DOM once
const bitEls = {};
COLS.forEach((col, idx) => {
  if (idx === 2 || idx === 4) {
    const sep = document.createElement('div');
    sep.className = 'separator';
    grid.appendChild(sep);
  }
  const colEl = document.createElement('div');
  colEl.className = `digit-col ${col.cls}`;
  bitEls[col.id] = [];
  for (let b = BITS - 1; b >= 0; b--) {
    const bit = document.createElement('div');
    bit.className = 'bit';
    bit.dataset.bit = b;
    colEl.appendChild(bit);
    bitEls[col.id].push(bit);
  }
  grid.appendChild(colEl);
});

function updateClock() {
  const now = new Date();
  const h = now.getHours();
  const m = now.getMinutes();
  const s = now.getSeconds();

  const vals = {
    h1: Math.floor(h / 10), h2: h % 10,
    m1: Math.floor(m / 10), m2: m % 10,
    s1: Math.floor(s / 10), s2: s % 10,
  };

  COLS.forEach(col => {
    const v = vals[col.id];
    bitEls[col.id].forEach((el, i) => {
      // i=0 is top (MSB = bit 3), i=3 is bottom (LSB = bit 0)
      const bitPos = BITS - 1 - i;
      el.classList.toggle('on', !!(v & (1 << bitPos)));
    });
  });

  const pad = n => String(n).padStart(2, '0');
  timeText.textContent = `${pad(h)}:${pad(m)}:${pad(s)}`;
}

updateClock();
setInterval(updateClock, 1000);

// Fullscreen
document.getElementById('fs-btn').addEventListener('click', () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
});
document.addEventListener('keydown', e => {
    if (e.key === 'Escape') window.close();
});
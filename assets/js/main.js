// Fade sections in as they scroll into view
const io = new IntersectionObserver(es => es.forEach(e => e.isIntersecting && e.target.classList.add('in')), { threshold: .15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Typewriter effect for the tagline
const t = document.getElementById('typed');
if (t && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const text = t.dataset.text; t.textContent = ''; let i = 0;
  (function type() { if (i <= text.length) { t.textContent = text.slice(0, i++); setTimeout(type, 35); } })();
}

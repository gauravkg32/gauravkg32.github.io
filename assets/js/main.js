// Edgecraft Studio: interactions. Vanilla JS, no dependencies; respects prefers-reduced-motion.
(function () {
  'use strict';
  const root = document.documentElement;
  root.classList.add('js');

  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canHover = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));

  // Hero entrance: staggered fade-up once the page is ready
  requestAnimationFrame(() => requestAnimationFrame(() => root.classList.add('ready')));
  setTimeout(() => root.classList.add('ready'), 400);

  // Header turns solid after scrolling, plus a thin progress bar
  const nav = $('.nav');
  const bar = $('.scroll-progress');
  const onScroll = () => {
    const y = scrollY;
    if (nav) nav.classList.toggle('scrolled', y > 16);
    if (bar) {
      const max = root.scrollHeight - root.clientHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';
    }
  };
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });

  // Highlight the nav link for the section in view
  const links = $$('.nav-links a[href*="#"]:not(.btn)');
  const byId = {};
  links.forEach(a => { byId[a.getAttribute('href').split('#')[1]] = a; });
  // Phone tab bar: sections without their own tab light up the nearest one
  const tabs = $$('.tabbar a');
  const tabFor = { home: 'home', services: 'services', work: 'work', process: 'work', pricing: 'pricing', about: 'contact', contact: 'contact' };
  const spy = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    const a = byId[e.target.id];
    links.forEach(l => l.classList.toggle('active', l === a));
    const t = tabFor[e.target.id];
    tabs.forEach(l => l.classList.toggle('active', l.dataset.tab === t));
  }), { rootMargin: '-45% 0px -50% 0px' });
  Object.keys(tabFor).forEach(id => { const s = document.getElementById(id); if (s) spy.observe(s); });

  // Phone carousels: card grids become swipeable rows with dots
  $$('[data-carousel]').forEach(track => {
    const cards = Array.from(track.children);
    const dots = document.createElement('div');
    dots.className = 'dots';
    dots.setAttribute('aria-hidden', 'true');
    cards.forEach((c, i) => {
      const d = document.createElement('button');
      d.type = 'button';
      d.tabIndex = -1;
      d.addEventListener('click', () => track.scrollTo({ left: c.offsetLeft - track.offsetLeft - 16, behavior: reduced ? 'auto' : 'smooth' }));
      dots.appendChild(d);
    });
    track.after(dots);
    const setDot = () => {
      const mid = track.scrollLeft + track.clientWidth / 2;
      let best = 0, dist = Infinity;
      cards.forEach((c, i) => {
        const d = Math.abs(c.offsetLeft - track.offsetLeft + c.offsetWidth / 2 - mid);
        if (d < dist) { dist = d; best = i; }
      });
      Array.from(dots.children).forEach((d, i) => d.classList.toggle('on', i === best));
    };
    setDot();
    track.addEventListener('scroll', setDot, { passive: true });
  });

  // Section headings slide up word by word
  if (!reduced) {
    $$('.section h2, .contact-card h2').forEach(h => {
      const text = h.textContent.trim();
      h.setAttribute('aria-label', text);
      h.innerHTML = text.split(/\s+/).map((w, i) =>
        '<span class="w" aria-hidden="true"><span class="wi" style="--i:' + i + '">' + w.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</span></span>'
      ).join(' ');
      h.classList.add('split');
    });
  }

  // Fade cards and headings in as they scroll into view
  const revealEls = $$('.reveal, h2.split');
  if ('IntersectionObserver' in window && !reduced) {
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('in'));
  }

  // Pointer effects (desktop only): hero spotlight, card glow, magnetic buttons, showcase tilt
  if (canHover && !reduced) {
    const hero = $('.hero');
    if (hero) hero.addEventListener('pointermove', e => {
      const r = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      hero.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });

    $$('.card').forEach(c => c.addEventListener('pointermove', e => {
      const r = c.getBoundingClientRect();
      c.style.setProperty('--cx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--cy', (e.clientY - r.top) + 'px');
    }));

    $$('.magnetic').forEach(b => {
      b.addEventListener('pointermove', e => {
        const r = b.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width / 2) * .18;
        const y = (e.clientY - r.top - r.height / 2) * .3;
        b.style.transform = 'translate(' + x + 'px,' + y + 'px)';
      });
      b.addEventListener('pointerleave', () => { b.style.transform = ''; });
    });

    const show = $('.showcase');
    if (show && hero) {
      const dash = $('.dash', show), phone = $('.phone', show);
      hero.addEventListener('pointermove', e => {
        const x = e.clientX / innerWidth - .5, y = e.clientY / innerHeight - .5;
        dash.style.transform = 'perspective(1200px) rotateY(' + (x * 6) + 'deg) rotateX(' + (-y * 5) + 'deg)';
        phone.style.transform = 'translate(' + (x * 18) + 'px,' + (y * 14) + 'px)';
      });
      hero.addEventListener('pointerleave', () => { dash.style.transform = ''; phone.style.transform = ''; });
    }
  }

  // Live dashboard: counters, growing bars, incoming orders, phone checklist
  const showcase = $('.showcase');
  if (showcase && !reduced) {
    const fmt = n => n.toLocaleString('en-IN');
    const countUp = (el, to, dur) => {
      const t0 = performance.now();
      const step = now => {
        const p = Math.min((now - t0) / dur, 1);
        el.textContent = fmt(Math.round(to * (1 - Math.pow(1 - p, 3))));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    const counters = $$('[data-count]', showcase);
    counters.forEach(el => { el.textContent = '0'; });
    setTimeout(() => {
      counters.forEach(el => countUp(el, +el.dataset.count, 1400));
      showcase.classList.add('live');
    }, 700);

    const orders = counters[0];
    const visits = counters[1];
    const feed = $('[data-feed]', showcase);
    const hiBar = $('.bars .hi', showcase);
    const shops = [
      ['Gupta Furnishings', 12600], ['Verma & Sons', 7480], ['New Lakshmi Store', 21900],
      ['Royal Sleep Centre', 15250], ['Agarwal Traders', 8900], ['Om Sai Retail', 11300],
    ];
    let k = 0, total = +orders.dataset.count, vTotal = +visits.dataset.count, barH = 100;

    const phoneSteps = $$('[data-step]', showcase);
    const book = $('[data-book]', showcase);
    const runPhone = () => {
      phoneSteps.forEach(s => s.classList.remove('done'));
      book.classList.remove('booked');
      book.textContent = 'Book order';
      phoneSteps.forEach((s, i) => setTimeout(() => s.classList.add('done'), 500 + i * 650));
      setTimeout(() => { book.classList.add('booked'); book.textContent = '✓ Order booked'; }, 500 + phoneSteps.length * 650 + 500);
    };

    const tick = () => {
      if (document.hidden) return;
      runPhone();
      setTimeout(() => {
        const [name, amt] = shops[k++ % shops.length];
        const li = document.createElement('li');
        li.className = 'new';
        li.innerHTML = '<span>' + name + '</span><em>₹' + fmt(amt) + '</em><b class="pending">New</b>';
        feed.prepend(li);
        requestAnimationFrame(() => requestAnimationFrame(() => li.classList.remove('new')));
        while (feed.children.length > 2) feed.lastElementChild.remove();
        total += 1; orders.textContent = fmt(total);
        orders.classList.remove('bump'); void orders.offsetWidth; orders.classList.add('bump');
        if (k % 2) { vTotal += 1; visits.textContent = fmt(vTotal); }
        barH = Math.min(barH + 2, 100);
        if (hiBar) hiBar.style.height = barH + '%';
      }, 3300);
    };
    setTimeout(() => { tick(); setInterval(tick, 5200); }, 1600);
  }
})();

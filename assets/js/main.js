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
  const tabFor = { home: 'home', noz: 'noz', services: 'noz', work: 'work', process: 'work', pricing: 'noz', about: 'about', projects: 'about', contact: 'contact' };
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
    $$('.section h2:not(.noz-title), .contact-card h2').forEach(h => {
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
    if (show) {
      const dash = $('.dash', show), phone = $('.phone', show);
      const zone = show.closest('section') || hero;
      zone.addEventListener('pointermove', e => {
        const x = e.clientX / innerWidth - .5, y = e.clientY / innerHeight - .5;
        dash.style.transform = 'perspective(1200px) rotateY(' + (x * 6) + 'deg) rotateX(' + (-y * 5) + 'deg)';
        phone.style.transform = 'translate(' + (x * 18) + 'px,' + (y * 14) + 'px)';
      });
      zone.addEventListener('pointerleave', () => { dash.style.transform = ''; phone.style.transform = ''; });
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

  // Quick menu: Ctrl+K / Cmd+K opens a searchable list of sections and actions
  const cmdk = $('.cmdk');
  if (cmdk) {
    const body = document.body;
    const email = body.dataset.email, github = body.dataset.github, linkedin = body.dataset.linkedin;
    const onHome = location.pathname === '/' || location.pathname === '/index.html';
    const go = id => () => {
      const el = document.getElementById(id);
      if (onHome && el) el.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth' });
      else location.href = '/#' + id;
    };
    const ico = {
      go: '<path d="M5 12h14M13 6l6 6-6 6"/>',
      star: '<path d="M12 3v18M3 12h18"/>',
      mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
      copy: '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>',
      ext: '<path d="M14 4h6v6M20 4l-9 9M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/>',
    };
    const items = [
      { label: 'Get in touch', group: 'Action', icon: 'star', keys: 'contact hire quote enquiry project', run: go('contact') },
      { label: 'Home', group: 'Go to', icon: 'go', keys: 'top start kumar gaurav', run: go('home') },
      { label: 'NOZ Studio', group: 'Go to', icon: 'go', keys: 'noz studio business software company', run: go('noz') },
      { label: 'NOZ services', group: 'Go to', icon: 'go', keys: 'what we build websites apps software', run: go('services') },
      { label: 'Selected work', group: 'Go to', icon: 'go', keys: 'portfolio case studies clients', run: go('work') },
      { label: 'How NOZ works', group: 'Go to', icon: 'go', keys: 'process steps', run: go('process') },
      { label: 'Pricing', group: 'Go to', icon: 'go', keys: 'price cost plans monthly fee', run: go('pricing') },
      { label: 'About me', group: 'Go to', icon: 'go', keys: 'founder bio kumar gaurav', run: go('about') },
      { label: 'Projects', group: 'Go to', icon: 'go', keys: 'ventures side projects', run: go('projects') },
      { label: 'Contact', group: 'Go to', icon: 'go', keys: 'reach talk message', run: go('contact') },
    ];
    if (email) {
      items.push({ label: 'Email us', group: 'Action', icon: 'mail', keys: 'mail ' + email, run: () => { location.href = 'mailto:' + email; } });
      items.push({ label: 'Copy email address', group: 'Action', icon: 'copy', keys: 'clipboard ' + email, run: () => { if (navigator.clipboard) navigator.clipboard.writeText(email); } });
    }
    if (github) items.push({ label: 'GitHub', group: 'Link', icon: 'ext', keys: 'code repositories', run: () => open(github, '_blank', 'noopener') });
    if (linkedin) items.push({ label: 'LinkedIn', group: 'Link', icon: 'ext', keys: 'profile', run: () => open(linkedin, '_blank', 'noopener') });

    const input = $('.cmdk-input', cmdk), list = $('.cmdk-list', cmdk);
    let shown = items, sel = 0, lastFocus = null;
    const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');
    const render = () => {
      if (!shown.length) { list.innerHTML = '<li class="cmdk-empty">No matches. Try "pricing" or "work".</li>'; input.removeAttribute('aria-activedescendant'); return; }
      list.innerHTML = shown.map((it, i) =>
        '<li id="cmdk-' + i + '" class="cmdk-item' + (i === sel ? ' sel' : '') + '" role="option" aria-selected="' + (i === sel) + '" data-i="' + i + '">' +
        '<svg viewBox="0 0 24 24" aria-hidden="true">' + ico[it.icon] + '</svg><span>' + esc(it.label) + '</span><em>' + it.group + '</em></li>'
      ).join('');
      input.setAttribute('aria-activedescendant', 'cmdk-' + sel);
      const cur = list.children[sel];
      if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: 'nearest' });
    };
    const openMenu = () => {
      lastFocus = document.activeElement;
      cmdk.hidden = false;
      root.classList.add('cmdk-open');
      input.value = ''; shown = items; sel = 0; render();
      requestAnimationFrame(() => { cmdk.classList.add('show'); input.focus(); });
    };
    const closeMenu = () => {
      cmdk.classList.remove('show');
      root.classList.remove('cmdk-open');
      cmdk.hidden = true;
      if (lastFocus && lastFocus !== document.body && lastFocus.focus) lastFocus.focus();
      else input.blur();
    };
    const runSel = () => { const it = shown[sel]; if (it) { closeMenu(); it.run(); } };

    input.addEventListener('input', () => {
      const q = input.value.trim().toLowerCase();
      shown = q ? items.filter(it => (it.label + ' ' + it.keys).toLowerCase().includes(q)) : items;
      sel = 0; render();
    });
    input.addEventListener('keydown', e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(sel + 1, shown.length - 1); render(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(sel - 1, 0); render(); }
      else if (e.key === 'Enter') { e.preventDefault(); runSel(); }
      else if (e.key === 'Tab') { e.preventDefault(); }
    });
    list.addEventListener('click', e => { const li = e.target.closest('.cmdk-item'); if (li) { sel = +li.dataset.i; runSel(); } });
    list.addEventListener('pointermove', e => {
      const li = e.target.closest('.cmdk-item');
      if (li && +li.dataset.i !== sel) { sel = +li.dataset.i; render(); }
    });
    $$('[data-cmdk-close]', cmdk).forEach(el => el.addEventListener('click', closeMenu));
    $$('.cmdk-hint').forEach(el => el.addEventListener('click', openMenu));
    addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); cmdk.hidden ? openMenu() : closeMenu(); }
      else if (e.key === 'Escape' && !cmdk.hidden) closeMenu();
    });
    if (/Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent)) {
      $$('.cmdk-hint kbd').forEach(k => { if (k.textContent === 'Ctrl') k.textContent = '⌘'; });
    }
  }
})();

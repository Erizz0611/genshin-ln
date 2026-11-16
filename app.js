(function () {
  var KEY = 'ln-settings', PROG = 'ln-progress', READ = 'ln-read';
  function get(k, d) { try { return JSON.parse(localStorage.getItem(k)) || d; } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  var root = document.documentElement, s = get(KEY, {});
  s.fs = s.fs || 18; s.lh = s.lh || 1.8; s.font = s.font || 'serif'; s.theme = s.theme || 'light';

  // ----- cài đặt đọc -----
  var sheet = document.getElementById('settings'), fsVal = document.getElementById('fs-val');
  function apply() {
    root.dataset.theme = s.theme; root.dataset.font = s.font;
    root.style.setProperty('--fs', s.fs + 'px'); root.style.setProperty('--lh', s.lh);
    if (fsVal) fsVal.textContent = s.fs;
    var m = document.querySelector('meta[name=theme-color]');
    if (m) m.content = s.theme === 'dark' ? '#16191b' : s.theme === 'sepia' ? '#f3e9d4' : '#fbf8f2';
    sheet.querySelectorAll('[data-lh]').forEach(function (b) { b.classList.toggle('on', +b.dataset.lh === +s.lh); });
    sheet.querySelectorAll('[data-font]').forEach(function (b) { b.classList.toggle('on', b.dataset.font === s.font); });
    sheet.querySelectorAll('[data-theme]').forEach(function (b) { b.classList.toggle('on', b.dataset.theme === s.theme); });
    set(KEY, s);
  }
  apply();
  document.querySelectorAll('[data-open-settings]').forEach(function (b) { b.onclick = function () { sheet.hidden = false; }; });
  sheet.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (e.target === sheet || (b && b.hasAttribute('data-close-settings'))) { sheet.hidden = true; return; }
    if (!b) return;
    if (b.dataset.fs) s.fs = Math.min(28, Math.max(14, s.fs + +b.dataset.fs));
    if (b.dataset.lh) s.lh = +b.dataset.lh;
    if (b.dataset.font) s.font = b.dataset.font;
    if (b.dataset.theme) s.theme = b.dataset.theme;
    apply();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') sheet.hidden = true; });

  // ----- trang chương -----
  var reader = document.querySelector('.reader');
  if (reader) {
    var id = reader.dataset.chapter, bar = document.querySelector('.progress div'), top = document.querySelector('.topbar');
    var prog = get(PROG, {});
    if (prog.ch === id && prog.y > 200 && location.hash !== '#dau') setTimeout(function () { window.scrollTo(0, prog.y); }, 60);
    var lastY = 0, t;
    window.addEventListener('scroll', function () {
      var y = window.scrollY, h = document.documentElement.scrollHeight - innerHeight;
      bar.style.width = (h > 0 ? Math.min(100, y / h * 100) : 100) + '%';
      top.classList.toggle('hide', y > lastY && y > 300); lastY = y;
      clearTimeout(t);
      t = setTimeout(function () {
        set(PROG, { ch: id, y: y, url: location.pathname.split('/').slice(-2).join('/'), title: reader.dataset.title });
      }, 250);
    }, { passive: true });
    set(PROG, Object.assign(get(PROG, {}), prog.ch === id ? {} : { ch: id, y: 0, url: location.pathname.split('/').slice(-2).join('/'), title: reader.dataset.title }));
    document.querySelectorAll('[data-jump]').forEach(function (sel) { sel.onchange = function () { location.href = sel.value; }; });
    document.addEventListener('keydown', function (e) {
      if (e.target.tagName === 'SELECT' || !sheet.hidden) return;
      var a = e.key === 'ArrowLeft' ? document.querySelector('a[rel=prev]') : e.key === 'ArrowRight' ? document.querySelector('a[rel=next]') : null;
      if (a) location.href = a.href;
    });
  }

  // ----- đánh dấu đã đọc (người đọc tự bấm, bấm lại để bỏ) -----
  var p = get(PROG, null);
  function paint() {
    var r = get(READ, {});
    document.querySelectorAll('[data-mark]').forEach(function (b) {
      var on = !!r[b.dataset.mark], big = b.classList.contains('big');
      b.setAttribute('aria-pressed', on); b.title = on ? 'Bấm để bỏ đánh dấu' : 'Bấm để đánh dấu đã đọc';
      b.querySelector('.mt').textContent = on ? (big ? 'Đã đọc xong (bấm lần nữa để bỏ)' : 'Đã đọc, bấm để bỏ') : (big ? 'Đánh dấu đã đọc phần này' : 'Chưa đọc, bấm để đánh dấu');
    });
    document.querySelectorAll('li[data-ch]').forEach(function (li) {
      li.classList.toggle('read', !!r[li.dataset.ch]);
      li.classList.toggle('current', !!(p && p.ch === li.dataset.ch));
    });
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-mark]'); if (!b) return;
    var r = get(READ, {}), k = b.dataset.mark;
    if (r[k]) delete r[k]; else r[k] = 1;
    set(READ, r); paint();
  });
  paint();
  var cont = document.getElementById('continue');
  if (cont && p && p.url) {
    cont.href = p.url; cont.hidden = false;
    var note = document.getElementById('continue-note');
    // lấy tên hiện tại từ mục lục (tên màn có thể đã đổi sau khi lưu)
    var li = p.ch && document.querySelector('li[data-ch="' + p.ch + '"]'), t = p.title;
    if (li) {
      var k = li.closest('.act').querySelector('.kick'), act = k ? k.firstChild.textContent.trim() : '';
      t = act + ' · ' + li.querySelector('.lab').textContent + ': ' + li.querySelector('.ttl').textContent;
    }
    if (note && t) { note.textContent = 'Đang đọc: ' + t; note.hidden = false; }
  }
  // ----- hồ sơ nhân vật: thẻ nổi -----
  var modal = document.getElementById('modal');
  if (modal) {
    var src = Array.prototype.slice.call(document.querySelectorAll('.profs-src .prof')), mb = modal.querySelector('.modal-body'), cur = -1;
    function show(i) {
      cur = (i + src.length) % src.length;
      mb.innerHTML = src[cur].outerHTML; mb.firstChild.removeAttribute('id');
      modal.querySelector('.modal-pos').textContent = src[cur].dataset.name + ' · ' + (cur + 1) + '/' + src.length;
      modal.hidden = false; document.body.classList.add('noscroll'); modal.querySelector('.modal-card').scrollTop = 0;
      history.replaceState(null, '', '#' + src[cur].id);
    }
    function close() { modal.hidden = true; document.body.classList.remove('noscroll'); history.replaceState(null, '', location.pathname); }
    document.addEventListener('click', function (e) {
      var o = e.target.closest('[data-open]');
      if (o) { e.preventDefault(); show(src.findIndex(function (p) { return p.id === o.dataset.open; })); return; }
      if (modal.hidden) return;
      var s = e.target.closest('[data-step]');
      if (s) show(cur + +s.dataset.step);
      else if (e.target === modal || e.target.closest('[data-close]')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (modal.hidden) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
    });
    var h = location.hash.slice(1), k = src.findIndex(function (p) { return p.id === h; });
    if (k >= 0) show(k);
  }

  // ----- tìm nhân vật (không phân biệt dấu) -----
  var q = document.getElementById('psearch');
  if (q) {
    var norm = function (s) { return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase(); };
    q.addEventListener('input', function () {
      var t = norm(q.value.trim()), n = 0;
      document.querySelectorAll('.pcard').forEach(function (c) { var ok = !t || norm(c.dataset.q).indexOf(t) >= 0; c.hidden = !ok; if (ok) n++; });
      document.getElementById('pempty').hidden = n > 0;
    });
  }

  // ----- thanh các màn ở trang chủ: tô sáng màn đang xem -----
  var navs = document.querySelectorAll('[data-nav]');
  if (navs.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        navs.forEach(function (a) {
          var on = a.dataset.nav === e.target.id; a.classList.toggle('on', on);
          if (on && a.parentNode.scrollWidth > a.parentNode.clientWidth) a.parentNode.scrollTo({ left: a.offsetLeft - 16, behavior: 'smooth' });
        });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    navs.forEach(function (a) { var el = document.getElementById(a.dataset.nav); if (el) io.observe(el); });
    navs.forEach(function (a) { a.addEventListener('click', function () { setTimeout(function () { navs.forEach(function (b) { b.classList.toggle('on', b === a); }); }, 700); }); });
  }
  // ----- mục lục: các màn mặc định đóng; bấm thanh màn hoặc link #id thì mở màn đó -----
  function openAct(h) { var d = h && document.getElementById(h); if (d && d.tagName === 'DETAILS') d.open = true; }
  document.querySelectorAll('.an-arc').forEach(function (b) {
    b.addEventListener('click', function () { var g = b.parentNode, o = g.classList.toggle('open'); b.setAttribute('aria-expanded', o); });
  });
  navs.forEach(function (a) { a.addEventListener('click', function () { openAct(a.dataset.nav); }); });
  openAct(location.hash.slice(1));
  window.addEventListener('hashchange', function () { openAct(location.hash.slice(1)); });
})();

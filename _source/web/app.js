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
      b.setAttribute('aria-pressed', on);
      b.querySelector('.mt').textContent = on ? (big ? 'Đã đọc xong · bấm để bỏ đánh dấu' : 'Đã đọc') : (big ? 'Đánh dấu đã đọc chương này' : 'Chưa đọc');
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
    if (note && p.title) { note.textContent = 'Đang đọc: ' + p.title; note.hidden = false; }
  }
})();

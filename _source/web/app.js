(function () {
  var KEY = 'ln-settings', PROG = 'ln-progress', READ = 'ln-read';
  function get(k, d) { try { return JSON.parse(localStorage.getItem(k)) || d; } catch (e) { return d; } }
  var onLocal = null; // đồng bộ tài khoản (gắn ở cuối file)
  function set(k, v, quiet) {
    if (k === PROG && v && !quiet) v.t = Date.now();
    try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {}
    if (!quiet && onLocal && (k === PROG || k === READ)) onLocal(k);
  }
  var root = document.documentElement, s = get(KEY, {});
  s.fs = s.fs || 18; s.lh = s.lh || 1.8; s.font = s.font || 'serif'; s.theme = s.theme || 'light';

  var THEMES = { light: 'Sáng', sepia: 'Giấy', dark: 'Tối' };
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
    document.querySelectorAll('[data-theme-name]').forEach(function (e) { e.textContent = THEMES[s.theme] || 'Sáng'; });
    set(KEY, s);
  }
  apply();
  document.querySelectorAll('[data-open-settings]').forEach(function (b) { b.onclick = function () { sideOpen(false); sheet.hidden = false; }; });
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

  // ----- thanh bên trái (máy tính: cố định; điện thoại: ngăn kéo mở bằng nút menu) -----
  var side = document.getElementById('side'), scrim = document.querySelector('.side-scrim'), menuBtn = document.querySelector('[data-open-side]');
  function sideOpen(o) {
    if (!side) return;
    document.body.classList.toggle('side-open', o);
    if (scrim) scrim.hidden = !o;
    if (menuBtn) menuBtn.setAttribute('aria-expanded', o);
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-open-side]')) { sideOpen(true); return; }
    if (e.target.closest('[data-close-side]') || (document.body.classList.contains('side-open') && e.target.closest('.rail a'))) sideOpen(false);
    if (e.target.closest('[data-theme-cycle]')) {
      var ks = Object.keys(THEMES); s.theme = ks[(ks.indexOf(s.theme) + 1) % ks.length]; apply();
    }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') sideOpen(false); });
  function sideCont() {
    var a = side && side.querySelector('[data-continue]'), pr = get(PROG, null);
    if (!a || !pr || !pr.url) return;
    a.href = (side.dataset.root || '') + pr.url; a.hidden = false;
    a.querySelector('[data-continue-t]').textContent = pr.title || '';
  }
  sideCont();

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
  function showContinue() {
    sideCont();
    if (!cont || !p || !p.url) return;
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
  showContinue();
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
  // ----- tài khoản Google: đồng bộ dấu đã đọc + vị trí "Đọc tiếp" lên Firestore (users/{uid}) -----
  // Chưa đăng nhập: chỉ lưu localStorage như cũ. Thư viện Firebase chỉ tải khi đã/đang đăng nhập.
  var FBV = 'https://www.gstatic.com/firebasejs/10.14.1/', SYNC = 'ln-sync';
  var CFG = { apiKey: 'AIzaSyAIcdBv-1_o66dvgdv8T5MT3FkccvYZ-B4', authDomain: 'genshinln.firebaseapp.com', projectId: 'genshinln',
    storageBucket: 'genshinln.firebasestorage.app', messagingSenderId: '883911656308', appId: '1:883911656308:web:f2a2e1be72755e6e90e221' };
  var fbP = null, user = null, state = 'off', tRead = 0, tProg = 0, lastProg = 0;
  function imp(u) { return (new Function('u', 'return import(u)'))(u); }
  function loadFb() {
    if (!fbP) fbP = Promise.all([imp(FBV + 'firebase-app.js'), imp(FBV + 'firebase-auth.js'), imp(FBV + 'firebase-firestore.js')]).then(function (m) {
      var app = m[0].initializeApp(CFG), A = m[1], F = m[2], auth = A.getAuth(app);
      var fb = { A: A, F: F, auth: auth, db: F.getFirestore(app) };
      if ((get(SYNC, {}) || {}).pending) A.getRedirectResult(auth).catch(function () { state = 'err'; ui(); });
      A.onAuthStateChanged(auth, function (u) {
        user = u;
        if (u) pull(fb); else { state = 'off'; try { localStorage.removeItem(SYNC); } catch (e) {} ui(); }
      });
      return fb;
    });
    fbP.catch(function () { fbP = null; state = 'err'; ui(); });
    return fbP;
  }
  function doc(fb) { return fb.F.doc(fb.db, 'users', user.uid); }
  function push(fb) {
    if (!user) return;
    var meta = get(SYNC, {}); meta.uid = user.uid; meta.dirty = 1; set(SYNC, meta, true);
    fb.F.setDoc(doc(fb), { read: get(READ, {}), prog: get(PROG, null), t: Date.now() }).then(function () {
      var m = get(SYNC, {}); delete m.dirty; set(SYNC, m, true); if (state !== 'ok') { state = 'ok'; ui(); }
    }, function () { state = 'err'; ui(); });
  }
  function pull(fb) {
    var uid = user.uid; state = 'busy'; ui();
    fb.F.getDoc(doc(fb)).then(function (snap) {
      if (!user || user.uid !== uid) return;
      var meta = get(SYNC, {}), first = meta.uid !== uid, d = snap.exists() ? snap.data() : null;
      var lr = get(READ, {}), lp = get(PROG, null), r = lr, pr = lp, needPush = !d;
      if (d) {
        if (first || meta.dirty) { r = Object.assign({}, d.read || {}, lr); needPush = true; } // lần đầu: gộp tiến trình cũ lên tài khoản
        else r = d.read || {};
        var rp = d.prog || null;
        if (rp && (!lp || (rp.t || 0) > (lp.t || 0))) pr = rp; else if (lp && (!rp || (lp.t || 0) > (rp.t || 0))) needPush = true;
      }
      set(READ, r, true); if (pr) set(PROG, pr, true);
      meta.uid = uid; set(SYNC, meta, true);
      p = get(PROG, null); paint(); showContinue();
      state = 'ok'; ui();
      if (needPush) push(fb);
    }, function () { state = 'err'; ui(); });
  }
  onLocal = function (k) {
    if (!user || !fbP) return;
    if (k === READ) { clearTimeout(tRead); tRead = setTimeout(function () { fbP.then(push); }, 600); }
    else if (!tProg) { // vị trí đọc: gửi tối đa ~10 giây một lần
      tProg = setTimeout(function () { tProg = 0; lastProg = Date.now(); fbP.then(push); }, Math.max(1500, 10000 - (Date.now() - lastProg)));
    }
  };
  function flush() { if (tProg && user && fbP) { clearTimeout(tProg); tProg = 0; lastProg = Date.now(); fbP.then(push); } }
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') flush(); });
  window.addEventListener('pagehide', flush);

  function signIn() {
    state = 'busy'; ui();
    loadFb().then(function (fb) {
      var pv = new fb.A.GoogleAuthProvider(); pv.setCustomParameters({ prompt: 'select_account' });
      return fb.A.signInWithPopup(fb.auth, pv).catch(function (e) {
        if (e && (e.code === 'auth/popup-blocked' || e.code === 'auth/operation-not-supported-in-environment')) {
          set(SYNC, { pending: 1 }, true); return fb.A.signInWithRedirect(fb.auth, pv);
        }
        throw e;
      });
    }).catch(function (e) {
      state = e && (e.code === 'auth/popup-closed-by-user' || e.code === 'auth/cancelled-popup-request') ? 'off' : 'err'; ui();
    });
  }
  function signOut() { if (!fbP) return; flush(); fbP.then(function (fb) { fb.A.signOut(fb.auth); }); }

  // giao diện: một dòng trong bảng "Cài đặt đọc" + một dòng gợi ý dưới nút Đọc tiếp ở trang chủ
  var acctRow = document.createElement('div');
  acctRow.className = 'row acct';
  acctRow.innerHTML = '<span>Tài khoản</span><div class="acct-r"><span class="acct-who"></span><button type="button" class="acct-btn" data-acct></button></div>';
  var acctNote = document.createElement('p'); acctNote.className = 'acct-note';
  sheet.querySelector('.sheet').appendChild(acctRow); sheet.querySelector('.sheet').appendChild(acctNote);
  var hint = null, cn = document.getElementById('continue-note');
  if (cn) { hint = document.createElement('p'); hint.className = 'acct-hint'; cn.parentNode.insertBefore(hint, cn.nextSibling); }
  function nm() { return user ? (user.displayName || user.email || 'Tài khoản Google') : ''; }
  function ui() {
    var b = acctRow.querySelector('.acct-btn'), who = acctRow.querySelector('.acct-who');
    b.textContent = user ? 'Đăng xuất' : 'Đăng nhập Google'; b.disabled = state === 'busy' && !user;
    who.textContent = user ? nm() : ''; who.hidden = !user;
    acctNote.textContent = user
      ? (state === 'busy' ? 'Đang đồng bộ tiến trình đọc…' : state === 'err' ? 'Chưa đồng bộ được, kiểm tra mạng rồi tải lại trang.' : 'Dấu đã đọc và vị trí "Đọc tiếp" được lưu theo tài khoản, dùng được trên mọi thiết bị.')
      : (state === 'err' ? 'Đăng nhập không thành công, thử lại nhé.' : 'Đăng nhập để lưu dấu đã đọc và vị trí "Đọc tiếp" trên mọi thiết bị. Không đăng nhập thì vẫn lưu trên trình duyệt này.');
    if (hint) hint.innerHTML = user
      ? 'Đã đăng nhập: <b></b> · tiến trình đọc được đồng bộ'
      : '<button type="button" class="linkish" data-acct>Đăng nhập Google</button> để lưu tiến trình đọc trên mọi thiết bị';
    if (hint && user) hint.querySelector('b').textContent = nm();
    var sa = document.getElementById('side-acct');
    if (sa) {
      if (user) {
        sa.innerHTML = '<span class="sa-av" aria-hidden="true"></span><span class="sa-t"><b></b><span class="sa-s"></span></span><button type="button" class="sa-out" data-acct>Đăng xuất</button>';
        var av = sa.querySelector('.sa-av');
        if (user.photoURL) { var im = document.createElement('img'); im.src = user.photoURL; im.alt = ''; im.referrerPolicy = 'no-referrer'; av.appendChild(im); }
        else av.textContent = nm().charAt(0).toUpperCase();
        sa.querySelector('b').textContent = nm();
        var st = sa.querySelector('.sa-s'); st.className = 'sa-s ' + state;
        st.textContent = state === 'busy' ? 'Đang đồng bộ…' : state === 'err' ? 'Chưa đồng bộ được' : 'Đã đồng bộ';
      } else {
        sa.innerHTML = '<button type="button" class="sa-in" data-acct' + (state === 'busy' ? ' disabled' : '') + '>Đăng nhập Google</button><span class="sa-note"></span>';
        sa.querySelector('.sa-note').textContent = state === 'err' ? 'Đăng nhập không thành công, thử lại nhé.' : 'Lưu tiến trình đọc trên mọi thiết bị';
      }
    }
  }
  document.addEventListener('pointerdown', function (e) { if (e.target.closest('[data-acct]') && !user) loadFb(); }, true);
  document.addEventListener('click', function (e) {
    if (!e.target.closest('[data-acct]')) return;
    if (user) signOut(); else signIn();
  });
  ui();
  var meta0 = get(SYNC, null);
  if (meta0 && (meta0.uid || meta0.pending)) { state = 'busy'; loadFb(); ui(); }
})();

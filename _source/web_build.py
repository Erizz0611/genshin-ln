# Dựng web đọc truyện tĩnh từ các file nguồn manX.txt + acts.py + characters.py
# Dùng:  python web_build.py [thư_mục_ra]      (mặc định: ../web)
# Thêm màn mới: thêm file nguồn + 1 mục trong ACTS (acts.py), cập nhật characters.py, rồi chạy lại lệnh này.
import os, sys, html, json, shutil, hashlib
from PIL import Image
from build import parse, esc, HERE, IMG
from acts import ACTS, SERIES, FOOT
from characters import P, UPDATED

OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'web')) + '/'
WEB = os.path.join(HERE, 'web') + '/'   # style.css, app.js
SITE = 'Genshin Impact LN'
DESC = 'Light novel tiếng Việt chuyển thể cốt truyện Genshin Impact, theo chân Nhà Lữ Hành Lumine đi tìm người anh trai song sinh.'

# ---------- ảnh ----------
_done = {}
def img(name, w, ratio=None, focus=0.25, q=80):
    """Cắt + thu nhỏ ảnh, lưu WebP vào web/img, trả về đường dẫn tương đối từ gốc web."""
    key = (name, w, ratio, focus)
    if key in _done: return _done[key]
    im = Image.open(IMG + name)
    im = im.convert('RGBA') if im.mode in ('RGBA', 'LA', 'P') else im.convert('RGB')
    if ratio:
        W, H = im.size
        if W / H > ratio:
            nw = int(H * ratio); x = (W - nw) // 2; im = im.crop((x, 0, x + nw, H))
        else:
            nh = int(W / ratio); y = int((H - nh) * focus); im = im.crop((0, y, W, y + nh))
    if im.width > w:
        im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    fn = f"{os.path.splitext(name)[0]}_{w}{'_r' + str(round(ratio, 2)) if ratio else ''}{'_f' + str(focus) if ratio else ''}.webp"
    im.save(OUT + 'img/' + fn, 'WEBP', quality=q, method=6)
    _done[key] = 'img/' + fn
    return _done[key]

def banner(name):
    f = 0.3 if 'card' in name else (0.12 if 'splash' in name else 0.2)
    return img(name, 1200, ratio=1200 / 560, focus=f)

def avatar(name):
    return img(name, 160, ratio=1, focus=0.1)

# ---------- khung trang ----------
VER = hashlib.md5(open(WEB + 'style.css', 'rb').read() + open(WEB + 'app.js', 'rb').read()).hexdigest()[:8]  # chống trình duyệt giữ bản cũ

def page(title, body, root='', cls='', extra_head=''):
    t = html.escape(title + (' — ' + SITE if title != SITE else ''))
    return f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{html.escape(DESC)}">
<meta name="theme-color" content="#f6f1e7">
<link rel="icon" href="{root}img/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css?v={VER}">
<script>try{{var s=JSON.parse(localStorage.getItem('ln-settings')||'{{}}');var d=document.documentElement;d.dataset.theme=s.theme||'light';d.dataset.font=s.font||'serif';d.style.setProperty('--fs',(s.fs||18)+'px');d.style.setProperty('--lh',s.lh||1.8)}}catch(e){{}}</script>
{extra_head}</head>
<body class="{cls}">
<header class="topbar"><a class="brand" href="{root}index.html"><img src="{root}img/icon.png" alt=""><span>Genshin Impact LN</span></a>
<nav class="mainnav"><a href="{root}index.html#muc-luc" data-nav-home>Mục lục</a><a href="{root}nhan-vat.html" data-nav-prof>Nhân vật</a>
<button class="icon-btn" data-open-settings aria-label="Cài đặt đọc">Aa</button></nav></header>
{body}
<div class="settings" id="settings" hidden>
  <div class="sheet" role="dialog" aria-label="Cài đặt đọc">
    <div class="sheet-head"><b>Cài đặt đọc</b><button class="icon-btn" data-close-settings aria-label="Đóng">✕</button></div>
    <div class="row"><span>Cỡ chữ</span><div class="seg"><button data-fs="-1">A−</button><output id="fs-val">18</output><button data-fs="1">A+</button></div></div>
    <div class="row"><span>Giãn dòng</span><div class="seg"><button data-lh="1.55">Hẹp</button><button data-lh="1.8">Vừa</button><button data-lh="2.05">Rộng</button></div></div>
    <div class="row"><span>Phông chữ</span><div class="seg"><button data-font="serif">Có chân</button><button data-font="sans">Không chân</button></div></div>
    <div class="row"><span>Nền</span><div class="seg"><button data-theme="light">Sáng</button><button data-theme="sepia">Giấy</button><button data-theme="dark">Tối</button></div></div>
  </div>
</div>
<footer class="foot"><p>{esc(FOOT)}</p></footer>
<script src="{root}app.js?v={VER}"></script>
</body></html>'''

# ---------- dữ liệu ----------
acts = []
for a in ACTS:
    chs = parse(HERE + a['src'])
    acts.append(dict(a, chapters=chs))
# thứ tự đọc toàn bộ
order = [(ai, ci) for ai, a in enumerate(acts) for ci in range(len(a['chapters']))]
def ch_url(ai, ci, root=''): return f"{root}{acts[ai]['id']}/{ci}.html"

def chapter_body(c):
    out = []
    for k, t in c['body']:
        if k == 'brk': out.append('<div class="brk" aria-hidden="true">◇ ◇ ◇</div>')
        elif k == 'bigbrk': out.append('<div class="brk big" aria-hidden="true">✦</div>')
        elif k == 'v': out.append(f'<p class="v">{esc(t)}</p>')
        elif k == 'end': out.append(f'<p class="end">{esc(t)}</p>')
        else:
            cls = ' class="d"' if t.startswith('“') or t.startswith('*(') else ''
            out.append(f'<p{cls}>{esc(t)}</p>')
    return '\n'.join(out)

def cast_html(cast, root):
    rows = []
    for c in cast:
        av = f'<img src="{root}{avatar(c["img"])}" alt="" loading="lazy">' if c.get('img') else html.escape(c['name'][0])
        rows.append(f'<li class="cast"><div class="av">{av}</div><div><div class="rl">{esc(c["role"])}</div><div class="nm">{esc(c["name"])}</div><div class="ds">{esc(c["desc"])}</div></div></li>')
    return '<ul class="cast-list">' + ''.join(rows) + '</ul>'

def chapter_list(ai, root):
    a = acts[ai]
    return '<ol class="chlist">' + ''.join(
        f'<li data-ch="{a["id"]}/{ci}"><a href="{ch_url(ai, ci, root)}"><span class="lab">{esc(c["label"])}</span><span class="ttl">{esc(c["title"])}</span></a>'
        f'<button class="mark" type="button" data-mark="{a["id"]}/{ci}" aria-pressed="false" title="Đánh dấu đã đọc"><span class="box" aria-hidden="true"></span><span class="mt">Chưa đọc</span></button></li>'
        for ci, c in enumerate(a['chapters'])) + '</ol>'

# ---------- xuất ----------
def write(rel, s):
    p = OUT + rel; os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(s)

if os.path.isdir(OUT + 'img'): shutil.rmtree(OUT + 'img')
os.makedirs(OUT + 'img', exist_ok=True)
for f in ('style.css', 'app.js'): shutil.copy(WEB + f, OUT + f)
Image.open(IMG + 'lumine_icon.png').convert('RGBA').resize((128, 122)).save(OUT + 'img/icon.png')

# Trang chủ
hero = img('traveler_portrait.png', 700, q=82)
def short(a):
    # nhãn ngắn trong nhóm: bỏ tên mục lớn ("Chương I · Màn II" -> "Màn II"); màn khác mục lớn (vd. Chương Đệm) giữ đủ tên
    pre = a['arc'].split(' · ')[0] + ' · '
    return a['act'][len(pre):] if a['act'].startswith(pre) else a['act']

arcs = []
for ai, a in enumerate(acts):
    if not arcs or arcs[-1][0] != a['arc']: arcs.append((a['arc'], []))
    arcs[-1][1].append(ai)
toc = []
nav = []
for arc, ais in arcs:
    nav.append(f'<div class="an-g"><button type="button" class="an-arc" aria-expanded="false">{esc(arc)}<span class="chev" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span></button><div class="an-items">')
    for ai in ais:
        a = acts[ai]
        nav.append(f'<a href="#{a["id"]}" data-nav="{a["id"]}"><span class="an-n">{esc(short(a))}</span><span class="an-t">{esc(a["title"])}</span></a>')
    nav.append('</div></div>')
for arc, ais in arcs:
    toc.append(f'<h3 class="arc">{esc(arc)}</h3>')
    for ai in ais:
        a = acts[ai]
        tag = '<span class="tag side">Nhiệm vụ bắt buộc</span>' if a['side'] else '<span class="tag">Ma Thần</span>'
        toc.append(f'''<details class="act" id="{a["id"]}"><summary><img src="{banner(a.get("thumb") or (a["chapters"][0]["img"] if a["side"] else a["hero"]))}" alt="" loading="lazy">
<div><div class="kick">{esc(short(a))} {tag}</div><div class="atitle">{esc(a["title"])}</div><div class="asub">{esc(a["sub"])} · {len(a["chapters"])} phần</div></div><span class="chev" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span></summary>
<div class="act-links"><a href="{a["id"]}/index.html">Giới thiệu & nhân vật</a></div>
{chapter_list(ai, "")}</details>''')
first = ch_url(*order[0])
home = f'''<main class="home">
<section class="hero"><div class="hero-text"><div class="kick">{esc(SERIES)}</div><h1>Genshin Impact</h1><div class="sub-h">Hành Trình Của Nhà Lữ Hành</div>
<p>{esc(DESC)}</p>
<div class="btns"><a class="btn primary" href="{first}">Đọc từ đầu</a><a class="btn" id="continue" hidden href="#">Đọc tiếp</a></div>
<p class="continue-note" id="continue-note" hidden></p>
<nav class="lookup" aria-label="Tra cứu"><span class="lk-l">Tra cứu</span><a class="lk" href="nhan-vat.html"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><circle cx="9" cy="8" r="3.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 19c.6-3.2 3-5 6-5s5.4 1.8 6 5M15.5 4.8a3.2 3.2 0 0 1 0 6.4M17.5 14.4c1.9.6 3.1 2.2 3.5 4.6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>Hồ sơ nhân vật</a></nav></div>
<img class="hero-img" src="{hero}" alt="Nhà Lữ Hành"></section>
<div class="toc-lyt"><nav class="actnav" aria-label="Đi tới màn"><div class="an-h">Các màn</div>{''.join(nav)}</nav>
<section class="toc" id="muc-luc"><h2>Mục lục</h2>{''.join(toc)}</section></div>
</main>'''
write('index.html', page(SITE, home, '', 'p-home'))

# Trang giới thiệu màn + chương
titles = {f"{a['id']}/{ci}": f"{a['act']} · {c['label']}: {c['title']}" for a in acts for ci, c in enumerate(a['chapters'])}
for ai, a in enumerate(acts):
    r = '../'
    body = f'''<main class="act-page">
<div class="banner"><img src="{r}{banner(a["hero"])}" alt=""></div>
<div class="kick c">{esc(a["act"])}</div><h1 class="c">{esc(a["title"])}</h1><p class="asub c">{esc(a["sub"])}</p>
<div class="btns c"><a class="btn primary" href="0.html">Bắt đầu đọc</a></div>
<h2>Nhân vật xuất hiện</h2>{cast_html(a["cast"], r)}
<h2>Các phần</h2>{chapter_list(ai, r)}
<p class="note">Toàn bộ lời thoại được lấy từ bản tiếng Việt chính thức của trò chơi. Ở những đoạn người chơi được chọn câu trả lời, truyện chọn một lựa chọn duy nhất.</p>
</main>'''
    write(f"{a['id']}/index.html", page(a['act'] + ' — ' + a['title'], body, r, 'p-act'))
    for ci, c in enumerate(a['chapters']):
        k = order.index((ai, ci))
        prev = ch_url(*order[k - 1], r) if k > 0 else None
        nxt = ch_url(*order[k + 1], r) if k + 1 < len(order) else None
        opts = ''
        for arc, ais in arcs:
            opts += f'<optgroup label="{esc(arc)}">' + ''.join(f'<option value="{ch_url(x, y, r)}"{" selected" if (x, y) == (ai, ci) else ""}>{esc(short(acts[x]))} · {esc(acts[x]["chapters"][y]["label"])}: {esc(acts[x]["chapters"][y]["title"])}</option>' for x in ais for y in range(len(acts[x]["chapters"]))) + '</optgroup>'
        nav = (f'<nav class="chnav">' + (f'<a class="btn" href="{prev}" rel="prev">‹ Trước</a>' if prev else '<span class="btn off">‹ Trước</span>')
               + f'<select aria-label="Chọn phần" data-jump>{opts}</select>'
               + (f'<a class="btn" href="{nxt}" rel="next">Sau ›</a>' if nxt else '<span class="btn off">Sau ›</span>') + '</nav>')
        log = f'<div class="log"><span>Nhật ký nhiệm vụ</span>{esc(c["log"])}</div>' if c['log'] else ''
        endnote = '' if nxt else '<p class="end-all">Bạn đã đọc đến phần mới nhất. Các màn tiếp theo sẽ được cập nhật sau.</p>'
        body = f'''<main class="reader" data-chapter="{a['id']}/{ci}" data-title="{html.escape(titles[a['id'] + '/' + str(ci)])}">
<div class="banner"><img src="{r}{banner(c['img'])}" alt=""></div>
<div class="kick c"><a href="index.html">{esc(a['act'])}</a></div>
<div class="ch-label c">{esc(c['label'])}</div><h1 class="c">{esc(c['title'])}</h1>
{'' if c['quest'] == c['title'] else '<div class="ch-quest c">✦ ' + esc(c['quest']) + ' ✦</div>'}
{nav}
<article class="text">{log}{chapter_body(c)}</article>
<div class="done-wrap"><button class="mark big" type="button" data-mark="{a['id']}/{ci}" aria-pressed="false"><span class="box" aria-hidden="true"></span><span class="mt">Đánh dấu đã đọc phần này</span></button></div>
{endnote}
{nav}
</main><div class="progress" aria-hidden="true"><div></div></div>'''
        write(f"{a['id']}/{ci}.html", page(f"{c['label']}: {c['title']}", body, r, 'p-reader'))

# Hồ sơ nhân vật: lưới thẻ + thẻ nổi (modal) + thanh bên "nhân vật theo chương"
# Nhân vật được coi là xuất hiện trong chương nếu tên (hoặc tên gọi khác) có trong văn bản chương.
ALIASES = {'Phong Ma Long': ['Phong Ma Long', 'Ma Long', 'Dvalin', 'con rồng', 'Con rồng']}
CAST_ALIASES = {'Phong Ma Long': ['Phong Ma Long', 'Dvalin']}
def in_cast(c, a):
    # chỉ tính nhân vật thật sự xuất hiện (có trong danh sách "Nhân vật xuất hiện" của màn), không tính người chỉ được nhắc tên
    names = [x['name'] for x in a['cast']]
    return any(n == m or n in m.split(' ') or (n in m and ' ' in n) for n in CAST_ALIASES.get(c['name'], [c['name']]) for m in names)
def appears(c, ch):
    text = ' '.join(t for _, t in ch['body']) + ' ' + (ch['log'] or '')
    return any(n in text for n in ALIASES.get(c['name'], [c['name']]))

cards, profs = [], []
for i, c in enumerate(P):
    pid = 'nv-' + str(i)
    pic = f'<img src="{img(c["img"], 520, ratio=52 / 74, focus=0.62 if "card" in c["img"] else 0.0)}" alt="{html.escape(c["name"])}" loading="lazy">' if c['img'] else f'<div class="ph">{html.escape(c["name"][0])}</div>'
    cards.append(f'<a class="pcard" href="#{pid}" data-open="{pid}" data-q="{html.escape((c["name"] + " " + c["title"] + " " + " ".join(v for _, v in c["info"])))}"><div class="pic">{pic}</div><div class="pn">{esc(c["name"])}</div><div class="pt">{esc(c["title"])}</div></a>')
    rows = ''.join(f'<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>' for k, v in c['info'])
    profs.append(f'''<article class="prof" id="{pid}" data-name="{html.escape(c["name"])}"><div class="top"><div class="pic">{pic}</div><div class="meta">
<div class="kick">Hồ sơ nhân vật</div><h2>{esc(c["name"])}</h2><div class="ptitle">{esc(c["title"])}</div><table>{rows}</table></div></div>
<h3>Là ai</h3><p>{esc(c["who"])}</p><h3>Xuất thân</h3><p>{esc(c["origin"])}</p><h3>Vai trò trong cốt truyện</h3><p>{esc(c["role"])}</p></article>''')

side = []
for arc, ais in arcs:   # gộp theo mục lớn (Mở Đầu, Chương I · Liyue...), mỗi nhân vật chỉ ghi một lần
    who = [(i, c) for i, c in enumerate(P) if any(in_cast(c, acts[ai]) for ai in ais)]
    chips = ''.join(f'<a href="#nv-{i}" data-open="nv-{i}" class="chip">{esc(c["name"])}</a>' for i, c in who) or '<span class="none">—</span>'
    side.append(f'<div class="sb-ch"><a class="sb-t" href="index.html#{acts[ais[0]]["id"]}"><span class="sb-act">{esc(arc)}</span>{len(ais)} màn · {len(who)} nhân vật</a><div class="chips">{chips}</div></div>')

body = f'''<main class="profiles"><div class="kick c">Phụ lục</div><h1 class="c">Hồ Sơ Nhân Vật</h1><p class="asub c">{esc(UPDATED)} · bấm vào nhân vật để xem hồ sơ</p>
<div class="plyt">
<aside class="sidebar"><details open><summary>Nhân vật theo chương</summary>{''.join(side)}</details></aside>
<div><div class="psearch"><input type="search" id="psearch" placeholder="Tìm nhân vật…" autocomplete="off" aria-label="Tìm nhân vật"></div>
<p class="pempty" id="pempty" hidden>Không tìm thấy nhân vật nào.</p><div class="pgrid">{''.join(cards)}</div>
<p class="note">Hồ sơ chỉ ghi những gì đã xuất hiện trong các màn đã viết, kèm thông tin hồ sơ chính thức trong game. Sẽ được bổ sung sau mỗi màn mới.</p></div>
</div>
<div class="profs-src" hidden>{''.join(profs)}</div>
</main>
<div class="modal" id="modal" hidden><div class="modal-card" role="dialog" aria-modal="true">
<div class="modal-bar"><button class="icon-btn" data-step="-1" aria-label="Nhân vật trước">‹</button><span class="modal-pos"></span><button class="icon-btn" data-step="1" aria-label="Nhân vật sau">›</button><button class="icon-btn" data-close aria-label="Đóng">✕</button></div>
<div class="modal-body"></div></div></div>'''
write('nhan-vat.html', page('Hồ Sơ Nhân Vật', body, '', 'p-prof'))

open(OUT + '.nojekyll', 'w').close()
print('Web ->', OUT, '|', len(acts), 'màn,', len(order), 'phần,', len(P), 'hồ sơ')

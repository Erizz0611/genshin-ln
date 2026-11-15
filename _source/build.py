import base64, io, re, sys, html, json
from PIL import Image
import subprocess, os, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'

IMG = HERE + 'img/'

def data_uri(name, w=None, ratio=None, focus=0.25, fmt='JPEG', q=82, bg=(250, 246, 238)):
    im = Image.open(IMG + name)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        if fmt == 'JPEG':
            b = Image.new('RGB', im.size, bg); b.paste(im, mask=im.split()[3]); im = b
    else:
        im = im.convert('RGB')
    if ratio:  # crop to width/height ratio
        W, H = im.size
        if W / H > ratio:
            nw = int(H * ratio); x = (W - nw) // 2; im = im.crop((x, 0, x + nw, H))
        else:
            nh = int(W / ratio); y = int((H - nh) * focus); im = im.crop((0, y, W, y + nh))
    if w and im.width > w:
        im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if fmt == 'PNG': im.save(buf, 'PNG', optimize=True); mt = 'png'
    else: im.save(buf, 'JPEG', quality=q, optimize=True); mt = 'jpeg'
    return f'data:image/{mt};base64,' + base64.b64encode(buf.getvalue()).decode()

CSS = r'''
@page { size: 148mm 210mm; margin: 16mm 14mm 18mm 14mm; }
@page cover { margin: 0; }
:root { --ink:#2b2622; --muted:#7a6f63; --accent:#2f8f83; --gold:#b08d57; --paper:#ffffff; }
* { box-sizing: border-box; }
html, body { margin:0; padding:0; background: var(--paper); color: var(--ink); }
body { font-family: 'Lora', serif; font-size: 9.4pt; line-height: 1.6; }
h1,h2,h3,.sans { font-family: 'Be Vietnam Pro', sans-serif; }
.cover { page: cover; height: 210mm; width: 148mm; position: relative; overflow: hidden; break-after: page;
  background: linear-gradient(160deg, #e9f4f1 0%, #fbf8f2 55%, #f3ead9 100%); }
.cover img.hero { position:absolute; right:-6mm; bottom:0; height: 150mm; }
.cover .t { position:absolute; left: 12mm; top: 16mm; width: 92mm; }
.cover .series { font-family:'Be Vietnam Pro'; letter-spacing: .28em; font-size: 8pt; color: var(--accent); text-transform: uppercase; }
.cover .act { font-family:'Be Vietnam Pro'; font-weight:600; font-size: 11pt; color: var(--gold); margin-top: 10mm; }
.cover h1 { font-size: 25pt; line-height: 1.18; margin: 2mm 0 4mm; font-weight: 700; color:#23413d; }
.cover .sub { font-style: italic; color: var(--muted); font-size: 10pt; }
.cover .foot { margin-top: 5mm; font-family:'Be Vietnam Pro'; font-size:7.5pt; color: var(--muted); width: 60mm; line-height:1.5 }
.sec { break-before: page; }
.sec-title { font-family:'Be Vietnam Pro'; font-weight:700; font-size: 15pt; color:#23413d; margin: 0 0 1mm; }
.sec-kicker { font-family:'Be Vietnam Pro'; letter-spacing:.22em; font-size:7.5pt; color: var(--accent); text-transform: uppercase; }
.rule { height:1px; background: linear-gradient(90deg, var(--gold), transparent); margin: 3mm 0 5mm; }
.cast { display:flex; gap: 3.5mm; margin-bottom: 3.6mm; break-inside: avoid; align-items: flex-start; }
.cast .av { width: 15mm; height: 15mm; border-radius: 50%; flex: none; background: #e7efe9; border: 1px solid #d9cdb8;
  overflow:hidden; display:flex; align-items:center; justify-content:center; font-family:'Be Vietnam Pro'; font-weight:700; color: var(--accent); font-size: 12pt; }
.cast .av img { width:100%; height:100%; object-fit: cover; }
.cast .nm { font-family:'Be Vietnam Pro'; font-weight:600; font-size: 10pt; }
.cast .rl { font-family:'Be Vietnam Pro'; font-size: 7.5pt; color: var(--gold); text-transform: uppercase; letter-spacing:.1em; }
.cast .ds { font-size: 9.4pt; line-height: 1.55; margin-top: .6mm; }
.toc a { color: inherit; text-decoration: none; }
.toc .row { display:flex; align-items: baseline; gap: 2mm; padding: 1.6mm 0; border-bottom: 1px dotted #d9cdb8; }
.toc .lab { font-family:'Be Vietnam Pro'; font-size: 8pt; color: var(--accent); width: 20mm; flex:none; }
.toc .ttl { flex:1; }
.chapter { break-before: page; }
.banner { width: 100%; height: 44mm; border-radius: 2.5mm; overflow:hidden; position: relative; margin-bottom: 6mm; }
.banner img { width:100%; height:100%; object-fit: cover; display:block; }
.banner::after { content:''; position:absolute; inset:0; background: linear-gradient(180deg, rgba(0,0,0,0) 45%, rgba(20,30,28,.35)); }
.ch-label { font-family:'Be Vietnam Pro'; letter-spacing:.24em; font-size: 8pt; color: var(--accent); text-transform: uppercase; text-align:center; }
.ch-title { font-family:'Be Vietnam Pro'; font-weight: 700; font-size: 17pt; text-align:center; margin: 1mm 0 1mm; color:#23413d; line-height:1.25 }
.ch-quest { text-align:center; font-family:'Be Vietnam Pro'; font-size: 7.5pt; color: var(--muted); margin-bottom: 5mm; }
.ch-quest::before, .ch-quest::after { content: ' ✦ '; color: var(--gold); }
.log { border-left: 2px solid var(--gold); background: #f4eee2; padding: 2.5mm 3.5mm; font-style: italic; font-size: 9.3pt; color: #5b5147; margin: 0 0 5mm; line-height:1.55; }
.log::before { content: 'Nhật ký nhiệm vụ'; display:block; font-style: normal; font-family:'Be Vietnam Pro'; font-size: 6.8pt; letter-spacing:.18em; text-transform: uppercase; color: var(--gold); margin-bottom: .8mm; }
p { margin: 0 0 1.9mm; text-align: justify; text-indent: 0; hyphens: auto; orphans: 2; widows: 2; }
p.n { text-indent: 5mm; }
p.v { text-align:center; font-style: italic; color: #3e5f5a; }
p.end { text-align:center; font-style: italic; color: var(--muted); margin-top: 8mm; }
.brk { text-align:center; color: var(--gold); letter-spacing: .6em; margin: 4mm 0; font-size: 9pt; }
.brk.big { margin: 7mm 0; }
em { color: #4e6f69; }
.note { font-size: 8.4pt; color: var(--muted); line-height: 1.55; }
/* profile */
.prof { break-before: page; }
.prof .top { display:flex; gap: 5mm; align-items: stretch; }
.prof .pic { width: 52mm; height: 74mm; flex:none; border-radius: 3mm; overflow:hidden; background: linear-gradient(160deg,#e3efeb,#f3ead9); border:1px solid #e1d6c3; display:flex; align-items:center; justify-content:center; }
.prof .pic img { width:100%; height:100%; object-fit: cover; object-position: top center; }
.prof .pic .ph { font-family:'Be Vietnam Pro'; font-weight:700; font-size: 34pt; color: #b9cfc8; }
.prof .meta { flex:1; display:flex; flex-direction:column; }
.prof h2 { font-size: 19pt; margin: 0; color:#23413d; line-height:1.15 }
.prof .title { font-style: italic; color: var(--gold); margin: 1mm 0 3mm; font-size: 10pt; }
.prof table { border-collapse: collapse; font-family:'Be Vietnam Pro'; font-size: 8pt; width:100%; }
.prof td { padding: 1.2mm 0; border-bottom: 1px solid #e8dfcf; vertical-align: top; }
.prof td:first-child { color: var(--muted); width: 22mm; }
.prof h3 { font-size: 8.5pt; letter-spacing:.18em; text-transform: uppercase; color: var(--accent); margin: 5mm 0 1.5mm; }
.prof p { font-size: 9.8pt; line-height:1.62; }
.prof .first { font-family:'Be Vietnam Pro'; font-size:7.5pt; color: var(--muted); margin-top:auto; padding-top: 2mm; }
'''

def esc(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    return s

def parse(path):
    chs = []; cur = None
    for raw in open(path, encoding='utf-8').read().split('\n'):
        l = raw.rstrip()
        if l.startswith('#CH|'):
            _, lab, title, img, quest = l.split('|')
            cur = dict(label=lab, title=title, img=img, quest=quest, log=None, body=[]); chs.append(cur); continue
        if cur is None or not l: continue
        if l == '---': cur['body'].append(('brk', '')); continue
        if l == '***': cur['body'].append(('bigbrk', '')); continue
        if l.startswith('>'):
            t = l[1:].strip()
            if cur['log'] is None and not cur['body'] and cur['label'] != 'Lời Mở Đầu':
                cur['log'] = t
            elif t.startswith('(Hết'): cur['body'].append(('end', t))
            else: cur['body'].append(('v', t))
            continue
        cur['body'].append(('p', l))
    return chs

def chapter_html(i, c):
    out = [f'<section class="chapter" id="ch{i}">']
    f = 0.3 if 'card' in c['img'] else (0.12 if 'splash' in c['img'] else 0.2)
    out.append(f'<div class="banner"><img src="{data_uri(c["img"], w=1100, ratio=1100/520, focus=f)}"></div>')
    out.append(f'<div class="ch-label">{esc(c["label"])}</div><div class="ch-title">{esc(c["title"])}</div>')
    out.append(f'<div class="ch-quest">{esc(c["quest"])}</div>')
    if c['log']: out.append(f'<div class="log">{esc(c["log"])}</div>')
    for k, t in c['body']:
        if k == 'brk': out.append('<div class="brk">◇ ◇ ◇</div>')
        elif k == 'bigbrk': out.append('<div class="brk big">✦</div>')
        elif k == 'v': out.append(f'<p class="v">{esc(t)}</p>')
        elif k == 'end': out.append(f'<p class="end">{esc(t)}</p>')
        else:
            cls = '' if t.startswith('“') or t.startswith('*(') else ' class="n"'
            out.append(f'<p{cls}>{esc(t)}</p>')
    out.append('</section>')
    return '\n'.join(out)

def cast_html(cast):
    out = ['<section class="sec"><div class="sec-kicker">Trước khi đọc</div><div class="sec-title">Nhân vật xuất hiện</div><div class="rule"></div>']
    for c in cast:
        av = f'<img src="{data_uri(c["img"], w=200, ratio=1, focus=0.1)}">' if c.get('img') else html.escape(c['name'][0])
        out.append(f'<div class="cast"><div class="av">{av}</div><div><div class="rl">{esc(c["role"])}</div><div class="nm">{esc(c["name"])}</div><div class="ds">{esc(c["desc"])}</div></div></div>')
    out.append('</section>')
    return '\n'.join(out)

def toc_html(chs):
    out = ['<section class="sec toc"><div class="sec-kicker">Mục lục</div><div class="sec-title">Các chương</div><div class="rule"></div>']
    for i, c in enumerate(chs):
        out.append(f'<a href="#ch{i}"><div class="row"><span class="lab">{esc(c["label"])}</span><span class="ttl">{esc(c["title"])}</span></div></a>')
    out.append('<p class="note" style="margin-top:6mm">Toàn bộ lời thoại được lấy từ bản tiếng Việt chính thức của trò chơi. Ở những đoạn người chơi được chọn câu trả lời, truyện chọn một lựa chọn duy nhất. Phần dẫn truyện chỉ mô tả lại những gì diễn ra trong game.</p>')
    out.append('</section>')
    return '\n'.join(out)

def cover_html(series, act, title, sub, hero, foot):
    return (f'<section class="cover"><img class="hero" src="{data_uri(hero, w=900, fmt="PNG")}">'
            f'<div class="t"><div class="series">{esc(series)}</div><div class="act">{esc(act)}</div><h1>{esc(title)}</h1><div class="sub">{esc(sub)}</div><div class="foot">{esc(foot)}</div></div></section>')

def render(body, out_pdf, footer_label):
    doc = f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
    hp=os.path.join(tempfile.gettempdir(), out_pdf.split('/')[-1].replace('.pdf','.html')); open(hp, 'w', encoding='utf-8').write(doc)
    subprocess.run(['node', HERE + 'pdf.js', hp, out_pdf, html.escape(footer_label)], check=True)

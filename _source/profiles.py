import sys, html
from build import *

OUT = '/mnt/project-files/LN/'
from characters import P, UPDATED

def page(c):
    if c['img']:
        pic = f'<img src="{data_uri(c["img"], w=620, ratio=52/74, focus=1.0 if "card" in c["img"] else 0.0)}">'
    else:
        pic = f'<div class="ph">{html.escape(c["name"][0])}</div>'
    rows = ''.join(f'<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>' for k, v in c['info'])
    return (f'<section class="prof"><div class="top"><div class="pic">{pic}</div><div class="meta">'
            f'<div class="sec-kicker">Hồ sơ nhân vật</div><h2>{esc(c["name"])}</h2><div class="title">{esc(c["title"])}</div>'
            f'<table>{rows}</table></div></div>'
            f'<h3>Là ai</h3><p>{esc(c["who"])}</p><h3>Xuất thân</h3><p>{esc(c["origin"])}</p>'
            f'<h3>Vai trò trong cốt truyện</h3><p>{esc(c["role"])}</p></section>')

intro = ('<section class="sec"><div class="sec-kicker">Mục lục</div><div class="sec-title">Danh sách nhân vật</div><div class="rule"></div>'
         + ''.join(f'<div class="toc"><div class="row"><span class="lab">{i+1:02d}</span><span class="ttl">{esc(c["name"])} — <em>{esc(c["title"])}</em></span></div></div>' for i, c in enumerate(P))
         + f'<p class="note" style="margin-top:6mm">{UPDATED}. Hồ sơ chỉ ghi những gì đã xuất hiện trong các màn đã viết, kèm thông tin hồ sơ chính thức trong game (danh hiệu, Vision, sinh nhật, cung mệnh). Sẽ được bổ sung sau mỗi màn mới.</p></section>')
body = cover_html('Genshin Impact · Light Novel', 'Phụ lục', 'Hồ Sơ Nhân Vật', UPDATED, 'traveler_portrait.png',
                  'Tài liệu tra cứu đi kèm bộ light novel. Thông tin hồ sơ lấy từ bản tiếng Việt chính thức của game.') + intro + ''.join(page(c) for c in P)
render(body, OUT + 'GenshinLN_HoSoNhanVat.pdf', 'Hồ Sơ Nhân Vật — ' + UPDATED)
print('ok')

import sys, os
from build import *
from acts import *

D = HERE
OUT = '/mnt/project-files/LN/'
os.makedirs(OUT, exist_ok=True)

def build_act(src, act, title, sub, hero, cast, out, footer):
    chs = parse(D + src)
    body = cover_html(SERIES, act, title, sub, hero, FOOT) + cast_html(cast) + toc_html(chs) + '\n'.join(chapter_html(i, c) for i, c in enumerate(chs))
    render(body, OUT + out, footer)
    print('built', out, len(chs))

# Dùng: python make.py man1 man1-1   (id trong acts.py)
if __name__ == '__main__':
    for a in ACTS:
        if a['id'] in sys.argv[1:] or a['id'].replace('-', '') in sys.argv[1:]:
            build_act(a['src'], a['act'], a['title'], a['sub'], a['hero'], a['cast'], a['pdf'], a['footer'])

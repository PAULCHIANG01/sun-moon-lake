"""Copy ../網站 (the Claude Artifact source) into this GitHub Pages folder.

The Artifact platform wraps the page in <!doctype html><head>…<body> and a small CSS reset
at publish time; GitHub Pages does not, so this adds them.
Run:  python build.py   then commit and push.
"""
import os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '網站')

os.makedirs(os.path.join(HERE, 'img'), exist_ok=True)
for f in os.listdir(os.path.join(SRC, 'img')):
    shutil.copy2(os.path.join(SRC, 'img', f), os.path.join(HERE, 'img', f))

s = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()
s = '\n'.join(l for l in s.split('\n') if 'claude:viewport-fit-sides' not in l and l.strip() != '<meta charset="utf-8">')
head_end = s.index('<style>')
style_end = s.index('</style>') + len('</style>')
reset = '''<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>
'''
out = ('<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n' + s[:head_end] + reset
       + s[head_end:style_end] + '\n</head>\n<body>\n' + s[style_end:].lstrip('\n') + '\n</body>\n</html>\n')
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8', newline='\n').write(out)
print('built index.html', len(out) // 1024, 'KB')

import re, sys, os, subprocess, glob
def plain(path, accent):
    h=open(path).read()
    m=re.search(r'</helmet>\s*(.*)\s*</x-dc>', h, re.S)
    body=m.group(1).replace('{{accent}}', accent).replace('{{ accent }}', accent)
    F='/tmp/fonts/node_modules/@fontsource'
    ff=''.join(f"@font-face{{font-family:'Plus Jakarta Sans';font-weight:{w};src:url(file://{F}/plus-jakarta-sans/files/plus-jakarta-sans-latin-{w}-normal.woff2)}}@font-face{{font-family:'Noto Sans Thai';font-weight:{w};src:url(file://{F}/noto-sans-thai/files/noto-sans-thai-thai-{w}-normal.woff2)}}" for w in (400,700))
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{ff}body{{margin:0}}</style></head><body>{body}</body></html>'
def render(src, out, W, H, accent):
    p=out.replace('.png','.html'); open(p,'w').write(plain(src, accent))
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--disable-gpu','--hide-scrollbars','--allow-file-access-from-files','--force-device-scale-factor=1',f'--window-size={W},{H}','--virtual-time-budget=4000',f'--screenshot={out}','file://'+p],check=True,capture_output=True,timeout=90)
if __name__=='__main__':
    d, outd, W, H, accent = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    os.makedirs(outd, exist_ok=True)
    for f in sorted(glob.glob(f'{d}/AI_45_*.dc.html')):
        n=re.search(r'AI_45_(\w+)\.dc',f).group(1)
        render(f, f'{outd}/card{n}.png', W, H, accent); print(n)

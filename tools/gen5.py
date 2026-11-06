import json, os, re
exec(open('/home/claude/gen.py').read().split("def footer")[0])  # page(), F, SANS, SERIF
MACRO = dict(label="Macro Daily", accent="#BFDDF2", why="Why markets care", pre="M",
 cover_head="AI selloff shakes global markets", cover_ph="city financial district",
 items=["Wall Street's worst day since April 2025","Asia follows: Kospi −8%, trading halted","US jobs report lands 20:30 Bangkok time","Investors rush to safety: gold and bonds","Bitcoin falls with tech stocks"],
 S=[
 (2,"US · Equities","−4.4%","S&amp;P 500","Wall Street's worst day since April 2025","","Nasdaq −5.5%; about $2.5T erased from the Nasdaq 100","Fears that Democratic midterm gains could slow the AI data-centre build-out","CNN, AP","Wall Street, New York"),
 (3,"Asia · Equities","−8%","Kospi","Asia follows Wall Street down","","Nikkei in bear market; Thailand's SET −1.13% to 1,481","Chip leaders Samsung and SK Hynix fell more than 9% at the open","The Nation Thailand, Fox Business, CNBC-TV18","Seoul or Tokyo skyline"),
 (4,"US · Rates and Fed","65K","October payrolls, consensus","US jobs report lands 20:30 Bangkok time","","Unemployment 4.2% and wage growth below 3% expected","A firm print could revive December Fed hike bets","Reuters, Morningstar","Federal Reserve building"),
 (5,"Global · Safe havens","4.84%","10-year Treasury yield","Investors rush to safety","","Gold at $4,092; VIX up 65% to 27.1","Bonds and gold are being bought while equities fall","CNN, Motley Fool, Vantage","gold bars"),
 (6,"Global · Crypto","$75,220","Bitcoin","Bitcoin falls with tech stocks","","Low on 5 Nov, its lowest since mid-September, after a rebound above $81K","Crypto is trading with the AI-builder complex, not as a hedge","Benzinga, Ted Pillows","bitcoin coin"),
 ],
 mood="fearful", quote="Be fearful when others are greedy, and be greedy when others are fearful.", who="Warren Buffett", by="The New York Times · 2008", qph="stormy sky clearing over a city", qsize=58)
AI = dict(label="AI &amp; Web3 Daily", accent="#F7C9A8", why="Why it matters", pre="AI",
 cover_head="AI's build-out is hitting limits", cover_ph="data centre at night",
 items=["Anthropic files for a Nasdaq IPO","Microsoft passes on doubling Nscale deal","China slows chip and AI listings","Thai SEC drafts crypto derivatives rules","Thailand tightens data centre rules"],
 S=[
 (2,"US · AI Companies","$16.3B","H1 2026 revenue","Anthropic files for a Nasdaq IPO","","Up from $1.2B a year earlier. Net loss of $80.7B is mostly non-cash; Q2 was its first operating profit.","The first full look at what frontier AI costs to run","Reuters via Yahoo Finance, The Next Web (filed 26 Oct)","data centre racks"),
 (3,"Global · AI Infrastructure","$35B","Nscale planned IPO","Microsoft passes on doubling its Nscale deal","","The original deal, worth tens of billions, covers AI capacity tied to a Texas contract.","Even the biggest buyers are rationing AI capacity commitments","FT via AI Weekly","server hall"),
 (4,"Asia · Semiconductors","$4.9B","YMTC Shanghai IPO, paused","China slows chip and AI listings","","The chip-AI stock index is down about 40% from its July peak.","Funding for China's AI chip push is getting tighter","Reuters","chip fabrication"),
 (5,"Thailand · Digital Assets","28 Nov","comment deadline","Thai SEC drafts crypto derivatives rules","","Eight draft notifications are open for public comment.","Sets the framework for regulated crypto derivatives in Thailand","Thailand Business News, TechFlow","Bangkok skyline"),
 (6,"Thailand · Data Centres","49","projects asked to pause","Thailand tightens data centre rules","","Draft power tariff of about THB 5–6/kWh vs THB 3 for households. Rules expected in Q4.","Power costs now decide where AI capacity gets built","Eco-Business, Bloomberg via AI Weekly","power lines and data centre"),
 ],
 mood="cautious", quote="We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run.", who="Roy Amara", by="Institute for the Future · Amara's Law", qph="fog lifting over a city skyline", qsize=54)

def build(c, W, H, d, kind):
    A=c["accent"]; T=c["accent"]; L=c["label"]
    root=lambda bg,inner: f'<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {bg}; display: flex; flex-direction: column; font-family: {SANS}; color: #233F45">{inner}</div>'
    ph=lambda h,lab,w=None: f'<div style="position: relative; {"width: %dpx; "%w if w else ""}height: {h}px; flex: none; background: #DDE3E6; display: flex; align-items: center; justify-content: center; color: #4A5F63; font-size: 28px">[Photo · {lab}]</div>'
    credit=lambda pos: f'<div style="position: absolute; {pos}; padding: 8px 20px; border-radius: 9999px; background: #FFFFFF; font-size: 22px; color: #4A5F63">Photo: [credit]</div>'
    datepill=lambda t,pos="top: 56px; left: 86px": f'<div style="position: absolute; {pos}; padding: 12px 28px; border-radius: 9999px; background: #FFFFFF; font-size: 24px; font-weight: 700; color: #233F45">{t}</div>'
    pill=lambda t: f'<div style="align-self: flex-start; padding: 10px 28px; border-radius: 9999px; background: {{{{accent}}}}; font-size: 24px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #233F45">{t}</div>'
    ft=lambda n: f'<div style="display: flex; align-items: center; gap: 16px"><div style="width: 14px; height: 14px; border-radius: 50%; background: #F0937B"></div><div style="font-size: 24px; font-weight: 700">@siraptn</div><div style="flex: 1; height: 6px; border-radius: 9999px; background: {{{{accent}}}}"></div><div style="font-size: 24px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #1F6F78">{L} · {n}/7</div></div>'
    rows=lambda size=30,pad=9,circ=44,items=None: ''.join(f'<div style="display: flex; align-items: center; gap: 24px; padding: {pad}px 0; border-top: 2px solid #E9E3D6"><div style="width: {circ}px; height: {circ}px; flex: none; border-radius: 50%; background: {{{{accent}}}}; display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 700">{i+1}</div><div style="font-size: {size}px; font-weight: 700; line-height: 1.2">{t}</div></div>' for i,t in enumerate(items or c["items"]))
    sheet=lambda top,inner,bg="#FFFFFF",col="#233F45": f'<div style="position: absolute; left: 0; right: 0; top: {top}px; bottom: 0; box-sizing: border-box; border-radius: 56px 56px 0 0; background: {bg}; color: {col}; padding: 48px 86px 52px 86px; display: flex; flex-direction: column; justify-content: space-between">{inner}</div>'
    if kind=="cover":
        return root("#FFFFFF", f'{ph(700+d,c["cover_ph"])}{datepill("FRI 6 NOV 2026")}{credit("top: %dpx; left: 86px"%(560+d))}'+sheet(640+d, f'<div style="display: flex; flex-direction: column; gap: 16px">{pill(L)}<div style="font-size: 68px; font-weight: 700; line-height: 1.08">{c["cover_head"]}</div></div><div style="display: flex; flex-direction: column">{rows()}</div>{ft(1)}'))
    if kind=="wide":
        return root("#FFFFFF", f'<div style="display: flex; height: {H}px"><div style="position: relative; width: 760px; flex: none">{ph(H,c["cover_ph"],760)}{datepill("FRI 6 NOV 2026","top: 40px; left: 48px")}{credit("bottom: 28px; left: 48px")}</div><div style="flex: 1; box-sizing: border-box; padding: 48px 56px 40px 56px; display: flex; flex-direction: column; justify-content: space-between"><div style="display: flex; flex-direction: column; gap: 14px">{pill(L)}<div style="font-size: 54px; font-weight: 700; line-height: 1.08">{c["cover_head"]}</div></div><div style="display: flex; flex-direction: column">{rows(26,7,38)}</div><div style="display: flex; align-items: center; gap: 12px"><div style="width: 12px; height: 12px; border-radius: 50%; background: #F0937B"></div><div style="font-size: 22px; font-weight: 700">@siraptn</div><div style="flex: 1; height: 5px; border-radius: 9999px; background: {{{{accent}}}}"></div></div></div></div>')
    if kind=="quote":
        return root("#FFFFFF", f'{ph(700+d,c["qph"])}{datepill("6 NOV 2026")}{credit("top: %dpx; left: 86px"%(560+d))}'+sheet(640+d, f'<div style="display: flex; flex-direction: column; gap: 24px"><div style="align-self: flex-start; padding: 10px 28px; border-radius: 9999px; background: {T}; font-size: 24px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #233F45">Today\'s mood: {c["mood"]}</div><div style="font-size: {c["qsize"]}px; font-weight: 700; line-height: 1.2">“{c["quote"]}”</div><div><div style="font-size: 32px; font-weight: 700">{c["who"]}</div><div style="font-size: 26px; color: {T}">{c["by"]}</div></div></div><div style="display: flex; flex-direction: column; gap: 16px"><div style="align-self: flex-start; padding: 14px 32px; border-radius: 9999px; background: {T}; color: #233F45; font-size: 30px; font-weight: 700">Follow @siraptn</div><div style="font-size: 22px; color: {T}">Not investment advice</div></div>', "#233F45", "#FFFFFF"))
    n,tag,hero,hl,head,soft,ctx,why,src,pl = kind
    return root("#FFFFFF", f'{ph(600+d,pl)}{datepill(f"{n} / 7","top: 56px; right: 86px")}{credit("top: 56px; left: 86px")}'+sheet(500+d, f'<div style="display: flex; flex-direction: column; gap: 14px">{pill(tag)}<div style="display: flex; align-items: baseline; gap: 24px"><div style="font-size: 150px; font-weight: 700; line-height: 1; letter-spacing: -0.03em">{hero}</div><div style="font-size: 28px; line-height: 1.3; color: #4A5F63">{hl}</div></div><div style="font-size: 46px; font-weight: 700; line-height: 1.2">{head}</div><div style="font-size: 28px; line-height: 1.4; color: #4A5F63">{ctx}</div><div style="padding: 20px 28px; border-radius: 24px; background: {T}"><div style="font-size: 22px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #1F6F78">{c["why"]}</div><div style="font-size: 28px; font-weight: 700; line-height: 1.3">{c["why"] and why}</div></div></div><div style="display: flex; flex-direction: column; gap: 12px"><div style="font-size: 22px; color: #4A5F63">Source: {src}</div>{ft(n)}</div>')) 

def doc(c, title, inner, W, H):
    html = page(title, inner).replace('"default":"#BFDDF2"', f'"default":"{c["accent"]}"').replace("?? '#BFDDF2'", f"?? '{c['accent']}'")
    return html.replace('"width":1080,"height":1350', f'"width":{W},"height":{H}')

def make(c, outdir, sets):
    os.makedirs(outdir, exist_ok=True)
    boards = {}; order=[]; notes={}
    def add(nm, html, x, y, w, h, title):
        open(f"{outdir}/{nm}","w").write(html); boards[nm]={"x":x,"y":y,"w":w,"h":h,"title":title}; order.append(nm)
    y=0; ni=1
    for (key, name, W, H, d, hasset, tnote) in sets:
        notes[f"t{ni}"]={"kind":"title1","maxW":8040,"text":tnote,"x":0,"y":y-300}; ni+=1
        if hasset:
            seq=[("1","cover","Cover")]+[(str(s[0]),s,f"Story {s[0]-1}") for s in c["S"]]+[("7","quote","Quote")]
            for i,(num,k,t) in enumerate(seq):
                add(f'{c["pre"]}_{key}_{num}.dc.html', doc(c, f"{name} {num}", build(c,W,H,d,k), W, H), i*(W+80), y, W, H, f"{name} · {num} {t}")
        else:
            add(f'{c["pre"]}_{key}_1.dc.html', doc(c, f"{name} cover", build(c,W,H,d,"cover"), W, H), 0, y, W, H, f"{name} · Cover")
        y += H+420
    return boards, order, notes

def make2(c, outdir, y0, rows):
    os.makedirs(outdir, exist_ok=True)
    boards={}; order=[]; notes={}
    def add(nm, html, x, y, w, h, title):
        open(f"{outdir}/{nm}","w").write(html); boards[nm]={"x":x,"y":y,"w":w,"h":h,"title":title}; order.append(nm)
    y=y0
    for ri,(key,label,items,rh) in enumerate(rows):
        notes[f"{c['pre']}t{ri}"]={"kind":"title1","maxW":8040,"text":label,"x":0,"y":y-300}
        x=0
        for (name,W,H,d,kind,num) in items:
            nm=f'{c["pre"]}_{key}_{name}.dc.html'
            add(nm, doc(c, f"{key} {name}", build(c,W,H,d,kind), W, H), x, y, W, H, f'{c["label"].replace("&amp;","&")} · {key} · {name}')
            x+=W+80
        y+=rh+420
    return boards, order, notes
def rows_for(c):
    S=c["S"]
    def setrow(W,H,d):
        it=[("1",W,H,d,"cover",1)]+[(str(s[0]),W,H,d,s,s[0]) for s in S]+[("7",W,H,d,"quote",7)]
        return it
    return [
     ("45","4:5 · Instagram, LinkedIn · 1080×1350",setrow(1080,1350,0),1350),
     ("34","3:4 · Lemon8, Rednote · 1080×1440",setrow(1080,1440,90),1440),
     ("916","9:16 cover (TikTok, Reels, Shorts, 1080×1920) and 16:9 image (X, YouTube, 1600×900)",[("cover",1080,1920,570,"cover",1),("wide",1600,900,0,"wide",1)],1920),
    ]

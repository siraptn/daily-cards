import re, json, os, sys
src=open('/home/claude/gen5.py').read()
SHADE="linear-gradient(to top, rgba(35,63,69,0.92) 0%, rgba(35,63,69,0.78) 38%, rgba(35,63,69,0) 72%)"
NEW916 = '''if kind=="cover" and H==1920:
        return root("#233F45", f'{ph(1920,c["cover_ph"],1080)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 86px; top: 1080px; display: flex; flex-direction: column; gap: 28px"><div style="font-size: 30px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Sat 7 Nov 2026</div><div style="font-size: 118px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 300px; left: 86px")}')
    '''
NEWWIDE = '''if kind=="wide":
        return root("#233F45", f'{ph(900,c["cover_ph"],1600)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 200px; bottom: 96px; display: flex; flex-direction: column; gap: 20px"><div style="font-size: 26px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Sat 7 Nov 2026</div><div style="font-size: 96px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 40px; left: 86px")}')
    if False:'''
src=src.replace('FRI 6 NOV 2026','SAT 7 NOV 2026').replace('"6 NOV 2026"','"7 NOV 2026"')
# placeholder photo + credit -> real photos
src=src.replace('''ph=lambda h,lab,w=None: f'<div style="position: relative; {"width: %dpx; "%w if w else ""}height: {h}px; flex: none; background: #DDE3E6; display: flex; align-items: center; justify-content: center; color: #4A5F63; font-size: 28px">[Photo · {lab}]</div>\'''','''ph=lambda h,lab,w=None: PHOTO(h,lab,w)''')
src=src.replace('''credit=lambda pos: f'<div style="position: absolute; {pos}; padding: 8px 20px; border-radius: 9999px; background: #FFFFFF; font-size: 22px; color: #4A5F63">Photo: [credit]</div>\'''','''credit=lambda pos: CREDIT(pos)''')
src=src.replace('if kind=="cover":', NEW916+'if kind=="cover":',1)
src=src.replace('if kind=="wide":', NEWWIDE,1)
assert 'PHOTO(h,lab,w)' in src and 'CREDIT(pos)' in src

src=src.replace('credit("top: 56px; left: 86px")','credit("top: %dpx; left: 86px"%(448+d))')
src=src.replace('datepill=lambda t,pos="top: 56px; left: 86px"','datepill=lambda t,pos="top: 56px; left: 176px"')
src=src.replace('"top: 40px; left: 48px")','"top: 40px; left: 138px")')
src=src.replace("root=lambda bg,inner: f'<div style=\"width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {bg}; display: flex; flex-direction: column; font-family: {SANS}; color: #233F45\">{inner}</div>'",
 "root=lambda bg,inner: f'<div style=\"width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {bg}; display: flex; flex-direction: column; font-family: {SANS}; color: #233F45\">{inner}</div>'.replace('</div>', ICON(kind)+'</div>', 1) if False else f'<div style=\"width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {bg}; display: flex; flex-direction: column; font-family: {SANS}; color: #233F45\">{inner}{ICON(kind)}</div>'")
assert 'ICON(kind)' in src
def ICON(kind):
    pos='top: 40px; left: 48px' if kind=='wide' else 'top: 48px; left: 86px'
    return f'<div style="position: absolute; {pos}; width: 72px; height: 72px; border-radius: 50% 4px 50% 50%; background: #233F45; display: flex; align-items: center; justify-content: center; color: #FFFFFF; font-family: \'Instrument Serif\', Georgia, serif; font-style: italic; font-size: 46px; line-height: 1; padding-bottom: 6px; box-sizing: border-box">Si<div style="position: absolute; top: 20px; right: 17px; width: 7px; height: 7px; border-radius: 50%; background: #F0937B"></div></div>'
exec(src)
PH={ # key: (file id, credit, bg-position)
 'wyo':('4508751','Brett Sayles','center'),
 'oai':('5203849','Brett Sayles','center'),
 'thdc':('17489153','panumas nikhomkhai','center'),
 'sol':('11262197','Markus Winkler','center 35%'),
 'hk':('785418','Jonas Svidras','center'),
 'qte':('20020757','Markus Winkler','center 60%'),
}
URLS={}   # key -> url, set per render mode
CUR=[None]
def PHOTO(h,lab,w=None):
    CUR[0]=lab; fid,cr,pos=PH[lab]
    return f'<div style="position: relative; {"width: %dpx; "%w if w else ""}height: {h}px; flex: none; background: #DDE3E6 url({URLS[fid]}) {pos} / cover no-repeat"></div>'
def CREDIT(pos):
    fid,cr,_=PH[CUR[0]]
    return f'<div style="position: absolute; {pos}; font-size: 22px; font-weight: 500; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 3px rgba(0,0,0,0.9), 0 1px 10px rgba(0,0,0,0.75)">Photo: {cr} / Pexels</div>'
AI['cover_ph']='wyo'; AI['qph']='qte'
AI['cover_head']="Google commits $17B to Wyoming"
AI['mood']="curious"; AI['quote']="Any sufficiently advanced technology is indistinguishable from magic."; AI['who']="Arthur C. Clarke"; AI['by']="Profiles of the Future · 1973"; AI['qsize']=58
AI['items']=["Google to invest $17B in Wyoming data centre","OpenAI says business grew 70% in Q3","Zhi Sheng backs Thailand AI data centre","Solana tokenized stocks hit $657M in a day","Hong Kong approves 17 tokenized products"]
AI['S']=[
 (2,"US · AI Infrastructure","$17B","Google, first Wyoming data centre","Google to invest $17B in a Wyoming data centre","","Google said on Thursday 5 Nov that it will build its first data centre in Wyoming. Reuters reported it on 6 Nov.","A new US site was committed the same week OpenAI said it will end NDAs with local officials","Reuters via Investing.com (6 Nov)","oai"),
 (3,"US · AI Companies","70%","OpenAI growth, Q3 vs Q2","OpenAI says its business grew 70% in Q3","","CFO Sarah Friar told CNBC that enterprise demand doubled over the same period. The figures are the company's own.","OpenAI says it will keep building out data centres","Reuters via Investing.com (6 Nov)","oai"),
 (4,"Thailand · AI Data Centres","$1.6B","10-year colocation contract, excl. power","Zhi Sheng lines up a loan for its Thailand AI data centre","","The loan was announced as US$590M; its chairman cited US$580M. Phase one, about a third of capacity, is due in early 2027.","Thailand's Eastern Economic Corridor gains a contract-backed AI site","DataCenterNews Asia (6 Nov)","thdc"),
 (5,"Global · Tokenization","$657M","Solana tokenized stocks, 2 Nov","Solana tokenized stock trading hits $657M in a day","","Backpack Securities made up $598M, about 91%. It is the highest since June.","It is trading volume, not the amount invested","COINTURK News (5 Nov)","sol"),
 (6,"Hong Kong · Tokenization","17","tokenized products approved for retail","Hong Kong has approved 17 tokenized products for retail investors","","The SFC's chief executive said they manage about $1.3B, up 34% from last year.","The figures were given at Hong Kong FinTech Week","U.Today (6 Nov), citing SCMP","hk"),
]
def write(outdir, urls, rows_only=None):
    URLS.clear(); URLS.update(urls)
    return make2(AI, outdir, 0, rows_for(AI))

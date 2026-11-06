import re, json, os, sys
src=open('/home/claude/gen5.py').read()
SHADE="linear-gradient(to top, rgba(35,63,69,0.92) 0%, rgba(35,63,69,0.78) 38%, rgba(35,63,69,0) 72%)"
NEW916 = '''if kind=="cover" and H==1920:
        return root("#233F45", f'{ph(1920,c["cover_ph"],1080)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 86px; top: 1080px; display: flex; flex-direction: column; gap: 28px"><div style="font-size: 30px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Fri 6 Nov 2026</div><div style="font-size: 118px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 300px; left: 86px")}')
    '''
NEWWIDE = '''if kind=="wide":
        return root("#233F45", f'{ph(900,c["cover_ph"],1600)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 200px; bottom: 96px; display: flex; flex-direction: column; gap: 20px"><div style="font-size: 26px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Fri 6 Nov 2026</div><div style="font-size: 96px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 40px; left: 86px")}')
    if False:'''
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
 'srv1':('4508751','Brett Sayles','center'),
 'srv2':('5203849','Brett Sayles','center'),
 'srv3':('17489153','panumas nikhomkhai','center'),
 'chip':('785418','Jonas Svidras','center'),
 'bkk1':('20020757','Markus Winkler','center 60%'),
 'bkk2':('11262197','Markus Winkler','center 35%'),
 'srv1b':('4508751','Brett Sayles','10% 50%'),
}
URLS={}   # key -> url, set per render mode
CUR=[None]
def PHOTO(h,lab,w=None):
    CUR[0]=lab; fid,cr,pos=PH[lab]
    return f'<div style="position: relative; {"width: %dpx; "%w if w else ""}height: {h}px; flex: none; background: #DDE3E6 url({URLS[fid]}) {pos} / cover no-repeat"></div>'
def CREDIT(pos):
    fid,cr,_=PH[CUR[0]]
    return f'<div style="position: absolute; {pos}; font-size: 22px; font-weight: 500; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 3px rgba(0,0,0,0.9), 0 1px 10px rgba(0,0,0,0.75)">Photo: {cr} / Pexels</div>'
AI['cover_ph']='srv1'; AI['qph']='srv1b'
AI['items']=["OpenAI pledges to pay for data centre power","Microsoft declines to double Nscale deal","Nvidia reportedly caps China cloud business","Thai SEC drafts crypto derivatives rules","Bank of Thailand eyes stablecoin rules"]
AI['S']=[
 (2,"US · AI Companies","38+","jurisdictions voted to restrict data centres","OpenAI reaffirms full power-cost pledge and drops NDAs","","It will also report water use and publish construction plans, two days after the vote.","Public backlash is now a cost of building AI capacity","The Washington Post, CNBC (5 Nov)","srv2"),
 (3,"Global · AI Infrastructure","$35B","Nscale planned IPO","Microsoft declines to double its Nscale contract","","It held an option to more than double its Texas AI capacity deal, worth tens of billions.","Even the biggest buyers are rationing AI capacity commitments","Financial Times via AI Weekly (5 Nov)","srv3"),
 (4,"Asia · AI Infrastructure","49%","cap on Chinese customers, reportedly","Nvidia reportedly tells cloud partners to cap China business","","The FT reported on 3 Nov that at least 51% of services on new contracts must go to non-Chinese firms. Nvidia has not confirmed it.","Chip access rules now reach Southeast Asia's data centres","Financial Times (3 Nov) via The Next Web, Techzine","chip"),
 (5,"Thailand · Digital Assets","28 Nov","comment deadline","Thai SEC drafts crypto derivatives rules","","Eight draft notifications are open for public comment.","Sets the framework for regulated crypto derivatives in Thailand","Thailand Business News (31 Oct), The Asian Banker (29 Oct)","bkk1"),
 (6,"Thailand · Stablecoins","5","new central bank measures, Nov 2026 to Mar 2027","Bank of Thailand to bring stablecoins under closer supervision","","The package also covers buy now pay later and gold dealers' cash payments. The stablecoin rules have not been detailed.","Thai crypto now faces two regulators moving at once, the SEC and the central bank","FinTech Global (2 Nov), citing FinTech Singapore","bkk2"),
]
def write(outdir, urls, rows_only=None):
    URLS.clear(); URLS.update(urls)
    return make2(AI, outdir, 0, rows_for(AI))

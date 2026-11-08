import re, json, os, sys
src=open('/home/claude/gen5.py').read()
SHADE="linear-gradient(to top, rgba(35,63,69,0.92) 0%, rgba(35,63,69,0.78) 38%, rgba(35,63,69,0) 72%)"
NEW916 = '''if kind=="cover" and H==1920:
        return root("#233F45", f'{ph(1920,c["cover_ph"],1080)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 86px; top: 1080px; display: flex; flex-direction: column; gap: 28px"><div style="font-size: 30px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Sun 8 Nov 2026</div><div style="font-size: 118px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 300px; left: 86px")}')
    '''
NEWWIDE = '''if kind=="wide":
        return root("#233F45", f'{ph(900,c["cover_ph"],1600)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 200px; bottom: 96px; display: flex; flex-direction: column; gap: 20px"><div style="font-size: 26px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Sun 8 Nov 2026</div><div style="font-size: 96px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 40px; left: 86px")}')
    if False:'''
src=src.replace('FRI 6 NOV 2026','SUN 8 NOV 2026').replace('"6 NOV 2026"','"8 NOV 2026"')
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
 'dc':('4508751','Brett Sayles','center'),
 'dc2':('4508751','Brett Sayles','center 80%'),
 'rack':('5203849','Brett Sayles','center'),
 'blue':('17489153','panumas nikhomkhai','center'),
 'pool':('11262197','Markus Winkler','center 35%'),
 'chip':('785418','Jonas Svidras','center'),
 'bkk':('20020757','Markus Winkler','center 60%'),
}
URLS={}
CUR=[None]
def PHOTO(h,lab,w=None):
    CUR[0]=lab; fid,cr,pos=PH[lab]
    return f'<div style="position: relative; {"width: %dpx; "%w if w else ""}height: {h}px; flex: none; background: #DDE3E6 url({URLS[fid]}) {pos} / cover no-repeat"></div>'
def CREDIT(pos):
    fid,cr,_=PH[CUR[0]]
    return f'<div style="position: absolute; {pos}; font-size: 22px; font-weight: 500; color: #FFFFFF; font-weight: 600; text-shadow: 0 0 3px rgba(0,0,0,0.9), 0 1px 10px rgba(0,0,0,0.75)">Photo: {cr} / Pexels</div>'
AI['cover_ph']='dc'; AI['qph']='pool'
AI['cover_head']="Voters push back on data centres"
AI['mood']="cautious"; AI['quote']="We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run."; AI['who']="Roy Amara"; AI['by']="Institute for the Future · Amara's Law"; AI['qsize']=54
AI['items']=["US voters favour data centre limits, 40 of 41","OpenAI reportedly closes $11B round","Thailand plans to block Bitget on 5 Dec","Nigeria sets stablecoin licensing rules","Stablecoin supply falls about $5B in a week"]
AI['S']=[
 (2,"US · AI Infrastructure","40/41","local data centre measures favoured limits, 3 Nov","US voters favour limits on data centres","","27 measures limited data centres or opposed them, including 5 full bans. Voters defeated 13 pro-development measures.","The measures covered bans, moratoriums and zoning rules in several US states","Ballotpedia News (6 Nov)","rack"),
 (3,"Global · AI Companies","$11B","OpenAI, first part of its new round, reportedly","OpenAI reportedly closes $11B at a $1.25T valuation","","Bloomberg reported on 6 Nov that a further $9B is expected in the coming weeks.","The reports do not include a statement from OpenAI","Bloomberg via Unusual Whales (6 Nov), Analytics Insight (7 Nov)","chip"),
 (4,"Thailand · Digital Assets","5 Dec","date set to block access to Bitget","Thai SEC files complaint against Bitget","","On 5 Nov it filed a criminal complaint against BG Limited, alleging unlicensed operation in 2022–2025.","The block covers access from Thailand; the case is at complaint stage","CoinGape (5 Nov), CryptoSlate and CoinIdol (7 Nov)","bkk"),
 (5,"Africa · Stablecoins","180","days for existing operators to apply for a licence","Nigeria sets stablecoin licensing rules","","Issuers need approval for each token. Foreign-currency stablecoins need a Nigerian licensed issuer. Rules took effect 5 Nov.","The central bank covers payments and FX; the SEC keeps securities activity","The Block (6 Nov)","blue"),
 (6,"Global · Stablecoins","$4.99B","weekly fall in stablecoin supply, DefiLlama","Stablecoin supply falls about $5B in a week","","Supply was $293.25B, from $298.24B a week earlier (−1.7%). Sentora shows $293.69B on 6 Nov.","Trackers measure supply differently, so figures vary","24/7 Wall St. (7 Nov), citing DefiLlama and Sentora","dc2"),
]
def write(outdir, urls, rows_only=None):
    URLS.clear(); URLS.update(urls)
    return make2(AI, outdir, 0, rows_for(AI))

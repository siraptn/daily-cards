import re, json, os, sys
src=open('/home/claude/gen5.py').read()
SHADE="linear-gradient(to top, rgba(35,63,69,0.92) 0%, rgba(35,63,69,0.78) 38%, rgba(35,63,69,0) 72%)"
NEW916 = '''if kind=="cover" and H==1920:
        return root("#233F45", f'{ph(1920,c["cover_ph"],1080)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 86px; top: 1080px; display: flex; flex-direction: column; gap: 28px"><div style="font-size: 30px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Tue 10 Nov 2026</div><div style="font-size: 118px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 300px; left: 86px")}')
    '''
NEWWIDE = '''if kind=="wide":
        return root("#233F45", f'{ph(900,c["cover_ph"],1600)}<div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background: {SHADE}"></div><div style="position: absolute; left: 86px; right: 200px; bottom: 96px; display: flex; flex-direction: column; gap: 20px"><div style="font-size: 26px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: {{{{accent}}}}">{L} · Tue 10 Nov 2026</div><div style="font-size: 96px; font-weight: 700; line-height: 1.04; color: #FFFFFF">{c["cover_head"]}</div></div>{credit("bottom: 40px; left: 86px")}')
    if False:'''
src=src.replace('FRI 6 NOV 2026','TUE 10 NOV 2026').replace('"6 NOV 2026"','"10 NOV 2026"')
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
AI['cover_ph']='dc'; AI['qph']='dc2'
AI['cover_head']="Thailand pauses 166 data centre projects"
AI['mood']="cautious"; AI['quote']="We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run."; AI['who']="Roy Amara"; AI['by']="Institute for the Future · Amara's Law"; AI['qsize']=54
AI['items']=["Thailand pauses or freezes 166 data centre projects","Anthropic reportedly takes over $3.4B of generator orders","Thai AI-linked exports: 802B baht last year","Bank of Thailand stablecoin hearing closes 17 Nov","Crypto liquidations top $1B in a day"]
AI['S']=[
 (2,"Thailand · AI Infrastructure","166","data centre projects paused or frozen, reportedly","Thailand pauses 166 data centre projects","","Construction is paused on 49 projects and approval decisions are frozen on 117 more, reportedly.","Thailand's data centre policy board made the decision at its first meeting, on 4 September 2026","ShiftDelete.Net (8 Nov), citing the Guardian (7 Nov)","rack"),
 (3,"Global · AI Infrastructure","$3.4B","generator orders Anthropic reportedly took over","Anthropic reportedly takes over $3.4B of generator orders","","The gas-powered generators total 1.7 gigawatts. The orders were taken over from Texas-based OnePWR Solutions, per the Financial Times.","Neither Anthropic nor OnePWR had publicly confirmed the deal","The Neuron (9 Nov), citing the Financial Times and Reuters","blue"),
 (4,"Thailand · AI and Economy","802B","baht of AI-linked exports last year","Thai AI-linked exports reach 802B baht","","Laptops, optical transceivers and backup power equipment made up more than 7% of Thailand's shipments.","Bloomberg-compiled estimates say the data revisions could add 0.2–0.3 points to 2026 GDP growth","VnExpress International (8 Nov), citing Bloomberg estimates","pool"),
 (5,"Thailand · Digital Assets","1:1","baht stablecoin peg proposed by the Bank of Thailand","Bank of Thailand stablecoin hearing closes 17 Nov","","The public hearing runs from 19 Oct to 17 Nov. The stablecoin would be fully backed by reserve assets.","Issuers and wallet providers would hold separate, regulated roles","Bank of Thailand public hearing page (read 10 Nov); CoinGeek (6 Nov)","bkk"),
 (6,"Global · Crypto Markets","$1B","crypto positions liquidated in 24 hours, CoinGlass","Crypto liquidations top $1B in a day","","Longs were $913M of the total. Ether saw $448M and bitcoin $272M. Bitcoin fell to about $73,761, its lowest since August.","A liquidation closes a leveraged position when price moves against it","CoinDesk (9 Nov), citing CoinGlass","chip"),
]
def write(outdir, urls, rows_only=None):
    URLS.clear(); URLS.update(urls)
    return make2(AI, outdir, 0, rows_for(AI))

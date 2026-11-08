import sys, os
exec(open('/home/claude/gen6b.py').read())
from render import render
PH.clear(); PH.update({
 'cn':('12768829','Kirandeep Singh Walia','center'),
 'cz':('30576160','Willfried Wende','center'),
 'uk':('27796863','James Wong','center'),
 'us':('30795043','dumitru bumbu','center 40%'),
 'fed':('6016794','Samuel Sweet','center'),
 'q':('9712998','Josh Sorenson','center')})
MACRO['cover_head']="Rates and inflation this week"; MACRO['cover_ph']='cn'; MACRO['qph']='q'
MACRO['items']=["China inflation data due Monday","Czech central bank raises rate to 4%","Bank of England lifts rate to 4%","US inflation data due Tuesday","Traders price a December Fed hike"]
MACRO['mood']="watchful"
MACRO['S']=[
 (2,"China · Inflation","0.8%","Forecast: October CPI, year on year","China's October inflation data lands today","","Forecast is 0.8%, down from 0.9% in September. Release due 08:30 Bangkok time on Mon 9 Nov.","CPI tracks the prices households pay for goods and services","Trading Economics (6 Nov), Lundgreen's Investor Insights (6 Nov)","cn"),
 (3,"Czech Republic · Central bank","4%","Czech National Bank two-week repo rate","Czech central bank raises rates to 4%","","Four board members voted to raise by 0.25 points, three to hold. It sees 2027 inflation at 3.2% and cut 2026 growth to 1.7% from 2.2%.","The article says markets price three more quarter-point rises over the next year","Expats.cz, citing ČTK (5 Nov)","cz"),
 (4,"UK · Central bank","4%","Bank of England Bank Rate","Bank of England lifts Bank Rate to 4%","","Eight members voted for +0.25 points; one wanted +0.5. UK CPI was 3.5% in September and is expected to reach around 5% by mid-2027.","The next decision is on 17 December","Bank of England (5 Nov)","uk"),
 (5,"US · Inflation","0.3%","Forecast: October CPI, month on month","US inflation data is due on Tuesday","","Headline CPI is forecast at 0.3%, from 0.6% in September. Core CPI is forecast at 0.2%, from 0.3%. Release: Tue 10 Nov, 20:30 Bangkok time.","October payrolls rose 165,000; unemployment was 4.1%","FXEmpire (8 Nov), Trading Economics (6 Nov)","us"),
 (6,"US · Rates and Fed","80%","Roughly, chance of a December Fed hike","Traders price a December Fed hike","","Fed-funds futures show about an 80% chance. Trading Economics also has another 25 bp rise priced in for December.","Fed speakers this week include Bowman, Goolsbee and Barkin (Mon 9 Nov)","FXEmpire (8 Nov), Trading Economics (6 Nov)","fed"),
]
URLS.clear(); URLS.update({f:f'file:///home/claude/photos/p{f}.jpg' for f,_,_ in PH.values()})
os.system('rm -rf /tmp/mrender /tmp/mpng')
b,o,n=make2(MACRO,'/tmp/mrender',0,rows_for(MACRO))
out='/tmp/mpng'; os.makedirs(out,exist_ok=True); acc=MACRO['accent']
for i in range(1,8): render(f'/tmp/mrender/M_45_{i}.dc.html',f'{out}/card{i}.png',1080,1350,acc)
render('/tmp/mrender/M_916_cover.dc.html',f'{out}/cover-9x16.png',1080,1920,acc)
render('/tmp/mrender/M_916_wide.dc.html',f'{out}/image-16x9.png',1600,900,acc)
print(sorted(os.listdir(out)))

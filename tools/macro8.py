import sys, os
exec(open('/home/claude/gen6b.py').read())
from render import render
PH.clear(); PH.update({
 'eu':('30576160','Willfried Wende','center'),
 'id':('34786065','Jeffry Surianto','center'),
 'th':('12768829','Kirandeep Singh Walia','center'),
 'oil':('33333825','Eyüpcan Timur','center 60%'),
 'us':('30795043','dumitru bumbu','center 40%'),
 'q':('9712998','Josh Sorenson','center')})
MACRO['cover_head']="Inflation, oil and rates: the week in macro"; MACRO['cover_ph']='th'; MACRO['qph']='q'
MACRO['items']=["Euro-area inflation rises to 4.0%","Indonesia grows 5.47% in Q3","Thai stocks fall 2.16% on Friday","Oil heads for a 12% weekly loss","Traders price 78% odds of a Fed hike"]
MACRO['mood']="watchful"
MACRO['S']=[
 (2,"Euro area · Inflation","4.0%","October flash inflation, year on year","Euro-area inflation rises to 4.0%","","Up from 3.8% in September and the highest since September 2023. Energy +20.8%; core inflation 2.5%.","The ECB held its deposit rate at 2.5% on 29 Oct; next meeting 16–17 Dec","Euronews, citing Eurostat (4 Nov)","eu"),
 (3,"Indonesia · Growth","5.47%","Q3 GDP, year on year","Indonesia's economy grows 5.47% in Q3","","Up from 5.29% in Q2 and above the 5.2% consensus. Exports +4.59%; investment +6.06%.","Private consumption grew 5.04% in the quarter","MUFG Research (6 Nov)","id"),
 (4,"Thailand · Equities","−2.16%","SET Index, Fri 6 Nov","Thai stocks fall 2.16% to 1,465.70","","The SET lost 32.29 points on turnover of THB 79.43B. Kaohoon links the fall to AI data-centre worries and US–Iran risk.","Thai October inflation was 3.9%, above the 1–3% target band","Kaohoon International (6 Nov)","th"),
 (5,"Global · Oil","−12%","Brent and WTI, week to 6 Nov","Oil heads for a 12% weekly loss","","Brent was $99.42 and WTI $91.24 at time of writing. Reuters counts five vessel incidents in the Gulf since Sunday.","Brent averaged $108 in the 15 UK working days to 27 Oct","Oilprice.com (6 Nov), Bank of England (5 Nov)","oil"),
 (6,"US · Rates and Fed","78%","Market-implied chance of a December hike","Traders price a December Fed hike","","October payrolls rose 165,000, over twice forecasts; unemployment 4.1%. The Fed meets 8–9 Dec.","Inflation has run above the Fed's 2% target for more than five years","Reuters via Business Recorder (6 Nov)","us"),
]
URLS.clear(); URLS.update({f:f'file:///home/claude/photos/p{f}.jpg' for f,_,_ in PH.values()})
shutil_rm=os.system('rm -rf /tmp/mrender /tmp/mpng')
b,o,n=make2(MACRO,'/tmp/mrender',0,rows_for(MACRO))
out='/tmp/mpng'; os.makedirs(out,exist_ok=True); acc=MACRO['accent']
for i in range(1,8): render(f'/tmp/mrender/M_45_{i}.dc.html',f'{out}/card{i}.png',1080,1350,acc)
render('/tmp/mrender/M_916_cover.dc.html',f'{out}/cover-9x16.png',1080,1920,acc)
render('/tmp/mrender/M_916_wide.dc.html',f'{out}/image-16x9.png',1600,900,acc)
print(sorted(os.listdir(out)))

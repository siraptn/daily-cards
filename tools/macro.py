import sys
exec(open('/home/claude/gen6.py').read())
from render import render
PH.clear(); PH.update({
 'us':('6016794','Samuel Sweet','center'),
 'th':('12768829','KIRANDEEP SINGH','center'),
 'au':('31609948','David Williams','center'),
 'uk':('27796863','James Wong','center'),
 'oil':('18905793','David Brown','center'),
 'q':('4386157','Karolina Grabowska','center')})
MACRO['cover_head']="Jobs, inflation and oil move markets"; MACRO['cover_ph']='th'; MACRO['qph']='q'
MACRO['items']=["US adds 165,000 jobs in October","Thai inflation hits 3.90%","RBA lifts rate to 4.85%","Bank of England hikes to 4%","Brent tops $100; gold slips"]
MACRO['mood']="cautious"
MACRO['S']=[
 (2,"US · Jobs and the Fed","165K","October payrolls, over twice forecast","US employers add 165,000 jobs in October","","Unemployment ticked down to 4.1%. Markets priced about a 78% chance of a December Fed hike.","Rate expectations move bond yields, currencies and stocks","Reuters via Yahoo Finance (6 Nov)","us"),
 (3,"Thailand · Inflation","3.90%","October headline CPI, year on year","Thai inflation breaches the central bank's target","","A Reuters poll expected 3.24%; September was 2.82%. Fuel prices rose 29.18%. Core inflation was 1.58%.","The Bank of Thailand's target range is 1% to 3%","Reuters via Business Recorder, The Nation (6 Nov)","th"),
 (4,"Australia · Central bank","4.85%","RBA cash rate target","Australia raises rates to an 18-year high","","The RBA lifted its cash rate from 4.60% on 3 Nov. Six board members voted to raise, three to hold.","The highest level since 2008","SBS News (3 Nov), Reuters via Global Banking &amp; Finance (5 Nov)","au"),
 (5,"UK · Central bank","4%","Bank of England Bank Rate","Bank of England raises rates for the first time since 2023","","Decision on 5 Nov. All members voted to raise rates; one backed a larger rise.","The first hike since August 2023","Reuters via Global Banking &amp; Finance (5 Nov)","uk"),
 (6,"Global · Oil and gold","$102.05","Brent crude, per barrel","Oil tops $100 while gold slips","","Brent was up $2.53 from the day before. Spot gold fell 0.6% to $4,063 in early trade.","Fuel prices fed Thailand's October inflation","Fortune via BizToc (6 Nov), Whalesbook (6 Nov)","oil"),
]
import os
os.makedirs('/home/claude/macro_out',exist_ok=True)
URLS.clear(); URLS.update({f:f'file:///home/claude/photos/p{f}.jpg' for f,_,_ in PH.values()})
b,o,n=make2(MACRO,'/tmp/mrender',0,rows_for(MACRO))
out='/tmp/mpng'; os.makedirs(out,exist_ok=True)
acc=MACRO['accent']
for i in range(1,8): render(f'/tmp/mrender/M_45_{i}.dc.html',f'{out}/card{i}.png',1080,1350,acc)
render('/tmp/mrender/M_916_cover.dc.html',f'{out}/cover-9x16.png',1080,1920,acc)
render('/tmp/mrender/M_916_wide.dc.html',f'{out}/image-16x9.png',1600,900,acc)
print(sorted(os.listdir(out)))

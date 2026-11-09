import sys, os
sys.path.insert(0,'/home/claude')
exec(open('/home/claude/gen6b.py').read())
from render import render
PH.clear(); PH.update({
 'cn':('30576160','Willfried Wende','center'),
 'th':('12768829','Kirandeep Singh Walia','center'),
 'us':('6016794','Samuel Sweet','center 40%'),
 'gold':('29336321','Sergei Starostin','center'),
 'bk':('20020757','Markus Winkler','center 60%'),
 'q':('9712998','Josh Sorenson','center')})
MACRO['cover_head']="Inflation, jobs and gold: the week in macro"; MACRO['cover_ph']='th'; MACRO['qph']='q'
MACRO['items']=["China inflation at 0.7% in October","Thai inflation 3.9%, above target","US employers add 165,000 jobs","Gold up 5% for the week","Bank of Thailand sees 2026 growth at 2.4%"]
MACRO['mood']="watchful"
MACRO['S']=[
 (2,"China · Inflation","0.7%","October CPI, year on year","China's consumer prices rose 0.7% in October","","Prices were unchanged from September. Food prices fell 2.9% on the year; non-food prices rose 1.5%.","CPI tracks the prices households pay for goods and services","Xinhua (9 Nov)","cn"),
 (3,"Thailand · Inflation","3.9%","October headline inflation, year on year","Thai inflation rises to 3.9%","","Up from 2.82% in September and above the Bank of Thailand's 1–3% target range. Core inflation was 1.58%.","Higher oil prices and flood-related food costs were cited as drivers","Trading Economics (6 Nov)","th"),
 (4,"US · Jobs","165K","October payrolls, change in jobs","US employers add 165,000 jobs","","Unemployment was 4.1%. September was revised up to 60,000 from 29,000. Average hourly earnings rose 3.1% over 12 months.","The next jobs report is due on 4 December","US Bureau of Labor Statistics (6 Nov)","us"),
 (5,"Global · Gold","$4,071","Spot gold per ounce, 6 Nov","Gold heads for its best week in over two months","","Up about 5% for the week so far, after a one-year low of $3,869.85 on 30 October.","CME FedWatch showed a 70% chance of a Fed hike in December","Reuters via Kitco (6 Nov)","gold"),
 (6,"Thailand · Growth","2.4%","Bank of Thailand's 2026 GDP forecast","Bank of Thailand lifts 2026 growth outlook to 2.4%","","Up from 2.3%, said Governor Vitai Ratanakorn on 5 Nov. Revised factory data could add 0.1 to 0.5 points.","Third-quarter GDP has not yet been published by NESDC","Thai Examiner (6 Nov)","bk"),
]
URLS.clear(); URLS.update({f:f'file:///home/claude/photos/p{f}.jpg' for f,_,_ in PH.values()})
os.system('rm -rf /tmp/mrender /tmp/mpng')
b,o,n=make2(MACRO,'/tmp/mrender',0,rows_for(MACRO))
out='/tmp/mpng'; os.makedirs(out,exist_ok=True); acc=MACRO['accent']
for i in range(1,8): render(f'/tmp/mrender/M_45_{i}.dc.html',f'{out}/card{i}.png',1080,1350,acc)
render('/tmp/mrender/M_916_cover.dc.html',f'{out}/cover-9x16.png',1080,1920,acc)
render('/tmp/mrender/M_916_wide.dc.html',f'{out}/image-16x9.png',1600,900,acc)
print(sorted(os.listdir(out)))

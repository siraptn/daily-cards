# @siraptn daily news cards: runbook for scheduled runs

Two series, 7 cards each, 4:5 (1080x1350) plus 9:16 cover (1080x1920) and 16:9 image (1600x900).
- Macro Daily: post slot 06:54 Asia/Bangkok, accent #BFDDF2. Config: MACRO dict in tools/gen5.py.
- AI & Web3 Daily: post slot 09:09 Asia/Bangkok, accent #F7C9A8. Config: AI dict in tools/gen6.py (stories S, items, cover_head, quote).
Design: photo on top, overlapping white sheet, series accent. 9:16 cover and 16:9 image are photo and headline only (see build() in gen6.py).
Icon: siraptn "Si" teardrop (ICON in gen6.py). Words never go on photos except headline on the 9:16/16:9 covers and the photo credit.

## Setup in a fresh session
1. Attach the repo siraptn/daily-cards with push access (add_repo), clone to /home/claude/daily-cards.
2. cp tools/gen5.py tools/gen6.py tools/render.py /home/claude/ ; mkdir -p /tmp/fonts && cp tools/fonts-package.json /tmp/fonts/package.json && (cd /tmp/fonts && npm install)
3. Photos: download free-licence Pexels photos (shell can reach images.pexels.com / pexels.com) into /home/claude/photos as p<ID>.jpg. Credit line is "Photo: <Name> / Pexels". Avoid Unsplash+ (paid). Never photos of public figures.
4. Update PH (photo map), AI/MACRO stories in the config, then render locally with URLS pointing at file:///home/claude/photos/p<ID>.jpg:
   python3 -c "exec(open('/home/claude/gen6.py').read()); write('/tmp/render', {f:f'file:///home/claude/photos/p{f}.jpg' for f,_,_ in PH.values()})"
   python3 render.py /tmp/render /tmp/png 1080 1350 '<accent>'  (cards)  and render() for AI_916_cover (1080x1920) and AI_916_wide (1600x900) via 'from render import render'.
5. Look at every PNG before posting.

## Hard rules (Sira's standing approval: daily series may go live without review ONLY if all five hold)
1. Every figure has a dated link (outlet + date of the article, fetched and read, not from memory). Stories must be from the last ~7 days; older sources fail.
2. Every photo has its credit on the card.
3. Nothing is opinion. Each caption has a plain-fact Learning line; the card "Why it matters" lines are approved.
4. The "Not investment advice" line is in every caption (Thai: ข้อมูลไม่ใช่คำแนะนำการลงทุนนะคะ).
5. If any source cannot be verified, STOP: do not post that story (swap it) or the set; report to Sira.
Never invent numbers or stories. A report not confirmed by the company must say "reportedly" and name the outlet and date. No disclosure line (Sira removed it for this series).

## Captions and channels
- English: LinkedIn, X, Medium, Substack. Thai (in Sira's voice: refer to herself as "เอ๋ย", ends with ค่ะ/นะคะ, readers are เพื่อนๆ): Instagram, Threads, TikTok, Lemon8, Rednote.
- Hashtags #EmergingTech #FrontierTech #AIWeb3Daily (Thai IG adds #AI #Web3). Sources go in the first comment (firstCommentText), with dates.
- Template to copy: Claude Doc "Sira's Content Ecosystem Notes", tab "Captions 6 Nov" (slug ba0053b2-3dbd-4d83-8ebc-b0ce5f1e611b).

## Publishing
1. Copy PNGs to daily-cards/<YYYY-MM-DD>/<series>/card1..7.png, cover-9x16.png, image-16x9.png; git add, commit, push to main. Public URL: https://raw.githubusercontent.com/siraptn/daily-cards/main/<YYYY-MM-DD>/<series>/<file>. Check the URL returns 200.
2. Metricool createScheduledPost (live), blogId 4819339, timezone Asia/Bangkok, date = the series slot (must be in the future; if the slot has passed, use now + 15 minutes). Channels: Instagram (7-card carousel, Thai), LinkedIn (7 images, English), X (single post, 16:9 image, English, <=280 chars), Threads (cover card, Thai), TikTok (7 photos, Thai). Not auto-posted: Facebook, YouTube (video needed), Lemon8 and Rednote (no scheduler; hand-off pack).
3. Update the Claude Doc captions tab and finish with a short report to Sira: what was posted where and when, anything swapped or stopped, and what she must post by hand.

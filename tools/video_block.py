#!/usr/bin/env python3
"""Baut aus video/<slug>.json alles, was ein Erklärvideo auf der Seite braucht:
Untertitel (.vtt), Video-Block mit Poster-Bild (alt), Transkript, VideoObject-JSON-LD
und den Eintrag in sitemap.xml. Aufruf: python3 tools/video_block.py <slug>
Wiederholbar: bestehende Blöcke werden ersetzt (Marker <!-- video:<slug> -->)."""
import json, math, re, sys, html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://kaffeetester.de'
slug = sys.argv[1]
S = json.load(open(f'{ROOT}/video/{slug}.json'))
mp4, poster, vtt = (f'/assets/video/{slug}.{e}' for e in ('mp4', 'jpg', 'vtt'))

def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f'{int(h):02d}:{int(m):02d}:{s:06.3f}'

# 1. VTT (gleiche Logik wie im Video: Szene = Audio + Pause, Sätze proportional zur Länge)
cues, start = [], 0.0
for sc in S['scenes']:
    dur = sc['audio_seconds']; text = sc['text']
    parts = re.split(r'(?<=[.?!])\s+', text); total = len(text); t = start
    for p in parts:
        d = len(p) / total * dur
        cues.append((t, t + d, p)); t += d
    start += math.ceil((dur + S['pad']) * S['fps']) / S['fps']
open(f'{ROOT}{vtt}', 'w').write('WEBVTT\n\n' + '\n'.join(f'{i+1}\n{ts(a)} --> {ts(b)}\n{p}\n' for i, (a, b, p) in enumerate(cues)))

transcript = ' '.join(s['text'] for s in S['scenes'])
e = html.escape
block = f'''<!-- video:{slug} -->
      <h3>{e(S['heading'])} ({S['duration_seconds']} Sek.)</h3>
      <div class="video" data-src="{mp4}" data-vtt="{vtt}" data-title="{e(S['title'])}" data-width="{S['width']}" data-height="{S['height']}">
        <button type="button" class="video-start" aria-label="Video abspielen: {e(S['title'])}">
          <img src="{poster}" alt="{e(S['poster_alt'])}" width="{S['width']}" height="{S['height']}" loading="lazy" />
          <span class="video-play">▶ Video abspielen</span>
        </button>
      </div>
      <p class="video-hinweis">{e(S['hinweis'])} Das Video liegt auf unserem eigenen Server, es werden keine Daten an Dritte übertragen.</p>
      <details class="transkript"><summary>Transkript und Untertitel</summary><p>{e(transcript)}</p><p><a href="{vtt}">Untertitel-Datei (WebVTT)</a></p></details>
      <script src="/assets/video.js?v=20261018" defer></script>
      <!-- /video:{slug} -->'''
ld = '<script type="application/ld+json" data-video="%s">%s</script>' % (slug, json.dumps({
    "@context": "https://schema.org", "@type": "VideoObject", "name": S['title'], "description": S['description'],
    "thumbnailUrl": BASE + poster, "uploadDate": S['upload_date'], "duration": f"PT{S['duration_seconds']}S",
    "contentUrl": BASE + mp4, "inLanguage": "de", "transcript": transcript,
    "publisher": {"@type": "Organization", "name": "Kaffee Tester", "logo": {"@type": "ImageObject", "url": BASE + "/assets/icon-512.png"}}},
    ensure_ascii=False))

# 2. Seite: Block + JSON-LD ersetzen oder erstmalig einsetzen
p = f'{ROOT}{S["page"]}index.html'
t = open(p).read()
if f'<!-- video:{slug} -->' in t:
    t = re.sub(rf'<!-- video:{slug} -->.*?<!-- /video:{slug} -->', lambda m: block, t, flags=re.S)
else:
    t, n = re.subn(r'<h3>Erklärvideo:.*?</script>', lambda m: block, t, count=1, flags=re.S)
    assert n == 1, 'alten Video-Block nicht gefunden: Block von Hand an die gewünschte Stelle setzen'
t = re.sub(rf'<script type="application/ld\+json" data-video="{slug}">.*?</script>\n?', '', t, flags=re.S)
t = t.replace('</head>', '  ' + ld + '\n</head>', 1)
open(p, 'w').write(t)

# 3. Sitemap: <video:video> am Seiteneintrag
sm = open(f'{ROOT}/sitemap.xml').read()
if 'xmlns:video' not in sm:
    sm = sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">')
vid = (f'<video:video><video:thumbnail_loc>{BASE}{poster}</video:thumbnail_loc><video:title>{e(S["title"])}</video:title>'
       f'<video:description>{e(S["description"])}</video:description><video:content_loc>{BASE}{mp4}</video:content_loc>'
       f'<video:duration>{S["duration_seconds"]}</video:duration><video:publication_date>{S["upload_date"]}</video:publication_date></video:video>')
sm = re.sub(rf'<video:video><video:thumbnail_loc>{re.escape(BASE+poster)}.*?</video:video>', '', sm, flags=re.S)
loc = f'<loc>{BASE}{S["page"]}</loc>'
sm = re.sub(rf'({re.escape(loc)}.*?)(</url>)', lambda m: m.group(1) + vid + m.group(2), sm, count=1, flags=re.S)
open(f'{ROOT}/sitemap.xml', 'w').write(sm)
print('ok:', slug)

# kaffeetester.de: Regeln für dieses Repo

Statische HTML-Seite auf Vercel. Design: Berlin-Theme in `assets/style.css`. Auf Deutsch schreiben, keine erfundenen Zahlen, Preise nur mit Datum, keine "Test"-Behauptungen ohne eigenen Test.

## Videos: immer über das Werkzeug einbauen (Pflicht für jedes neue Video)

1. Dateien nach `assets/video/<slug>.mp4` und `<slug>.jpg` (Poster, 1920x1080). Die `.vtt` erzeugt das Werkzeug.
2. Spezifikation in `video/<slug>.json` anlegen (siehe `video/mahlwerk-stahl-vs-keramik.json`): Titel, Beschreibung, `poster_alt`, Dauer, Szenen mit Text und echter Audiolänge, Seite (`page`), Hinweistext.
3. `python3 tools/video_block.py <slug>` ausführen. Das setzt automatisch:
   - Poster als echtes `<img>` mit `alt`, Play-Button mit `aria-label`,
   - Untertitel (`.vtt`, `<track>`), Transkript im Seitentext (`<details>`),
   - `VideoObject`-JSON-LD im `<head>` und `<video:video>` in `sitemap.xml`,
   - Laden erst nach Klick (`assets/video.js`, `preload`, feste Breite/Höhe).
4. Pflichttext bei synthetischer Stimme: "Die Stimme ist synthetisch." (steht im `hinweis`-Feld). Kein Video als Test oder Review ausgeben, wenn es Animation oder Herstellerwerbung ist.
5. Fremdvideos (YouTube) nur über youtube-nocookie, erst nach Klick, mit Hinweis "Herstellerwerbung, kein Test von uns", nur Videos des offiziellen Herstellerkanals.
6. Nach dem Einbau: Seite lokal öffnen, Video abspielen, Poster-alt und Transkript prüfen.

## Bilder
Jedes `<img>` braucht `alt`, `width`, `height`. Nur Fotos mit freier kommerzieller Lizenz (Pexels/Unsplash) oder eigene; Quelle in `assets/bilder/QUELLEN.txt` eintragen.

## Git
Nicht ohne Freigabe der Nutzerin committen oder pushen. Mehrere Themen = mehrere Commits.

## Rechtliches (Stand Oktober 2026: privates, nicht kommerzielles Projekt)
Impressum und Datenschutz sind bewusst minimal (nur E-Mail, keine Werbung, keine Partnerlinks). **Vor der ersten Affiliate-Verlinkung, Werbung oder Awin-Bewerbung zwingend ersetzen:** vollständiges Impressum nach § 5 DDG (echter Name, ladungsfähige Anschrift, E-Mail), Datenschutz um Partnerprogramme ergänzen, Hinweis "Anzeige/Affiliate-Link" an den Links. Google Fonts durch lokale Schriften ersetzen und den Abschnitt "Schriftarten" in der Datenschutzerklärung anpassen.

## Cache
CSS und JS werden mit `max-age=0, must-revalidate` ausgeliefert (vercel.json) und mit `?v=` eingebunden. Bei größeren CSS/JS-Änderungen `?v=` in allen HTML-Dateien hochzählen, sonst sehen Besucher mit altem Cache kaputte Layouts.

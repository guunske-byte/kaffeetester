# SEO-Strategie – kaffeetester.de

> Pragmatischer SEO-Fahrplan für eine junge Domain. Ziel: mit begrenztem Aufwand
> schnell thematische Autorität in **einem** Cluster aufbauen, statt Ressourcen über
> viele umkämpfte Head-Keywords zu verstreuen.
> Stand: August 2026.

---

## 1. Ausgangslage & Grundprinzip

kaffeetester.de ist eine **neue Domain ohne Autorität und ohne Backlinks**. Head-Terms wie
„Kaffeevollautomat Test" oder „beste Kaffeemaschine" werden von etablierten Seiten dominiert
(u. a. coffeeness.de, testberichte.de, Stiftung Warentest, CHIP). Dort direkt anzutreten ist
für die ersten 6–12 Monate aussichtslos.

**Der pragmatische Ansatz:**

1. **Ein Cluster statt Gießkanne.** Wir bauen zuerst *einen* Themenbereich vollständig aus –
   den kommerziell wertvollsten: **Kaffeevollautomat**.
2. **Long-Tail vor Head.** Wir zielen zuerst auf konkrete, kaufnahe und informationsgetriebene
   Long-Tail-Suchen mit erreichbarer Konkurrenz, die auf die Geldseite (Pillar) einzahlen.
3. **Topical Authority durch interne Verlinkung.** Pillar + Cluster-Seiten verweisen sauber
   aufeinander. Google versteht so: „Diese Seite kennt sich mit Kaffeevollautomaten aus."
4. **Ehrlichkeit statt Fake-Rankings.** Keine erfundenen Testergebnisse, Preise oder
   Sterne-Wertungen. Evergreen-Ratgeber sind glaubwürdiger (E-E-A-T) und altern langsamer.

---

## 2. Warum der Cluster „Kaffeevollautomat" zuerst?

| Kriterium | Bewertung |
|---|---|
| Kommerzieller Wert | Sehr hoch – hohe Warenkörbe (300–1.500 €), starke Affiliate-Provisionen |
| Suchvolumen | Sehr hoch über die gesamte Themenfamilie |
| Kaufintention | Hoch – viele Suchen sind entscheidungs- bzw. kaufnah |
| Long-Tail-Chancen | Viele erreichbare Unterthemen (Pflege, Preisklassen, Vergleiche) |
| Inhaltliche Tiefe | Groß genug, um echte Autorität aufzubauen |

Fazit: bester Hebel aus „Wert × Erreichbarkeit". Andere Typen (Siebträger, Kapsel, Pad, Filter)
folgen in späteren Phasen als eigene Cluster.

---

## 3. Cluster-Architektur (Phase 1 – live)

**Pillar (Themen-Hub):** `/kaffeevollautomat/`
→ breiter Überblick, verlinkt auf alle Cluster-Seiten und fängt den Oberbegriff ab.

**Cluster-/Support-Seiten** (jede zielt auf eine eigene Suchintention und verlinkt zurück zum Pillar):

| Seite | URL | Primäres Keyword (Intention) | Sekundär-Keywords |
|---|---|---|---|
| Pillar / Ratgeber | `/kaffeevollautomat/` | kaffeevollautomat (Info/Navigational) | kaffeevollautomat kaufen, ratgeber |
| Kaufberatung | `/kaffeevollautomat/kaufberatung/` | kaffeevollautomat worauf achten (Info→Commercial) | kaufberatung, kaufkriterien, mahlwerk vergleich |
| Preisklasse | `/kaffeevollautomat/bis-500-euro/` | kaffeevollautomat bis 500 euro (Commercial) | günstiger vollautomat, unter 500 euro |
| Vergleich | `/kaffeevollautomat/vollautomat-oder-siebtraeger/` | vollautomat oder siebträger (Commercial) | unterschied siebträger vollautomat |
| Pflege | `/kaffeevollautomat/reinigen-entkalken/` | kaffeevollautomat entkalken / reinigen (Info) | brühgruppe reinigen, milchsystem reinigen |

**Warum diese fünf zuerst?**
- Die Pflege-Seite (`reinigen-entkalken`) ist **rein informativ und am leichtesten zu ranken** –
  guter früher Traffic-Lieferant und Vertrauensaufbau.
- `bis-500-euro` und `vollautomat-oder-siebtraeger` sind **kaufnah** und zahlen direkt auf
  Monetarisierung ein.
- `kaufberatung` ist die inhaltliche Brücke zwischen Info- und Kaufintention.

---

## 4. Internes Verlinkungsmodell

```
                 Startseite (/)
                      │  (Hub verlinkt Pillar + Top-Cluster)
                      ▼
        ┌──────  /kaffeevollautomat/  (PILLAR)  ──────┐
        │            ▲   ▲   ▲   ▲                     │
        │  verlinkt auf alle Cluster, jede Cluster-    │
        │  Seite verlinkt zurück zum Pillar            │
        ▼            │   │   │   │                     ▼
  kaufberatung ──► bis-500-euro ──► vollautomat-oder-siebtraeger ──► reinigen-entkalken
        (Cluster-Seiten verlinken zusätzlich seitlich untereinander)
```

Regeln:
- Jede Cluster-Seite verlinkt **mindestens einmal zurück zum Pillar** und auf **2–3 Schwester-Seiten**.
- Ankertexte natürlich und keyword-nah, aber nicht überoptimiert.
- Der Pillar bündelt die interne Linkkraft und ist die Seite, die mittelfristig auf den Oberbegriff ranken soll.

---

## 5. Technische & On-Page-SEO – Checkliste

**Bereits umgesetzt (Phase 1):**
- [x] Saubere, sprechende URLs mit Ordnerstruktur (`/kaffeevollautomat/…/`)
- [x] Ein `<h1>` pro Seite, sinnvolle H2/H3-Hierarchie
- [x] Individuelle `<title>` (≤ ~60 Zeichen) und `meta description` (~155 Zeichen) je Seite
- [x] Canonical-Tags auf jeder Seite
- [x] Open-Graph- & Twitter-Card-Tags
- [x] Strukturierte Daten (JSON-LD): `WebSite`, `Article`, `BreadcrumbList`, `FAQPage`, `HowTo`
- [x] Sichtbare Breadcrumb-Navigation
- [x] `robots.txt` + `sitemap.xml`
- [x] Mobile-first, responsives Layout, sticky Navigation
- [x] Interne Verlinkung Pillar ⇄ Cluster
- [x] Gemeinsames, schlankes CSS (eine Datei, schnelle Ladezeit)
- [x] `hreflang`-Auszeichnung (`de` + `x-default`, selbstreferenzierend) auf jeder Seite
- [x] Favicon-Set (SVG + PNG), Apple-Touch-Icon, `site.webmanifest`, `theme-color`
- [x] OG-Vorschaubild (`og:image`, 1200×630, gebrandet) + `og:image:width/height` + `twitter:image`
- [x] Alle Seiten ausdrücklich indexierbar (`robots: index, follow`, kein `noindex`)
- [x] „Über uns"-Seite für E-E-A-T (Grundsätze, Methodik, Transparenz)
- [x] Impressum & Datenschutzerklärung als **ausfüllfertige Vorlagen** (im Footer jeder Seite verlinkt)

**Als Nächstes (Aufgaben des Betreibers vor dem Launch):**
- [ ] **Impressum & Datenschutz mit echten Daten füllen** (`[…]`-Platzhalter ersetzen) – rechtlich Pflicht in DE
- [ ] „Über uns" + Autorenangaben mit echtem Namen/Foto vervollständigen (E-E-A-T)
- [ ] Domain live schalten, HTTPS erzwingen, `www`/non-`www` auf eine Variante umleiten
- [ ] Google Search Console + Bing Webmaster Tools einrichten, `sitemap.xml` einreichen
- [ ] Cookie-Hinweis, falls einwilligungspflichtige Cookies/Analyse-Tools eingesetzt werden
- [ ] Bilder mit `alt`-Texten und `loading="lazy"` einbauen (aktuell textbasiert)
- [ ] Ladezeit/Core Web Vitals prüfen (aktuell sehr leicht – guter Startpunkt)

---

## 6. Redaktioneller Fahrplan (nächste Phasen)

**Phase 2 – Kaffeevollautomat-Cluster vertiefen (jetzt live):**
- [x] Kaffeevollautomat bis 1.000 Euro (nächste Preisklasse) → `/kaffeevollautomat/bis-1000-euro/`
- [x] Milchsystem-Vergleich: Karaffe vs. Schlauch vs. LatteGo → `/kaffeevollautomat/milchsystem/`
- [x] Häufige Probleme & Lösungen (mahlt nicht, Brühgruppe klemmt, …) → `/kaffeevollautomat/probleme-loesungen/`
- [x] Kaffeebohnen für den Vollautomaten → `/kaffeevollautomat/bohnen/`

**Phase 2b – weitere Long-Tail-Ideen (offen):**
- Kaffeevollautomat mit App / Smart-Funktionen – lohnt sich das?
- Kaffeevollautomat für 1–2 Personen / kleine Küche
- Mahlgrad richtig einstellen (eigener Ratgeber)
- Kaffeevollautomat entkalken: Hausmittel vs. Entkalker im Detail

**Phase 3 – neue Cluster (jeweils eigener Pillar + Support-Seiten):**
- Siebträgermaschine (Pillar + Kaufberatung, Zubehör, Einsteiger-Guide)
- Kapselmaschine / Padmaschine (Kosten pro Tasse, Nachhaltigkeit)
- Filterkaffeemaschine
- Übergreifend: Kaffeebohnen, Mahlgrad, Zubereitungsarten

**Priorisierung:** immer nach „kommerzieller Wert × Erreichbarkeit". Erst einen Cluster
inhaltlich „fertig" machen, dann den nächsten öffnen.

---

## 7. Monetarisierung & E-E-A-T (Leitplanken)

- Affiliate-Links (z. B. Amazon/Fachhandel) **transparent kennzeichnen** – Pflicht in DE und
  gut fürs Vertrauen. Auf produktbezogenen Seiten einen Werbe-/Affiliate-Hinweis einblenden.
- **Keine erfundenen Testergebnisse.** Wenn echte Tests/Erfahrungen ergänzt werden, klar als
  eigene Methodik oder als Verweis auf seriöse Quellen (z. B. Stiftung Warentest) ausweisen.
- Inhalte aktuell halten (Datum „Aktualisiert am …") – signalisiert Pflege und Frische.

---

## 8. Erfolgsmessung (KPIs)

| Zeitraum | Realistisches Ziel |
|---|---|
| Monat 1–2 | Indexierung aller Seiten, erste Impressionen (v. a. Pflege-/Long-Tail-Themen) |
| Monat 3–4 | Erste Klicks über informative Long-Tails, Rankings in Top 20–50 |
| Monat 5–8 | Cluster vertieft, erste kaufnahe Keywords in Top 10–20, wachsende Klicks |
| ab Monat 9 | Pillar rankt für Mittel-Long-Tail, Aufbau des zweiten Clusters |

**Zu beobachten:** Impressionen & Klicks (Search Console), Ranking-Entwicklung der Primär-Keywords,
Verweildauer, und ob die internen Links Nutzer sinnvoll durch den Cluster führen.
```

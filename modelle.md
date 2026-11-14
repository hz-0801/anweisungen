# Modelle, Aufwand und Wochenkontingent

Stand 2026-11-14 (Lehrer 12.10.: Weg B; 14.11.: Ausnahme Anweisungen in § 3). Gilt für alle Projekte. Lesen
bei jeder Runde mit Agenten, bei jedem neuen Modell und einmal im
Monat (Neubewertung, § 5).

## 1 Ziel und Maß

Ziel: aus dem Wochenkontingent des Abos so viel gutes, abgenommenes
Ergebnis wie möglich. Maß ist der Wochenpunkt je abgenommenem
Ergebnis, Nacharbeit eingerechnet – nicht Token, nicht Listenpreis,
nicht Tempo allein. Ein billiger Lauf, der nachgebessert werden muss,
ist teurer als ein teurer, der sitzt.

## 2 Fakten (Stand, Quelle; bei Neubewertung prüfen)

- Fable zieht aus dem Wochenkontingent, höchstens 50 % davon; kein
  Zusatzbudget. Bei Woche 100 % geht nichts mehr (support.claude.com,
  Artikel 15424964, gelesen 12.10.2026).
- Listenpreis je Mio Token Ein-/Ausgabe: Fable 5.1 10/50 $, Opus 5.5
  4/20 $, also Faktor 2,5 (Anthropic, Preisseite, laut Sekundärquelle
  22.09.2026).
- Neu 09.11.2026: Fable 5.2, allgemein verfügbar, 8/40 $ (Opus 5.5 4/20 $, also Faktor 2),
  Standardaufwand high; Anthropic rät weiter: mit Opus beginnen, Fable erst, wenn Opus auf
  höherem Aufwand nicht reicht (platform.claude.com, fable-5-2/overview, whats-new). Max-Abo:
  ein bis drei „Fable-Resets“ je nach Abodauer (< 6 Monate 1, 6–12 Monate 2, > 12 Monate 3);
  ein Reset gibt den auf Fable verbrauchten Teil der Woche zurück, nicht den übrigen; verfallen
  08.03.2027 (support.claude.com, Artikel 17506494). Ob die 50-%-Grenze für Fable 5.2 gilt,
  sagt Artikel 15424964 nicht (nennt nur Fable 5/5.1).
- Lehrer: Ultra-Abo (= früher Max 20x, 200 $), 2 Fable-Resets, verfallen 09.03.2027 08:59 MEZ (Anzeige 09.11.).
  Ultra hat eine eigene Wochengrenze für Fable: „bis zu 50 % deines Wochenlimits“ (Nutzungsanzeige 09.11.).
  Unabhängig (Artificial Analysis Intelligence Index, 09.11.): Opus 5.5 high 52 Punkte, 56 M Ausgabe-Token,
  3,46 $ und 9,5 min je Aufgabe; Opus 5.5 max 59, 218 M, 10,04 $, 25,4 min; Fable 5.2 high 62, 85 M Ausgabe-
  und 7,9 Mrd Eingabe-Token (Opus high 4,7 Mrd); Fable 5.2 max 65, ≈ 26,5 $ je Aufgabe. Daraus geschätzt:
  Fable high ≈ 3× Opus high je Aufgabe (Token × Preis), ≈ +10 Indexpunkte. Vals (Fable high): bei Code
  gemischt (SWE-bench Multimodal Opus vorn, Terminal-Bench gleich).
  Niedrigere Stufen (AA, 09.11.): Fable 5.2 medium 56 Punkte, 41 M Aus-/2,6 Mrd Eingabe-Token; low 54, 35 M/2,0 Mrd;
  Opus 5.5 medium 48, 2,45 $, 7,1 min. Kosten je Aufgabe gegen Opus high (Token × Listenpreis, an Opus high/medium
  geprüft: gerechnet 1,45, gemessen 1,41): Fable low ≈ 0,9×, medium ≈ 1,1×, high ≈ 3,3×. Annahme: das Abo zählt
  Fable im Verhältnis des Listenpreises – ungeprüft, Messung an der Nutzungsanzeige.
- Eigene Messung (mathe-nachhilfe plan.md § 8): Fable ≈ 0,25 Mio Token
  je Wochenpunkt, Opus ≈ 0,75 Mio – gleiche Arbeit kostet mit Fable
  etwa dreimal so viel Woche.
- Qualität: Anthropic nennt Opus 5.5 (22.09.2026) „auf dem Niveau von
  Fable 5.1 bei den meisten Aufgaben“; im Launch-Vergleich vorn in
  allen neun Benchmarks. Empfehlung von Anthropic: mit Opus beginnen,
  Fable erst, wenn Opus bei xhigh oder max nicht reicht
  (platform.claude.com, choosing-a-model).
- Aufwand (low · medium · high · xhigh · max) steuert, wie viel das
  Modell denkt, schreibt und Werkzeuge ruft; laut Anthropic oft der
  bessere Hebel als der Modellwechsel. Standard: Opus 5.5 medium,
  Fable 5.1 high. low spart deutlich, verliert etwas Können (Unter-
  agenten, Einfaches); xhigh kostet spürbar mehr als high; max kann
  zerdenken. Zahlen je Stufe veröffentlicht Anthropic nicht
  (platform.claude.com, effort).

## 3 Regel: Leiter

Das günstigste Modell auf der niedrigsten Stufe, das die Qualität
trägt. Erst die Aufwandsstufe drehen, dann das Modell wechseln.

| Arbeit | Modell | Aufwand |
|---|---|---|
| Zählen, Abnahme-Check, Formprüfung | Haiku | low |
| Mechanik mit Skriptprüfung (Zahlen tauschen, umformen) | Sonnet | medium |
| Chat, Planen, Regeln fassen | Opus | medium; high bei Konzept |
| Bau eines Ergebnisses, Kritiker | Opus | high |
| Langer, schwerer Bau, an dem Opus gescheitert ist | Opus | xhigh |
| erst dann | Fable | high |

Fable nur mit Beleg: Ein Kritiker hat Opus auf high oder xhigh an
derselben Aufgabe schlechter bewertet, und der Grund war nicht
Prompt oder Daten. Prüfungen, die ein Skript kann, macht das Skript.

Ausnahme Anweisungen (Lehrer 14.11.2026, Werkstatt 35): Anweisungen, die
oft benutzt werden (Bestellanweisung, Bauanweisungen, Aufträge für viele
Läufe), schreibt das Modell, das für Urteilsarbeit vorn steht (derzeit
Fable; Eichung 13.11.: blind gleich gut oder besser als Opus high), mit dem
höchsten Aufwand, der sich bewährt hat – auch über eine Sparregel der Woche
hinweg. Ist offen, was besser ist, entscheidet ein blinder Vergleich an
Testfällen; das Ergebnis kommt in die Messtabelle (§ 6). Ausgeführt wird
mit dem billigsten Modell, das die Qualität trägt. Grund: einmal teuer
schreiben, oft billig nutzen.

## 4 Was nicht gilt

- Kontingent voll nutzen heißt nicht Läufe ohne Nutzen: Rest vor dem
  Reset für Arbeit, die Ergebnis erzeugt (global.md „Kontingent“).
- Das Fable-Teilkontingent ist kein Ziel und kein Bonus.
- Ersetzt: „Fable aufbrauchen, nicht wieder Opus vorschlagen“
  (verbessereBlaetter, 10./11.10.2026).

## 4a Sparregeln (Messung 12./13.10.)

Ein Agent liest bei jedem Schritt seinen ganzen Verlauf neu; Kosten
wachsen mit Schritten × Verlauflänge. Nach mehr als etwa 5 min Pause
wird der Verlauf neu gemerkt (doppelt teuer).
1. Ein Ergebnis je Agent, Schrittgrenze im Auftrag (Richtwert 60).
   Auch der Qualität wegen (Lehrer 02.11.): Bau und Kritik eines
   Blatts oder Hefts macht je ein eigener Agent, nie mehrere
   hintereinander. Warum – in der Serie sinkt die Mühe je Stück
   (3–8 statt 17–45 min), der Agent kopiert seine erste Lösung,
   spätere Stücke werden dünner; Versuch Einzelbau 26./27.10.
   (verbessereBlaetter): Lehrer 6 : 0, Kritiker blind 3 : 2 : 1.
   Beispiel – P10-Breite 31.10., 12 Hefte, je ein Agent. Grenze –
   mechanische Arbeit nach fester Regelliste darf gebündelt werden
   (P10-Nachbesserung 02.11., zwei Hefte je Agent, sauber).
2. Prüfen mit Skript; Bild-Durchsicht nur der Endfassung, kleine
   Auflösung.
3. Aufwand medium für Datenarbeit und Setzen, high für Kritiker und
   Urteil; Agenten erben den Aufwand des Chats.
4. Keine Doppel- oder Vergleichsläufe ohne Anlass.
5. Chat kurz, Umzug nach jeder Runde.
Messen: gewichtet aus dem Sitzungsprotokoll (Cache lesen 0,1, Cache
schreiben 2, Ausgabe 5, Eingabe 1), nicht aus der Token-Zahl der
Agenten-Rückmeldung – die zeigte 0,34 Mio, wo gewichtet 22 Mio waren.

## 5 Neubewertung

Auslöser: jedes neue Modell (Ankündigung, Preis- oder Limitänderung)
und monatlich am ersten Chat nach dem Monatswechsel.

1. Quellen lesen: Anthropic-Ankündigung, choosing-a-model, effort,
   support.claude.com zu Limits; § 2 mit Datum nachziehen.
2. Vergleichslauf, wenn sich die Leiter ändern könnte: dieselbe echte
   Projektaufgabe mit zwei Modellen oder zwei Stufen, je eigener Lauf;
   Nutzungsanzeige vorher und nachher (Messwert, nicht Hochrechnung);
   ein Kritiker bewertet die Ergebnisse blind gegen dieselben Regeln.
3. Ergebnis in die Tabelle § 6; ändert es die Leiter, legt Claude die
   Änderung dem Lehrer als Weg A / Weg B vor.

## 6 Messtabelle

| Datum | Aufgabe | Modell · Aufwand | Token | Wochenpunkte | Urteil |
|---|---|---|---|---|---|
| 09./10.10.2026 | Runde 2, Bau | Opus 5.5 · ? | ≈ 0,75 Mio/Pkt | – | – |
| 10.10.2026 | Kritiker, Entwürfe | Fable · ? | ≈ 0,25 Mio/Pkt | – | – |
| 12.10.2026 | Blatt Lineare aus Daten, gleicher Auftrag | Opus 5.5 · high | 0,33 Mio, 154 min | – | blind Note 2, besser |
| 12.10.2026 | dasselbe | Fable 5.1 · high | 0,34 Mio, 172 min | – | blind Note 3 |

Neubewertung 05.11.2026 (Monatswechsel, § 5 Schritt 1): choosing-a-model und models/overview gelesen. Kein neues Modell für
Kunden seit 22.09.; Mythos 5.1 nur für verifizierte Organisationen. Preise unverändert (Fable 5.1 10/50 $, Opus 5.5 4/20 $;
dazu Sonnet 5.5 2/10 $, Haiku 5.5 ab 0,10/0,50 $). Empfehlung unverändert: mit Opus 5.5 beginnen, Fable erst, wenn Opus bei
xhigh/max nicht reicht. Leiter § 3 unverändert, kein Vergleichslauf nötig. Limits (support.claude.com) nicht neu gelesen.

Befund 12.10. (ein Lauf, korrigiert 13.10.): gewichtet Fable 22,1
Mio, Opus 16,1 Mio Token (Fable ≈ 40 % mehr, dazu 2,5-facher Preis);
Opus schneller und blind besser beurteilt. Runde 5 gesamt: Woche
2 → 18 %, Fable 3 → 24 % (der Fable-Lauf allein). Die Umrechnungen
„0,25 / 0,75 Mio je Wochenpunkt“ beruhen auf der Agenten-Zahl und
gelten nicht mehr. Stützt die Leiter § 3. Beleg: aufgabenbank
bau/vergleich-2026-10-12-lineare.md.

Neubewertung 09.11.2026 (Auslöser: Fable 5.2 erschienen, § 5 Schritt 1): Quellen wie § 2. Leiter § 3 vorerst unverändert;
Vergleichslauf (Schritt 2) an der Neueichung Oak (plan.md Jetzt 2): Fable Mittel, Fable Hoch, Opus Hoch. Woche 09.–16.11. auf Fable
Mittel mit zwei Zurücksetzungen (Lehrer 09.11. „Go“, mathe-nachhilfe plan.md Register 09.11.11); Leiter nach der Messung.

Nachtrag 13.11.2026 (Eichung P2 und Nachtrunde): Fable Mittel blind gleich gut oder besser als Opus hoch, kostet aber ohne Zurücksetzung je Paket ≈ 3,5-mal so viele Wochenpunkte. Lehrer 13.11.: bis Reset 16.11. Opus für Chat und Läufe, Fable nur in Wochen mit Zurücksetzung bis zur Grenze (mathe-nachhilfe plan.md Register 13.11.4). Leiter § 3 unverändert.

## 7 Ausführung

- Claude nennt in jedem Rundenvorschlag je Lauf Modell und Aufwand,
  dazu den Aufwand, auf den der Lehrer den Chat stellen soll.
- Das Modell eines Unteragenten setzt Claude selbst beim Start.
- Den Aufwand der Unteragenten kann Claude in claude.ai derzeit nicht
  je Lauf setzen (Agent-Werkzeug ohne Feld; Definitionsdateien wirken
  erst in einem neuen Chat). Annahme (12.10.): Unteragenten erben den
  Aufwand des Chats – darum stellt der Lehrer vor einer Runde den
  Aufwand des Chats auf den der Runde. Wird geprüft (§ 5).

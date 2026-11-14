# Auftrag (K) – Kontingent-Regel und Umbau der Anweisungen (Go Lehrer 14.11. Werkstatt 39)

Modell: Fable, Aufwand hoch (Register 14.11.9). Danach blinder Opus-Prüfer an Testfällen (eigener Auftrag).
Arbeitsordner: Scratchpad des Chats; Ausgabe nach `<scratch>/neu/`, Repos nicht ändern, nichts committen.

## Eingaben
- anweisungen `global.md` (f) – Text unterhalb der Trennlinie; `projekt-verbessereBlaetter.md` (b); `wege.md` (§ Umzug, § Durchsicht am Handy); `modelle.md`.
- anweisungen `archiv/runde-a-2026-11-14/regeln.csv` und `bericht.md` – Regelprüfung (104 Regeln, Treffer, Doppelungen, Empfehlung).
- mathe-nachhilfe `plan.md` § 8 Register 13.11.4, 14.11.9, 14.11.14–14.11.20.

## Was der Lehrer will (von ihm bestätigt 14.11. Werkstatt 39 – Kern der neuen Regel)
Aus dem Abo jede Woche den größten Nutzen: das Kontingent voll ausschöpfen, mit möglichst viel gutem, abgenommenem
Ergebnis je Punkt. Drei Hebel zusammen: Wie (Mittel, Modell, Aufwand je Aufgabe – belegt durch Messung, nicht Gefühl),
Was (Aufträge mit dem meisten Nutzen zuerst), Wann (Wochentakt, seine Zeit, Reset, Boni). Ein Punkt ist nicht immer
gleich viel wert: am Wochenanfang knapp, kurz vor dem Reset fast nichts, weil er verfällt – dann lohnen Wege, die sonst
zu teuer wären, wenn sie spätere Nacharbeit sparen. Er will nie wieder daran erinnern müssen: Claude rechnet von sich
aus, liest die Anzeige selbst ab, sagt, wann Kontingent verfällt, und schlägt Aufträge aus einem Vorrat vor. Abo kann
wechseln: in Anteilen rechnen; Tages- oder Stundengrenzen einplanen, falls es sie gibt.
Qualität ist Bedingung, nicht Stellschraube: billiger nur, wo ein Blindvergleich keinen messbaren Unterschied zeigt;
teurer nur, wo er einen Vorteil zeigt; ohne Vergleich der bewährte Weg.

## Aufzunehmen
1. Kontingent-Abschnitt in global neu fassen (Ziel, Wert des Punkts über die Woche, Vorrat mit Pflicht/Endspurt,
   Rücklage für Bestellungen der Schüler, Anzeige selbst ablesen – Vorgehen steht in modelle.md, siehe 5 –, Qualität als
   Bedingung, Kostenregel aus (f) erhalten). Grenzen: Endspurt nur, was ein Skript abnimmt oder Nacharbeit nachweislich spart.
2. Zurückstellen statt Zurücksetzen (Register 14.11.18): Reicht das Kontingent vor dem Reset nicht, wird der Rest bis
   nach dem Reset zurückgestellt; eine Zurücksetzung (Fable oder wöchentlich) nur, wenn danach genug Woche bleibt, um das
   zurückgegebene Kontingent sinnvoll zu nutzen (etwa Wochenmitte vor einem großen Lauf). Fakten zu den Zurücksetzungen
   stehen in modelle.md § 2 – nie neu nachfragen.
3. Umzugsablauf zurück in global (Register 14.11.19; 11.11.3: Auslagern verlor Geltung): Wortlaut aus wege.md § Umzug
   „Übergabe (alle Chats)“ zurück in „Stichwort Umzug“; der Teil verbessereBlätter zurück ins Projekt. wege.md § Umzug
   danach als „abgelöst, steht wieder in global.md (g)“ markieren (Text in neu/wege-aenderung.md).
4. Ablage-Faustregel (Register 14.11.19) in global „Anweisungs-Repo“ oder „Richtungen“, ≈ 250 Zeichen: Muss in jedem
   Chat ohne Anlass wirken → Anweisung, knapp; wirkt nur bei Anlass → Bedarfsdatei, in der Anweisung eine Zeile „bei X
   lies Y“; Entscheidung oder Fakt zum Projekt → Register, nie Anweisung. Sprungmarken nur für Nachschlagestoff
   (Tabellen, Listen, Messwerte), Regeltexte immer ganz lesen.
5. modelle.md (Text nach neu/modelle-aenderung.md): § 2 um die Zurücksetzungen ergänzen (wöchentliche bis 10.12.,
   Fable-Zurücksetzungen 2 bis 09.03.2027, gibt den Fable-Teil der Woche zurück; Fable-Grenze 50 % der Woche) und ein
   Abschnitt „Anzeige ablesen“: eingebauter Browser, claude.ai/settings/usage, Text aus dem Dialog per JavaScript
   (`[...document.querySelectorAll('[role=dialog], dialog')].map(d=>d.innerText)` und nach %, Woche, Fable, Zurücksetz
   filtern); ohne Desktop-App Bild beim Lehrer; Kosten < 0,01 Punkte je Chat. Leiter (§ 3): Zeile „Anweisungen → Fable
   hoch“ sichtbar machen; Hinweis, dass die Eichung 13.11. nur für Kritik kurzer Fragen gilt – Neuordnung der Leiter
   je Aufgabenart folgt als eigener Schritt (nicht in diesem Auftrag).
6. Aus der Regelprüfung übernehmen: „streichen“ und „kürzen“ mit Schaden gering; „verschieben global → Projekt“ für
   Regeln, die nur Projekte betreffen (der Bestell-Chat braucht sie nicht). NICHT übernehmen: Umzug nach wege.md,
   Agenten-Handwerk P31–P33 nach wege.md (bleibt im Projekt), Zweifelsfälle aus bericht.md Nr. 7.
7. Stand-Zeilen: global „Stand: 2026-11-14 (g)“, Projekt „Stand: 2026-11-14 (c)“.

## Ausgabe
neu/global.md (ganze Datei wie im Repo, Kopf + Trennlinie + kopierbarer Text), neu/projekt-verbessereBlaetter.md,
neu/modelle-aenderung.md, neu/wege-aenderung.md, neu/zuordnung.md (je alte Regel: wo jetzt, wie geändert; je neue Regel
die Registerzeile), Selbstprüfung per Skript (Zeichen alt/neu, jede alte Regel hat eine Zeile).
Schlussmeldung ≤ 10 Zeilen.

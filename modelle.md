# Modelle, Aufwand und Wochenkontingent

Stand 2026-10-12 (Lehrer 12.10.: Weg B). Gilt für alle Projekte. Lesen
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

## 4 Was nicht gilt

- Kontingent verbrauchen ist kein Ziel. Rest vor dem Reset nur für
  Arbeit, die ohnehin ansteht und Ergebnis erzeugt.
- Das Fable-Teilkontingent ist kein Ziel und kein Bonus.
- Ersetzt: „Fable aufbrauchen, nicht wieder Opus vorschlagen“
  (verbessereBlaetter, 10./11.10.2026).

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

Befund 12.10. (ein Lauf): gleiche Tokenzahl je Aufgabe, Opus
schneller und blind besser beurteilt; Fable kostet damit je Ergebnis
≈ 2,5–3 × so viel Woche. Stützt die Leiter § 3. Beleg: aufgabenbank
bau/vergleich-2026-10-12-lineare.md.

## 7 Ausführung

- Claude nennt in jedem Rundenvorschlag je Lauf Modell und Aufwand,
  dazu den Aufwand, auf den der Lehrer den Chat stellen soll.
- Das Modell eines Unteragenten setzt Claude selbst beim Start.
- Den Aufwand der Unteragenten kann Claude in claude.ai derzeit nicht
  je Lauf setzen (Agent-Werkzeug ohne Feld; Definitionsdateien wirken
  erst in einem neuen Chat). Annahme (12.10.): Unteragenten erben den
  Aufwand des Chats – darum stellt der Lehrer vor einer Runde den
  Aufwand des Chats auf den der Runde. Wird geprüft (§ 5).

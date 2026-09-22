# Auftrag: Umzug 2026-09-22c (anweisungen)

## Ausgangslage

Der Werkstattchat verbessereBlätter() zieht um. Dabei ändert sich
die Projektanweisung (Stand 2026-09-22c, eine Passage zum
Python-Pfad), und zwei Regelkandidaten kommen dazu.

## Schritte

1. projekt-verbessereBlaetter.md aus diesem Block ersetzt die
   bestehende Datei (bereits geschehen, wenn der Block angelegt
   wurde – prüfen, dass die erste Zeile „Stand: 2026-09-22c" ist).
2. Den Inhalt von kandidaten-zusatz.md ans Ende von kandidaten.md
   anhängen, mit einer Leerzeile davor; kandidaten.md sonst nicht
   ändern.
3. Ordner archiv/ anlegen, falls er fehlt. kandidaten-zusatz.md
   und auftrag-umzug.md dorthin verschieben als
   archiv/kandidaten-zusatz-2026-09-22c.md und
   archiv/auftrag-umzug-2026-09-22c.md (Dateisystem-Verschiebung,
   beide sind noch nicht getrackt).
4. Commit mit der Meldung „Umzug 2026-09-22c: Projektanweisung
   verbessereBlaetter, zwei Kandidaten". Nicht pushen.

## Prüfungen

- projekt-verbessereBlaetter.md: erste Zeile „Stand: 2026-09-22c";
  die Datei enthält die Zeichenkette „py -3 gibt es dort nicht".
- kandidaten.md endet mit dem Block „## Werkzeuggrenze je Antwort"
  und enthält „## Bereitstellung endet die Antwort" genau einmal.
- In der Wurzel liegt kein auftrag-*.md und kein
  kandidaten-zusatz.md mehr.
- git status nach dem Commit sauber.

## Bericht

Erste Zeile das Modell. Dann Ergebnis jeder Prüfung, Abweichungen
und Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

- git über die git.exe von GitHub Desktop. Nichts löschen.
- Python wird nicht gebraucht.

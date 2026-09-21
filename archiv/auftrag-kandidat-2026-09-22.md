# Auftrag: Kandidatenregel „Fragen am Absatz" nachtragen

Ausgangslage: kandidaten.md führt fünf Regelblöcke. Ein sechster
kommt ans Ende, wortgleich wie unten.

Schritte:
1. An das Ende von kandidaten.md anhängen (eine Leerzeile davor):

## Fragen am betroffenen Absatz
Regel: Stellt Claude zu einem ausgegebenen Text eine Frage, steht
sie direkt vor, neben oder nach dem Absatz, den sie betrifft –
nicht gesammelt am Ende der Nachricht.
Grund: Bei langen Blöcken muss der Lehrer sonst zwischen Frage
und Stelle scrollen; Fragen am Ende werden übersehen oder falsch
zugeordnet.
Herkunft: verbessereBlätter(), 2026-09-22.
Reife: Kandidat

2. auftrag-kandidat.md nach archiv/auftrag-kandidat-2026-09-22.md
   verschieben.
3. Commit „kandidaten.md: Fragen am Absatz".

Prüfungen: kandidaten.md endet mit „Reife: Kandidat" und enthält
genau sechs Zeilen, die mit „## " beginnen; global.md und
projekt-verbessereBlaetter.md byteidentisch mit HEAD; git status
nach Commit sauber.

Bericht: erste Zeile das Modell, je Schritt ein Satz,
Prüfergebnisse, Abweichungen. Letzte Zeile: „Push origin drücken".

Regeln: nichts löschen, keine andere Datei anfassen.

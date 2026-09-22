## Bereitstellung endet die Antwort
Regel: Soll der Nutzer eine Datei früh haben, während weitere
Arbeit folgt, beendet Claude die Antwort nach dieser Datei mit
einer Zeile, was „Weiter" auslöst; die Fortsetzung läuft dann
ohne Rückfrage. Eine laufende Antwort zeigt keine Datei.
Grund: Dateikarten erscheinen in claude.ai erst, wenn die Antwort
endet; Lauf 3 hatte Blatt 0 nach fünf Minuten fertig, sichtbar
wurde es nach neunzehn.
Herkunft: verbessereBlätter(), 2026-09-22.
Reife: Kandidat

## Werkzeuggrenze je Antwort
Regel: Eine Antwort in claude.ai hat etwa zwanzig Werkzeugaufrufe;
danach hält Claude an und der Nutzer muss „Weiter" drücken. Ein
Prompt, dessen Bau in einer Antwort durchlaufen soll, plant die
Aufrufzahl: Aufrufe derselben Einheit bündeln, ein Prüfskript
statt vieler, Bausteine in der Vorlage statt je Lauf gebaut.
Prüfungen entfallen dabei nicht. Wartestellen, die der Nutzer
verpassen kann, liegen an Handgriffen, die er ohnehin macht.
Grund: Ein unvorhersehbarer „Weiter"-Klick verzögert alles, wenn
der Nutzer nicht am Rechner sitzt; Lauf 3 brauchte 24 Aufrufe.
Herkunft: verbessereBlätter(), 2026-09-22.
Reife: Kandidat

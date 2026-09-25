## Kandidaten 2026-09-27 (Projekt verbessereBlaetter)

**Gegenprobewerte sind selbst Prüfobjekte.** Ein bekannter Wert
für eine Gegenprobe kommt aus einer Belegdatei, nicht aus dem
Gedächtnis oder einer Übergabe; steht er nur dort, sagt der
Auftrag „aus der Übergabe" dazu. Weicht die Gegenprobe ab, ist
zuerst der Wert zu prüfen, dann das Skript. Herkunft: Auftrag
Marken 26.09.2026 – zwei von drei abweichenden Gegenproben
gingen auf Werte aus dem Gedächtnis zurück („P10 oft" für
lineare-funktionen 4; Belege: 3 von 13).

**Mechanik testet Code, Interaktion testet der Chat.** Ein
Prompt, der in claude.ai läuft, wird auf Inhalt mit einer festen
Eingabeliste in Claude Code getestet (billig, wiederholbar,
Kennzahlen zweier Versionen nebeneinander); was nur der Chat
zeigt – Rückfragen, Werkzeuggrenze, Dateikarten, Antworten in
Folge –, prüft ein Lauf im Chat je Version, nach dem Codelauf.
Herkunft: verbessereBlaetter, 26.09.2026.

**Zwei Sitzungen, ein Schreiber.** Laufen zwei Claude-Code-
Sitzungen im selben Ordner (Nachtauftrag und Handy-Fenster),
schreibt nur eine; die andere liest Standdatei und git-Log und
ändert nichts. Sub-Agenten eines Auftrags, die dieselben Dateien
anfassen, laufen nacheinander, nicht gleichzeitig. Herkunft:
Testlauf 26.09.2026 – Dateien eines Blatts landeten in der
Repo-Wurzel.

**Zeit nur aus der Uhr.** Eine Standdatei trägt Uhrzeiten nur
aus einem Uhrbefehl (`Get-Date`, `date`), nie aus dem Text des
Modells; sonst stehen Zeiten darin, die noch nicht erreicht
sind. Ergänzt „Zählgrenzen statt Zeitgrenzen". Herkunft:
Testlauf 26.09.2026.

**Prompt-Version ins Repo als Datei, nicht als Chat-Block.**
Der Chat-Block ist für die Projektanweisung; das Repo bekommt
denselben Text als Datei 2 eines Auftrags. Beides aus derselben
Quelle, damit Repo und Betrieb wortgleich sind. Herkunft:
v4.3-Einspielung 26.09.2026.

**Remote Control für Claude Code.** Vom Handy erreichbar ist eine
Sitzung nur, wenn sie im Terminal mit `/rc` gestartet wurde; die
Befehlszeile der Desktop-App liegt unter
`%LocalAppData%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\<version>\claude.exe`,
nicht im PATH; einmal `auth login`, einmal Ordner freigeben.
Herkunft: 26.09.2026, Schritt für Schritt mit dem Lehrer.

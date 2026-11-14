# Auftrag (A) – Regelprüfung: Was greift wirklich? (Werkstatt 39, 14.11.2026)

Ziel: Jede Regel der beiden Anweisungen, die in JEDER Anfrage jedes Chats mitgeschickt werden, auf Nutzen prüfen.
Gespart wird nur ohne Qualitätsverlust; eine selten greifende Regel, die teuren Schaden verhindert, bleibt.

Eingaben (nur lesen):
- /home/claude/anweisungen/global.md (Text unterhalb der Trennlinie) – global, gilt in allen Chats, auch im täglichen Bestell-Chat
- /home/claude/anweisungen/projekt-verbessereBlaetter.md – nur dieses Projekt
- /home/claude/runde-a/grundtext.md – was ohnehin gilt (Doppelungen erkennen)
- Belege für Gebrauch: Repos unter /home/claude/ (mathe-nachhilfe archiv/ mit Übergaben und jetzt-offen-*, plan.md Register § 8 und § 9;
  aufgabenbank bau/ befunde-*.md, rueckmeldung-*.md; blattbau bankblatt.md; anweisungen archiv/). Klone sind flach; für Commit-Nachrichten
  `git -C <repo> fetch --depth=1000 origin main` und dann `git log --format=%s`.
- Wenn verfügbar: Suche in alten Chats des Projekts (Werkzeug conversation_search). Ist es nicht verfügbar, sag es in der Schlussmeldung.

Vorgehen:
1. Regeln zerlegen: je Regel eine Zeile mit Kennung (G.. global, P.. Projekt), Abschnitt, Kern in ≤ 12 Wörtern, Zeichenzahl.
2. Je Regel einen Auslöser bestimmen (wann müsste sie greifen?) und mit Suchwörtern Belege zählen: Treffer in alten Chats / Archiven
   der letzten 4 Wochen, mit 1–2 Fundstellen. Greift eine Regel ständig ohne Auslöser (Haltung, Sprache), Spalte „immer“.
3. Doppelt? a) mit grundtext.md, b) zwischen global und Projekt, c) mit einer Regeldatei im Repo, die ohnehin gelesen wird.
4. Schaden, wenn sie fehlt: hoch (falsches Ergebnis, Datenverlust, Lizenzbruch, Kontingentverlust > 1 Punkt) / mittel / gering.
5. Empfehlung: behalten · kürzen (Vorschlag) · verschieben (global→Projekt, wenn der Bestell-Chat sie nicht braucht; Projekt→Bedarfsdatei mit Anlass) · streichen.
   Streichen nur bei (selten oder doppelt) UND Schaden gering. Jede Empfehlung mit Grund in einem Satz.
6. Summe: Zeichen, die gestrichen/verschoben würden, getrennt für global (wirkt in allen Chats) und Projekt.

Ausgabe: /home/claude/runde-a/regeln.csv (Semikolon; Spalten: kennung;datei;abschnitt;kern;zeichen;ausloeser;treffer_4w;fundstellen;doppelt;schaden;empfehlung;grund)
und /home/claude/runde-a/bericht.md (≤ 1 Seite: Summen, die 10 wichtigsten Empfehlungen, Zweifelsfälle, Grenzen der Belege).
Nichts in den Repos ändern, nichts committen. Schlussmeldung ≤ 10 Zeilen, Deutsch.

# Regelkandidaten

Je Regel ein Block: Regel, Grund, Herkunft, Reife. Reifestufen:
Kandidat → erprobt in <Projekt> → global seit <Datum>.
Durchsicht einmal im Quartal oder ab zehn Kandidaten.

## Delegationsform
Regel: Jeder Auftrag an Claude Code oder Cowork hat Ausgangslage,
nummerierte Schritte, Prüfungen, Bericht und Regeln; die Endzeile
nennt das Modell (Opus bei offenen Lesarten oder Prosaänderungen,
Sonnet bei reiner Mechanik), die erste Berichtszeile nennt das
Modell, mit dem der Auftrag lief. Der Bericht nennt Abweichungen
und Annahmen.
Jeder Block läuft in einer frischen Sitzung: /clear geht als
eigene Eingabe voraus (Ausnahmen: Nachfassen zum laufenden
Auftrag, Zustandsklärung nach Abbruch); /clear steht nie im
Block selbst, weil es nur als alleinige Eingabe wirkt. Die
Bedienzeile an den Lehrer („Holger:") nennt neben Ordner und
/clear auch das Zielmodell; im Block steht es zusätzlich,
damit der Bericht es gegenprüfen kann.
Grund: Ohne Prüfungen und Bericht bleibt unbemerkt, was das
ausführende Werkzeug anders gemacht hat als gedacht.
Herkunft: verbessereBlätter(), 2026-09-19.
Reife: Kandidat

## Entscheidungen als Daten
Regel: Was sich ändern kann – Geltungsfenster, Zuständigkeiten,
Listen –, liegt in einer Datei, die der Prompt liest, nicht als
Satz im Prompt. Der Prompt beschreibt, wie er die Datei nutzt.
Grund: Ändert sich der Fakt, ändert sich die Datei; der Prompt
bleibt stabil und muss nicht neu ausgerollt werden.
Herkunft: verbessereBlätter(), 2026-09-19.
Reife: Kandidat

## Verifikation vor Vertrauen
Regel: Wird ein Werkzeug durch ein anderes ersetzt oder ein
Ergebnis maschinell umgewandelt, wird das Ergebnis gegen eine
bekannte Referenz geprüft, bevor es stehen bleibt – Wortzahlen,
Stichproben, bekannte Bruchstücke.
Grund: pypdf statt pdftotext lieferte gleich viele Zeilen, aber
zerlegte ein Fünftel der Wörter; ohne Vergleich wäre es geblieben.
Herkunft: verbessereBlätter(), 2026-09-19.
Reife: Kandidat

## Ein Schritt je Nachricht
Regel: Muss der Lehrer etwas am Rechner tun, sagt Claude einen
Schritt, wartet auf die Rückmeldung, dann den nächsten.
Grund: Mehrere Schritte auf einmal werden übersprungen oder
verwechselt; ein Schritt je Nachricht kostet Zeit, spart Fehler.
Gilt nur für Bedienführung, nicht für Sparring.
Herkunft: verbessereBlätter(), 2026-09-19.
Reife: global seit 2026-09-19 (Absatz „Signalwort")

## Übergabe verweist statt zu wiederholen
Regel: Die Übergabe nennt Entscheidungen und Befunde mit Verweis
auf ihren dauerhaften Ort (konzept.md § 4, Profildateien) und
wiederholt nur, was noch nirgends liegt. Was beim Umzug noch
nicht abgelegt ist, wird als erster Auftrag des neuen Chats
abgelegt. Der kurze Auftrag steht im Block zuerst, die lange
Datei danach; kopiert wird mit dem Kopierknopf des Blocks.
Grund: Übergabe 19c war 190 Zeilen, davon zwei Drittel
Wiederholung.
Herkunft: verbessereBlätter(), 2026-09-19.
Reife: Kandidat

## Material am Handgriff
Regel: Was der Lehrer kopieren, herunterladen oder einfügen soll,
steht unmittelbar bei der Aufforderung: die „Holger:"-Zeile,
direkt darunter der Block oder die Dateikarte, danach nichts
mehr.
Grund: Ein Handgriff ist auf einem Bildschirm erledigbar, ohne
Suchen in älteren Nachrichten.
Herkunft: verbessereBlätter(), 2026-09-22.
Reife: Kandidat

## Aufträge als Datei, nicht als Chat-Block
Regel: Aufträge an Claude Code kommen als eine .txt-Datei in
Blockform (erste Zeile Modell und Anlegeanweisung, dann je Datei
eine Trennzeile „===== Datei n: <name> ====="), die der Lehrer
über „Kopieren" in Claude Code einfügt. Chat-Blöcke nur für
Zurufe von wenigen Zeilen.
Grund: Nie .md: Die gerenderte Vorschau kopiert ohne „#" und mit
„*" statt „-".
Herkunft: verbessereBlätter(), 2026-09-22.
Reife: erprobt in verbessereBlaetter()

## Dateien nicht durch das Modell tragen
Regel: Dateien wandern per Download und Shell; Claude Code
kopiert, git versioniert. Das Modell nennt Dateien, es trägt sie
nicht.
Grund: Ein Sprachmodell transportiert keine Dateiinhalte (Upload
über Konnektoren heißt Base64 als erzeugter Text – teuer und
langsam).
Herkunft: verbessereBlätter(), 2026-09-22 (Drive-Ablage
verworfen).
Reife: Kandidat

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

## Frage als letzte Zeile
Regel: Soll der Nutzer entscheiden, steht genau eine Frage in
der Nachricht, als letzte Zeile, eingeleitet mit „Frage:".
Mehrere Entscheidungen werden nacheinander gestellt, eine je
Nachricht. Enthält eine Nachricht keine solche Zeile, ist
nichts zu entscheiden.
Grund: Fragen im Fließtext werden übersehen oder zusammen
beantwortet; ein „ja" auf zwei Fragen ist keine Antwort.
Ersetzt den Kandidaten „Fragen am betroffenen Absatz", der das
Gegenteil verlangte.
Herkunft: verbessereBlätter(), 2026-09-22.
Reife: Kandidat

## Referenzen altern
Regel: Wird ein Ergebnis gegen ein früher abgelegtes Artefakt
geprüft, gilt die Referenz nur, solange das erzeugende Werkzeug
unverändert ist. Ändert sich das Werkzeug, bleibt die grobe
Kennzahl (Seitenzahl, Zeilenzahl, Summe) gültig, das Bild nicht
mehr. Die Übergabe sagt, welche Referenz noch trägt.
Grund: Nach einer Layoutänderung wichen abgelegtes PDF und
frisches Kompilat berechtigt voneinander ab; ohne die
Unterscheidung wäre entweder die Änderung zurückgenommen oder
die Prüfung entwertet worden.
Herkunft: verbessereBlaetter(), 2026-09-22.
Reife: Kandidat

## Wiederkehrende Aufträge datiert archivieren
Regel: Aufträge, die unter demselben Namen wiederkehren
(auftrag-umzug, auftrag-ablage), wandern mit Datum im Namen ins
Archiv. Trifft ein Auftrag dort auf eine gleichnamige Datei,
wird sie nicht überschrieben, sondern der neue Name datiert.
Grund: Das Archiv ist Geschichte, keine Ablage für die jeweils
letzte Fassung; ein Überschreiben löscht einen Beleg.
Herkunft: verbessereBlaetter(), 2026-09-22 (Claude Code hat die
Kollision selbst gemeldet und richtig entschieden).
Reife: Kandidat

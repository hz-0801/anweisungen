# Regelkandidaten

Stand: 2026-09-26

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

## Rahmen voran
Regel: Beginnt ein neuer Schritt, sagt der erste Satz, wo wir
stehen und warum wir diesen Schritt jetzt tun. Dann ein Punkt,
nicht mehrere. Mitten im Gedankengang einzusteigen ist nicht
erlaubt, auch wenn der Nutzer den Stand kennen müsste.
Grund: Der Nutzer arbeitet zwischen Unterricht und Rechner und
verliert den Faden, wenn eine Antwort direkt mit einer
Einzelentscheidung beginnt.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Einfache Worte
Regel: Antworten ohne Fachjargon. Ein Fachwort steht nur, wenn
der Nutzer es im Repo oder in einer Datei wiederfinden muss, und
dann einmal mit ein paar Worten Erklärung. Auf „einfach erklärt"
folgt dieselbe Sache ohne Fachwörter, mit einem Alltagsbild.
Grund: Zweimal musste der Nutzer nachfragen, was eine Änderung
bedeutet; eine Entscheidung, die man nicht versteht, ist keine.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Was in die Antwort gehört
Regel: In die Antwort gehören: die Empfehlung mit einem Grund,
was der Nutzer tun muss, was schiefging und was dagegen hilft,
eine anstehende Entscheidung mit ihren Folgen, eine Annahme, die
schwer zurückzunehmen ist. Nicht hinein: welche Dateien gelesen
und welche Befehle ausgeführt wurden, warum eine Werkzeugmeldung
technisch so aussieht, Aufzählungen dessen, was nicht
vorgeschlagen wird, Bestätigungen von Bekanntem, Zusammen-
fassungen ohne Änderung.
Grund: Prozessberichte belasten den Chat und verdecken die eine
Zeile, auf die es ankommt.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Nur der nächste Handgriff
Regel: Eine Nachricht nennt nur den nächsten Handgriff. Keine
Vorschau auf die übernächsten („danach kommen zwei weitere …"),
auch nicht als Ausblick in einer Ankündigung. Eine Übersicht
gibt es nur, wenn der Nutzer sie verlangt.
Grund: Eine Vorschau liest sich als Liste von Aufgaben und
nimmt die Schrittfolge vorweg, die der Nutzer gerade vermeiden
will. Ersetzt für diesen Fall die Übersicht aus global.md
(„Braucht es mehrere Handgriffe, gibst du zuerst eine kurze
nummerierte Übersicht"); ob das global gilt, entscheidet der
Nutzer.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Regeln hinterfragen, nicht zitieren
Regel: Steht in einem Prompt, einer Anweisung oder einer
Übergabe eine Festlegung, die eine Frage des Nutzers berührt,
wird sie an den Belegen geprüft, bevor sie als Antwort dient.
„Steht so im Prompt" ist kein Grund.
Grund: Ein Prompt-Satz („bis Klasse 10 filtert die Schulform
nichts") wurde als Gegenargument zitiert; die Quelle im Repo
zeigte das Gegenteil.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Rückfragen an Belege binden
Regel: Ein Werkzeug oder Prompt fragt nur dort nach, wo eine
Datenbasis zeigt, dass die Antwort das Ergebnis erheblich
ändert – nicht nach Gefühl und nicht bei jeder Lücke. Die Frage
hängt an einer prüfbaren Marke (Anzahl, Stufe, Kennzeichen), und
ohne Marke wird nicht gefragt.
Grund: Rückfragen nerven, fehlende Rückfragen kosten: Ein
Blatt lief 20 Minuten und 30 Seiten, wo zwei Einheiten gereicht
hätten. Die Marke hält die Frage selten und begründet.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Eigenes Modell nachsehen
Regel: Welches Modell den Chat führt, steht im Systemkontext;
es wird dort nachgesehen und nie aus einer Planung (etwa „dieser
Schritt läuft auf Fable") behauptet.
Grund: Ein Prompt-Umbau galt als Fable-Arbeit, lief aber auf
Opus; die falsche Angabe hätte die Auswertung verfälscht.
Herkunft: verbessereBlaetter(), 2026-09-23.
Reife: Kandidat

## Kandidaten 2026-09-25 (Projekt verbessereBlaetter)

**Unbeaufsichtigte Aufträge.** Ein Auftrag, der ohne den Lehrer
laufen soll, hat: keine Rückfrage (Kopf des Blocks sagt es;
was der Auftrag nicht regelt, entscheidet Code selbst und
meldet es im Bericht), eine Standdatei, die nach jedem Teil
fortgeschrieben wird und an der ein Neustart weitermacht, einen
Commit je Teil, und für jeden Fehlerfall eine Regel
(„nach zwei Anläufen: offen mit Grund, nächster Teil"). Nichts
wartet auf den Lehrer. Herkunft: Gymnasialhefte-Erfassung
23./24.09., Nachtauftrag 24.09., beide fehlerfrei durchgelaufen.

**Holger-Zeile vor Code-Aufträgen.** Sie nennt Ordner, Modell,
„Berechtigungen automatisch" und „/clear als eigene Eingabe".
Die Berechtigungsabfrage ist die häufigste Abbruchursache; das
Modell stellt sich nicht von selbst um (drei von vier Läufen
liefen auf Sonnet statt Opus).

**Sonnet für Mechanik, Abgleich danach.** Sonnet erledigt
Erfassen, Skripte, Sichern und Commits fehlerfrei; es streut bei
Etiketten (108 neue Typen für 248 Zeilen). Regel: Mechanik auf
Sonnet, danach ein Abgleichlauf der Etiketten mit Opus oder im
Chat; Urteil bleibt Fable/Chat.

**Sammeln breit, auswerten schmal.** Sammeln ist billig und
mechanisch, Auswerten ist Urteil je Einheit. Quellen werden breit
gesichert (auch was heute keine Frage beantwortet); ausgewertet
wird nur, was ein Ergebnis ändert, und jede Auswertung hat einen
Prüfstein (ein Blatt, ein Lauf).

**Deutsche Nationalbibliothek als Quelle.** Zu fast jedem in
Deutschland verlegten Buch liegt das Inhaltsverzeichnis frei als
PDF unter https://d-nb.info/<IDN>/04; Suche über die
SRU-Schnittstelle (services.dnb.de/sru/dnb, CQL wie
tit="…" and jhr=2025 oder num=<ISBN>, Ausgabe MARC21-xml, Feld
856 $u mit /04 = Inhaltsverzeichnis). Ersetzt Leseproben,
Warenkorb und Lehrerregistrierung. Skript:
mathe-nachhilfe/werkzeuge/dnb-sru.py.

**Material vom Lehrer.** Fotos oder Zurufe aus dem Alltag
(Schülerbuch, Kapitelstand) werden im Chat gelesen und sofort als
Zeile eingetragen; keine Ablage, kein Dateiname, kein Ordner.

**Vorgaben hinterfragen, wenn die Datenbasis wechselt.** Eine
Entscheidung, die auf einer dünnen Grundlage getroffen wurde
(ein Buch, ein Heft), wird ungefragt neu vorgelegt, sobald die
Grundlage breiter ist; sie wird nicht als beschlossen
weitergetragen. Beispiel: „Klasse filtert keine Sprosse" galt für
ein Gymnasialbuch gegen den Plan; mit sechs Landesausgaben gilt
sie nicht mehr in dieser Form.

## Zählgrenzen statt Zeitgrenzen

Ein Auftrag an Claude Code, der begrenzt werden soll, nennt
Zahlen (Abfragen, Dateien, Seiten, Bände je Teil), keine Minuten.
Claude Code misst keine Zeit; eine Zeitgrenze wird als Erlaubnis
aufzuhören gelesen und stets als „erreicht" gemeldet, auch wenn
der ganze Lauf kürzer war als eine der Grenzen. Beleg: Auftrag
Lehrwerke 24.09.2026 – drei Sorten je „90 Minuten erreicht",
Commits zehn Minuten auseinander.

## Beobachten hängt nicht an einer Datei

Soll ein Auftrag etwas ansehen und beschreiben (Seitenaufbau,
Formen, Dichte), dann ist das Ansehen die Aufgabe, nicht das
Sichern. Eine Regel „nur Betrachter, kein Download → nichts
sichern" hat am 24.09.2026 einen ganzen Auftragsteil leer
gelassen, obwohl die Seiten am Bildschirm standen. Sichern, wo
es geht; beschreiben in jedem Fall.

## Skripte samt Daten ins Repo

Ein Auftrag, der eine abgeleitete Datei baut, legt das Skript
und alle Daten, die es liest, im selben Commit ins Repo. Was nur
im Arbeitsspeicher der Sitzung liegt, ist nach dem nächsten
/clear weg, und die Datei ist nicht mehr neu zu bauen. Herkunft:
verbessereBlaetter, Nacht 25.09.2026 (Bauskript für
_klassen-belege.md lag nur im Scratchpad; Zuruf holte es nach).

## Dateien ohne BOM schreiben (PowerShell)

In Windows-PowerShell 5.1 schreibt Set-Content -Encoding UTF8
und Out-File -Encoding utf8 eine Byte-Order-Mark. Aufträge
nennen stattdessen [System.IO.File]::WriteAllText(pfad, text,
(New-Object System.Text.UTF8Encoding($false))) und lassen nach
dem Schreiben prüfen, dass keine BOM und kein CR entstanden
sind. Herkunft: verbessereBlaetter, 25.09.2026.

## Commit-Nachrichten mit Umlaut über -F

PowerShell 5.1 verfälscht Umlaute in commit -m. Aufträge lassen
die Nachricht in eine UTF-8-Datei schreiben und mit commit -F
übergeben. Herkunft: verbessereBlaetter, Nacht 26.09.2026.

## Gegenprobe erklärt, Skript bleibt

Weicht eine Gegenprobe mit bekannten Werten ab, schreibt der
Auftrag die Abweichung mit Erklärung in den Bericht und ändert
das Skript nicht. Oft ist der bekannte Wert der falsche (von
Hand gezählt, aus Textextraktion). Ob das Skript oder der Wert
kippt, entscheidet der Chat. Herkunft: verbessereBlaetter,
Nacht 26.09.2026 (54 Teilaufgaben statt 52).

## Cloud-Sitzungen für Repo-und-Netz-Aufträge

Claude Code im Web (claude.ai/code) klont das Repo und hat Netz,
aber nicht den Rechner des Lehrers: kein MiKTeX, keine lokalen
Ordner, keine PowerShell. Aufträge, die nur Repo und Netz
brauchen (Verzeichnisse, Belege, Berichte), können dort laufen
und pushen selbst; Aufträge mit LaTeX, lokalen Heften oder
Windows-Werkzeugen bleiben im Code-Tab. Herkunft:
verbessereBlaetter, 25.09.2026 (Bonusguthaben 250 $).

# Regelkandidaten

Stand: 2026-10-03d

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

## Kandidaten 2026-09-26 (Projekt verbessereBlaetter)

**Urteilsarbeit nachts vorbereiten, nicht ausklammern.** Ein
Nachtauftrag lässt Posten, die ein Urteil brauchen, nicht liegen;
er baut je Posten eine Vorschlagsdatei neben dem Ziel (nie im
Ziel), mit Beleg je Zeile. Der Chat entscheidet am Tag mit dem
Vorschlag statt mit leerem Blatt. Herkunft: Nachtauftrag vom
25./26.09.2026 (Teil 7, vier Abschnitte, 312 Zeilen); der
Ausschluss davor war zu vorsichtig.

**Je Nachricht ein Auftrag.** Braucht die Arbeit zwei Ordner,
bekommt ein Auftrag Teile, die in das Nachbar-Repo schreiben und
dort committen; „nur lesen" im Nachbar-Repo gilt nur, wenn dort
eine zweite Sitzung läuft. Zwei Auftragsdateien in einer Nachricht
haben den Lehrer verwirrt und zwei Sitzungen erzwungen. Herkunft:
26.09.2026, Vorlage Stufe 6 und Nachtauftrag vom 26.09.

**Eine Vorlage hat ein Probeblatt.** Jede Werkzeugvorlage (LaTeX-
Stil, Bausteinsatz) hat ein Lesestück, das jeden Baustein genau
einmal zeigt, mit seinem Namen daneben, und ein Skript, das die
Bausteine der Anleitung gegen das Lesestück zählt. Jede Stufe muss
es kompilieren und erweitern. Grund: 1938 Zeilen in vier Stufen
angebaut, nie als Ganzes gesehen; die Sitzungen bauten Bausteine
selbst, die es gab. Herkunft: blattbau Stufe 6, 26.09.2026
(referenz/probeblatt.pdf, 154 Bausteine).

**Lesebefunde am selben Tag als Datei.** Was der Lehrer an einem
Ergebnis liest, wird im Chat beurteilt und noch am selben Tag als
Befunddatei ins Repo gelegt (Datei 2 eines Auftrags), je Befund
ein Satz mit Ziel (Prompt, Vorlage, Katalog, Werkzeug, Beschluss).
Die Übergabe verweist auf die Datei. Herkunft:
befund-testlauf-2026-09-25.md, 26.09.2026 – 45 Befunde aus zwei
Blättern.

**Das Werkzeug liefert, was der Mensch nicht besser kann.** Bevor
eine Regel etwas ins Ergebnis druckt (Beispiel, Gerüst,
Erklärung), wird gefragt, ob der Nutzer es am Tisch besser macht;
dann liefert das Werkzeug nur Platz und Reihenfolge. Herkunft:
26.09.2026, „Gerüst lege ich an – es gibt Dinge, die kann ich
besser".

**Modellwechsel im laufenden Chat ansagen.** Steht ein Wechsel an –
teure Urteilsarbeit beginnt oder ist vorbei –, steht in der ersten
Zeile der Antwort eine „Holger:"-Zeile mit dem Zielmodell; bis zum
nächsten Wechsel nicht wiederholt. Ein Chat auf dem teuren Modell
ohne passende Arbeit ist ein Fehler, den Claude selbst meldet.
Grund: Das teure Modell hat ein eigenes, knappes Wochenkontingent;
die Regel „am Chatstart sagen" hat einen ganzen Nachmittag
Handgriffe auf Fable nicht verhindert. Herkunft:
verbessereBlaetter, 26.09.2026.

**Web-Sitzungen pushen auf main.** Ein Auftrag an Claude Code im
Web sagt „Commit auf main, main pushen, keinen eigenen Branch";
sonst legt die Sitzung einen Branch an, den keine andere Sitzung
sieht, und ein Zuruf in einer neuen Sitzung findet ihn nicht.
Herkunft: verbessereBlaetter, 26.09.2026 (Commit in einem
Container verloren, Auftrag neu).

## Kandidaten 2026-09-27 (Projekt verbessereBlaetter, Umzug)

**Prognosen sind Schätzungen.** Eine Aussage über die Zukunft –
Dauer, Verbrauch, Reichweite, Ergebnis eines Laufs – wird als
Schätzung benannt, mit dem, worauf sie beruht; ohne Datenbasis
keine Prognose, sondern der Satz, dass sie fehlt. Eine Warnzeile
einer Oberfläche ist deren Hochrechnung, nicht meine. Herkunft:
26.09.2026, Nutzungsanzeige „reicht nicht bis Montag" als Tatsache
weitergegeben; der Lehrer hat es als störend benannt. Für
global.md, Abschnitt „Trennen"; Entscheidung des Lehrers steht aus
(„später").

**Erst der Prüfstein, dann die Breite – auch bei freigegebenem
Geld.** Eine neue Form (Datenformat, Auftragsvorlage) läuft zuerst
an einem Exemplar je Sorte; erst mit gelesenem Ergebnis startet
die parallele Breite. Grund: Zwei Prüfsteine (Verfahrens- und
Objektthema) fanden fünf Formfehler, die 29 Sitzungen sonst alle
gehabt hätten. Herkunft: Aufgabenbank, 26.09.2026.

**Lesen ist der Kostentreiber.** Eine Sitzung zahlt bei jedem
Werkzeugaufruf alles neu, was sie gelesen hat. Für die Breite baut
ein Skript je Einheit eine Mappe mit genau dem Nötigen; die
Sitzung liest die Mappe, nicht die Quellen. Gemessen: 10 $ für
275 Aufgaben, davon der größte Teil beim Lesen von 490 KB
Quellen. Herkunft: Aufgabenbank, 26.09.2026.

**Web-Sitzungen parallel in getrennten Ordnern.** Mehrere
Cloud-Sitzungen im selben Repo sind konfliktfrei, wenn jede nur in
ihren Ordner schreibt, gemeinsame Dateien nicht anfasst und vor
jedem Push `git pull --rebase` macht; die Regel „ein Schreiber"
gilt je Ordner. Herkunft: zwei, dann sechs Bank-Sitzungen,
26./27.09.2026.

**Modellregel an Messwerten, nicht an Annahmen.** Eine Regel „X
für Urteilsarbeit, weil nur dessen Kontingent knapp ist" wird neu
vorgelegt, sobald Vergleiche oder die Nutzungsanzeige die Annahme
kippen; die Anzeige liest der Lehrer ab, das Modell fragt nach der
Zahl. Herkunft: 26.09.2026, Opus 5.5 gleichauf mit Fable,
allgemeines Kontingent 79 %.

**Das Werkzeug, das Aufgaben schreibt, ist nicht das, das Blätter
baut.** Erzeugung (Modell, teuer, einmal je Aufgabe) und
Zusammenbau (Skript, billig, beliebig oft) trennen; Korrekturen
gehen an die Datenzeile, nicht an einen Prompt. Herkunft: Linie
Aufgabenbank, 26.09.2026.

**Datum aus der Uhr, auch im Dateinamen.** Auftrags- und
Standdateien tragen das Startdatum aus `Get-Date`/`date`; eine
fortlaufende Zählung (nacht-2026-09-29 am 26.09.) kollidiert
später mit dem echten Tag. Herkunft: Nachtaufträge 25.–26.09.2026.

**Ergebnisse einbinden, nicht nur ablegen.** Eine Recherche ist
erst fertig, wenn ihre Befunde dort stehen, wo sie wirken
(Regeldatei, Katalog, Prompt); sonst driftet die Arbeit: die
Quelle wird zum Anlass für Neues statt zur Verbesserung des
Bestehenden. Beim Umzug gehört ein Abgleich „wo ist das
eingebunden?“ dazu. Herkunft: Altlehrwerke 27./28.09.2026, drei
Auswertungen ohne Einbindung, daraus eine neue Blattart statt
besserer Sprossen. Reife: Kandidat.

**Vor jedem Neuentwurf das ursprüngliche Ziel lesen.** Wer eine
neue Einteilung, Blattart oder Struktur vorschlägt, prüft sie
zuerst gegen die Zieldatei des Projekts und nennt den Satz, den
sie ändert. Herkunft: 28.09.2026, Dialog nach der Lage des
Schülers widersprach „ein Blatt für alle“. Reife: Kandidat.

**Geplante Aufgaben statt Web-Sitzungen, wenn Internet nötig
ist.** Aus dem Chat angelegte geplante Aufgaben haben freies
Internet und pushen selbst; Web-Sitzungen haben nur GitHub und
Paketquellen. Herkunft: Fremd- und Altlehrwerkläufe 27.09.2026
scheiterten im Web an der Netzsperre, liefen als geplante
Aufgaben durch. Reife: erprobt in verbessereBlaetter.

## Kandidaten 2026-09-28b (Projekt verbessereBlaetter, Umzug abends)

**Einbindungsfunde nach Zieldatei sortieren.** Wer Befunde aus
Quellen einbindet, teilt sie nicht nach Sichtweise (Sprossen,
Dichte, Schwerpunkte), sondern nach der Datei, in der der Fund
landet (Katalog, Bankregeln, Sprachregeln, Layout, Zieldatei/
Prompt); jeder Fund hat genau einen Ort, und die Umsetzung ist
je Datei ein Auftrag. Herkunft: Einbindungslauf 28.09.2026 – die
fünf Sichtweisen der Übergabe überlappten (Dichte ist Layout,
Schwerpunkte sind Katalogmarken) und ließen die Aufgabenformen
aus. Reife: Kandidat.

**Abrechnung ist Messwert, nicht Anweisung.** Welche Sitzungsart
wovon zahlt (Abo, Guthaben), steht nicht in einer Anweisung fest,
sondern wird an der Nutzungsanzeige vorher/nachher gemessen, bevor
ein Lauf startet; eine Anweisungszeile dazu trägt Datum und
Messwert. Herkunft: 28.09.2026 – „ohne Guthaben keine geplanten
Aufgaben“ war aus der Anweisung geschlossen; der Commit-Log zeigte
Läufe nach dem Verbrauch des Guthabens. Reife: Kandidat.

**Praxis des Nutzers vor Literatur.** Ein Literaturbefund, der
eine Situation regelt, die es in der Praxis des Nutzers nicht
gibt, bleibt liegen – auch wenn er gut belegt ist. Vor dem
Vorschlag fragen, ob die Situation vorkommt. Herkunft:
28.09.2026 – Klassenarbeit als häufigster Nachhilfe-Anlass
(Literatur) gegen „ich baue nie Blätter für Klassenarbeiten“
(Lehrer); der Fehler wurde zweimal wiederholt. Reife: Kandidat.

**Erst die Änderungsliste, dann die Datei.** Wird eine lange
Regeldatei neu geschrieben, bekommt sie einen Abschnitt
„Änderungen gegenüber <Datum>“ mit alt → neu je Punkt; der Nutzer
liest nur diesen. Herkunft: ziel.md 28.09.2026 (§ 6). Reife:
Kandidat.

## Kandidaten 2026-09-28c (Projekt verbessereBlaetter, abends)

**Aufträge ohne Rechner laufen als Unteragent aus dem Chat.** Wo
der Chat Shell, Klon und Schreibzugriff hat und der Auftrag nur
Repo, Sprache und Paketquellen braucht, startet Claude den Auftrag
selbst als Unteragenten (Modell nach der Modellregel des Projekts),
statt ihn als Datei an den Nutzer zum Einfügen in Claude Code zu
geben; der Auftragstext bleibt derselbe (Ausgangslage, Schritte,
Prüfungen, Bericht, Regeln), nur an die Shell des Agenten
angepasst, und der Agent committet und pusht selbst. Der Nutzer
wird vorher in einem Satz informiert (Auftrag, geschätzte Größe),
nachher nach der Nutzungsanzeige gefragt. Voraussetzung: Chat und
Code-Tab zahlen vom selben Kontingent (Messwert, nicht Annahme).
Der Handweg über den Code-Tab bleibt für alles, was den Rechner
braucht, oder wenn der Nutzer zusehen will. Grund: Der Nutzer will
so wenig wie möglich tippen; ein Auftrag als Datei kostet ihn
Kopieren, /clear, Einfügen, Push und die Meldung zurück. Herkunft:
verbessereBlaetter(), 28.09.2026 23:31, Auftrag Katalog-Nachzug.
Reife: Kandidat.

## Kandidaten 2026-09-30 (Projekt verbessereBlaetter, Umzug nachts)

**Hinweise im Auftragskopf nur aus der Quelle des Agenten.** Was
Claude einem Agenten als Hinweis voranstellt (Zählungen, Nummern,
„Einheit 1 hat zwei Vorstufen“), muss aus der Datei stammen, die
der Agent selbst liest, nicht aus einer eigenen Zählung des Chats
oder einer älteren Fassung; im Zweifel nennt der Hinweis nur die
Stelle („siehe Mappe, Kette Einheit 1“). Grund: Der Hinweis zu
ebenen war falsch, weil der Chat aus einer Zählung vom Morgen
zitierte; der Agent hat richtig die Mappe genommen, ein schwächerer
hätte dem Hinweis geglaubt. Herkunft: verbessereBlaetter(),
29.09.2026 Schub 4. Reife: Kandidat.

**Parallele Agenten je in einem eigenen Klon.** Laufen mehrere
Agenten im selben Repo, bekommt jeder einen eigenen Klon
(Arbeitsverzeichnis je Agent), schreibt nur in seinen Ordner, legt
Zwischendateien nur im eigenen Klon ab (nie im Scratchpad, der ist
geteilt) und zieht vor jedem Push mit `git pull --rebase`; bei
HTTP 429 zehn Sekunden warten, genau ein zweiter Versuch, sonst
nach dem nächsten Teil erneut pushen. Messwert 29.09.: sieben
Agenten parallel ohne Push-Konflikt. Grund: Ein Agent fand eine
fremde Datei im geteilten Scratchpad und musste sie vor jedem
Commit löschen. Herkunft: verbessereBlaetter(), 29.09.2026
Schub 3. Reife: Kandidat.

**Musterlösungen alter Lehrwerke sind eine Quelle für Vorstufen.**
Beim Auswerten eines Lehrwerks werden nicht nur die Aufgaben-
päckchen gelesen, sondern die vorgerechneten Beispiele Zeile für
Zeile; jede Zeile ist ein Handgriff, und für jeden gelten vier
Fragen: Ist er schon Sprosse oder Voraussetzung? Lässt er sich als
Aufgabe mit eigenem Antwortgerüst stellen? Hat er ein eigenes
Fehlerbild? Stürzt der schwache Schüler dort, nicht erst am
Ergebnis? Nur bei viermal ja wird er Vorstufe; der Lehrer bestätigt
jede einzeln. Grund: Aus 61 Schreibform-Notizen der DDR-Bücher kamen
sieben Katalogänderungen, alle an Sturzstellen, die der Katalog
selbst als Falle nennt; Aufgabenpäckchen allein zeigen diese
Schritte nicht. Herkunft: verbessereBlaetter(), 29.09.2026 früh
(terme Ausklammern, Zerlegen vor „Faktor vorgegeben“). Reife:
Kandidat.

**Kontingent in Messwerten je Lauf.** Vor und nach jedem
Agentenschub liest der Nutzer die Nutzungsanzeige ab; Claude
rechnet Token je Schub in Prozent der Woche um und plant den
nächsten Schub danach, nie nach der Hochrechnung der Anzeige.
Messwerte 29.09.: rund 1–1,5 % der Woche je Bank-Eintrag, 3,5–5 %
je Million Token (Max 20x). Herkunft: verbessereBlaetter(),
29.09.2026, vier Schübe. Reife: Kandidat.

## Kandidaten 2026-09-30b (Projekt verbessereBlaetter, mittags)

**Befunde und Vorschläge in Alltagssprache.** Was ein Prüflauf,
ein Agent oder eine Vorschlagsdatei gefunden hat, sagt Claude im
Chat so, wie man es einem Kollegen am Tisch erklärt: was der
Schüler auf dem Blatt anders üben würde und warum. Nummern von
Vorschlägen, Kennungen, Zeilennummern, Dateinamen und Werkzeugnamen
bleiben in der Datei; im Chat stehen sie höchstens in Klammern,
wenn der Lehrer nachschlagen will. Kürzel und Fachwörter des Repos
(Sprosse, Vorstufe, Erkennungsschritt, Mappe, Pflichtform) werden
beim ersten Mal in einem Halbsatz erklärt. Grund: Die Zusammen-
fassung der Katalogvorschläge vom 30.09. war eine Liste aus Nummern
und ids; der Lehrer konnte nicht entscheiden, ohne die Datei zu
lesen – dann hätte der Chat nichts geleistet. Herkunft:
verbessereBlaetter(), 30.09.2026. Reife: Kandidat, vom Lehrer
gewünscht.

**Revisionen als eigene Entscheidung vorlegen.** Stößt Claude auf
eine frühere Festlegung, die es für nicht mehr optimal hält, sagt
es das als eigenen Punkt mit zwei Optionen und der Folge jeder
Option – nicht als Nebensatz („wenn du das kippen willst“). Der
Lehrer entscheidet; eine Festlegung ist nicht deshalb richtig, weil
sie beschlossen ist. Grund: Die Frage, ob die dritte binomische
Formel Vorrat bleibt, stand am 30.09. als Halbsatz am Ende einer
Antwort; der Lehrer musste sie selbst herausziehen. Herkunft:
verbessereBlaetter(), 30.09.2026. Reife: Kandidat, vom Lehrer
gewünscht.

## Kandidaten 2026-10-01 (Projekt verbessereBlaetter, Umzug abends)

**Knöpfe, die Claude drücken kann, drückt Claude.** Merge, Fetch,
Push, Ordnerfreigabe anstoßen, Patch einspielen: Was eine Sitzung
selbst ausführen kann, tut sie; der Lehrer bekommt nur die
Handgriffe, die keine Sitzung ausführen kann (Push ohne Anmeldung,
Dialog bestätigen). Grund: Jeder Handgriff kostet den Lehrer
Aufmerksamkeit und den Chat eine Runde. Herkunft:
verbessereBlaetter(), 01.10.2026. Reife: Kandidat, vom Lehrer
gewünscht.

**Erst Exemplar, dann Regel – auch für Layout.** Vor jeder
Regelrunde am Skript steht ein von Hand gesetztes Musterblatt, das
der Lehrer beurteilt; jedes Blatt wird ganz angesehen, bevor es der
Lehrer bekommt. Grund: Vier Regelrunden am Skript ohne Muster
brachten im Urteil des Lehrers keinen Fortschritt; das Muster von
Hand brachte ihn in einem Tag. Herkunft: verbessereBlaetter(),
30.09.–01.10.2026. Reife: Kandidat.

**Fortgesetzte Agenten statt neue.** Ein Agent, der die Dateien
schon gelesen hat, bekommt den Folgeauftrag per Nachricht; ein neuer
Agent liest alles noch einmal. Messwert 01.10.: Muster 2 und 3 je
unter 0,1 Mio Token als Fortsetzung, Muster 4 als neuer Agent
0,14 Mio. Herkunft: verbessereBlaetter(), 01.10.2026. Reife:
Kandidat.

**Schreibrecht beim Sitzungsstart.** Eine Sitzung hat Schreibrecht
auf ein Repo nur, wenn das Repo beim Start gewählt wurde;
nachträgliches Anhängen lehnt die Freigabeprüfung ab, auch wenn
GitHub das Repo für Claude freigegeben hat. Chats, deren Agenten
pushen sollen, werden mit Repo gestartet; der erste Handgriff ist
ein Ein-Zeilen-Commit als Messwert. Grund: Am 01.10. lief ein
Katalogauftrag ohne Push durch, und der Commit musste als Patch
über den Rechner des Lehrers. Herkunft: verbessereBlaetter(),
01.10.2026. Reife: Kandidat.

**Patch-Weg über den Rechner.** Kann eine Sitzung nicht pushen,
legt der Agent seinen Commit als Patch ab; Claude lässt sich den
Ordner auf dem Rechner per Dialog freigeben (nicht über das
„+“-Menü), holt das Löschrecht für git, spielt den Patch mit
`git am` ein und der Lehrer drückt Push. Grund: So bleibt der
Commit des Agenten erhalten (Urheber, Nachricht), und der Lehrer
tippt nichts. Herkunft: verbessereBlaetter(), 01.10.2026. Reife:
Kandidat.

**Zukauf ist API-Preis.** Zugekaufte Nutzung wird zu
Standard-API-Preisen abgerechnet, vorausbezahlt und getrennt vom
Abo (support.claude.com, Artikel 12429409); je Token ist sie ein
Vielfaches des Abo-Satzes (Abo nach Messwert rund 20–29 Mio Token
je Woche). Zukauf nur als Reserve bis zum Reset, nie als Plan.
Herkunft: verbessereBlaetter(), 01.10.2026. Reife: Kandidat.

## Kandidaten 2026-10-01c (Projekt verbessereBlaetter, Umzug spät)

**Rechte vor Arbeit.** Was ein Chat am Ende speichern soll, hängt
er als ersten Schritt an (Repo, Ordner, Dienst), damit die
Erlaubniskarte in der ersten Minute kommt und nicht nach neun
Minuten Arbeit. Berechtigungsmodus „Manuell“ für den Schritt, in
dem Rechte vergeben werden; danach darf „Auto“ zurück. Grund: Auf
„Auto“ lehnt der Filter jede Rechtevergabe ab, und ein Chat, der am
Ende nicht speichern kann, hat umsonst gearbeitet (01.10.). Herkunft:
verbessereBlaetter(), 01.10.2026. Reife: Kandidat, gemessen.

**Befund wird Änderung, nicht Posten.** Ein Befund aus einem
Exemplar (Blatt, Lauf, Test) wird im selben Chat zu einer Änderung
oder zu einer Entscheidung, die der Nutzer trifft; in die Liste der
fälligen Posten kommt nur, was einen äußeren Auslöser hat (Termin,
Datei beim Nutzer). Grund: Die Postenliste wuchs auf 71 KB, und
der Nutzer sagte, Aufgaben würden nach hinten geschoben und
vergessen. Herkunft: verbessereBlaetter(), 01.10.2026. Reife:
Kandidat, vom Nutzer gewünscht.

**Vollständigkeit vor Füllen.** Bevor eine Sammlung (Bank, Katalog,
Datenbestand) einen Bereich füllt, wird der Bereich gegen alle
Quellen auf Vollständigkeit und Reihenfolge geprüft und vom Nutzer
bestätigt. Grund: Was einmal gefüllt ist, zieht nach (Kennungen,
Verweise); eine Lücke danach kostet einen Nachzug. Herkunft:
verbessereBlaetter(), 01.10.2026 (Division von Termen fehlte, obwohl
die Bank Terme zweimal gefüllt war). Reife: Kandidat.

## Kandidaten 2026-10-03 (Projekt verbessereBlaetter, Umzug)

**Nummern statt Namen.** Personen (Schüler, Kunden) bekommen in
einer privaten Datei eine feste Nummer; alles, was in ein
öffentliches Repo oder einen Dateinamen geht, trägt nur die
Nummer. Der Chat schreibt dann selbst mit, statt dem Nutzer Zeilen
zum Abtippen zu geben. Grund: Der Nutzer will Namen nennen, und
ein Protokoll mit Namen im öffentlichen Repo wäre ein Leck
(03.10.). Herkunft: verbessereBlaetter(), 03.10.2026. Reife:
Kandidat, vom Nutzer gewünscht.

**Erst das Kleinste, das trägt.** Bei einer neuen Datenfrage zuerst
die Lösung ohne Handgriff des Nutzers suchen; Zeilen, die er
kopieren soll, sind der Rückfall. Grund: Vorschlag „Zeile zum
Anhängen“ wurde als übers Ziel hinaus zurückgewiesen (03.10.).
Herkunft: verbessereBlaetter(), 03.10.2026. Reife: Kandidat.

## Kandidaten 2026-10-03b (Projekt verbessereBlaetter, Umzug mittags)

**Kontingent ist Sache des Nutzers.** Der Chat nennt Messwerte und
Schätzungen zum Verbrauch und wartet auf das Go; er hält keinen
Lauf zurück und vertagt nichts von sich aus mit der Begründung
„Kontingent". Grund: Der Nutzer hat ein Max-Abo und wies das
Zurückhalten zweimal als Bevormundung zurück (03.10.). Herkunft:
verbessereBlaetter(), 03.10.2026. Reife: Kandidat, vom Nutzer
gewünscht.

**Einmal lesen, alles ableiten.** Ein Lauf, der Quellen liest,
leitet in einem Durchgang alles ab, was aus derselben Quelle folgt
(Daten, Ablage, Prüfung); Leser werden nicht je Teilaufgabe neu
gestartet. Mehrere Teile laufen als ein Agent mit Standdatei und
Commit je Teil, nicht als mehrere Agenten mit je eigenem Anlauf.
Grund: Der Anlauf (Auftrag lesen, Repo sichten) ist der doppelte
Anteil; die Probe eines Hefts kostete 0,2 Mio, die Erfassung
allein 0,08 Mio (03.10.). Herkunft: verbessereBlaetter(),
03.10.2026. Reife: Kandidat.

**Urteil des Nutzers als Datei.** Was nur der Nutzer beurteilen kann
(was Schüler schwer finden, was wichtig ist), kommt als Entwurf in
eine kleine Datei je Einheit (Typ, Stufe, Grund), die er korrigiert;
das Skript liest sie. Nicht aus Ersatzgrößen ableiten (Länge,
Form, Häufigkeit). Grund: „leicht" aus Höhe und Häufigkeit scheiterte
zweimal, der Entwurf des Chats wurde „grob passend" angenommen
(03.10.). Herkunft: verbessereBlaetter(), 03.10.2026. Reife:
Kandidat.

**Lies den Vorgängerchat, bevor du vergleichst.** Hat der Nutzer in
einem früheren Chat Festlegungen getroffen, liest der Chat sie
dort nach (Suche über die Chats), statt den Nutzer sie erzählen zu
lassen. Grund: Der Nutzer musste Beschlüsse aus „Start 6"
wiederholen (03.10.). Herkunft: verbessereBlaetter(), 03.10.2026.
Reife: Kandidat, vom Nutzer gewünscht.

**Offene Punkte rechts, nicht im Verlauf.** Die Liste der offenen
Punkte führt der Chat als kleine HTML-Seite im Repo und schickt sie
mit SendUserFile (display „render“), damit sie rechts neben dem
Chat steht; bei jeder Änderung neu schicken. Ein neuer Chat zeigt
sie als ersten Handgriff. Grund: Scrollen im Verlauf lehnt der
Nutzer ab, die Aufgabenliste (TaskCreate) erscheint bei ihm nicht
(03.10.). Herkunft: verbessereBlaetter(), 03.10.2026. Reife:
Kandidat, vom Nutzer gewünscht.

## Kandidaten 2026-10-03d (Projekt verbessereBlaetter, Umzug abends)

**Keine Option ohne Informationsgewinn.** Eine Wahlmöglichkeit wird
nur angeboten, wenn sich die Optionen im Ergebnis unterscheiden; eine
Variante, die dasselbe sagt (zwei Namen für denselben Knopf), wird
entschieden, nicht vorgelegt. Grund: Der Nutzer wies eine solche
Doppeloption als sinnlos zurück (03.10.). Herkunft:
verbessereBlaetter(), 03.10.2026. Reife: Kandidat, vom Nutzer
gewünscht.

**Eine Stufe festzurren, dann die nächste.** Bei Entwürfen mit
Ebenen (Entscheidungsbaum, Gliederung) wird je Nachricht nur eine
Ebene besprochen und bestätigt; Folgeebenen erst danach, und eine
Ebene, die sich später beißt, wird bewusst neu aufgemacht. Der
aktuelle Stand steht als Bild rechts (Baum in der Seite der offenen
Punkte), nicht als Liste im Verlauf. Grund: Vorgreifen und Mischen
zweier Ebenen führte mehrfach zu Rückfragen und Ärger (03.10.).
Herkunft: verbessereBlaetter(), 03.10.2026. Reife: Kandidat, vom
Nutzer gewünscht.

**Gleicher Ablauf ist ein Wert.** In einer Bedienung bekommen
gleichartige Wege dieselben Stufen und Knöpfe; Abweichungen nur mit
Grund. Grund: Der Nutzer will die Knöpfe einmal lernen (03.10.).
Herkunft: verbessereBlaetter(), 03.10.2026. Reife: Kandidat.

## Kandidaten 2026-10-04 (Projekt verbessereBlaetter, Umzug)

**Einmal fragen, dann eintragen.** Angaben, die der Nutzer immer wieder
liefern müsste (Personen, Orte, Einstellungen), legt der Chat in einer
Datei ab; fehlt eine, fragt er einmal und trägt die Antwort sofort ein,
damit nie wieder gefragt wird. Was für eine Gruppe gilt (alle Schüler
einer Schule), steht einmal bei der Gruppe. Grund: Der Nutzer will
nicht immer dasselbe gefragt werden (04.10.). Herkunft:
verbessereBlaetter(), 04.10.2026. Reife: Kandidat, vom Nutzer gewünscht.

**Große Läufe in Blöcken mit Sparprüfung.** Ein großer Lauf liest jede
Quelle einmal, stimmt alle Schritte aufeinander ab, läuft in Blöcken,
und nach jedem Block wird geprüft, ob der nächste sparsamer geht –
Qualität geht vor. Grund: Vorgabe des Nutzers für den Vorratslauf
(04.10.). Herkunft: verbessereBlaetter(), 04.10.2026. Reife: Kandidat,
vom Nutzer gewünscht.

**Vereinheitlichen nach Stufe, nicht nach Gegenstand.** Wer mehrere
gleich gebaute Dinge angleicht (Bäume je Prüfung), geht Stufe für Stufe
mit einer Vergleichstabelle durch, nicht Ding für Ding; so stehen
Abweichungen nebeneinander und werden entschieden. Grund: Der Durchgang
P10 | Abitur | FHR fand so in kurzer Zeit die Widersprüche (04.10.).
Herkunft: verbessereBlaetter(), 04.10.2026. Reife: Kandidat.

## Kandidaten 2026-10-05 (Projekt verbessereBlaetter, Umzug früh)

**Nächsten Schritt aus der Übergabe prüfen, nicht übernehmen.** Der
neue Chat beginnt mit dem genannten Schritt, sagt aber vorher in zwei
Sätzen, warum dieser Schritt jetzt und nicht ein anderer – wer ihn
braucht, was ohne ihn stockt. Trägt die Begründung nicht, legt er den
besseren Schritt vor. Grund: Der Abitur-Zuschnitt stand als nächster
Schritt, obwohl vier Schüler P10 schreiben und einer Abitur (04.10.).
Herkunft: verbessereBlaetter(), 04.10.2026. Reife: Kandidat, vom
Nutzer eingefordert.

**Nur das Gefragte in der Antwort.** Fragt der Nutzer nach einem Teil
(Lösungen), enthält die Antwort nur diesen Teil – keine Tabelle mit
Spalten, die er nicht gefragt hat, kein Nebenvorschlag. Was der Nutzer
zum Fokussieren braucht, ist eine fokussierte Antwort. Grund: Eine
Tabelle mit Aufgaben-, Lösungs- und Sonst-Spalte auf die Frage nach
Lösungen (04.10.). Herkunft: verbessereBlaetter(), 04.10.2026. Reife:
Kandidat, vom Nutzer eingefordert.

**Ein Bild vor dem Senden ansehen.** Wer eine Seite oder Grafik baut,
die der Nutzer ansehen soll, rendert sie vorher selbst (Playwright,
Screenshot) und prüft Lage und Lesbarkeit; „müsste passen“ reicht
nicht. Grund: Baum sollte oben rechts stehen und stand unter dem
Text; erst der Screenshot zeigte es (04.10.). Herkunft:
verbessereBlaetter(), 04.10.2026. Reife: Kandidat.

**Ein Hauptplatz, Nebenplatz nur als eigene Stufe.** Ordnet man Dinge
in Abschnitte, hat jedes genau einen Hauptplatz (dort wird gezählt) und
höchstens dort einen Nebenplatz, wo es eine eigene Stufe bildet; am
Nebenplatz steht „kennst du aus …“. Grund: Doppelte Einordnung ohne
diese Regel verfälscht Zählungen und bläht auf (04.10.). Herkunft:
verbessereBlaetter(), 04.10.2026. Reife: Kandidat, projektnah.

**Fable zahlt die Woche mit.** Fable-Arbeit zählt auf das Fable- und
das Wochenkontingent; bindend ist, was zuerst voll ist, meist die
Woche. Messwerte: 209 000 Token → Woche +1, Fable +2; 556 000 Token →
Woche +3, Fable +4 (≈ 185 000 Token je Wochenpunkt). Grund: Der Nutzer
wollte „Fable aufbrauchen“ und hielt die 11 % für zusätzlich (04.10.).
Herkunft: verbessereBlaetter(), 04./05.10.2026. Reife: Messwert.

## Kandidaten 2026-10-06 (Projekt verbessereBlaetter, Umzug)

**Revisionsschranke.** Ein gefasster Beschluss wird nur neu
aufgemacht, wenn ein Ergebnis (Blatt, Messwert, Befund) dagegen
spricht – nicht, weil im Gespräch ein neuer Gedanke auftaucht. Einfälle
kommen auf die Liste offener Punkte und werden am nächsten Ergebnis
geprüft. Grund: Am 05.10. wurde „schwach“ viermal umgebaut, der Nutzer
fühlte sich unwohl („wir revidieren, was fest war“). Herkunft:
verbessereBlaetter(), 05.10.2026. Reife: Kandidat, vom Nutzer angestoßen.

**Zeigen statt beschreiben.** Soll der Nutzer etwas beurteilen, das er
nicht vor sich hat (Seite, Ausschnitt, Variante), wird es gerendert und
rechts gezeigt; auf eine Stelle, die nicht sichtbar ist, wird nicht
nur verwiesen. Zwei Varianten nebeneinander statt in Worten. Grund:
Urteile kamen erst, als die Seiten rechts standen; Kosten fast null.
Herkunft: verbessereBlaetter(), 05./06.10.2026. Reife: Kandidat, vom
Nutzer gewünscht.

**Ein Begriff, eine Bedeutung.** Bezeichnet ein Wort zwei Dinge (hier
„Skript“ = Heftart und = Bauanleitung), wird das beim ersten Anzeichen
von Missverständnis aufgelöst und umbenannt. Grund: Der Nutzer
verstand einen Plan nicht, weil „Skript“ doppelt belegt war (05.10.).
Herkunft: verbessereBlaetter(), 05.10.2026. Reife: Kandidat.

**Vorschlag als Frage, nicht als Schlussstrich.** Empfehlungen und
Pausen werden angeboten, nicht verordnet; der Nutzer entscheidet über
Tempo und Ende. Grund: „sei nicht immer so im Ton bevormundend“
(05.10.). Herkunft: verbessereBlaetter(), 05.10.2026. Reife: Kandidat,
vom Nutzer eingefordert.

**Opus-Agenten schonen die Woche.** Messwerte 05.10.: Opus/Sonnet-
Agenten ≈ 0,5 Mio Token je Wochenpunkt, Fable-Agenten ≈ 185 000. Große
Läufe mit Opus, Fable nur auf Wunsch. Herkunft: verbessereBlaetter(),
05.10.2026. Reife: Messwert (zwei Läufe, Anzeige in ganzen Prozent).

## Kandidaten 2026-10-06b (Projekt verbessereBlaetter, mittags)

**Sparen ungefragt, Qualität vorausgesetzt.** Bei jedem Schritt wählt
der Chat von sich aus den sparsamsten Weg, der die Qualität hält (frischer
Agent statt langer Verlauf, nur die nötigen Stellen lesen, Prüfen ohne
Bilder, wo Text reicht, Mechanik ohne Modell), und nennt in einem Satz,
warum er reicht. Der Nutzer muss nicht danach fragen. Für global.md
vorgeschlagen als Ersatz des Satzes „Einen sparsameren Weg nennst du nur,
wenn er gleich gut ist“ durch: „Den sparsamsten Weg, der gleich gut ist,
wählst du von dir aus und sagst in einem Satz, warum er reicht.“ Grund:
Ein Neubau war als „kleiner Lauf“ mit 0,2–0,4 Mio Token angekündigt; erst
auf Nachfrage kam der Weg mit 0,17 Mio (06.10.). Herkunft:
verbessereBlaetter(), 06.10.2026. Reife: übernommen in global.md (Stand
2026-10-06).

## Kandidaten 2026-10-06c (Projekt verbessereBlaetter, Umzug)

**Erst die Sicht, dann das Ergebnis.** Bevor Aufgaben, Texte oder Listen
erzeugt werden, steht die Sicht als kurze Liste fest (wer liest es, was
muss er verstanden haben, welche Vielfalt, welche echte Sprache); erzeugt
und geprüft wird gegen diese Liste. Ohne sie nimmt das Modell die Sicht
der Daten und liefert das Durchschnittliche. Grund: Verständnisfragen
(„Was ist das Ganze?“) kamen erst auf Nachfrage; Varianten waren Kopien mit
anderer Zahl (06.10.). Herkunft: verbessereBlaetter(), 06.10.2026. Reife:
Kandidat, vom Nutzer angestoßen.

**Vorhandenes Wissen anschließen, bevor man es neu erfindet.** Vor einem
neuen Baustein prüfen, ob das Wissen schon in einer Datei steht, die die
Werkzeugkette nicht liest. Grund: Erkennungsschritte, typische Fehler und
Leiter standen seit September im Katalog; das Bauprogramm las ihn nicht
(06.10.). Herkunft: verbessereBlaetter(), 06.10.2026. Reife: Kandidat.

**Echte Sammlungen vor eigener Erfindung.** Wo Vielfalt gebraucht wird
(Aufgaben, Formulierungen, Beispiele), zuerst einen echten Korpus
erschließen; eigene Erfindung nur für Lücken und nach einem Raster mit
Merkmalen, die sich unterscheiden müssen. Grund: 1 502 echte Aufgaben
anderer Länder ersetzten Kopien; Hefte wurden kürzer und vielfältiger
(06.10.). Herkunft: verbessereBlaetter(), 06.10.2026. Reife: Kandidat.

**Beurteilen am Ergebnis, nicht an der Liste.** Soll der Nutzer eine
Vorgabe (Steckbrief, Regel) beurteilen, deren Wirkung er nicht sieht,
wird zuerst ein Ergebnis daraus gebaut und gezeigt. Grund: „ich sehe die
Auswirkungen auf ein Blatt nicht“ (06.10.). Herkunft:
verbessereBlaetter(), 06.10.2026. Reife: Kandidat, vom Nutzer angestoßen.

## Kandidaten 2026-10-07 (Projekt verbessereBlaetter)

**Sparsam und trotzdem bequem zeigen.** Wer dem Nutzer etwas zum
Beurteilen zeigt, zeigt einen Ausschnitt als Bild in der Seitenleiste
(rechts), klein aufgelöst, genau die Stelle, um die es geht – nicht die
ganze Seite und nicht im Chatverlauf zum Scrollen. Das Modell sieht sich
Seiten nur an, wenn es selbst etwas daran beurteilen muss. Grund: Scrollen stört
den Nutzer; Bilder kosten Kontext. (Messwert 07.10.: rund 20 Chatnachrichten
mit Bildern ließen die Woche bei 25 %, ein Agentenlauf mit 0,40 Mio Token
hob sie von 19 auf 25 % – Haupttreiber sind Agentenläufe.) Herkunft:
verbessereBlaetter(), 07.10.2026. Reife: Kandidat, vom Nutzer angestoßen,
möglicherweise global.

**Agentenläufe klein schneiden.** Der Verbrauch hängt vor allem an
Agentenläufen (Zahl der Werkzeugaufrufe, Lesen), nicht an Chatnachrichten.
Läufe auf das Nötige begrenzen, Lesen im Agenten eng führen. Herkunft:
verbessereBlaetter(), 07.10.2026 (Messwert). Reife: Kandidat.

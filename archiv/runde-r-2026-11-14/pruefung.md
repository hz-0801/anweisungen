# Prüfung (R) – alt gegen neu, blind

Prüfer: Opus, hat die Neufassung nicht geschrieben. Teil 1 vor dem Lesen von `neu/zuordnung.md`.
Grundlage: Wortdiff alt/neu (beide Dateien), `neu/auslagerung.md`, Register 14.11.15, dazu zur Gegenprobe
plan.md Register 14.11.9/14.11.12/14.11.14/09.11.2 und anweisungen `modelle.md` § 3, `wege.md` (Kopf).
`pruefe.py` meldet: 26 681 → 25 393 Zeichen (−4,8 %), **1 FEHLER** (N1, siehe M3).

## Teil 1 – Testfälle

| Nr | Fall | alt | neu | Urteil |
|---|---|---|---|---|
| 1 | „Ableitung von x²?“ | Haltung zurück, wenige Sätze: „2x“. | Global gleich. Projekt neu: „Aufbau **jeder** Nachricht: Antwort; Entscheidung; „Bei dir:“; Hintergrundzeile“ – lädt dazu ein, auch an „2x“ ein leeres „Bei dir:“ oder eine Hintergrundzeile zu hängen. | gleich, leichtes Risiko neu schlechter (K1/S1) |
| 2 | 40 Blätter, keine Schätzung | Go nötig; Vorschlag mit Mittel, Aufwand, Schätzung, Wanduhr, Rückkehrzeit, Gelingen/Scheitern; Pilot vor Breite; Faustwerte; Nutzungsanzeige. | Dasselbe, dazu Kostenregel: Auftrag ≥ 3 Punkte → mindestens ein Sparweg mit Kosten; „höchstens eine Entscheidung“ hält den Vorschlag knapp. | neu besser (gewollt) |
| 3 | „Umzug“ | Arbeitsdatei auf Stand (übernehmen, nichts Verworfenes, Widersprüche prüfen) → Projektschritte (Wirkort, Skript Entscheidungsmarken, Liste zeigen, `uebergabe.md` neu mit Verweis auf „Jetzt“, alte datiert nach `archiv/`, Jetzt/Offen kürzen) → Übergabe 6 Punkte mit Inhaltsangaben → stille Prüfung → ablegen, committen, ein Satz → Ende: „Holger:“ (Projekt) + Startwort-Block. | Gleiche Reihenfolge, aber Inhaltsangaben, stille Prüfung und Projektschritte im Wortlaut nur noch in `wege.md` § Umzug – der dort noch **nicht** steht (Auslagerung „nicht eingespielt“). Ohne Einspielen: „nicht lesbar, sag es“, Übergabe nur nach sechs Überschriften. Projekttext „Schritte aus wege.md …, dazu: …“ liest sich, als kämen die Kurzschritte zusätzlich. Ende der Nachricht kollidiert mit Weg A („zuletzt der Hintergrund“). | gleich **nur** nach Einspielen; sonst neu schlechter (M2, S4, S1, K5) |
| 4 | Langer Chat, Phase fertig, langer Lauf | Angebot einmal, Uhrzeit MEZ, Grund, „Holger:“ + Startwort-Block, Übergabe gleich angelegt; Wiederholung nur bei gravierenden Folgen, dann mit Grund, neue Läufe erst nach Umzug; Beispiel „Nachtrunde nach Umzug“ in Mitdenken. | Gleich (Kontextdisziplin trägt „langer Lauf“; Beispiel fehlt, Verhalten nicht). Für die Übergabe muss `wege.md` gelesen werden. | gleich |
| 5 | Datei ins Repo kopieren | Erst „Selbst machen“ (Chat hat Schreibzugang, committet selbst); sonst „Holger:“ + App/Reiter/Projekt/Repo/Datei, Link, Block darunter, bei mehreren Handgriffen Übersicht. | Wortgleich bis auf Füllwörter. | gleich |
| 6 | Neuer Chat, „weiter, Repos anhängen“ | Repos anhängen/klonen → global (1) Stand-Zeilen vergleichen (liest beide Dateien) → (2) einfache Erklärung → plan.md-Abschnitte, Übergabe Kopf/Arbeitsstand, `git log`-Satz, ≤ 5 Zeilen, > 2 Tage ansprechen, `kandidaten.md`, `modelle.md` § 6. | Wortgleich. Neue Stand-Zeilen (f)/(b) lösen beim ersten Start den Kopierhinweis aus, bis die Einstellung ersetzt ist. | gleich |
| 7 | Falsche Auskunft bemerkt | Ein Satz Korrektur, weiterarbeiten, Herleitung nur auf Nachfrage. | Gleich. | gleich |
| 8 | Fremde Frage während zwei Agenten laufen | Sofort antworten, Agenten laufen weiter; Meldung erst am Rundenende. | Gleich, dazu Weg A: Antwort zuerst, Laufstand höchstens als eine Hintergrundzeile. | neu besser (gewollt) |
| 9 | Festlegung suboptimal | Ungefragt sagen, Revision vorlegen, „statt sie stehenzulassen, **weil sie beschlossen ist**“; Lehrer entscheidet. | Gleich, Begründungsklausel fehlt (sie benennt genau die Neigung, die die Regel bricht). | gleich, minimal schwächer (K2) |
| 10 | Kommentiertes PDF als Zip | Skript liest Kommentare mit Stelle, wörtlich ablegen; Projekt: Sammeln in `bau/befunde-M<n>.md`. | Wortgleich. | gleich |
| 11 | „selbstständig bis Montag“ | Vorrats-/Nachbesserungsrunden im Rahmen von plan.md ohne Go je Runde; Satz vorher, Messwert danach; nie neue Formen, Unumkehrbares, Anweisungen; ausdrücklich Vorrang vor „Teure Aktionen“. | Vorrangsatz gestrichen, aber global deckt ihn („außer eine Projektanweisung erteilt eine Freigabe“). Neu unklar: Runde ≥ 3 Punkte „legst du immer mit Sparweg **vor**“ – wartet Claude unter Freigabe auf eine Wahl? | gleich, neue Unschärfe (S3) |
| 12 | Pilot 0,6 P. / Auftrag 5 P. mit Sparweg 0,8 P. | Pilot: Go nötig („Agent erst nach Go“), obwohl Register 14.11.14 Piloten < 1 Punkt ohne Go erlaubt (stand schon alt nicht in der Anweisung). Auftrag: Go, sparsamster gleich guter Weg ohne Schwelle. | Pilot: unverändert Go – widerspricht 14.11.14 weiter. Auftrag: Sparweg mit beiden Kosten vorlegen (0,8 = 16 % zählt). Unklar, ob Claude den Sparweg still nimmt („ab 0,5 ohne Rückfrage“) oder vorlegt („ab 3 immer vorlegen“). | Auftrag neu besser; Pilot in beiden falsch gegen Register (M1, S3) |
| 13 | „die Formel gehört abgesetzt“ | Formkommentar → sammeln in `befunde-M<n>.md`, Formänderung am Rundenende; sofort nur Handwerksfehler. | Wortgleich. | gleich |
| 14 | Aktuelles Gesetz | Recherche vor Antwort; geltende Fassung, amtliche Quellen, Stand nennen, Unsicherheit offen. | Gleich („statt eine plausible als sicher darzustellen“ entfällt, deckt „sag offen“). | gleich |
| 15 | „wäre schön, wenn …“ | Als Richtung mit Grund festhalten, nicht als Regel; ggf. Kandidat für `kandidaten.md`. | Gleich. | gleich |
| 16 | Urteil über einen Schüler | Vorher `lieferungen.csv` lesen (`geliefert.py --zeige`); nachsehen statt fragen; Namen nur in `-privat`. | Wortgleich („Antworte aus dem Bestand“ steht jetzt nur global als „Nachsehen statt erinnern“). | gleich |

Bilanz: 11 gleich, 3 neu besser (2, 8, 12-Auftrag), Fall 3 nur gleich nach Einspielen der Auslagerung; Unschärfen in 1, 3, 11, 12.

## Teil 2 – Vollständigkeit

Stichprobe 15 Zeilen aus `zuordnung.md` gegen alt und neu:

| Kennung | Angabe | stimmt? |
|---|---|---|
| G07 | „Haltung ist ein Grund …“ gekürzt, gedeckt durch G05/G24 | ja |
| G10 | Beispiel Nachtrunde gestrichen, gedeckt durch Kontextdisziplin | ja |
| G19 | „weil sie beschlossen ist“ „begründet nur“ | ja, aber Begründung trägt Verhalten (K2) |
| G34 | „damit nie wieder gefragt wird“ gekürzt | ja |
| G35 | „statt sie als Aussage zu nehmen“ gekürzt | ja |
| G60 | Handy-Form → wege.md Block B | ja; Block B wortgleich (Skriptprüfung), nur Perspektive „der Lehrer“/„mein Kommentar“ gemischt (K6) |
| G75 | Arbeitsdatei-Details → Block A | ja, wortgleich |
| G77 | stille Prüfung → Block A | ja, wortgleich; Folge siehe S4 |
| G86 | Repo-Name bei `modelle.md` gestrichen, steht in „Anweisungs-Repo“ | ja |
| G97 | Nachsatz Recht gekürzt | ja |
| P17 | Zitat 22.10. gestrichen, „Regel in Register 09.11.2“ | teils: 09.11.2 regelt Chatlänge, nicht die Neigung „öfter umziehen“ (K9) |
| P19 | Umzugsangebot → global Kontextdisziplin | ja, global enthält Uhrzeit, Holger-Zeile, Startwort |
| P53 | Vorrang Freigabe gestrichen, doppelt mit global | ja |
| P63 | Fable → `modelle.md` § 3 | ja; § 3 enthält Fable-Beleg **und** Ausnahme Anweisungen (14.11.9) – neu besser |
| N1 | Kostenregel, Anker ⟨Unter 0,5 Punkten Ersparnis wägst du nicht ab⟩ | **nein**: Text wurde nach der Zuordnung geschärft (Werkstatt 39); Anker fehlt in global.md, Sätze zu Wiederholtem/Einmaligem ohne Zeile (M3) |

Eigene Suche (Wortdiff alt → neu, jeder gestrichene Satzteil einzeln): Alle Streichungen sind Belege, Zweckklauseln oder Doppelungen, außer
„weil sie beschlossen ist“ (K2), „zwinge dich und mich öfter zum Umzug“ (K9) und dem Umzugswortlaut, der nur mit eingespielter Auslagerung wirkt (M2).
Keine Regel fehlt in neu **und** Auslagerung. Eine Lehrer-Entscheidung fehlt in alt **und** neu: Register 14.11.14 (M1).

## Teil 3 – Befunde

### muss

**M1 – Register 14.11.14 fehlt, Text widerspricht ihm.** Stelle: Projekt „Runden“ („Ein Agent startet erst nach meinem Go“) und „Freigabe bis zum Reset“. Der Lehrer hat am 14.11. (Werkstatt 38) beschlossen: Piloten unter einem Wochenpunkt ohne Go, solange Ultra, höchstens 2 Punkte je Woche. Folge: Pilot 0,6 Punkte wartet weiter auf Go (Fall 12); Piloten stauen sich, wenn er fehlt – genau der Anlass des Beschlusses. Der Verfasser hat es als V2 gesehen, aber nicht aufgenommen. Vorschlag, als zweiter Satz in „Freigabe bis zum Reset“:
> Piloten unter einem Wochenpunkt startest du ohne Go, solange ich das Ultra-Abo habe – vorher ein Satz (was, Schätzung), danach der Messwert; höchstens 2 Wochenpunkte je Woche auf diesem Weg.

(Der folgende Satz „Neue Formen, Unumkehrbares und Änderungen an Anweisungen nie ohne mein Go“ deckt die Grenze; „Breite“ dort ergänzen: „Breite, neue Formen, …“.)

**M2 – Auslagerung muss vor den neuen Texten wirken.** Stelle: global „Stichwort Umzug“, „Zeigen“; Projekt „Ein Chat zur Zeit“. Block A/B stehen noch nicht in `wege.md`, dessen Kopf sagt „Nur lesen, wenn … Rechner, Code-Tab …“ und „aus der Projektanweisung verbessereBlätter“. Folge: Setzt der Lehrer die neuen Texte vor dem Einspielen ein, schreibt der nächste Umzug eine Übergabe ohne Inhaltsangaben und ohne Entscheidungsmarken-Skript. Vorschlag: In einem Commit Block A und B einspielen, Kopf von `wege.md` und README nach „Folgeänderungen“ ändern; erst dann bekommt der Lehrer die Texte zum Einsetzen. Kopfsatz:
> Nur lesen, wenn ein Auftrag … braucht oder wenn global.md oder die Projektanweisung hierher verweist (Umzug, Durchsicht am Handy).

**M3 – Kostenregel-Schärfung ohne Zuordnung und Registerzeile.** Stelle: global „Kostenregel“ Satz 2–3; `zuordnung.md` N1; Register 14.11.15. `pruefe.py` meldet 1 Fehler, zwei neue Sätze ohne Zeile; die Schärfung (Lehrer 14.11. Werkstatt 39: Wiederkehrendes über die Woche rechnen, dort auch unter 0,5 Punkten) steht in keiner Registerzeile. Folge: Die Selbstprüfung ist nicht bestanden; ein späterer Chat findet die Regel nicht im Register und hält sie für Abweichung. Vorschlag: N1-Anker auf ⟨Bei einmaligen Aufträgen wägst du unter 0,5 Punkten nicht ab⟩ setzen, Zeile N3 für ⟨Was sich wiederholt … über alle Wiederholungen einer Woche⟩; Register 14.11.15 um einen Satz ergänzen:
> Geschärft Lehrer 14.11. Werkstatt 39: Wiederkehrendes (Anweisungen, Chatstart, Werkzeuge, Skripte im Betrieb) über alle Wiederholungen der Woche rechnen; dort auch unter 0,5 Punkten sparen, wenn ohne Qualitätsverlust.

### sollte

**S1 – Was steht am Ende der Nachricht?** Stelle: Projekt „Antworten“ (Weg A: „zuletzt der Hintergrund“) gegen global „Signalwort“ („Was ich kopieren … steht am Ende jeder Antwort noch einmal“), global „Stichwort Umzug“ („endet mit Holger-Zeile und Startwort“) und Projekt „Erinnern“ (am Ende jedes Schritts bis zu drei Zeilen „Offen“). Folge: Vier Regeln beanspruchen das Ende; der Chat ordnet je Nachricht anders, oder die Hintergrundzeile wird zu vier Zeilen – gegen das Ziel von Weg A. Dazu Fall 1: „jeder Nachricht“ verleitet zu leeren Teilen. Vorschlag (Projekt „Antworten“, Satz 1 ersetzen):
> Aufbau jeder Nachricht: zuerst die Antwort auf meine letzte Nachricht; dann höchstens eine Entscheidung; dann „Bei dir:“ – nur, was dich gerade aufhält, meist eine Frage, höchstens zwei, je mit Empfehlung; dann der Hintergrund als eine Zeile, am Ende eines Schritts dazu die Zeilen aus „Erinnern“; den Bericht nur, wenn ich „Bericht“ schreibe. Darunter steht nur noch, was ich nach global „Signalwort“ kopieren oder öffnen soll (beim Umzug Holger-Zeile und Startwort). Was leer wäre, fällt weg.

**S2 – Kostenregel erlaubt still gekürzte Anweisungen.** Stelle: global „Kostenregel“ („Was sich wiederholt (Anweisungen, …) … nimmst du dort auch unter 0,5 Punkten“). „Nimmst“ heißt ohne Rückfrage; das kollidiert mit Projekt „Änderungen an Anweisungen nie ohne mein Go“ und mit „Iterative Arbeit“/„Betrieb“ (Prompt vollständig an den Lehrer). Folge: Ein Chat könnte Prompts oder Anweisungen eigenmächtig straffen. Vorschlag:
> … eine Ersparnis ohne Qualitätsverlust nimmst du dort auch unter 0,5 Punkten – bei Anweisungen und Prompts als Vorschlag an mich.

**S3 – Schwelle 0,5 „ohne Rückfrage“ gegen Schwelle 3 „immer vorlegen“, und unter Freigabe.** Stelle: global „Kostenregel“ Satz 4–5; Projekt „Freigabe bis zum Reset“. Bei 5 Punkten mit unbemerkbarem Sparweg 0,8 gelten beide Sätze (Fall 12); unter „selbstständig“ heißt „vorlegen“ womöglich warten (Fall 11). Vorschlag (global, Satz 5):
> Aufträge ab etwa 3 Punkten legst du immer mit mindestens einem Sparweg vor, auch wenn du ihn sonst ohne Rückfrage nähmest (…), beide Wege mit Kosten und deiner Empfehlung; gilt eine Freigabe, nennst du beide im Satz vorher und nimmst die Empfehlung.

**S4 – Umzug ohne lesbare `wege.md`.** Stelle: global „Stichwort Umzug“. Global gilt in allen Chats, auch ohne Klon und ohne Abruf von Raw-URLs; dann bleibt nur „sag es“ und sechs nackte Überschriften. Der tragende Qualitätssatz ist einer. Vorschlag: in global nach „6. nächster Arbeitsschritt.“ stehen lassen (≈ 130 Zeichen):
> Prüf vor der Ausgabe still, ob ein neuer Chat allein mit Arbeitsgrundlage und Übergabe sachgerecht weiterarbeiten könnte.

### kann

**K1** – Fall 1 ist mit S1 („Was leer wäre, fällt weg“) erledigt; sonst eigener Halbsatz.

**K2** – global „Verbindliche Entscheidungen“: „statt sie stehenzulassen, weil sie beschlossen ist“ wiederherstellen (3 Wörter). Folge ohne: Die Neigung, Beschlossenes aus Ehrfurcht stehenzulassen, ist nicht mehr benannt.

**K3** – global „Zeigen“: Handy-Form (130 Zeichen) inline lassen; am Handy fehlt oft der Klon, der Verweis kostet fast so viel wie die Regel (dieselbe Begründung, mit der „Kommentiertes PDF“ blieb).

**K4** – global „Antwortaufbau“ („wichtigste Erkenntnis zuerst“) gegen Projekt Weg A („Antwort auf die letzte Nachricht zuerst“): Ist der Laufstand das Wichtigste (Lauf gescheitert), ist die Reihenfolge offen. Vorschlag Projekt: „Scheitert ein Lauf oder musst du handeln, steht das vor der Antwort.“

**K5** – Projekt „Ein Chat zur Zeit“: „Beim Umzug kommen die Schritte aus … dazu:“ → „Beim Umzug gilt zusätzlich `wege.md` § Umzug, Teil verbessereBlätter (kurz: …)“, damit die Kurzschritte nicht als weitere Schritte gelesen werden; „Jetzt“ und „Offen“ kürzen → „Erledigtes aus ‚Jetzt‘ ins Archiv, ‚Offen‘ kürzen“.

**K6** – Block B: „Nur wenn der Lehrer sagt …“ und „mein Kommentar“ in einem Satz; einheitlich „sein Kommentar“ oder „wenn ich sage“.

**K7** – Weg A gilt nur im Projekt, die Kostenregel global. Ob Weg A auch anderen Projekten mit Hintergrundarbeit dienen soll, entscheidet der Lehrer (Register 14.11.15 sagt nichts zum Ort).

**K8** – Zwischenmeldungen „oder ein Lauf scheitert“ geht über Register 14.11.15 („nur, wenn der Lehrer handeln muss“) hinaus; beibehalten ist sicherer, im Register vermerken.

**K9** – Zitat „zwinge dich und mich öfter zum Umzug“ gestrichen; global „Kontextdisziplin“ zieht eher zurück („nicht allein wegen der Zahl der Nachrichten“). Wirkt nur, wenn Umzüge wieder ausbleiben; dann als Satz „Im Zweifel bietest du den Umzug an.“

**Hinweis Kostenrechnung:** `auslagerung.md` „Rechnung“ nennt 1 506 Zeichen netto, `pruefe.py` misst 1 288 (−4,8 %); Ziel 35–45 % weit verfehlt – laut Auftrag kein Muss, aber die Zahl in der Rechnung sollte stimmen.

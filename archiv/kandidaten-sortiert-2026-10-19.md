# kandidaten.md sortiert (Stand 2026-10-19)

Grundlage: anweisungen/kandidaten.md (78 Überschriften: 27 Einzelregeln
ohne Datum, 51 Blöcke „## Kandidaten …“), geprüft gegen global.md
(19.10.), projekt-verbessereBlaetter.md (19.10. c), modelle.md, wege.md;
wo eine Regel schon im Fachrepo steht, ist plan.md / gemeinsam.md /
pruefung.md (mathe-nachhilfe) genannt.

Block = laufende Nummer der Überschrift in kandidaten.md + Kurzzeichen
(Einzelregel: Name; Datumsblock: K MM-TT). Status:
a = steht schon · b = fehlt und lohnt · c = veraltet/überholt (auch:
Fachregel, die ins Fachrepo gehört, oder Einzelbefund ohne zweiten
Beleg) · d = Werkzeug-/Wege-Wissen. Doppelte stehen als „= Zeile n“.
Zählung: 183 Regeln · a 107 · b 35 (= 16 Regeln) · c 33 · d 8.

## 1 Tabelle

| # | Block | Kurzname | Status |
|---|---|---|---|
| 1 | 01 Delegationsform | Auftragsform mit Prüfung und Bericht | a – wege.md „Arbeitsteilung“ (Auftrag, /clear, Holger-Zeile) |
| 2 | 02 Entscheidungen als Daten | Wechselndes in Datei, nicht Prompt | a – projekt „Entscheidungen“ (Eintrag in wirkender Datei), plan.md Linie 2 |
| 3 | 03 Verifikation vor Vertrauen | Werkzeugwechsel gegen Referenz prüfen | a – wege.md „Arbeitsteilung“ (Gegenprobe mit bekannten Werten) |
| 4 | 04 Ein Schritt je Nachricht | Ein Handgriff je Nachricht | a – global „Signalwort“ |
| 5 | 05 Übergabe verweist | Übergabe verweist, wiederholt nicht | a – global „Stichwort Umzug“, projekt „Ein Chat zur Zeit“ |
| 6 | 06 Material am Handgriff | Block direkt unter Holger-Zeile | b – global „Signalwort“ (steht nur in wege.md, das selten gelesen wird) |
| 7 | 07 Aufträge als Datei | Code-Auftrag als .txt-Block | c – Unteragenten statt Einfügen seit 28.09. |
| 8 | 08 Dateien nicht tragen | Dateien per Shell, nie durchs Modell | a – wege.md „Arbeitsteilung“ Schluss, „Ablage“ (base64) |
| 9 | 09 Bereitstellung endet Antwort | Dateikarte erst am Antwortende | d – wege.md (claude.ai-Verhalten) |
| 10 | 10 Werkzeuggrenze je Antwort | ~20 Aufrufe je Antwort planen | d – wege.md; Messwert neu prüfen |
| 11 | 11 Frage als letzte Zeile | „Frage:“ als letzte Zeile | a – projekt „Antworten“, global „Keine Auswahlbuttons“ |
| 12 | 12 Referenzen altern | Referenz gilt nur bei gleichem Werkzeug | c – Einzelfall; Gegenprobe-Regel deckt es |
| 13 | 13 Aufträge datiert archivieren | Archiv nie überschreiben, datieren | a – wege.md „Arbeitsteilung“, projekt „Ein Chat zur Zeit“ |
| 14 | 14 Rahmen voran | Erster Satz: wo wir stehen | c – Widerspruch global „Antwortaufbau“; projekt 19.10. gestrichen |
| 15 | 15 Einfache Worte | Kein Jargon, Fachwort einmal erklärt | a – global „Sprache“, projekt „Antworten“ |
| 16 | 16 Was in die Antwort gehört | Kein Prozessbericht in der Antwort | a – global „Kein Prozessbericht“, „Antwortökonomie“ |
| 17 | 17 Nur der nächste Handgriff | Keine Vorschau übernächster Schritte | c – Widerspruch global „Signalwort“ (Übersicht zuerst) |
| 18 | 18 Regeln hinterfragen | Festlegung an Belegen prüfen | a – global „Verbindliche Entscheidungen“, plan.md Linie 9 |
| 19 | 19 Rückfragen an Belege | Rückfrage nur mit prüfbarer Marke | a – global „Rückfragen“; Marke = Blatt-Prompt-Sache |
| 20 | 20 Eigenes Modell nachsehen | Modell im Systemkontext ablesen | b – global „Kontingent/Kontext klein“ (fiel mit projekt 19.10. weg) |
| 21 | 21 K 09-25 | Unbeaufsichtigte Aufträge: Standdatei, Commit je Teil | a – wege.md „Arbeitsteilung“ |
| 22 | 21 K 09-25 | Holger-Zeile vor Code-Aufträgen | a – wege.md „Arbeitsteilung“ |
| 23 | 21 K 09-25 | Sonnet für Mechanik, Abgleich danach | a – modelle.md § 3, wege.md, projekt „Runden“ |
| 24 | 21 K 09-25 | Sammeln breit, auswerten schmal | a – wege.md „Quellen“ |
| 25 | 21 K 09-25 | DNB-Inhaltsverzeichnisse als Quelle | a – wege.md „Quellen“ |
| 26 | 21 K 09-25 | Material vom Lehrer sofort eintragen | a – wege.md „Quellen“, global „Einmal fragen“ |
| 27 | 21 K 09-25 | Dünne Grundlage neu vorlegen | a – plan.md Linie 9, global „Verbindliche Entscheidungen“ |
| 28 | 22 Zählgrenzen | Zählgrenzen statt Zeitgrenzen | a – wege.md, modelle.md § 4a (Schrittgrenze) |
| 29 | 23 Beobachten | Ansehen ist Aufgabe, nicht Sichern | a – wege.md „Quellen“ (Betrachter genügt) |
| 30 | 24 Skripte samt Daten | Skript und Daten ins Repo | a – wege.md „Arbeitsteilung“ |
| 31 | 25 BOM PowerShell | UTF-8 ohne BOM schreiben | a – wege.md „Auf dem Rechner“ |
| 32 | 26 Commit -F | Umlaut-Commit über -F | a – wege.md „Auf dem Rechner“ |
| 33 | 27 Gegenprobe erklärt | Abweichung melden, Skript bleibt | a – wege.md „Arbeitsteilung“ |
| 34 | 28 Cloud-Sitzungen | Web-Sitzung für Repo-und-Netz | a – wege.md (Web: kein freies Netz, 0 € Guthaben) |
| 35 | 29 K 09-27 | Gegenprobewerte aus Belegdatei | b – global „Trennen“ („Nachsehen statt erinnern“, mit 63, 114, 151) |
| 36 | 29 K 09-27 | Inhalt per Code, Interaktion im Chat testen | a – wege.md „Vom Repo in den Betrieb“ (Testlauf) |
| 37 | 29 K 09-27 | Zwei Sitzungen, ein Schreiber | a – wege.md „Handy“, projekt „Runden“ |
| 38 | 29 K 09-27 | Uhrzeit nur aus Uhrbefehl | a – wege.md „Arbeitsteilung“ |
| 39 | 29 K 09-27 | Prompt-Version als Auftragsdatei | c – Chat committet seit Klonzugriff selbst |
| 40 | 29 K 09-27 | Remote Control mit /rc | a – wege.md „Handy“ |
| 41 | 30 K 09-26 | Urteilsarbeit nachts vorbereiten | c – keine Nachtaufträge seit 28.09. |
| 42 | 30 K 09-26 | Je Nachricht ein Auftrag | c – Code-Tab-Weg, Unteragenten ersetzen ihn |
| 43 | 30 K 09-26 | Vorlage hat Probeblatt | c – umgesetzt im Repo blattbau, kein Anweisungsstoff |
| 44 | 30 K 09-26 | Lesebefunde am selben Tag als Datei | a – projekt „Entscheidungen“ (befunde-M<n>.md) |
| 45 | 30 K 09-26 | Werkzeug liefert, was Mensch nicht besser kann | c – Blattregel, gehört in gemeinsam.md, nicht hierher |
| 46 | 30 K 09-26 | Modellwechsel im Chat ansagen | a – global „Kontext klein“ (teurer als nötig) |
| 47 | 30 K 09-26 | Web-Sitzungen pushen auf main | a – wege.md (Web-Sitzungen) |
| 48 | 31 K 09-27 U | Prognosen sind Schätzungen | a – global „Trennen“, projekt „Runden“ (Messwert statt Hochrechnung) |
| 49 | 31 K 09-27 U | Erst Prüfstein, dann Breite | a – global „Mittel“ (Pilot), projekt „Runden“ |
| 50 | 31 K 09-27 U | Lesen ist der Kostentreiber | a – modelle.md § 4a, wege.md (Mappe) |
| 51 | 31 K 09-27 U | Web-Sitzungen parallel je Ordner | a – wege.md, projekt „Runden“ (eigener Klon) |
| 52 | 31 K 09-27 U | Modellregel an Messwerten | a – modelle.md § 5, global „Nennen“ |
| 53 | 31 K 09-27 U | Erzeugen und Setzen trennen | a – plan.md Linie 2, projekt „Runden“ (Setzer) |
| 54 | 31 K 09-27 U | Datum im Dateinamen aus der Uhr | a – wege.md „Arbeitsteilung“ |
| 55 | 31 K 09-27 U | Ergebnisse einbinden, nicht ablegen | b – global „Stichwort Umzug“ (steht nur projekt) |
| 56 | 31 K 09-27 U | Vor Neuentwurf Zieldatei lesen | b – global „Chatstart“ (2) |
| 57 | 31 K 09-27 U | Geplante Aufgaben bei Netzbedarf | a – wege.md „Arbeitsteilung“ |
| 58 | 32 K 09-28b | Einbindungsfunde nach Zieldatei | a – projekt „Entscheidungen“ (Datei, in der es wirkt) |
| 59 | 32 K 09-28b | Abrechnung ist Messwert | a – modelle.md § 2 (Fakt mit Datum, Quelle) |
| 60 | 32 K 09-28b | Praxis des Nutzers vor Literatur | a – gemeinsam.md (03.10.); global nicht nötig |
| 61 | 32 K 09-28b | Erst Änderungsliste, dann Datei | a – global „Chatstart“ (vergleichen, benennen) |
| 62 | 33 K 09-28c | Aufträge ohne Rechner als Unteragent | a – wege.md „Arbeitsteilung“, projekt „Runden“ |
| 63 | 34 K 09-30 | Hinweise im Auftrag aus Agentenquelle | b – = Zeile 35 („Nachsehen statt erinnern“) |
| 64 | 34 K 09-30 | Je Agent eigener Klon | a – projekt „Runden“; 429-Regel → d wege.md |
| 65 | 34 K 09-30 | Musterlösungen als Vorstufenquelle | c – Fachmethode Katalog, kein Anweisungsstoff |
| 66 | 34 K 09-30 | Kontingent in Messwerten je Lauf | a – projekt „Runden“, global „Vorausplanen“ |
| 67 | 35 K 09-30b | Befunde in Alltagssprache | a – projekt „Antworten“ |
| 68 | 35 K 09-30b | Revision als eigene Entscheidung | a – global „Verbindliche Entscheidungen“, plan.md Linie 9 |
| 69 | 36 K 10-01 | Knöpfe, die Claude drücken kann | a – global „Selbst machen“ |
| 70 | 36 K 10-01 | Erst Exemplar, dann Regel (Layout) | a – wege.md „Vorgehen“ 7, projekt „Runden“ (Muster) |
| 71 | 36 K 10-01 | Fortgesetzte Agenten statt neue | c – Widerspruch global „Kontext klein“ (frisch statt lang), modelle § 4a |
| 72 | 36 K 10-01 | Schreibrecht nur beim Sitzungsstart | c – Repos werden seither mit Schreibzugang angehängt |
| 73 | 36 K 10-01 | Patch-Weg über den Rechner | d – wege.md (Rückfallweg) |
| 74 | 36 K 10-01 | Zukauf ist API-Preis | d – modelle.md § 2 (Fakt mit Quelle) |
| 75 | 37 K 10-01c | Rechte vor Arbeit | a – projekt „Repos/Zugriff“; Modus-Detail → d wege.md |
| 76 | 37 K 10-01c | Befund wird Änderung, nicht Posten | c – überholt durch plan.md Linie 8 (Form hält eine Runde) |
| 77 | 37 K 10-01c | Vollständigkeit vor Füllen | c – Fachregel Bank/Katalog |
| 78 | 38 K 10-03 | Nummern statt Namen | a – projekt „Repos“ |
| 79 | 38 K 10-03 | Erst das Kleinste, das trägt | a – global „Selbst machen“, „Teure Aktionen“ (sparsamster Weg) |
| 80 | 39 K 10-03b | Kontingent ist Sache des Nutzers | a – global „Kontingent“ (Abbruch nur auf mein Wort) |
| 81 | 39 K 10-03b | Einmal lesen, mehrere Teile ein Agent | c – Widerspruch modelle § 4a (ein Ergebnis je Agent) |
| 82 | 39 K 10-03b | Urteil des Nutzers als Datei | a – gemeinsam.md („leicht“ ist Lehrerurteil) |
| 83 | 39 K 10-03b | Vorgängerchat lesen | c – Register plan.md § 8 ersetzt Chat-Suche |
| 84 | 39 K 10-03b | Offene Punkte als HTML rechts | c – plan.md „Offen“ + projekt „Erinnern“ |
| 85 | 40 K 10-03d | Keine Option ohne Informationsgewinn | b – global „Keine Auswahlbuttons“ (mit Zeile 116) |
| 86 | 40 K 10-03d | Eine Stufe festzurren, dann nächste | a – global „Keine Auswahlbuttons“ (eine je Nachricht); Bild rechts c |
| 87 | 40 K 10-03d | Gleicher Ablauf ist ein Wert | c – Einzelfall Bedienentwurf 03.10. |
| 88 | 41 K 10-04 | Einmal fragen, dann eintragen | a – global „Einmal fragen“ |
| 89 | 41 K 10-04 | Große Läufe in Blöcken mit Sparprüfung | a – global „Mittel“ (Pilot, dann Breite), „Teure Aktionen“ |
| 90 | 41 K 10-04 | Vereinheitlichen Stufe für Stufe | c – Arbeitstechnik, Einzelfall 04.10. |
| 91 | 42 K 10-05 | Nächsten Schritt prüfen, nicht übernehmen | b – global „Chatstart“ (2) |
| 92 | 42 K 10-05 | Nur das Gefragte | a – global „Antwortökonomie“ |
| 93 | 42 K 10-05 | Bild vor dem Senden ansehen | b – global „Zeigen“ (mit 97, 105, 110, 175) |
| 94 | 42 K 10-05 | Ein Hauptplatz je Ding | a – pruefung.md (Hauptplatz) |
| 95 | 42 K 10-05 | Fable zahlt die Woche mit | a – modelle.md § 2 |
| 96 | 43 K 10-06 | Revisionsschranke | a – plan.md Linie 9, global „Chatstart“ (2) |
| 97 | 43 K 10-06 | Zeigen statt beschreiben | a – global „Zeigen“ (Kern); Varianten nebeneinander → Zeile 93 |
| 98 | 43 K 10-06 | Ein Begriff, eine Bedeutung | a – begriffe.md, projekt „Antworten“ |
| 99 | 43 K 10-06 | Vorschlag anbieten, nicht verordnen | a – global „Kontingent“ (Abbruch), „Kontextdisziplin“ (vorschlagen) |
| 100 | 43 K 10-06 | Opus-Agenten schonen die Woche | c – Messwert überholt durch modelle § 6 (12.10.) |
| 101 | 44 K 10-06b | Sparen ungefragt | a – global „Teure Aktionen“ (übernommen 06.10.) |
| 102 | 45 K 10-06c | Erst die Sicht, dann das Ergebnis | c – Bauregel, Ort gemeinsam.md/bankblatt.md |
| 103 | 45 K 10-06c | Vorhandenes Wissen anschließen | a – global „Chatstart“ (zitieren statt herleiten) |
| 104 | 45 K 10-06c | Echte Sammlungen vor Erfindung | a – plan.md Linie 3 (Originale zuerst) |
| 105 | 45 K 10-06c | Beurteilen am Ergebnis, nicht Liste | b – global „Zeigen“ (= Zeile 93) |
| 106 | 46 K 10-07 | Ausschnitt klein zeigen | a – global „Zeigen“, modelle § 4a |
| 107 | 46 K 10-07 | Agentenläufe klein schneiden | a – modelle § 4a, global „Kontext klein“ |
| 108 | 47 K 10-07b | Bestand lesen, bevor man plant | a – global „Chatstart“ (2), projekt „Chatstart“ |
| 109 | 47 K 10-07b | Ideen sind zuerst Richtungen | b – global „Haltung“ (mit Zeile 112) |
| 110 | 47 K 10-07b | Selbst prüfen, dann zeigen | b – global „Zeigen“ (= Zeile 93) |
| 111 | 47 K 10-07b | Messwert Kosten 07.10. | c – überholt durch modelle § 6 |
| 112 | 48 K 10-09 | Einfach vor vollständig, Leitsatz ein Satz | b – = Zeile 109 |
| 113 | 48 K 10-09 | Stehender Plan als Anker | b – global „Stichwort Umzug“ Punkt 6 |
| 114 | 48 K 10-09 | Daten vor Bauen prüfen | b – = Zeile 35 („Nachsehen statt erinnern“) |
| 115 | 48 K 10-09 | Messwert Kosten 08./09.10. | c – überholt durch modelle § 6 |
| 116 | 49 K 10-08 | Jede Frage mit Empfehlung | b – global „Keine Auswahlbuttons“ (= Zeile 85); projekt hat es |
| 117 | 49 K 10-08 | Begriffstabelle mit Beispiel | a – begriffe.md (mathe-nachhilfe) |
| 118 | 49 K 10-08 | Regeln für Handwerk, Zweck fürs Urteil | a – projekt „Entscheidungen“ (Warum – Beispiel – Grenze) |
| 119 | 49 K 10-08 | Beim Plan bleiben | a – plan.md Linie 8 („Nebenfragen nach § 6“) |
| 120 | 49 K 10-08 | Erst nachsehen, dann definieren | a – projekt „Entscheidungen“ (Register), global „Chatstart“ |
| 121 | 50 K 10-09b | Vom Ende her sparen | a – projekt „Runden“ (Setzer ohne Modell), plan.md Linie 2 |
| 122 | 50 K 10-09b | Aufräumen statt schichten | a – plan.md § 0 (eine Stelle), projekt „Ein Chat zur Zeit“ |
| 123 | 50 K 10-09b | Daten jetzt, Sorte später | c – Fachregel Bank |
| 124 | 50 K 10-09b | Linien vom Lehrer, Kleines vom Chat | a – projekt „Entscheidungen“ |
| 125 | 50 K 10-09b | Messwert 09.10. | c – überholt durch modelle § 6 |
| 126 | 51 K 10-10 | Gespeichertes Gerüst füllen, nicht neu planen | c – Bauregel, Ort bankblatt.md/bauauftrag.md |
| 127 | 51 K 10-10 | Ziel neben jede Runde legen | b – = Zeile 91 (global „Chatstart“ (2)) |
| 128 | 51 K 10-10 | Keine Regel aus Einzelbefunden | a – projekt „Entscheidungen“ (Tendenz → zweites Blatt) |
| 129 | 51 K 10-10 | Vorbild als Maß, Vergleich vor Abgabe | a – projekt „Runden“ (Kritiker, Skripte) |
| 130 | 51 K 10-10 | Messwert 10.10. | c – überholt durch modelle § 6 |
| 131 | 52 K 10-10b | Ein fester Stand je Sorte | a – plan.md Linie 6 |
| 132 | 52 K 10-10b | Sorten getrennt, Technik teilen | a – plan.md Linie 3 |
| 133 | 53 K 10-10c | Entscheidungen an einer Stelle, Markensuche | a – projekt „Ein Chat zur Zeit“, „Entscheidungen“; plan.md § 0 |
| 134 | 53 K 10-10c | Übergabe keine Quelle für Entscheidungen | a – projekt „Chatstart“ |
| 135 | 53 K 10-10c | Gezeigte Datei ganz lesen | a – projekt „Chatstart“ (Sortendatei ganz) |
| 136 | 54 K 10-10d | Einträge schreibt ein Skript | a – global „Mittel“ (einmal zum Skript), projekt „Betrieb“ |
| 137 | 54 K 10-10d | Zugriff einmal regeln | a – projekt „Repos/Zugriff“ |
| 138 | 54 K 10-10d | Prompt per Verweis statt Kopie | c – Widerspruch projekt „Betrieb“ (Prompt als Block); offen für Lehrer |
| 139 | 55 K 10-10e | Erzeugte Dateien nie direkt ändern | b – projekt „Runden“ (gilt für Chat und Agent) |
| 140 | 55 K 10-10e | Kritiker eng, zwei Prüffragen | d – modelle.md § 4a (Sparregel mit Messwert) |
| 141 | 56 K 10-10f | Mit Regeldatei ihre Leser ablösen | a – projekt „Repos“ |
| 142 | 56 K 10-10f | Stand Repo gegen Einstellung | a – global „Chatstart“ (1) |
| 143 | 57 K 10-11 | Agenten erst nach Go | a – projekt „Runden“ |
| 144 | 57 K 10-11 | Regeln als Warum, nicht Wie | a – projekt „Entscheidungen“ |
| 145 | 57 K 10-11 | Tendenz vor Regel | a – projekt „Entscheidungen“ |
| 146 | 57 K 10-11 | Muster und Stichprobe | a – projekt „Runden“, plan.md Linie 7 |
| 147 | 58 K 10-11b | Wege mit Namen | b – global „Keine Auswahlbuttons“ (= Zeile 85); projekt hat es |
| 148 | 59 K 10-13 | Dauer mit Uhrzeit nennen | a – projekt „Runden“ |
| 149 | 60 K 10-13b | Entscheidung in die Daten, Skript vergleicht | a – plan.md § 0 (erst umgesetzt, wenn Skript prüft) |
| 150 | 61 K 10-14 | Kein Bedientext auf Gedrucktem | a – gemeinsam.md, bankblatt.md |
| 151 | 61 K 10-14 | Erst suchen, dann „gibt es nicht“ | b – = Zeile 35 („Nachsehen statt erinnern“) |
| 152 | 62 K 10-15 | Paket mit Grenze statt Go je Runde | c – Widerspruch global „Teure Aktionen“ (Go je Aktion), projekt „Runden“ |
| 153 | 62 K 10-15 | Durchsicht als kommentiertes PDF | a – global „Kommentiertes PDF“, „Zeigen“ |
| 154 | 63 K 10-15b | Große Dateien nicht über Drive-Chat | a – wege.md „Ablage“ |
| 155 | 64 K 10-16 | Ganzer Bestand vor Folgepunkten | c – Einzelbefund, noch kein zweites Exemplar |
| 156 | 65 K 10-16 Bau | Billigen Weg neben teuren stellen | a – global „Teure Aktionen“ (sparsamster Weg), „Mittel“ |
| 157 | 65 K 10-16 Bau | Stumme Fehler laut machen | b – projekt „Runden“ („Prüfskript hält an“, mit 158, 171, 177, 179) |
| 158 | 66 K 10-16b | Regel ins Werkzeug | b – = Zeile 157; plan.md § 0 hat den Kern |
| 159 | 66 K 10-16b | Vor Festlegung Bestand durchsuchen | a – projekt „Entscheidungen“ (im Register nachsehen) |
| 160 | 67 K 10-16c | Anzeige vor dem Start, Chat mitschätzen | b – projekt „Runden“ (Absatz Modelle) |
| 161 | 68 K 10-16d | Pilot Zeile für Zeile gegen Muster | b – projekt „Runden“ („Muster vor Breite“, mit 174) |
| 162 | 69 K 10-17a | Kennung frisch holen bei zwei Chats | c – ein Chat führt alles (19.10.) |
| 163 | 69 K 10-17a | Erreichbarkeit erst nach zweitem Versuch | d – wege.md (Rechnerbrücke) |
| 164 | 70 K 10-17b B5 | Eigene Grenze als eigene benennen | b – global „Haltung“ (mit 178); fiel mit projekt 19.10. weg |
| 165 | 70 K 10-17b B5 | Nie lesen und überschreiben im selben Zug | d – wege.md (Skript-Handwerk) |
| 166 | 71 K 10-17b A1 | Doppelte Kennung nach letztem Pull | c – ein Chat führt alles (19.10.) |
| 167 | 71 K 10-17b A1 | Gestaltung erst als Text, dann bauen | c – Einzelfall; beißt sich mit Zeile 175 (Probe zeigen) |
| 168 | 72 K 10-17c | Zwischendateien nur im eigenen Ordner | a – projekt „Runden“ (eigener Klon) |
| 169 | 72 K 10-17c | Abnehmer nennen vor Vorratslauf | a – projekt „Runden“ (Token → Daten für den Setzer) |
| 170 | 73 K 10-17d | Bei Formstreit Muster des Lehrers als Anker | b – projekt „Entscheidungen“ (mit 180); Widerspruch prüfen |
| 171 | 74 K 10-18 | Aufteilung per Skript prüfen | b – = Zeile 157 (Prüfskript vor dem Start) |
| 172 | 74 K 10-18 | Lizenz vor Wortlaut | b – projekt „Repos“ (mit 176) |
| 173 | 74 K 10-18 | Original vor OCR | d – wege.md „Quellen“ |
| 174 | 75 K 10-18a | Muster abnehmen, dann vervielfältigen | b – = Zeile 161 |
| 175 | 75 K 10-18a | Bei Formfragen Probe zeigen | b – = Zeile 93 (global „Zeigen“) |
| 176 | 76 K 10-18b B6 | Bedingt freie Texte erst privat | b – = Zeile 172 |
| 177 | 76 K 10-18b B6 | Prüfregel nicht durch Umschreiben erfüllen | b – = Zeile 157 |
| 178 | 76 K 10-18b B6 | Eigene Grenze nicht als Linie ablegen | b – = Zeile 164 |
| 179 | 77 K 10-18b F3 | Verbote mechanisch prüfen | b – = Zeile 157 |
| 180 | 77 K 10-18b F3 | Vorschlag des Lehrers wörtlich umsetzen | b – = Zeile 170; Widerspruch projekt „Entscheidungen“ |
| 181 | 77 K 10-18b F3 | Vorgaben aus Ausschnitt locker halten | a – projekt „Entscheidungen“ (Warum – Beispiel – Grenze) |
| 182 | 78 K 10-18c | Große Runden durchlaufen lassen | a – projekt „Runden“ (Spannung zu global, s. § 3) |
| 183 | 78 K 10-18c | Agenten-Klone lokal ziehen | a – projekt „Runden“ |

## 2 Fehlt und lohnt (10 von 17, nach Nutzen)

Stichprobe vorab (§ 3): Zeile 180 ist c, nicht b. Je Regel: Ziel ·
Wortlaut · Grund.

1. **Nachsehen statt erinnern** (35, 63, 114, 151) → global.md
   „Haltung“, neuer Absatz nach „Trennen“:
   „Nachsehen statt erinnern: Werte, Festlegungen und „gibt es nicht“
   stützt du auf eine Datei, die du in diesem Zug gelesen oder
   durchsucht hast, nie auf Gedächtnis oder Übergabe; weicht eine
   Gegenprobe ab, prüfst du zuerst den Wert.“
   Grund: vier Vorfälle (26.09., 30.09., 08.10., 14.10.); heute
   verlangt das nur projekt „Entscheidungen“ fürs Register.
2. **Werkzeug hält an** (157, 158, 171, 177, 179) → projekt „Runden“,
   Absatz Agenten, am Ende:
   „Eine gebrochene Formregel und stille Verluste prüft das erzeugende
   Werkzeug und hält an; eine richtige Lösung bleibt, auch wenn es
   meldet (Ausnahme mit Grund). Aufteilungen prüft vor dem Start ein Skript.“
   Grund: fünf Belege in vier Tagen; global „Mittel“ sagt nur, dass ein
   Skript prüft, nicht dass es anhält.
3. **Lizenz vor Wortlaut** (172, 176) → projekt „Repos“, nach
   „Öffentlich außer -privat“:
   „Fremder Wortlaut kommt erst nach erfasster Lizenz je Quelle ins
   Repo, Bilder einzeln; Agenten schreiben ihn zuerst nach `-privat`,
   öffentlich erst nach geprüfter Bedingung.“
   Grund: 18.10. lagen 1 052 Prüfungstexte öffentlich – Rechtsrisiko,
   das eine Zeile verhindert.
4. **Selbst prüfen, dann zeigen** (93, 105, 110, 175) → global.md
   „Zeigen“, als erster Satz:
   „Bevor du mir etwas zeigst, siehst du es gerendert selbst an und
   prüfst es gegen die Handwerksregeln; bei Formfragen zeigst du eine
   kleine Probe statt beschriebener Varianten.“
   Grund: 07.10. war die Hälfte der Befunde Handwerk, das das Modell
   selbst hätte finden können; „Zeigen“ regelt nur die Form.
5. **Ideen sind Richtungen** (109, 112) → global.md „Haltung“, nach
   „Verbindliche Entscheidungen“:
   „Richtungen: Meine Bemerkungen hältst du als Richtung mit Grund
   fest, nicht als Regel mit „immer/nie“; Regel wird daraus erst auf
   mein Wort oder mit einem Befund am Ergebnis.“
   Grund: projekt „Entscheidungen“ sagt das nur für Lösungsideen; die
   Kreisläufe 07.–09.10. entstanden an Regeln, Plänen, Prompts.
6. **Eigene Grenze als eigene** (164, 178) → global.md „Haltung“,
   ans Ende von „Trennen“:
   „Lehnst du etwas aus eigenem Grund ab, nennst du es als deine
   Grenze mit Grund – im Chat und in Dateien –, nie als meine
   Entscheidung.“
   Grund: zwei Vorfälle 17./18.10.; eine falsch zugeschriebene Linie
   verfälscht das Register und wird nie wieder geprüft.
7. **Nächsten Schritt prüfen** (91, 127) → global.md „Chatstart“ (2),
   ersetzt „beginne mit dem genannten nächsten Schritt“:
   „beginne mit dem genannten nächsten Schritt, nachdem du in einem
   Satz gesagt hast, wem er dient; trägt der Grund nicht, leg den
   besseren vor“
   Grund: 04.10. stand Abitur vor P10 (vier Schüler P10, einer Abitur);
   „vorlegen“ lässt die Entscheidung beim Lehrer.
8. **Muster abnehmen, dann Breite** (161, 174) → projekt „Runden“,
   nach „Pilot vor Breite, wo Form oder Kosten neu sind“:
   „Ist die Form neu, startet die Breite erst, wenn ich Muster und
   Pilot gesehen habe; den Pilot hältst du Zeile für Zeile gegen das
   Muster – „Skript 0“ reicht nicht.“
   Grund: 16.10. und 18.10. trug ein lückenhaftes Muster seine Lücke
   in jedes Ergebnis.
9. **Anzeige vor dem Start** (160) → projekt „Runden“, Absatz Modelle,
   ersetzt „Nach jeder Runde fragst du nach der Nutzungsanzeige“:
   „Vor und nach jeder Runde fragst du nach der Nutzungsanzeige; die
   Schätzung enthält die Chat-Antworten, nicht nur die Agenten.“
   Grund: 16.10. 0,3 Punkte geschätzt, 2 gemessen; ohne Vorher-Wert
   lässt sich der Verbrauch keiner Runde zuordnen.
10. **Erzeugte Dateien nie direkt ändern** (139) → projekt „Runden“,
    Absatz Agenten (gilt auch für den Chat):
    „Vor jeder Änderung prüfst du, ob die Datei erzeugt wird
    (Kopfzeile, Skript im Repo); geändert wird die Quelle, dann neu
    erzeugt.“
    Grund: steht nur in der CLAUDE.md der Erfassung; 10.10. musste ein
    Agent eine Handänderung des Chats nachziehen.

Nicht aufgenommen, obwohl b: 55 Ergebnisse einbinden und 85/116/147
Frage mit Empfehlung, Wege mit Namen (stehen in der Projektanweisung,
global nützte nur anderen Projekten); 56 und 113 (deckt global
„Chatstart“ (2) und projekt „Ein Chat zur Zeit“ weitgehend); 20
Modell nachsehen (ein Vorfall, 23.09.); 170 Muster des Lehrers als
Anker (Formstreit, gehört in plan.md/pruefung.md, wenn er wiederkommt);
6 Material am Handgriff (seit Unteragenten selten; s. W3).

Widersprüche, einzeln:
- W1 Zeile 180 „Vorschlag des Nutzers wörtlich umsetzen; eine
  Rückfrage ist meist ein Einwand“ widerspricht global „Fragezeichen“
  (Frage beantworten, nicht als Aussage nehmen) und projekt
  „Entscheidungen“ („Lösungsideen sind Beispiele“). Nicht aufnehmen.
- W2 Zeile 182 und projekt „Runden“ („bis zum Ende laufen lassen“)
  gegen global „Teure Aktionen“ („Zustimmung gilt für die einzelne
  Aktion … der zweite Durchlauf wird angekündigt“). Steht heute so in
  beiden Dateien; die Konfliktregel in „Haltung“ löst es nicht
  eindeutig. Entscheidung des Lehrers.
- W3 Zeile 6 (und wege.md „Arbeitsteilung“): „Holger:“-Zeile, darunter
  der Block – global „Stichwort Umzug“: Codeblock, darunter die
  „Holger:“-Zeile. Reihenfolge umgekehrt.
- W4 schon als c geführt: 14 gegen „Antwortaufbau“, 17 gegen
  „Signalwort“, 71 gegen „Kontext klein“, 81 gegen modelle § 4a, 138
  gegen projekt „Betrieb“, 152 gegen „Teure Aktionen“.

## 3 Zahlen

Stichprobe 15 Zeilen gegen kandidaten.md und die heutigen Dateien
(6, 14, 20, 35, 55, 61, 71, 85, 93, 139, 152, 160, 164, 172, 180):
13 bestätigt, 1 mit Vorbehalt (6: Widerspruch W3, Nutzen klein),
1 falsch (180: b → c, W1). Kopfzeile oben zählt 16 eigenständige
b-Regeln; es sind 17.

Nach Korrektur: **183 Regeln · a 107 (58 %) · b 34 (19 %; 17
eigenständig, 10 in § 2) · c 34 (19 %) · d 8 (4 %).**

Befund dazu: Mehr als die Hälfte der Einträge stand beim Schreiben
oder kurz danach schon in einer Regeldatei; 51 Umzugsblöcke in 24
Tagen, im Mittel 3,6 Regeln je Umzug. Die Datei wuchs, weil jeder
Umzug Blöcke schrieb, nicht weil Regeln fehlten.

## 4 Vorschlag: kandidaten.md als kurzer Eingang

Weg: `git mv kandidaten.md archiv/kandidaten-bis-2026-10-19.md`
(wortgleich, Geschichte bleibt), davor als Kopf § 1 dieser Tabelle
(Status je Regel). Neue `kandidaten.md`:

    # Regelkandidaten – Eingang

    Stand: 2026-10-19

    Nur offene Vorschläge der letzten 14 Tage, je Zeile: Datum ·
    Regel in einem Satz · Anlass · Zieldatei und Abschnitt. Was
    schon in global.md, projekt-<name>.md, modelle.md oder wege.md
    steht, kommt nicht hierher. Beim Umzug sortiert der Chat:
    übernommen (Zieldatei nennen, Zeile raus), verworfen (Zeile
    raus), älter als 14 Tage ohne Entscheidung: dem Lehrer
    vorlegen. Bis 19.10.2026: archiv/kandidaten-bis-2026-10-19.md.

    ## Eingang

Erste Füllung: was der Lehrer aus § 2 nicht sofort übernimmt, dazu
113 und 170. 6, 20, 55, 56, 85 bleiben im Archiv (Projekt deckt sie
oder Einzelfall).

**global.md „Chatstart“ – anpassen, ja.** Für dieses Projekt greift
der Satz nicht (die Projektanweisung nennt das Repo), für andere
Projekte zeigt er auf eine Datei, die es so nicht mehr gibt. Neuer
Absatz, geändert ist nur der dritte Satz:

    Chatstart im Projekt, in dieser Folge: (1) Lies `global.md` und,
    falls vorhanden, die `projekt-<name>.md` dieses Projekts aus
    `hz-0801/anweisungen` per Raw-URL; ist ein Stand dort jünger als
    der in der Einstellung, sag es in einem Satz und nenne den
    Kopierschritt. Nennt die Projektanweisung das Repo nicht, lies
    zusätzlich den Eingang von `kandidaten.md` (offene Vorschläge der
    letzten 14 Tage), sag in einem Satz, ob einer davon für dieses
    Projekt gilt, und gib den Verweissatz für die Projektanweisung
    aus. (2) Liegt eine Übergabe vor, nimm die dort
    genannte Arbeitsgrundlage als maßgeblich, beginne mit dem genannten
    nächsten Schritt und rolle getroffene Entscheidungen nicht ohne
    Anlass neu auf. Fehlt eine für die Fortsetzung nötige Datei, sag es.
    Liegt keine Übergabe vor, sieh zuerst nach, was im Projekt schon
    vorhanden ist, und lies den maßgeblichen Stand, bevor du inhaltlich
    arbeitest. Sag in einem Satz, worauf du dich stützt, oder dass
    nichts Passendes da ist. Was dort schon dokumentiert ist, wird
    zitiert oder fortgeschrieben, nicht neu hergeleitet. Bevor du eine
    Datei als neue Fassung ausgibst, vergleich sie mit der vorhandenen
    und benenne, was sich ändert; ist der Inhalt derselbe, sag das,
    statt eine Ersetzung zu behaupten. In Chats ohne Projekt nichts
    davon.

(Wird § 2 Nr. 7 übernommen, ändert sich in (2) zusätzlich der
Halbsatz „beginne mit dem genannten nächsten Schritt“.)

**global.md „Anweisungs-Repo“ – anpassen, ja** (Eingang, Filter
„steht schon“, wege.md fehlte in der Liste):

    Meine Arbeitsregeln liegen in `hz-0801/anweisungen` (`global.md`,
    `modelle.md`, `wege.md`, `projekt-<name>.md`, `kandidaten.md`);
    die Dateien sind die Wahrheit, die Einstellungen ihre
    Arbeitskopie mit Stand-Zeile. Sag im laufenden Gespräch, wenn
    eine Festlegung projektübergreifend nützlich wäre und in keiner
    dieser Dateien steht; ich entscheide mit einem Wort, ob sie in
    den Eingang von `kandidaten.md` kommt. Der Eingang hält nur
    offene Vorschläge der letzten 14 Tage; Übernommenes und
    Verworfenes geht nach `archiv/`.

**projekt-verbessereBlaetter.md „Chatstart“ – anpassen, ja** („den
jüngsten Block“ gibt es nicht mehr; ein offener Vorschlag liegt beim
Lehrer und fällt so unter die Zwei-Tage-Regel):

    Repos anhängen. Lies in plan.md „Wie dieser Plan gilt“, „Jetzt“ und
    „Offen“, von `uebergabe.md` Kopf und Arbeitsstand; sag in einem Satz,
    was laut `git log` seit der Übergabe geschah. Nenne in höchstens fünf
    Zeilen den Schritt aus „Jetzt“ und die obersten offenen Punkte, vor
    allem, was bei mir liegt; was länger als zwei Tage liegt, sprichst du
    an. Dann nimm, was ich meine, sonst den Schritt aus „Jetzt“.
    Entscheidungen nimmst du aus dem Register und der Datei, auf die es
    zeigt, nie aus der Übergabe. Vor inhaltlicher Arbeit an einer Sorte
    liest du ihre Datei ganz. Den Eingang von `kandidaten.md` liest du
    ganz; ein Vorschlag darin liegt bei mir. Ist ein neues Modell
    erschienen oder der letzte Eintrag in `modelle.md` § 6 älter als ein
    Monat, kommt die Neubewertung zuerst.

Im selben Commit nachziehen: anweisungen `README.md` („Dateien“:
kandidaten.md = Eingang, Archiv bis 19.10.; „Mechanismus“ (2): beim
Umzug nur Regeln, die in keiner Regeldatei stehen, als Zeile in den
Eingang; „Verweis in Projektanweisungen“: „Lies beim Chatstart den
Eingang von `kandidaten.md` …“). Die Reifestufen (Kandidat → erprobt →
global) entfallen mit dem Eingang: Es gab nur ein Projekt, „erprobt in
einem zweiten“ trat nie ein; übernommen wurde stets auf Lehrerwort.

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

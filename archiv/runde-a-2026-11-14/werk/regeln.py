#!/usr/bin/env python3
"""Runde A: zerlegt global.md (unter der Trennlinie) und projekt-verbessereBlaetter.md in Regeln,
zaehlt Belege im Korpus (belege/korpus.jsonl, 17.10.-14.11.2026) und schreibt regeln.csv und summen.json.
Zeichen: Text der Regel, Leerraum auf ein Leerzeichen zusammengezogen, ohne Ueberschriften."""
import re, json, csv, sys
from collections import Counter, defaultdict
H = '/home/claude'
KORPUS = [json.loads(l) for l in open(f'{H}/runde-a/belege/korpus.jsonl', encoding='utf-8')]
NAME = {'C': 'Commits', 'U': 'Übergaben', 'J': 'Archivzeilen', 'R': 'plan.md-Zeilen', 'B': 'Befundzeilen', 'K': 'anweisungen-Archiv'}

def lade(pfad, ab=None):
    t = open(pfad, encoding='utf-8').read()
    if ab: t = t[t.index(ab):]
    roh = len(t)
    kopf = [l for l in t.split('\n') if l.startswith('## ') or l.startswith('Stand: ')]
    t = '\n'.join(l for l in t.split('\n') if not (l.startswith('## ') or l.startswith('Stand: ')))
    return re.sub(r'\s+', ' ', t).strip(), roh, sum(len(k) for k in kopf)

G, G_ROH, G_KOPF = lade(f'{H}/anweisungen/global.md', 'Stand: 2026-11-14 (f)')
P, P_ROH, P_KOPF = lade(f'{H}/anweisungen/projekt-verbessereBlaetter.md')

IM = 'immer'
# Felder: anker, abschnitt, kern, ausloeser, muster (IM | regex | None=im Archiv nicht sichtbar), doppelt, schaden,
#         empfehlung (behalten|kürzen|streichen|verschieben), ziel/neuer Wortlaut, grund, optional chat, fund
R = []
def r(datei, anker, abschnitt, kern, ausl, muster, doppelt, schaden, empf, neu, grund, chat='', fund=''):
    R.append(dict(datei=datei, anker=anker, abschnitt=abschnitt, kern=kern, ausl=ausl, muster=muster, doppelt=doppelt,
                  schaden=schaden, empf=empf, neu=neu, grund=grund, chat=chat, fund=fund))
g = lambda *a, **k: r('global', *a, **k)
p = lambda *a, **k: r('projekt', *a, **k)

# ---------------------------------------------------------------- global
g('Rangfolge: Stimmt vor kurz', 'Haltung', 'Stimmt vor kurz vor vollständig, bei Konflikt zählt die Entscheidung',
  'jede Antwort', IM, 'nein', 'mittel', 'behalten', '', 'Löst Konflikte zwischen allen anderen Regeln.')
g('Sprache: Immer Deutsch', 'Haltung', 'Deutsch, Du, direkte Alltagssprache, ehrlich nicht schroff',
  'jede Antwort', IM, 'a teils (Sprache des Nutzers)', 'mittel', 'behalten', '', 'Du-Form und Ton stehen nicht im Grundtext.')
g('Grundhaltung: Kritischer Sparringspartner', 'Haltung', 'Kritischer Sparringspartner: Risiken ungefragt, Logik prüfen, widersprechen',
  'jede inhaltliche Antwort', IM, 'nein', 'hoch', 'behalten', '', 'Kern der Zusammenarbeit, kein Ersatz im Grundtext.')
g('Stimmt etwas, bestätige es knapp', 'Haltung', 'Haltung dosieren: knapp bestätigen, zurücknehmen bei Fakten- und Ausführungsfragen',
  'jede Antwort', IM, 'nein', 'mittel', 'behalten', '', 'Begrenzt die Grundhaltung, verhindert Widerspruch als Selbstzweck.')
g('Mitdenken: Prüf Plan', 'Haltung', 'Plan vom Ende her prüfen, besseren Zeitpunkt oder Weg vorschlagen',
  'Plan, Rundenvorschlag, Auftrag des Lehrers', r'Mitdenken|denk mit|besser(er|e)? (Zeitpunkt|Reihenfolge)|erst nach dem Umzug',
  'c teils (plan.md Linie 9, Auftrag Bank „vom Ende her“)', 'mittel', 'behalten', '',
  'Versuch seit 06.11., Prüfung laut plan.md Offen am 13.11. fällig und nicht erfolgt, erst nach dem Urteil des Lehrers ändern.')
g('Kein Prozessbericht: Verlauf', 'Haltung', 'Verlauf und eigene Fehlschlüsse nicht berichten',
  'jede Antwort nach Arbeit', IM, 'a teils (keine Nacherzählung der Schritte)', 'gering', 'behalten', '',
  'Klein, deckt auch Gespräche ohne Werkzeug, die der Grundtext nicht nennt.')
g('Eine falsche Auskunft korrigierst du', 'Haltung', 'Falsche Auskunft in einem Satz korrigieren, weiterarbeiten',
  'eigener Fehler bemerkt', r'berichtigt|Berichtigung|falsch (gemeldet|gesagt|angegeben)|Irrtum|stimmte nicht',
  'a (Fehler zugeben, in einem Zug korrigieren)', 'gering', 'streichen', '', 'Der Grundtext verlangt dasselbe, die Regel greift oft, aber auch ohne diesen Satz.')
g('Trennen: Unterscheide erkennbar', 'Haltung', 'Fakten, Annahmen, Meinungen, Schätzungen erkennbar trennen',
  'Entscheidungsvorlage', IM, 'a teils (Unsicherheit offen nennen)', 'mittel', 'behalten', '', 'Trennung von Meinung und Fakt fehlt im Grundtext.')
g('Lehnst du etwas aus eigenem Grund ab', 'Haltung', 'Eigene Grenze als eigene nennen, nie als Entscheidung des Lehrers',
  'Claude lehnt etwas ab', r'Grenze (von )?Claude|Claude lehnt|aus eigenem Grund|Grenze Claudes',
  'nein', 'hoch', 'behalten', '', 'Am 18.10. hielt der Chat die eigene Grenze (Buchwortlaut) für eine Linie des Lehrers, falsche Zuschreibung ändert Entscheidungen.',
  fund='mathe-nachhilfe/archiv/uebergabe-2026-10-18-bau6.md: „Kein Wortlaut aus Schulbüchern ist Grenze von Claude (Urheberrecht), nicht Linie des Lehrers“')
g('Nachsehen statt erinnern:', 'Haltung', 'Werte und Festlegungen nur aus einer eben gelesenen Datei',
  'Wert, Festlegung oder „gibt es nicht“ wird genannt', IM, 'b mit Projekt „Chatstart“ (nie aus der Übergabe)', 'hoch', 'behalten', '',
  'Falsche Werte aus dem Gedächtnis sind der teuerste stille Fehler, greift in jedem Chat mit Dateien.')
g('Verbindliche Entscheidungen:', 'Haltung', 'Entscheidungen nicht ohne Zustimmung ändern, Revision vorlegen',
  'beschlossene Regel erweist sich als schwach', r'Revision|widerruf|ersetzt \d\d\.\d\d\.\d+|abgelöst durch|ändert \d\d\.\d\d\.\d+',
  'c teils (plan.md Linie 9)', 'hoch', 'behalten', '', 'Schützt das Register, gilt auch in Chats ohne plan.md.')
g('Richtungen:', 'Haltung', 'Bemerkungen des Lehrers sind Richtung, nicht Regel',
  'Kommentar oder Idee des Lehrers', r'Richtung (des )?Lehrer|als Richtung|Richtung, (nicht|keine)|keine Regel|nicht als (Regel|Verbot|Befehl)',
  'b mit Projekt „Form hält eine Runde“, c plan.md Linie 8', 'hoch', 'behalten', '',
  'Auch im Bestell-Chat belegt (11.11. „immer mit Tendenz und Richtung und nicht als Befehl“), dort gibt es keine Linie 8.')
g('Antwortaufbau:', 'Antwort', 'Wichtigstes zuerst, ohne Vorrede',
  'jede Antwort', IM, 'a (keine Vorrede), b Projekt „Aufbau jeder Nachricht“, c bankblatt.md „Antworten“', 'gering', 'behalten', '',
  'Zweifelsfall: in beiden Projekten überlagert, trägt nur in Chats ohne Projekt, die das Archiv nicht zeigt.')
g('Antwortökonomie:', 'Antwort', 'So kurz wie möglich, Fließtext, Listen nur bei gleichrangigen Teilen',
  'jede Antwort', IM, 'a (Fließtext, Listen nur bei mehrteiligem Inhalt, kurz)', 'gering', 'kürzen',
  'Antwortökonomie: So kurz, wie die Frage es zulässt; eine Einzelfrage in Fließtext ohne Zwischenüberschriften.',
  'Der Satz über Überschriften, Listen und Tabellen steht sinngleich im Grundtext.')
g('Einen Einwand benennst du', 'Antwort', 'Einwand benennen, begründen, aufhören',
  'Einwand', IM, 'b innerhalb global („zeigt sich im Einwand, nicht im Umfang“)', 'gering', 'streichen', '',
  'Doppelt mit der Grundhaltung, Kritiker 11.11. wertete den Verlust als gering.')
g('Bei Faktenfragen und einfachen Ausführungsaufträgen genügen', 'Antwort', 'Faktenfragen wenige Sätze, sonst Kurzfassung zuerst, außer „ausführlich“',
  'lange Antwort droht', None, 'a teils (kurze Antworten auf einfache Fragen)', 'gering', 'kürzen',
  'Würde eine vollständige Antwort deutlich länger, gib zuerst die Kurzfassung und biete die Ausführung an. Sage ich „ausführlich“, gilt das nicht.',
  'Der erste Satz steht im Grundtext, Kurzfassung und Stichwort „ausführlich“ nicht.')
g('Ohne Blabla:', 'Antwort', 'Prüffrage je Satz, Formel oder Beispiel vor Erklärung',
  'jeder Text, auch auf Blättern', IM, 'c gemeinsam.md „Sprache“ (nur im Projekt)', 'mittel', 'behalten', '',
  'Lehrer 06.11. ausdrücklich global gewollt (Register 06.11.4), im Bestell-Chat am 11.11. wieder eingefordert.',
  fund='plan.md Register 06.11.4 (Lehrer „ja, warum nicht global?“) · aufgabenbank/bau/rueckmeldung-bestellchat.md 11.11.: „verzichte auf Blabla“')
g('Kürzt du ein Ergebnis', 'Antwort', 'Nach dem Kürzen Gegenprobe gegen den alten Stand',
  'Text oder Ergebnis wird gekürzt', r'(Kürzung|gestrafft|Straffung|gekürzt)[^|]{0,160}(Kritiker|Prüfer|Gegenprobe|Zählung)|kuerzen-2026|gegenprobe\.py|runde-r',
  'nein', 'hoch', 'behalten', '', 'Zweimal ausgelöst (11.11., 14.11.), der Kritiker meldete am 11.11. 20 Befunde, darunter 6 fehlende Regeln.',
  fund='anweisungen 3b66144 (11.11.): „Entwurf Kürzung: Befund des Kritikers“ · plan.md §7: Runde R 14.11. mit blindem Prüfer')
g('Rückfragen:', 'Antwort', 'Rückfrage nur bei echter Mehrdeutigkeit, höchstens zwei, sonst Annahme',
  'unklarer Auftrag', IM, 'a (nur bei teurer Mehrdeutigkeit, sonst Annahme nennen)', 'gering', 'kürzen',
  'Rückfragen: Nur bei Mehrdeutigkeit, die das Ergebnis verändert, höchstens zwei; bei kleinen Lücken Annahme in einem Halbsatz.',
  'Bis auf „höchstens zwei“ (Register 11.11.3) steht alles im Grundtext.')
g('Gehe ich auf eine Rückfrage nicht ein', 'Antwort', 'Unbeantwortete Rückfrage nicht wiederholen, später mit Annahme zurückkommen',
  'Lehrer übergeht eine Frage', r'nicht (neu|erneut|wieder) fragen|unbeantwortet|(noch|Lehrer) ohne Antwort',
  'nein', 'mittel', 'behalten', '', 'Belegt in Übergaben („nicht erneut fragen“), schützt die Zeit des Lehrers.')
g('Einmal fragen:', 'Antwort', 'Festhaltbare Angabe einmal erfragen und eintragen',
  'Angabe über Schüler, Projekt oder Vorgabe fehlt', r'einmal (ge)?frag|Einmal fragen',
  'c bankblatt.md (nur im Bestell-Chat)', 'mittel', 'behalten', '', 'Lehrer 19.10. (Register 19.10.6), gilt in jedem Projekt.')
g('Fragezeichen:', 'Antwort', 'Ein Fragezeichen ist eine Frage, nicht ein Auftrag',
  'Satz mit Fragezeichen, der wie ein Auftrag klingt', r'Eine Frage ändert nichts|29\.10\.8|Fragezeichen',
  'c plan.md Linie 8 „Eine Frage ändert nichts“ (nur im Projekt)', 'mittel', 'behalten', '',
  'Am 29.10. zweimal trotz Regel verletzt, im Projekt seither per Werkzeug gesichert, außerhalb trägt nur dieser Satz.')
g('Keine Auswahlbuttons:', 'Antwort', 'Entscheidungen im Text, eine je Nachricht, keine Buttons',
  'jede Entscheidungsfrage', IM, 'nein (Grundtext bietet Knöpfe an, die Regel verbietet sie)', 'mittel', 'behalten', '',
  'Gegenregel zum Grundtext, ohne sie kommen die Knöpfe zurück.')
g('Iterative Arbeit:', 'Antwort', 'Beim Feilen nur den geänderten Abschnitt zeigen',
  'mehrere Runden an einem Text', None, 'nein', 'gering', 'streichen', '',
  'Kein Beleg im Archiv, in der Werkstatt gilt fast immer die Ausnahme (vollständig ausgeben). Zweifelsfall: Chats ohne Projekt sieht das Archiv nicht.')
g('Ausnahme: Was ich irgendwo einsetze', 'Antwort', 'Einzusetzende Texte nach jeder Änderung vollständig ausgeben',
  'Anweisung, Prompt oder Auftrag ändert sich', r'vollständig (als Block|aus)|zum Einsetzen|vom Lehrer eingesetzt|noch einzusetzen|In der App eingesetzt|Kopierschritt',
  'b mit Projekt „Betrieb“ (Prompt vollständig als Block)', 'mittel', 'behalten', '',
  'Bleibt als eigene Regel ohne das Wort „Ausnahme:“, wenn „Iterative Arbeit“ fällt, 12 Übergaben nennen Texte zum Einsetzen.')
g('Teure Aktionen ankündigen:', 'Handeln', 'Vor Aufwendigem ein Satz und Go, je Aktion',
  'Agenten, lange Läufe, Unumkehrbares', r'Go (des )?Lehrer|Lehrer[^|]{0,40}„(Go|go)|\bGo\b[^|]{0,40}(Auftrag|Schätzung)|braucht Go',
  'a teils (Unumkehrbares anhalten), b Projekt „Runden“', 'hoch', 'behalten', '', 'Trägt außerhalb der Werkstatt allein, Kontingentverlust über 1 Punkt möglich.')
g('Ohne Rückfrage: eine einzelne Suche', 'Handeln', 'Kleine Suchen und Änderungen ohne Rückfrage',
  'jede kleine Aktion', IM, 'a teils (anfangen statt fragen)', 'gering', 'behalten', '', 'Grenzt die Go-Regel ab, ohne sie wird sie zu streng gelesen.')
g('Qualität geht vor Aufwand:', 'Handeln', 'Sparsamsten gleich guten Weg wählen und in einem Satz begründen',
  'mehrere Wege mit verschiedenem Aufwand', r'Sparweg|sparsam|Sonnet statt|Skript statt|statt Modell',
  'b innerhalb global („Mittel“, „Kostenregel“)', 'gering', 'streichen', '', 'Sagt dasselbe wie „Mittel“ (billigstes Mittel, das die Qualität trägt) und die Kostenregel.')
g('Selbst machen:', 'Handeln', 'Was Werkzeuge können, selbst erledigen, ein Satz Meldung',
  'jede Handlung, die ein Werkzeug kann', IM, 'nein', 'hoch', 'behalten', '', 'Spart dem Lehrer Handgriffe in jedem Chat, 4 981 der 5 143 Commits im Fenster tragen die Claude-Zeile.')
g('Signalwort:', 'Handeln', '„Holger:“-Zeile mit Ort und Handlung, Link, Block darunter',
  'Lehrer muss selbst etwas tun', r'Holger:', 'c bankblatt.md nutzt sie', 'hoch', 'behalten', '',
  'Auch im Bestell-Chat in Gebrauch (bankblatt.md Zeile 23), sonst übersieht der Lehrer Handgriffe.')
g('Bei mehreren Handgriffen', 'Handeln', 'Mehrere Handgriffe: Übersicht, dann einer je Nachricht',
  'mehr als ein Handgriff des Lehrers', None, 'nein', 'mittel', 'behalten', '', 'Im Archiv nicht sichtbar, schützt vor Fehlbedienung, wenn der Lehrer Texte einsetzt.')
g('Was ich kopieren oder öffnen soll und noch brauche', 'Handeln', 'Kopiergut am Ende jeder Antwort wiederholen (Karte, Block, Seite)',
  'offenes Kopiergut oder Datei', r'Zum Kopieren|kopierbrett|Dateikarte',
  'a teils (Dateikarte), c bankblatt.md „Antworten“ (nur Bestell-Chat)', 'mittel', 'behalten', '',
  'Lehrer 11.11. („Scrollen ist die Hölle“), in beiden Projekten belegt.',
  fund='anweisungen/archiv/kandidaten-sortiert-2026-11-11.md (übernommen, Lehrer 11.11.) · blattbau/bankblatt.md „Antworten“ verweist auf global „Signalwort“')
g('Beim Umzug nennt die Übergabe', 'Handeln', 'Übergabe nennt Kopiergut, neuer Chat stellt es bereit',
  'Umzug mit offenem Kopiergut', r'Zum Kopieren[^|]{0,200}(Artefakt|Slug)|wieder bereit|im neuen Chat gebraucht',
  'nein', 'gering', 'verschieben', 'wege.md § Umzug (wird vor jeder Übergabe gelesen)',
  'Greift nur beim Schreiben der Übergabe, und dort wird wege.md § Umzug ohnehin gelesen.')
g('Alles ohne dieses Wort', 'Handeln', 'Ohne Signalwort nur Information',
  'jede Antwort', IM, 'nein', 'gering', 'behalten', '', 'Gibt dem Signalwort seine Schärfe.')
g('Dateien: Leg nichts', 'Handeln', 'Nichts selbstständig ablegen, Ablage anbieten',
  'Dokument entsteht in einem Chat ohne feste Ablage', None,
  'c Projektregeln und bankblatt.md regeln die Ablage selbst', 'gering', 'kürzen',
  'Dateien: Leg nichts selbstständig ab; ist etwas Aufbewahrenswertes entstanden, biete die Ablage in einem Satz an. Auf „ablegen“ gelten die Regeln des Projekts.',
  'Kein Beleg im Archiv, in beiden Projekten legt der Chat nach Projektregel selbst ab, der Rest reicht für Chats ohne Projekt.')
g('Kommentiertes PDF:', 'Handeln', 'Kommentare im PDF per Skript mit Stelle auslesen und ablegen',
  'Lehrer lädt kommentiertes PDF hoch', r'kommentierte[sn]? PDF|PDF-Kommentar|Kommentare? (aus|im|des) PDF|kommentare\.py|kommentiert vom Lehrer|-kommentiert-',
  'nein', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Form hält eine Runde“ (oder wege.md § Durchsicht)',
  'Alle Belege aus der Werkstatt, im Bestell-Chat kein Fall, dort kommentiert der Lehrer im Chat.', chat='Chat 1 von 3 im Fenster (dirigent 3, 20.10.), zwei vom 15.10.')
g('Zeigen: Bevor du mir', 'Handeln', 'Gerendert selbst ansehen, Probe statt beschriebener Varianten',
  'etwas wird dem Lehrer gezeigt', r'gerendert|Sichtprüfung|selbst ansehen|im Bild (geprüft|angesehen)',
  'a teils (Dokument öffnen und prüfen)', 'hoch', 'behalten', '', 'Gilt auch für jedes gelieferte Blatt im Bestell-Chat, am 20.10. fand nur der Blick ins Bild den Gitterfehler.',
  fund='mathe-nachhilfe/archiv/uebergabe-2026-10-20.md: „Gerenderte Ausschnitte selbst ansehen: Den Gitterfehler fanden weder Kritiker noch Nachbesserung“')
g('Zur Durchsicht baust du', 'Handeln', 'Durchsicht als A4-PDF mit roter Fragenspalte, Handy nach wege.md',
  'Muster oder Stichprobe zur Durchsicht', r'rote[rn]? Spalte|durchsicht_rot|Durchsicht[^|]{0,40}(PDF|A4)|durchsicht\.py',
  'c wege.md § Durchsicht am Handy (Teil)', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Runden“ (oder wege.md § Durchsicht)',
  'Durchsichten gibt es nur in der Werkstatt, der Bestell-Chat liefert Blätter ohne Fragenspalte.')
g('Chatstart im Projekt: (1)', 'Projekte und Umzug', 'Chatstart: Stand-Zeile der Anweisungen mit dem Repo vergleichen',
  'jeder Chatstart in einem Projekt', r'Stand-Zeile|global\.md[^|]{0,30}\((a|b|c|d|e|f)\)|in der Einstellung|Kopierschritt',
  'c bankblatt.md Kurz-Anweisung: „Der Chatstart der globalen Anweisung (…) entfällt hier“', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Chatstart“',
  'Der Bestell-Chat schaltet den Absatz ausdrücklich ab, nur verbessereBlätter hat eine Projektdatei im Repo.')
g('Nennt die Projektanweisung das Repo nicht', 'Projekte und Umzug', 'Projekt ohne Repo-Verweis: Kandidaten lesen, Verweissatz ausgeben',
  'Chatstart in einem Projekt, dessen Anweisung das Repo nicht nennt', r'Verweissatz', 'nein', 'gering', 'streichen', '',
  'Kein Fall im Fenster, beide laufenden Projekte nennen das Repo.')
g('(2) Mit Übergabe:', 'Projekte und Umzug', 'Chatstart mit Übergabe: einfach erklären, nächster Schritt, nichts neu aufrollen',
  'Chatstart mit uebergabe.md', r'in einfachen Worten|Chatstart \d+|Chatstart Werkstatt',
  'b mit Projekt „Chatstart“ (fünf Zeilen aus „Jetzt“ und „Offen“)', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Chatstart“, dort mit den fünf Zeilen zusammenlegen',
  'Eine Übergabe gibt es nur in verbessereBlätter, dort verlangen zwei Absätze zwei Eröffnungen.',
  fund='77 von 126 Übergaben tragen den Hinweis „Zuerst dem Lehrer in einfachen Worten erklären“ · anweisungen 6fa6da4 (24.10.)')
g('(3) Ohne Übergabe:', 'Projekte und Umzug', 'Chatstart ohne Übergabe: Bestand lesen, zitieren statt neu herleiten',
  'Chatstart in einem Projekt ohne Übergabe', None, 'b teils („Nachsehen statt erinnern“)', 'gering', 'kürzen',
  'Im Projekt ohne Übergabe: Sieh zuerst nach, was vorhanden ist; Dokumentiertes wird zitiert oder fortgeschrieben, nicht neu hergeleitet.',
  'Kein Fall im Archiv (verbessereBlätter hat immer eine Übergabe, der Bestell-Chat schaltet den Chatstart ab).')
g('Bevor du eine Datei als neue Fassung ausgibst', 'Projekte und Umzug', 'Neue Fassung mit der alten vergleichen, Gleiches nicht als Ersetzung ausgeben',
  'Datei wird als neue Fassung ausgegeben', None,
  'nein', 'mittel', 'behalten', '', 'Gilt für jede Datei, nicht nur am Chatstart (Kritiker 11.11., Befund 7), der Schlusssatz „In Chats ohne Projekt nichts davon“ entfällt mit (1) und (2).')
g('Kontextdisziplin:', 'Projekte und Umzug', 'Umzug von sich aus anbieten: Phase fertig, langer Lauf, Verlauf erledigt',
  'Phase endet, langer Lauf steht an', r'Umzug \d+|Umzug Werkstatt|Umzug [a-z0-9. ]*:|Übergabe neu',
  'b mit Projekt „Ein Chat zur Zeit“, b „Kontext klein“', 'hoch', 'behalten', '',
  'Der Auslöser muss in jedem Chat stehen (Register 11.11.3: ausgelagert ging das Angebot verloren), 126 Übergaben im Fenster.',
  chat='Chat 3 von 10 im Fenster echte Umzüge (22.10., 01.11., 14.11.), alle verbessereBlätter')
g('Einmal, mit Uhrzeit', 'Projekte und Umzug', 'Form des Angebots: einmal, Uhrzeit, Startwort als Codeblock, Übergabe gleich anlegen',
  'Umzugsangebot', r'Startwort|kopierbare[rsn]? (Block|Blase|Codeblock)|Umzugsangebot|Umzug (an)?geboten',
  'b mit Projekt „Ein Chat zur Zeit“ (wiederholen nur mit Grund)', 'mittel', 'verschieben', 'wege.md § Umzug (wird laut Kopf „bei jedem Umzugsangebot“ gelesen)',
  'Weil mit dem Angebot die Übergabe entsteht, liest der Chat wege.md § Umzug in diesem Moment ohnehin.')
g('Stichwort „Umzug“ (oder dein Umzugsangebot):', 'Projekte und Umzug', 'Umzug: Arbeitsdatei auf Stand, Übergabe in sechs Punkten, wege.md lesen',
  '„Umzug“ oder Umzugsangebot', r'Übergabe neu|^# Übergabe', 'c wege.md § Umzug führt die sechs Punkte und die stille Prüfung wortgleich', 'mittel', 'kürzen',
  'Stichwort „Umzug“ (oder dein Umzugsangebot): Lies `wege.md` § Umzug (`hz-0801/anweisungen`) und handle danach; ist er nicht lesbar, sag es.',
  'Die Liste steht wortgleich in der Datei, die an derselben Stelle Pflichtlektüre ist.')
g('Hat der Chat Schreibzugriff auf die Standdatei', 'Projekte und Umzug', 'Übergabe selbst ablegen, sonst „Holger:“-Zeile, Ende mit Startwort',
  'Übergabe ist geschrieben', r'Übergabe neu|uebergabe\.md neu',
  'nein', 'mittel', 'verschieben', 'wege.md § Umzug', 'Greift nur nach dem Lesen von wege.md § Umzug, im Fenster legte der Chat jede Übergabe selbst ab.')
g('Speichern: Sage ich', 'Projekte und Umzug', '„Speichern“ oder „druckfertig“: eigenständige Ergebnisfassung',
  'Stichwort „Speichern“ oder „druckfertig“', r'„Speichern“ (gesagt|verlangt)|Ergebnisfassung (erstellt|geliefert|abgelegt)',
  'nein', 'gering', 'streichen', '', 'Kein einziger Fall im Fenster. Zweifelsfall: Der Kritiker vom 11.11. zählte den Verlust außerhalb der Projekte als Befund.',
  chat='Chat 0 von 3 (alle drei Treffer sind eingefügter Anweisungstext)')
g('Ziel: Mein Abo-Kontingent', 'Kontingent', 'Kontingent bis zum Reset voll nutzen, Maß Kosten je abgenommenem Ergebnis',
  'Planung von Runden', r'bis zum Reset|Reset (Mo|\d)',
  'c modelle.md § 1 und § 4, plan.md § 7', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Kontingent“',
  'Runden werden nur in der Werkstatt geplant, der Bestell-Chat liefert aus dem Vorrat.')
g('Vorausplanen:', 'Kontingent', 'Rundenvorschlag nennt Stand der Woche, Schätzung, Rest bis Reset',
  'Rundenvorschlag', r'Rundenvorschlag|Vorschlag Runde|Schätzung[^|]{0,60}(Punkte|Mio)',
  'b mit Projekt „Runden“ (Vorschlag nennt Mittel, Aufwand, Schätzung)', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Runden“, mit dem Satz über den Vorschlag zusammenlegen',
  'Alle Rundenvorschläge im Fenster stammen aus der Werkstatt.')
g('Nach der Runde vergleichst du', 'Kontingent', 'Messwert gegen Schätzung, Abbruch nur auf Wort des Lehrers',
  'Runde ist fertig', r'mehr als die Hälfte|Abweichung [−+-]|geschätzt[^|]{0,40}(Mio|Punkte)|Schätzung war',
  'b mit Projekt „Kontingent“ (Abweichung über die Hälfte), c plan.md Linie 11', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Kontingent“, dort steht die Abweichungsregel schon',
  'In der Werkstatt doppelt, außerhalb kein Beleg, der Satz „Abgebrochen wird nur auf mein Wort“ zieht mit um.')
g('Mittel: Das billigste', 'Kontingent', 'Billigstes tragendes Mittel, Skript vor Modell, enge Aufträge, Pilot',
  'Wahl von Modell, Aufwand, Werkzeug', IM, 'c modelle.md § 3 und § 4a (Bedarfsdatei)', 'hoch', 'behalten', '',
  'Gilt auch für kleine Arbeiten im Bestell-Chat (Skript statt Modell), Kern der Sparsamkeit.')
g('Kostenregel:', 'Kontingent', 'Sparen in Wochenpunkten: Schwellen 0,5 und 3 Punkte, Sparweg vorlegen',
  'Auftrag mit spürbaren Kosten', r'Kostenregel|Sparweg',
  'c plan.md Register 14.11.15 (voller Wortlaut)', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Kontingent“',
  'Seit 14.11. in Kraft, also noch ohne Gebrauchsbeleg. Aufträge ab 0,5 Punkten entstehen nur in der Werkstatt, die längste Einzelregel läuft in jedem Bestell-Chat mit.')
g('Kontext klein:', 'Kontingent', 'Kurze Chats, frische Agenten, teuren Chat ansagen',
  'Chat wird lang oder läuft auf teurem Modell', r'teurer als nötig|Chat (auf|bleibt auf|läuft auf) (Opus|Fable|Sonnet|Aufwand|Hoch|Mittel|Extra|Max)|Aufwand des Chats|Chat-Aufwand',
  'b mit „Kontextdisziplin“ und Projekt „Ein Chat zur Zeit“, c modelle.md § 4a Nr. 5', 'mittel', 'kürzen',
  'Läuft der Chat teurer als nötig (Modell, Aufwand, Länge), sag es in einem Satz.',
  'Der erste Satz wiederholt Kontextdisziplin und modelle.md, der zweite gilt auch im Bestell-Chat.')
g('Nennen: In jedem Vorschlag', 'Kontingent', 'Je Lauf Mittel, Aufwand, Schätzung nennen, dazu Modell des Chats',
  'Vorschlag mit Läufen', r'(Opus|Fable( 5\.2)?|Sonnet),? (hoch|Hoch|mittel|Mittel|Extra hoch)',
  'b mit Projekt „Runden“, c modelle.md § 7', 'mittel', 'verschieben', 'Projekt verbessereBlätter „Runden“ (steht dort fast wörtlich)',
  'Dreifach vorhanden, Läufe schlägt nur die Werkstatt vor.')
g('Bei jedem neuen Modell und monatlich', 'Kontingent', 'Neubewertung bei neuem Modell und monatlich',
  'neues Modell oder Monatswechsel', r'Neubewertung|neues Modell|Fable 5\.2 erschienen',
  'b mit Projekt „Chatstart“ (Neubewertung zuerst), c modelle.md § 5', 'gering', 'streichen', '',
  'Zweimal ausgelöst (05.11., 09.11.), beide Male in der Werkstatt, deren Chatstart die Regel selbst trägt.')
g('Recherche: Was sich', 'Recherche und Recht', 'Aktuelles vor der Antwort recherchieren, Zeitloses nicht',
  'Frage nach Preisen, Versionen, Stand', r'Recherche|recherchier', 'a (fast wörtlich)', 'gering', 'streichen', '',
  'Der Grundtext verlangt dasselbe mit denselben Beispielen.', chat='Chat 2 von 3 im Fenster (18.10. Buchkauf, 31.10. Prüfungshefte)')
g('Recht: Prüf', 'Recherche und Recht', 'Recht: geltende Fassung prüfen, amtliche Quellen, Stand nennen',
  'Rechtsfrage', r'UrhG|Urheberrecht|Nutzungsbedingungen|Gesetz(estext|blatt)|Schulgesetz|DSGVO|Datenschutz',
  'nein (Grundtext verlangt die Fassungsprüfung ausdrücklich nicht)', 'hoch', 'kürzen',
  'Recht: Prüf, welche Fassung in Kraft ist (Inkrafttreten, Übergangsfristen); amtliche Quellen gehen vor Ratgebern; gib den Stand an und sag, wenn er unsicher ist.',
  'Im Fenster viermal Urheberrecht (§ 2, § 5, § 53, § 60a UrhG), eine veraltete Fassung wäre ein falsches Ergebnis. Der kürzere Wortlaut behält alle vier Pflichten.',
  chat='Chat 0 von 3 (alle drei Treffer sind eingefügter Anweisungstext)')
g('Meine Arbeitsregeln liegen', 'Anweisungs-Repo', 'Regeln liegen im Repo anweisungen, Dateien sind die Wahrheit',
  'Änderung oder Zweifel an einer Anweisung', r'global\.md|projekt-verbessereBlaetter\.md',
  'nein', 'mittel', 'kürzen', 'Meine Arbeitsregeln liegen in `hz-0801/anweisungen`; die Dateien sind die Wahrheit, die Einstellungen ihre Arbeitskopie mit Stand-Zeile.',
  'Die Dateiliste in Klammern nennt jeder Verweis selbst.')
g('Sag im laufenden Gespräch', 'Anweisungs-Repo', 'Projektübergreifend Nützliches als Kandidat vorschlagen, Eingang 14 Tage',
  'neue Festlegung, die überall nützen würde', r'kandidaten\.md|Kandidat(en)? (\d|für|in|sortiert|übernommen|verworfen)|Regelkandidat',
  'b mit Projekt „Chatstart“ (Eingang lesen), c kandidaten.md Kopf', 'gering', 'verschieben', 'Projekt verbessereBlätter „Chatstart“',
  'Alle Kandidaten im Fenster kamen aus der Werkstatt, der Bestell-Chat meldet über rueckmeldung-bestellchat.md.')

# ---------------------------------------------------------------- Projekt
p('**Rolle:**', 'Rolle', 'Ziel des Projekts, plan.md maßgeblich, Vorrat statt Einzelbestellung',
  'jede Antwort', IM, 'c plan.md § 1 Ziel', 'hoch', 'kürzen',
  '**Rolle:** Du baust mit mir Katalog und Aufgabenbank so aus, dass aus wenigen Wörtern in kurzer Zeit ein sehr gutes Blatt entsteht – Prüfungsblatt und Alltagsblatt –, und steuerst die ganze Arbeit an den Repos. Maßgeblich ist `plan.md` in `hz-0801/mathe-nachhilfe`. Hier entstehen Vorratsblätter (plan.md Linie 13), keine Einzelbestellungen; die bestelle ich in neu*erzeugeBlatt().',
  'Der Schlusssatz („Es gilt meine globale Anweisung …“) sagt, was ohnehin gilt.')
p('`hz-0801/mathe-nachhilfe` (plan.md', 'Repos', 'Die fünf Repos und was in ihnen liegt',
  'Chatstart, jede Ablage', IM, 'c teils (CLAUDE.md-Einstieg nennt die Regeldateien)', 'hoch', 'behalten', '', 'Ohne die Namen lassen sich die Repos nicht anhängen.')
p('Öffentlich sind `blattbau`', 'Repos', 'Öffentlich und privat getrennt, Namen und unfreier Wortlaut nur in -privat',
  'Ablage von Wortlaut oder Namen', r'-privat|Nummer statt Name|Namen? (nur|im Chat)',
  'c bankblatt.md (Namen, nur Bestell-Chat)', 'hoch', 'behalten', '', 'Lizenz- und Datenschutzgrenze, 1 485 Commits ins private Repo im Fenster.')
p('Fremder Wortlaut kommt erst', 'Repos', 'Fremder Wortlaut erst nach erfasster Lizenz öffentlich, Agenten zuerst privat',
  'fremde Quelle wird erfasst', r'Lizenz', 'nein', 'hoch', 'behalten', '', 'Lizenzbruch wäre nicht zurückzunehmen (Git-Geschichte).')
p('Einzelne Aufforderungssätze', 'Repos', 'Satzmuster dürfen in aufgabenbank, ganze Aufgaben bleiben privat',
  'Arbeit an satzmuster.csv', r'Satzmuster', 'c plan.md Register 29.10.7, aufgabenbank unterlage.py (Kopf)', 'gering', 'verschieben',
  'aufgabenbank bank.md (Anlass: Arbeit an Satzmustern), Register 29.10.7 bleibt',
  'Eine Erlaubnis: fehlt sie, bleibt der Chat strenger, kein Schaden. Die Grenze steht im Satz davor.')
p('Die Rangfolge der Regeldateien', 'Repos', 'Rangfolge in plan.md, abgelöste Regeldatei überall nachziehen',
  'Regeldatei wird abgelöst', r'bankblatt\.md[^|]{0,60}(nachgezogen|nachziehen)|CLAUDE\.md|Einstieg(e)? nach',
  'c plan.md § 0 und CLAUDE.md-Einstieg (Satz 1)', 'mittel', 'kürzen',
  'Wird eine Regeldatei abgelöst, im selben Zug `bankblatt.md` und die CLAUDE.md-Einstiege nachziehen.',
  'Satz 1 steht in plan.md § 0, das der Chatstart ganz liest, und in beiden CLAUDE.md.')
p('Zugriff: Zu Beginn', 'Repos', 'Repos selbst anhängen und klonen, Startwort',
  'Chatstart', r'Repos anhängen|Startwort', 'nein', 'hoch', 'behalten', '', 'Ohne den Absatz scheitert der Chatstart an der Rechteprüfung.')
p('Commit auf main', 'Repos', 'Commit auf main, vorher pull --rebase, Nachricht nennt den Anlass',
  'jeder Commit', IM, 'nein', 'hoch', 'behalten', '', 'Weicht vom Standard ab (kein Branch), parallele Agenten pushen ins selbe Repo.')
p('Rechner, Code-Tab, geplante Aufgaben', 'Repos', 'Verweis auf wege.md für Rechner, Code-Tab, Quellensuche',
  'Auftrag braucht Rechner, Code-Tab, Quellen', r'wege\.md', 'nein', 'gering', 'behalten', '', 'Der Verweis mit Anlass, den jede Bedarfsdatei braucht.')
p('Ein Chat führt alles, mit einer Übergabe', 'Ein Chat zur Zeit', 'Ein Chat, Umzug nach Phase, Maß ist die Chatlänge',
  'Phase endet, langer Lauf', r'Umzug \d+|Umzug Werkstatt|Chatlänge',
  'c plan.md Linie 10, b global „Kontextdisziplin“', 'mittel', 'kürzen',
  'Ein Chat führt alles, mit einer Übergabe `uebergabe.md`. Maß für den Umzug ist die Länge des Chats, nicht die Zahl der Agentenläufe und nicht die Uhrzeit: Ein fertiger Lauf bringt nur Auftrag und Schlussmeldung in den Chat, Wartezeit lässt ihn nicht wachsen.',
  '„Breite als Agentenrunde“ und „nach Phase und vor langem Lauf“ stehen in Linie 10 und global, eigen ist nur das Maß (Register 09.11.2).')
p('Angeboten wird der Umzug', 'Ein Chat zur Zeit', 'Angebot wiederholen nur mit Grund, neue Läufe erst nach dem Umzug',
  'wiederholtes Umzugsangebot', r'erst nach dem Umzug|nach dem Umzug (starten|gestartet|startet)|Umzug einmal anbieten',
  'b teils global „Kontextdisziplin“', 'mittel', 'behalten', '', 'Der Halbsatz „neue Läufe erst nach dem Umzug“ steht nur hier.')
p('Beim Umzug kommen die Schritte', 'Ein Chat zur Zeit', 'Umzugsschritte: Wirkort prüfen, Marken-Skript, Übergabe neu, Jetzt kürzen',
  'Umzug', r'Marken-Skript|Entscheidungsmarke', 'c wege.md § Umzug „Teil verbessereBlätter“ (ausführlicher)', 'hoch', 'kürzen',
  'Beim Umzug gilt zusätzlich `wege.md` § Umzug, Teil verbessereBlätter.',
  'Dieselben vier Schritte stehen ausführlicher in der Datei, die beim Umzug Pflichtlektüre ist.')
p('Repos anhängen. Lies in plan.md', 'Chatstart', 'Chatstart: plan.md-Abschnitte und Übergabe lesen, git log in einem Satz',
  'Chatstart', r'Chatstart', 'nein', 'hoch', 'behalten', '', 'Bestimmt die Arbeitsgrundlage jedes Chats.')
p('Nenne in höchstens fünf Zeilen', 'Chatstart', 'Fünf Zeilen: Schritt aus Jetzt, Offenes, über zwei Tage Liegendes ansprechen',
  'Chatstart', r'seit \d+ Tagen|länger als zwei Tage|liegt seit|> ?2 Tage',
  'b global „Chatstart (2)“, c plan.md Linie 10', 'mittel', 'behalten', '', 'Zielort für den globalen Absatz (2), beim Zusammenlegen eine Eröffnung statt zwei.')
p('Entscheidungen nimmst du aus dem Register', 'Chatstart', 'Entscheidungen aus dem Register, nie aus der Übergabe, Sortendatei ganz lesen',
  'Entscheidung wird gebraucht', r'nur aus dem Register|nie aus (dieser Datei|der Übergabe)',
  'b global „Nachsehen statt erinnern“, c Kopf jeder Übergabe (114 von 126) und plan.md § 0', 'gering', 'behalten', '',
  'Dreifach gedeckt, aber kurz, und der zweite Satz (Sortendatei ganz lesen) steht nur hier.')
p('Den Eingang von `kandidaten.md`', 'Chatstart', 'Kandidaten-Eingang lesen, Neubewertung der Modelle zuerst',
  'Chatstart', r'kandidaten\.md|Neubewertung|Fable 5\.2 erschienen', 'b global „Nennen“ und „Anweisungs-Repo“', 'mittel', 'behalten', '',
  'Wird zum einzigen Träger, wenn die globalen Doppel fallen.')
p('Bevor du etwas vorschlägst', 'Nachlesen, dann fragen', 'Vorschlag gegen Ziel und Linien prüfen, Besprochenes suchen',
  'jeder Vorschlag', r'Linie \d+', 'b teils global „Chatstart (3)“', 'hoch', 'behalten', '', 'Belegt in 30 Übergaben, verhindert Neuaufrollen.')
p('Fragen darfst du nur', 'Nachlesen, dann fragen', 'Nur fragen, was nur der Lehrer entscheiden kann',
  'jede Frage an den Lehrer', IM, 'b teils global „Rückfragen“, „Einmal fragen“', 'mittel', 'behalten', '', 'Strenger als global, Lehrer 15.10. „zu viele Fragen auf einmal“.')
p('Am Ende jedes Schritts nennst du', 'Erinnern', 'Am Schrittende drei Zeilen aus Offen, Erledigtes streichen, Neues eintragen',
  'Ende jedes Schritts', r'Offen:|Offen –|Offen nachgeführt|Offen gestr|in Offen', 'c plan.md Linie 10 (Satz 1)', 'mittel', 'behalten', '',
  '121 Commits führen „Offen“ nach, Satz 2 (eine Zeile je Punkt, selber Commit) steht nur hier.')
p('Ich entscheide Ziel, Sorten', 'Entscheidungen', 'Lehrer entscheidet Ziel und Form, Claude das Wie mit einem Satz',
  'jede Entscheidung', r'Wie innerhalb|Festlegung Claude|Entscheidung Claude|entscheidet Claude|\(Wie\)|Lesart Claude',
  'c teils plan.md § 0', 'hoch', 'behalten', '', 'Trennt die Zuständigkeit, belegt in Register und Befunden.')
p('Eingetragen wird mit Warum', 'Entscheidungen', 'Eintrag mit Warum, Beispiel, Grenze, Registerzeile, vorher nachsehen',
  'neue Entscheidung', r'Register \d\d\.\d\d\.\d+', 'c plan.md § 0 letzter Punkt (wörtlich)', 'gering', 'kürzen',
  'Eingetragen wird nach plan.md „Wie dieser Plan gilt“; vorher im Register nachsehen, ob es die Entscheidung schon gibt.',
  'Die Form steht wörtlich in plan.md § 0, das jeder Chatstart ganz liest. Die Regel greift am häufigsten (473 Commits) und verliert nichts.')
p('Erst bauen, dann ändern:', 'Entscheidungen', 'Offene Form vorläufig bauen und als Muster vorlegen',
  'offene Formfrage', r'vorläufig|erst bauen', 'nein', 'mittel', 'behalten', '', 'Spart Abfragen vorab, mit Kostengrenze.')
p('Form hält eine Runde:', 'Entscheidungen', 'Kommentare in befunde-M sammeln, Form am Rundenende, sofort nur Handwerk',
  'Kommentar des Lehrers zu einem Blatt', r'befunde-M\d', 'c plan.md Linie 8 (fast wörtlich)', 'gering', 'kürzen',
  'Form hält eine Runde (plan.md Linie 8): Kommentare zu Blättern nach `bau/befunde-M<n>.md`, Formänderung als ein Vorschlag mit Wegen am Ende der Runde.',
  'Linie 8 trägt Wortlaut und Begründung und wird beim Chatstart ganz gelesen, eigen ist nur „als ein Vorschlag mit Wegen“.')
p('Eine Antwort auf einen Kommentar', 'Entscheidungen', 'Antwort ist keine Regel, Tendenz erst mit dem zweiten Blatt',
  'Kommentar des Lehrers', r'Tendenz|zweite[mn]? Blatt|Lösungsidee', 'b global „Richtungen“, c plan.md Linie 8 („Wie aus Kommentaren eine Regel wird“)', 'gering', 'streichen', '',
  'Global „Richtungen“ und Linie 8 sagen dasselbe, Linie 8 strenger (Anlass an zwei Themen).')
p('Eine Runde läuft vom Go', 'Runden', 'Runde: Bau, blinder Kritiker, Nachbesserung, Neusatz, Prüfskripte',
  'jede Runde', r'Kritiker|blind', 'nein', 'hoch', 'behalten', '', 'Der Qualitätsweg, in 319 Commits belegt.')
p('Der Vorschlag nennt je Lauf', 'Runden', 'Vorschlag nennt Mittel, Aufwand, Schätzung, Wanduhr, Rückkehrzeit, Messlatte',
  'Rundenvorschlag', r'Wanduhr|Gelingen|Scheitern|Rundenvorschlag|Vorschlag Runde',
  'b global „Nennen“, „Vorausplanen“', 'hoch', 'behalten', '', 'Zielort für die globalen Sätze, eigen sind Wanduhr, Rückkehrzeit und Messlatte.')
p('Ein Agent startet erst nach meinem Go', 'Runden', 'Agent erst nach Go auf Auftrag und Schätzung',
  'Start eines Agenten', r'Go (des )?Lehrer|Lehrer[^|]{0,40}„(Go|go)|\bGo\b[^|]{0,40}(Auftrag|Schätzung)|braucht Go',
  'b global „Teure Aktionen“, c plan.md Linie 10', 'hoch', 'behalten', '', 'Der Zusatz „ein mitgemeintes Ja reicht nicht“ steht nur hier, Kontingentverlust über 1 Punkt.')
p('Bündeln, was ohne mich', 'Runden', 'Bündeln, Pilot vor Breite, Pilot Zeile für Zeile gegen das Muster',
  'neue Form oder neue Kosten', r'Pilot', 'b teils global „Mittel“ (Pilot, dann Breite)', 'hoch', 'behalten', '',
  '306 Commits nennen einen Piloten, „Skript 0 Fehler reicht nicht“ steht nur hier.')
p('Freigabe bis zum Reset:', 'Runden', '„selbstständig“: Vorrats- und Nachbesserungsrunden ohne Go je Runde',
  'Lehrer sagt „selbstständig“', r'selbstst[aä]ndig|Freigabe', 'nein', 'hoch', 'behalten', '', 'In Übergaben und Plan belegt (22.10., 08.11., beendet 09.11.), begrenzt die Freigabe.')
p('Piloten unter einem Wochenpunkt', 'Runden', 'Piloten unter 1 Punkt ohne Go (Ultra), höchstens 2 je Woche',
  'Pilot unter 1 Wochenpunkt', r'Piloten? (unter|ohne Go)|14\.11\.14', 'c plan.md § 4 Jetzt (Rahmen, zeitweise)', 'hoch', 'behalten', '',
  'Seit 14.11. in Kraft (Register 14.11.14), noch ohne Gebrauchsbeleg, trägt die Grenze „Breite nie ohne Go“.')
p('Agenten: Die gemeinsamen Regeln', 'Runden', 'Auftragsdatei im Scratchpad, je Agent eigener Klon und ein Thema',
  'Vorbereitung einer Agentenrunde', r'eigener Klon|Klone? /home|agenten/|Auftragsdatei',
  'c teils modelle.md § 4a Nr. 1', 'hoch', 'verschieben', 'wege.md, neuer § Agentenrunde (Anlass: bevor die Auftragsdatei einer Runde entsteht)',
  'Handwerk mit klarem Anlass. Zweifelsfall: Schaden hoch, wenn der Verweis nicht gelesen wird, und 111 von 126 Übergaben nennen Läufe, die Ersparnis träfe also wenige Chats ganz.')
p('Commit nach jedem Teilschritt', 'Runden', 'Agent: Commit je Teilschritt, Zwischenstände sichern, harte Uhrzeit',
  'Agent läuft länger', r'Zwischenst[aä]nd|harte Uhrzeit|Neustart', 'nein', 'hoch', 'verschieben', 'wege.md, neuer § Agentenrunde',
  'Gehört in die Auftragsdatei der Runde, zieht mit dem Satz davor um oder bleibt mit ihm.')
p('Ein Agent weist die Wirkung', 'Runden', 'Wirkung am Ergebnis nachweisen, Werkzeug prüft Formregel und hält an',
  'Agent meldet fertig', r'(?-i:HALT)|hält an|stille[rn]? Verlust|Neusatz', 'a teils (letzter Schritt ist die Prüfung)', 'hoch', 'verschieben', 'wege.md, neuer § Agentenrunde',
  'Wie die beiden Sätze davor, als Block.')
p('Vor jeder Änderung prüfst du', 'Runden', 'Vor Änderung prüfen, ob die Datei erzeugt wird, dann Quelle ändern',
  'jede Änderung an einer Datei', r'wird erzeugt|erzeugte Datei|neu erzeugt|von Hand geändert|Quelle geändert|Erzeugte Dateien', 'nein', 'hoch', 'behalten', '',
  'Gilt ausdrücklich auch im Chat, eine Handänderung an erzeugter Datei geht beim nächsten Lauf still verloren.')
p('Agenten führen aus, das Urteil', 'Runden', 'Urteil bleibt im Chat, Lehrer sieht Muster und Stichprobe, Setzer ohne Modell',
  'jede Runde', r'Stichprobe', 'c plan.md Linie 7 und Linie 2 (Satz 2 und 3)', 'gering', 'kürzen',
  'Agenten führen aus, das Urteil bleibt im Chat.', 'Muster und Stichprobe sind Linie 7, Setzer ohne Modell ist Linie 2, beide liest der Chatstart.')
p('Kontingent: Modelle nach', 'Runden', 'Modelle nach modelle.md, Schätzung nur mit den Faustwerten aus plan.md',
  'Schätzung einer Runde', r'Faustwert', 'c plan.md § 7 Kopf (Regeln der Tabelle)', 'mittel', 'kürzen',
  'Kontingent: Modelle nach `modelle.md` (Fable nur nach § 3). Schätzungen rechnest du mit den Faustwerten oben in plan.md „Kontingent“ (Regeln dort), Chat-Antworten eingerechnet.',
  'Wie die Tabelle gepflegt wird, steht in ihrem Kopf.')
p('Vor und nach jeder Runde fragst du', 'Runden', 'Nutzungsanzeige vor und nach jeder Runde, Messung eintragen',
  'Beginn und Ende jeder Runde', r'Nutzungsanzeige|Anzeige (vorher|nachher|\d\d\.\d\d\.)|Woche \d+ ?%',
  'b global „Vorausplanen“ (Abweichung), c plan.md Linie 11', 'hoch', 'behalten', '', '122 Zeilen mit Anzeige in plan.md, ohne sie keine Faustwerte.')
p('Wege tragen Namen', 'Antworten', 'Wege mit Namen, Fachwörter nach begriffe.md, Befunde wie am Tisch',
  'jede Antwort', IM, 'nein', 'mittel', 'behalten', '', '„Weg A/B“ in 176 Commits, der Lehrer antwortet damit.')
p('Aufbau jeder Nachricht:', 'Antworten', 'Aufbau: Antwort zuerst, eine Entscheidung, „Bei dir“, Hintergrund eine Zeile',
  'jede Antwort', IM, 'b überlagert global „Antwortaufbau“', 'hoch', 'behalten', '', 'Lehrer 14.11. (Register 14.11.15), er liest von oben und kommentiert.')
p('Zwischenmeldungen nur', 'Antworten', 'Keine Zwischenmeldungen, eine Meldung je Runde, Stand in der Aufgabenliste',
  'Agenten laufen', r'Zwischenmeldung|Aufgabenliste|eine Meldung je Runde', 'a teils (Aufgabenliste, kaum Erzählung)', 'mittel', 'behalten', '',
  'Lehrer 26.10. „weg a“, jede Zwischenmeldung kostet einen Chat-Schritt.')
p('Blätter bestelle ich in neu*erzeugeBlatt()', 'Betrieb', 'Bestellt wird in neu*erzeugeBlatt() und den alt*-Projekten',
  'Frage zum Betrieb', r'alt\*erzeuge|neu\*erzeugeBlatt|Bestell-?[Cc]hat', 'b Rolle (bestellt wird in neu*erzeugeBlatt())', 'gering', 'kürzen',
  'Blätter bestelle ich in neu*erzeugeBlatt() (Prompt `blattbau/bankblatt.md`), bis es alles kann auch in den alt*-Projekten.',
  'Der Nebensatz über den Absatz „Lieferliste“ ist Bestandsnotiz, keine Regel.')
p('Wer was bekam', 'Betrieb', 'Lieferliste lesen, bevor über einen Schüler geurteilt wird',
  'Urteil oder Blatt für einen Schüler', r'lieferungen\.csv|geliefert\.py|Lieferliste', 'nein', 'hoch', 'behalten', '',
  'Ohne die Liste urteilt der Chat über Blätter, die der Schüler nie bekam.')
p('Ändert sich ein Prompt', 'Betrieb', 'Geänderten Prompt vollständig als Block, ins Repo per Commit',
  'Prompt ändert sich', r'bankblatt\.md v\d+|vollständig als Block', 'b global „Iterative Arbeit“ (Ausnahme)', 'gering', 'streichen', '',
  'Doppelt mit global, für bankblatt.md seit Register 10.11.10 überholt („eine Änderung ist ein Commit, kein Einfügen“).')
p('Kann neu*erzeugeBlatt() die', 'Betrieb', 'Melden, wenn ein altes Bestellprojekt archiviert werden kann',
  'neu*erzeugeBlatt() deckt ein altes Projekt ab', r'archivieren\?|altes? Projekt archiv', 'nein', 'gering', 'verschieben', 'plan.md „Offen“ (eine Zeile, einmaliger Anlass)',
  'Eine Erinnerung für einen einmaligen Moment, keine Regel für jeden Schritt.')

# ---------------------------------------------------------------- Zerlegung und Zeichen
def zerlege(text, regeln):
    pos = []
    for x in regeln:
        assert text.count(x['anker']) == 1, ('Anker nicht eindeutig', x['anker'], text.count(x['anker']))
        pos.append(text.index(x['anker']))
    assert pos == sorted(pos), 'Reihenfolge der Anker'
    assert pos[0] == 0, ('Text vor der ersten Regel', text[:60])
    for i, x in enumerate(regeln):
        x['text'] = text[pos[i]:(pos[i + 1] if i + 1 < len(regeln) else len(text))].strip()
        x['zeichen'] = len(x['text'])
RG = [x for x in R if x['datei'] == 'global']; RP = [x for x in R if x['datei'] == 'projekt']
zerlege(G, RG); zerlege(P, RP)
for i, x in enumerate(RG, 1): x['id'] = f'G{i:02d}'
for i, x in enumerate(RP, 1): x['id'] = f'P{i:02d}'

# ---------------------------------------------------------------- Belege
def kurz(o, m):
    t = o['text'].replace('\n', ' ').replace(';', ',')
    if o['q'] == 'C' and m.end() <= 115:
        s = t[:115] + ('…' if len(t) > 115 else '')
    else:
        a = max(0, m.start() - 40); a = t.rfind(' ', 0, a) + 1 if a else 0
        e = min(len(t), m.end() + 55); e = t.find(' ', e) if t.find(' ', e) > 0 else len(t)
        s = ('…' if a else '') + t[a:e].strip() + ('…' if e < len(t) else '')
    return f"{o['ort']}: „{s}“"
for x in R:
    if x['muster'] == IM:
        x['treffer'] = 'immer'; x['fundauto'] = ''
    elif x['muster'] is None:
        x['treffer'] = '0 Treffer (Auslöser im Archiv nicht sichtbar)'; x['fundauto'] = ''
    else:
        rx = re.compile(x['muster'], re.I | re.S); c = Counter(); ex = {}
        for o in KORPUS:
            m = rx.search(o['text'])
            if m:
                c[o['q']] += 1; ex.setdefault(o['q'], kurz(o, m))
        x['zahl'] = sum(c.values())
        if not c: x['treffer'] = '0 Treffer'
        else: x['treffer'] = ' · '.join(f'{NAME[q]} {c[q]}' for q in 'CURJBK' if c[q])
        x['fundauto'] = ' · '.join(ex[q] for q in 'CURJBK' if q in ex)[:1] and ' · '.join([ex[q] for q in 'CRUJBK' if q in ex][:2])
    if x['chat']: x['treffer'] += ' · ' + x['chat']

# ---------------------------------------------------------------- Ersparnis
STUB = {'Einmal, mit Uhrzeit': 60, 'Agenten: Die gemeinsamen Regeln': 115, 'Kann neu*erzeugeBlatt() die': 0}
for x in R:
    e = x['empf']; z = x['zeichen']
    if e == 'behalten': x['spar'] = 0
    elif e == 'streichen': x['spar'] = z
    elif e == 'kürzen': x['spar'] = z - len(x['neu']); assert x['spar'] > 0, (x['id'], x['spar'])
    elif e == 'verschieben': x['spar'] = z - STUB.get(x['anker'], 0)
feld = lambda s: re.sub(r'\s+', ' ', str(s)).replace(';', ',').strip()
with open(f'{H}/runde-a/regeln.csv', 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    w.writerow('kennung;datei;abschnitt;kern;zeichen;ausloeser;treffer_4w;fundstellen;doppelt;schaden;empfehlung;grund'.split(';'))
    for x in R:
        e = x['empf']
        if e == 'kürzen': emp = f"kürzen (−{x['spar']}) auf: {x['neu']}"
        elif e == 'verschieben': emp = f"verschieben (−{x['spar']}) nach: {x['neu']}"
        elif e == 'streichen': emp = f"streichen (−{x['spar']})"
        else: emp = 'behalten'
        dat = 'global.md' if x['datei'] == 'global' else 'projekt-verbessereBlaetter.md'
        assert len(x['kern'].split()) <= 12, (x['id'], x['kern'])
        # Wortlaut der Vorschlaege bleibt unveraendert (Semikolon inklusive, Feld dann in Anfuehrungszeichen)
        w.writerow([feld(v) for v in (x['id'], dat, x['abschnitt'], x['kern'], x['zeichen'], x['ausl'], x['treffer'],
                                      x['fund'] or x['fundauto'], x['doppelt'], x['schaden'])] + [re.sub(r'\s+', ' ', emp).strip(), feld(x['grund'])])

def summe(regeln):
    s = defaultdict(lambda: [0, 0])
    for x in regeln:
        k = x['empf']
        if k == 'verschieben':
            k = 'verschieben → Projekt' if 'Projekt verbessereBlätter' in x['neu'] else 'verschieben → Bedarfsdatei/Plan'
        s[k][0] += 1; s[k][1] += x['spar']
    return {k: v for k, v in s.items()}
aus = dict(global_zeichen=sum(x['zeichen'] for x in RG), global_roh=G_ROH, global_kopf=G_KOPF,
           projekt_zeichen=sum(x['zeichen'] for x in RP), projekt_roh=P_ROH, projekt_kopf=P_KOPF,
           global_=summe(RG), projekt_=summe(RP),
           zu_projekt=[(x['id'], x['zeichen']) for x in RG if x['empf'] == 'verschieben' and 'Projekt verbessereBlätter' in x['neu']],
           regeln=len(R), n_global=len(RG), n_projekt=len(RP))
json.dump(aus, open(f'{H}/runde-a/belege/summen.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(aus, ensure_ascii=False, indent=1))
if '-v' in sys.argv:
    for x in R: print(x['id'], x['zeichen'], x['empf'], x['spar'], '|', x['treffer'][:90], '|', (x['fund'] or x['fundauto'])[:150])

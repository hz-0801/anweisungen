# Auftrag kandidaten – drei Regeln nachtragen

## Ausgangslage

Ordner anweisungen. kandidaten.md sammelt Regeln, die
projektübergreifend gelten könnten. Aus der Werkstatt
verbessereBlaetter() kommen drei neue Blöcke; einer davon
ersetzt einen bestehenden.

git über die git.exe von GitHub Desktop:
C:\Users\holge\AppData\Local\GitHubDesktop\app-3.6.5\resources\app\git\cmd\git.exe

## Schritte

1. Entferne in kandidaten.md den Block „## Fragen am
   betroffenen Absatz" vollständig – er hat in der Praxis dazu
   geführt, dass Fragen im Text untergingen und mehrere
   Entscheidungen in einer Nachricht standen.

2. Häng die drei Blöcke unten aus diesem Auftrag ans Ende von
   kandidaten.md an, im Format der Datei (Regel, Grund,
   Herkunft, Reife), durch Leerzeile getrennt.

3. Setz beim Block „## Aufträge als Datei, nicht als Chat-Block"
   die Reife auf „erprobt in verbessereBlaetter()" – die Form
   ist am 22.09. viermal gelaufen.

4. Verschiebe auftrag-kandidaten.md nach archiv/, mit dem Datum
   im Namen (auftrag-kandidaten-2026-09-22.md), falls es dort
   schon eine gleichnamige Datei gibt. Committe alles mit der
   Nachricht „Kandidaten: Frage als letzte Zeile, alternde
   Referenz, datierte Archivnamen". Nicht pushen.

## Die drei Blöcke

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

## Prüfungen

- kandidaten.md enthält den Block „Fragen am betroffenen
  Absatz" nicht mehr und die drei neuen Blöcke vollständig.
- Die übrigen Blöcke sind unverändert; git diff zeigt keine
  Änderung außer den beschriebenen.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief.
Dann in vier Zeilen: was entfernt, was angehängt, was an der
Reife geändert, was committet wurde, plus Abweichungen.
Letzte Zeile: Push origin drücken.

## Regeln

- Lösche nichts außer dem genannten Block.
- Ändere keine andere Datei.
- Berichte, was war, auch wenn es scheiterte.

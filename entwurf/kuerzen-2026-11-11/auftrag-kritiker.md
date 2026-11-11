# Auftrag Kritiker – Gegenprobe zur gekürzten globalen Anweisung (blind)

Du prüfst eine Kürzung, die du nicht gebaut hast. Leser aller Texte ist ein Claude-Chat, der sie als
Arbeitsanweisung bekommt. Arbeite nur lesend; einzige Ausgabe ist `befund-kritiker.md` in diesem Ordner.

Alt (maßgeblich): `../../global.md`, ab der Zeile „Stand: 2026-11-11 (b)“.
Neu: `global-kurz-B.md` (käme in die Einstellung), `umzug.md` (neue Datei im Repo, vom Chat beim Start im
Projekt und beim Stichwort „Umzug“ gelesen), `modelle-nachtrag.md` (Ergänzung für `../../modelle.md` § 7).
Bestand, in dem Ausgelagertes schon stehen soll: `../../modelle.md`, `../../kandidaten.md`,
`../../projekt-verbessereBlaetter.md`.

1. Verlust: Geh die alte Fassung Regel für Regel durch – jede einzelne Handlungsanweisung, auch Halbsätze,
   Ausnahmen, Grenzen, Signalwörter und Stichwörter. Melde nur, was nicht unverändert wiederzufinden ist:
   steht woanders (Datei, Abschnitt) · abgeschwächt oder verschärft (wie) · fehlt.
2. Bedeutung: Stellen, an denen der neue Wortlaut mehr oder weniger verlangt als der alte.
3. Frischer Leser: Stellen in `global-kurz-B.md` und `umzug.md`, die ohne Vorwissen mehrdeutig sind, sich
   widersprechen oder ins Leere verweisen (Dateien oder Abschnitte, die es nicht gibt).
4. Auslagerung: Was fehlt einem Projekt-Chat, der `umzug.md` nicht lesen kann? Reicht die Notfassung in
   `global-kurz-B.md` „Stichwort Umzug“?

Nicht: Stil bewerten, neue Regeln vorschlagen, Dateien ändern. `gegenprobe.py` darfst du laufen lassen
(Aufruf im Kopf); es ersetzt das Lesen nicht. Schrittgrenze: 25 Werkzeugaufrufe.

Ausgabe `befund-kritiker.md`, höchstens 60 Zeilen: je Befund eine Zeile – Nr. · Art (fehlt / verändert /
woanders / unklar / Verweis) · Stelle alt (Zitat bis 12 Wörter) · Stelle neu · ein Satz, was der Leser dadurch
anders täte. Am Ende eine Zeile: Zahl der Befunde je Art und dein Urteil in einem Satz.

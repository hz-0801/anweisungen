# anweisungen

Arbeitsregeln für Claude: globale Anweisung, Regelkandidaten,
Projektanweisungen. Öffentlich, damit jeder Chat die Dateien per
Raw-URL lesen kann:
`https://raw.githubusercontent.com/hz-0801/anweisungen/main/<datei>`

## Dateien

- `global.md` – Wortlaut der globalen Anweisung (Einstellungen →
  Profil). Die Einstellungen sollen diesem Stand entsprechen; wer
  eine Abweichung findet, sagt es. Der kopierbare Text beginnt mit
  einer Stand-Zeile; Claude vergleicht sie beim Projektstart mit
  der Einstellung.
- `kandidaten.md` – Regeln, die sich in einem Projekt bewährt haben
  und projektübergreifend gelten könnten, mit Reifestufe.
- `projekt-<name>.md` – Projektanweisungen, je Projekt eine Datei,
  versioniert. Die Projekteinstellung soll dem Stand entsprechen.
  Der kopierbare Text beginnt mit einer Stand-Zeile; Claude
  vergleicht sie beim Projektstart mit der Einstellung.
- `archiv/` – erledigte Aufträge.

## Mechanismus

Ort: diese Dateien. Auslöser: (1) Im Chat entsteht eine Regel;
Claude formuliert den Block, der Lehrer entscheidet mit einem Wort.
(2) Beim Umzug eines Projekts prüft die Übergabe, ob Entscheidungen
projektübergreifend sind; Kandidaten kommen hierher. (3) Beim ersten
Chat eines Projekts, dessen Anweisung dieses Repo nicht nennt, liest
Claude `kandidaten.md` und sagt, was fehlt.

Reife: Kandidat (aus einem Projekt) → erprobt (in einem zweiten
Projekt bewährt) → global (in `global.md` übernommen, Block bleibt
mit Datum stehen). Rhythmus: einmal im Quartal oder ab zehn
Kandidaten durchsehen; was aufsteigt, ersetzt in der Regel etwas –
die globale Anweisung soll schärfer werden, nicht länger.

## Verweis in Projektanweisungen

„Lies beim Chatstart `kandidaten.md` aus `hz-0801/anweisungen` und
sag in einem Satz, ob eine Regel daraus für dieses Projekt fehlt.
Beim Umzug: Regeln, die projektübergreifend gelten, als Blöcke für
`kandidaten.md` in einem eigenen Textblock für den Ordner
`anweisungen` ausgeben."

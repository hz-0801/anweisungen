# anweisungen

Arbeitsregeln für Claude: globale Anweisung, Regelkandidaten,
Projektanweisungen. Öffentlich, damit jeder Chat die Dateien per
Raw-URL lesen kann:
`https://raw.githubusercontent.com/hz-0801/anweisungen/main/<datei>`

## Dateien

- `global.md` – Wortlaut der globalen Anweisung (Einstellungen →
  Profil). Die Einstellungen sollen diesem Stand entsprechen; wer
  eine Abweichung findet, sagt es.
  Der kopierbare Text beginnt mit einer Stand-Zeile; der Chat des Projekts
  verbessereBlätter vergleicht sie beim Start mit der Einstellung.
- `kandidaten.md` – Eingang: offene Regelvorschläge der letzten 14
  Tage; der Bestand bis 19.10.2026 liegt in
  `archiv/kandidaten-bis-2026-10-19.md`.
- `modelle.md` – Modellleiter, Messwerte, Zurücksetzungen, Anzeige ablesen,
  Umzug rechnen. `wege.md` – Rechner, Code-Tab, geplante Aufgaben,
  Quellensuche, Durchsicht am Handy.
- `projekt-<name>.md` – Projektanweisungen, je Projekt eine Datei,
  versioniert. Die Projekteinstellung soll dem Stand entsprechen.
  Der kopierbare Text beginnt mit einer Stand-Zeile; Claude
  vergleicht sie beim Projektstart mit der Einstellung.
- `archiv/` – erledigte Aufträge.

## Mechanismus

Ort: diese Dateien. Auslöser: (1) Im Chat entsteht eine Regel;
Claude formuliert sie, der Lehrer entscheidet mit einem Wort.
(2) Beim Umzug kommen nur Regeln, die in keiner Regeldatei stehen,
als Zeile in den Eingang von `kandidaten.md`. Übernommen wird auf
Lehrerwort; die globale Anweisung soll schärfer werden, nicht
länger.

## Verweis in Projektanweisungen

„Lies beim Chatstart den Eingang von `kandidaten.md` aus
`hz-0801/anweisungen` und sag in einem Satz, ob ein Vorschlag daraus
für dieses Projekt gilt. Beim Umzug: Regeln, die projektübergreifend
gelten und in keiner Regeldatei stehen, als Zeile für den Eingang
ausgeben."

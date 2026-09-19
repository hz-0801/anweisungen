# Auftrag: Stand-Zeile und Abgleichregel

## Ausgangslage

`global.md` und `projekt-verbessereBlaetter.md` tragen ihr Datum nur
im Kopf oberhalb der Trennlinie; der Text unterhalb wird in die
Einstellungen kopiert und ist dort ohne Datum. Beide bekommen eine
Stand-Zeile als erste Zeile des kopierbaren Textes, und der Zusatz
„Anweisungs-Repo" in `global.md` bekommt die Abgleichregel.

## Schritte

1. In `global.md` unmittelbar nach der Trennlinie `---` und der
   folgenden Leerzeile als erste Textzeile einfügen:
   `Stand: 2026-09-19`
   danach eine Leerzeile, dann der bisherige Text ab „Rangfolge".

2. In `global.md` den Absatz „Anweisungs-Repo:" durch diesen
   ersetzen (wortgleich):

   Anweisungs-Repo: Meine Arbeitsregeln liegen in
   `hz-0801/anweisungen` (`global.md`, `kandidaten.md`,
   `projekt-<name>.md`); die Dateien sind die Wahrheit, die
   Einstellungen ihre Arbeitskopie mit Stand-Zeile. Beginnt ein
   Chat in einem Projekt, lies `global.md` und, falls vorhanden,
   die `projekt-<name>.md` dieses Projekts per Raw-URL; ist ein
   Stand dort jünger als der in der Einstellung, sag es in einem
   Satz und nenne den Kopierschritt. Nennt die Projektanweisung
   das Repo nicht, lies zusätzlich `kandidaten.md`, sag in einem
   Satz, welche Regeln daraus für dieses Projekt fehlen, und gib
   den Verweissatz für die Projektanweisung aus. In Chats ohne
   Projekt nichts davon. Sag im laufenden Gespräch, wenn eine
   Festlegung projektübergreifend nützlich wäre; ich entscheide
   mit einem Wort, ob sie in `kandidaten.md` kommt.

3. In `projekt-verbessereBlaetter.md` unmittelbar nach der
   Trennlinie `---` und der folgenden Leerzeile als erste
   Textzeile einfügen:
   `Stand: 2026-09-19`
   danach eine Leerzeile, dann der bisherige Text ab „**Rolle:**".

4. In `README.md` unter „## Dateien" beim Punkt `global.md` und
   beim Punkt `projekt-<name>.md` jeweils anfügen: „Der kopierbare
   Text beginnt mit einer Stand-Zeile; Claude vergleicht sie beim
   Projektstart mit der Einstellung."

5. Diese Auftragsdatei nach `archiv/auftrag-stand-2026-09-19.md`
   verschieben (git mv).

6. Ein Commit: „Stand-Zeile und Abgleichregel".

## Prüfungen

- `global.md` und `projekt-verbessereBlaetter.md`: die erste
  nichtleere Zeile nach `---` ist `Stand: 2026-09-19`.
- `global.md` enthält den Absatz „Anweisungs-Repo:" genau einmal,
  mit dem Wort „Arbeitskopie".
- UTF-8, LF, kein BOM.

## Bericht (zurück in den Chat)

- Zeilennummern der Änderungen je Datei.
- Commit-Hash.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Sonst nichts ändern.
- Bei Unklarheit die einfachste Lesart wählen und im Bericht
  nennen, nicht rückfragen.

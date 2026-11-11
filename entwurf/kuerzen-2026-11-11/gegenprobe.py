"""Gegenprobe per Skript: Jeder Satz des alten Stands von global.md muss in der neuen Fassung oder in einer der
Zieldateien wiederzufinden sein. Je alter Satz: Anteil seiner Inhaltswörter (ab 4 Buchstaben), die in einem
einzigen Absatz des neuen Bestands vorkommen. Gemeldet wird, was unter der Schwelle liegt – das sieht ein Mensch
bzw. der Kritiker an. Aufruf: python3 -I gegenprobe.py <alt.md> <schwelle> <neu1.md> [<neu2.md> …]"""
import re, sys
from pathlib import Path

alt = Path(sys.argv[1]).read_text(encoding='utf-8').split('\n---\n', 1)[-1]
schwelle = float(sys.argv[2])
woerter = lambda s: {x for x in re.findall(r'[a-zäöüß]{4,}', s.lower())}

absaetze = []
for pfad in sys.argv[3:]:
    for a in re.split(r'\n\s*\n', Path(pfad).read_text(encoding='utf-8')):
        absaetze.append((Path(pfad).name, woerter(a)))

flach = ' '.join(l for l in alt.split('\n') if not l.startswith('## ') and not l.startswith('Stand:'))
flach = re.sub(r'\s+', ' ', flach)
saetze = [s.strip() for s in re.split(r'(?<=[.?!])\s+(?=[A-ZÄÖÜ„(0-9])', flach) if len(s.strip()) > 25]
unter = 0
for s in saetze:
    w = woerter(s)
    if len(w) < 3:
        continue
    anteil, datei = max(((len(w & a) / len(w)), d) for d, a in absaetze)
    if anteil < schwelle:
        unter += 1
        rest = sorted(w - max((a for d, a in absaetze), key=lambda a: len(w & a)))
        print(f'{anteil:.2f} [{datei}] {s[:150]}\n      fehlt: {", ".join(rest[:12])}')
print(f'{len(saetze)} Sätze alt, {unter} unter {schwelle}')

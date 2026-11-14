"""Selbstprüfung Runde R: Zeichenzahl alt/neu und Zuordnung alt -> neu.

Prüft: (1) Zeichenzahl je Datei, (2) Kennungen G01-G100, P01-P79, N1-N2 lückenlos und einmalig,
(3) jeder Anker ⟨...⟩ steht wörtlich in seiner Datei (Leerraum normalisiert), (4) jeder Satz des alten
Textes trägt mindestens einen Anker (keine Regel ohne Zeile), (5) Spalte 4 beginnt mit einer erlaubten Art,
ausgelagerte Zeilen zeigen auf auslagerung.md. Dazu als Auskunft: Sätze der neuen Texte ohne Anker.
Aufruf: python3 -I neu/pruefe.py   (liest ../alt-*.md, ../register-14-11-15.txt und die Dateien neben sich)
Ende mit Rückgabewert 1, wenn eine Prüfung fehlschlägt."""
import re
import sys
from pathlib import Path

NEU = Path(__file__).resolve().parent
ALT = NEU.parent
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
lies = lambda p: p.read_text(encoding='utf-8')

alt = {'G': lies(ALT / 'alt-global.md'), 'P': lies(ALT / 'alt-projekt.md'), 'N': lies(ALT / 'register-14-11-15.txt')}
neu = {'global.md': lies(NEU / 'global.md'), 'projekt.md': lies(NEU / 'projekt-verbessereBlaetter.md'),
       'auslagerung.md': lies(NEU / 'auslagerung.md')}
fehler = []

# ---------- (1) Zeichenzahl ----------
print('Zeichenzahl (ganze Datei, Zeichen statt Bytes)')
summe_a = summe_n = 0
for kurz, a, n in (('global', alt['G'], neu['global.md']), ('projekt', alt['P'], neu['projekt.md'])):
    summe_a += len(a)
    summe_n += len(n)
    print(f'  {kurz:8s} alt {len(a):6d}  neu {len(n):6d}  {(len(n) - len(a)) / len(a) * 100:+5.1f} %')
print(f'  zusammen alt {summe_a:6d}  neu {summe_n:6d}  {(summe_n - summe_a) / summe_a * 100:+5.1f} %')
kop = lambda t: t.split('\n---\n', 1)[1].strip()
print(f'  global, kopierbarer Teil: alt {len(kop(alt["G"]))}  neu {len(kop(neu["global.md"]))}')
for name, soll in (('global.md', 'Stand: 2026-11-14 (f)'), ('projekt.md', 'Stand: 2026-11-14 (b)')):
    if soll not in neu[name]:
        fehler.append(f'Stand-Zeile fehlt in {name}: {soll}')

# ---------- Zuordnung lesen ----------
zeilen = []
for z in lies(NEU / 'zuordnung.md').split('\n'):
    if not re.match(r'^\| [GPN]\d+ \|', z):
        continue
    sp = [s.strip() for s in z.strip().strip('|').split('|')]
    if len(sp) != 4:
        fehler.append(f'Zeile mit {len(sp)} statt 4 Spalten: {z[:40]}')
        continue
    zeilen.append(sp)

# ---------- (2) Kennungen ----------
soll = [f'G{i:02d}' for i in range(1, 101)] + [f'P{i:02d}' for i in range(1, 80)] + ['N1', 'N2', 'N3', 'N4', 'N5']
ist = [z[0] for z in zeilen]
if ist != soll:
    fehler.append('Kennungen nicht lückenlos/in Reihenfolge: fehlt ' + ', '.join(sorted(set(soll) - set(ist)))
                  + ' · zu viel ' + ', '.join(sorted(set(ist) - set(soll))) + ' · doppelt '
                  + ', '.join(sorted({k for k in ist if ist.count(k) > 1})))

# ---------- (3) Anker, (5) Art ----------
ARTEN = ('wörtlich', 'gekürzt', 'zusammengelegt', 'ausgelagert', 'gestrichen', 'neu')
altn = {k: norm(v) for k, v in alt.items()}
neun = {k: norm(v) for k, v in neu.items()}
anker_alt = {'G': [], 'P': [], 'N': []}   # (start, ende, kennung)
anker_neu = {k: [] for k in neu}
zahl = {a: 0 for a in ARTEN}
for kenn, alte, wo, art in zeilen:
    q = kenn[0]
    gefunden = re.findall(r'⟨([^⟩]*)⟩', alte)
    if not gefunden:
        fehler.append(f'{kenn}: kein Anker in „alte Stelle“')
    for a in gefunden:
        a = norm(a)
        n = altn[q].count(a)
        if n == 0:
            fehler.append(f'{kenn}: alter Anker nicht im alten Text: ⟨{a}⟩')
        elif n > 1:
            fehler.append(f'{kenn}: alter Anker {n}-mal im alten Text, nicht eindeutig: ⟨{a}⟩')
        else:
            s = altn[q].index(a)
            anker_alt[q].append((s, s + len(a), kenn))
    datei, n_anker, dateien = None, 0, set()
    for m in re.finditer(r'(global\.md|projekt\.md|auslagerung\.md)|⟨([^⟩]*)⟩', wo):
        if m.group(1):
            datei = m.group(1)
            continue
        a = norm(m.group(2))
        n_anker += 1
        if datei is None:
            fehler.append(f'{kenn}: Anker vor Dateiname in „wo jetzt“')
        elif a not in neun[datei]:
            fehler.append(f'{kenn}: neuer Anker nicht in {datei}: ⟨{a}⟩')
        else:
            dateien.add(datei)
            for t in re.finditer(re.escape(a), neun[datei]):
                anker_neu[datei].append((t.start(), t.end(), kenn))
    if n_anker == 0:
        fehler.append(f'{kenn}: kein Anker in „wo jetzt“')
    treffer = [a for a in ARTEN if art.startswith(a)]
    if not treffer:
        fehler.append(f'{kenn}: Art nicht erlaubt: {art[:30]}')
        continue
    zahl[treffer[0]] += 1
    if treffer[0] == 'ausgelagert' and 'auslagerung.md' not in dateien:
        fehler.append(f'{kenn}: ausgelagert, aber kein Anker in auslagerung.md')
    if treffer[0] == 'ausgelagert' and not (dateien - {'auslagerung.md'}):
        fehler.append(f'{kenn}: ausgelagert, aber kein Verweis mit Anlass im Text')
    if treffer[0] == 'gestrichen' and ':' not in art:
        fehler.append(f'{kenn}: gestrichen ohne Grund')
    if treffer[0] == 'neu' and q != 'N':
        fehler.append(f'{kenn}: Art „neu“ nur für N')

# ---------- (4) jeder Satz des alten Textes trägt einen Anker ----------
def saetze(text):
    """Sätze mit Spannen im normalisierten Text; Überschriften und Stand-Zeilen bleiben außen vor."""
    grenzen = [0] + [m.end() for m in re.finditer(r'(?<=[.?!])\s+', text)] + [len(text)]
    for a, b in zip(grenzen, grenzen[1:]):
        s = text[a:b].strip()
        s = re.sub(r'^(## [^:]{0,40}?)(?=[A-ZÄÖÜ`„(*])', '', s) if s.startswith('## ') else s
        if len(re.sub(r'[^A-Za-zÄÖÜäöüß]', '', s)) >= 8 and not s.startswith('Stand'):
            yield a, b, s

def ohne_anker(text, spannen):
    return [s for a, b, s in saetze(text) if not any(x < b and y > a for x, y, _ in spannen)]

for q, name in (('G', 'alt-global.md'), ('P', 'alt-projekt.md')):
    t = altn[q]
    if q == 'G':
        versatz = t.index('Stand: 2026-11-14 (e)')
        spannen = [(x - versatz, y - versatz, k) for x, y, k in anker_alt[q]]
        t = t[versatz:]
    else:
        spannen = anker_alt[q]
    for s in ohne_anker(t, spannen):
        if re.fullmatch(r'(Stand: )?[\d\-]+ \([a-z]\)( ## \w+)?( \w+:)?|## [\w ,]+', s):
            continue
        fehler.append(f'{name}: Satz ohne Zeile in der Zuordnung: {s[:90]}')

# ---------- Auskunft: neue Sätze ohne Anker ----------
print('\nSätze der neuen Texte, auf die keine Zeile zeigt (Auskunft; neu sind nur N1, N2 und Verweise):')
for name in ('global.md', 'projekt.md'):
    t = neun[name]
    if name == 'global.md':
        versatz = t.index('Stand: 2026-11-14 (f)')
        spannen = [(x - versatz, y - versatz, k) for x, y, k in anker_neu[name]]
        t = t[versatz:]
    else:
        spannen = anker_neu[name]
    rest = [s for s in ohne_anker(t, spannen) if not re.match(r'(Stand: )?[\d\-]+ \([a-z]\)', s)]
    for s in rest:
        print(f'  {name}: {s[:110]}')
    if not rest:
        print(f'  {name}: keine')

# ---------- Ergebnis ----------
print(f'\nZuordnung: {len(zeilen)} Zeilen (Soll {len(soll)}) · ' + ' · '.join(f'{a} {n}' for a, n in zahl.items()))
if fehler:
    print(f'\n{len(fehler)} FEHLER')
    for f in fehler:
        print('  ' + f)
    sys.exit(1)
print('alle Prüfungen bestanden')

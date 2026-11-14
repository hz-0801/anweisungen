#!/usr/bin/env python3
"""Baut den Belegkorpus der letzten 4 Wochen (17.10.-14.11.2026) als JSON-Zeilen: quelle, ort, text."""
import re, json, glob, os, sys
H = '/home/claude'
out = []
def win_iso(s):
    m = re.search(r'2026-(\d\d)-(\d\d)', s)
    if not m: return False
    mo, d = int(m.group(1)), int(m.group(2))
    return (mo == 10 and d >= 17) or (mo == 11 and d <= 14)
def win_dm(d, mo):
    return (mo == 10 and d >= 17) or (mo == 11 and d <= 14)
# C Commits
for l in open(f'{H}/runde-a/belege/commits.txt', encoding='utf-8'):
    repo, dat, h, s = l.rstrip('\n').split('|', 3)
    out.append(dict(q='C', ort=f'{repo} {h} {dat}', text=s))
# U Uebergaben (je Datei eine Einheit)
ue = [f for f in sorted(glob.glob(f'{H}/mathe-nachhilfe/archiv/uebergabe*.md')) if win_iso(os.path.basename(f))]
ue.append(f'{H}/mathe-nachhilfe/uebergabe.md')
for f in ue:
    out.append(dict(q='U', ort='mathe-nachhilfe/' + os.path.relpath(f, f'{H}/mathe-nachhilfe'), text=open(f, encoding='utf-8').read()))
# J jetzt-offen u. ae. (eindeutige Zeilen)
seen = set()
for f in sorted(glob.glob(f'{H}/mathe-nachhilfe/archiv/*.md')):
    b = os.path.basename(f)
    if b.startswith('uebergabe') or not win_iso(b): continue
    if b.startswith('plan-'): continue
    for i, l in enumerate(open(f, encoding='utf-8'), 1):
        l = l.strip()
        if len(l) < 20 or l in seen: continue
        seen.add(l); out.append(dict(q='J', ort=f'mathe-nachhilfe/archiv/{b}:{i}', text=l))
# R plan.md § 5, 7, 8, 9
lines = open(f'{H}/mathe-nachhilfe/plan.md', encoding='utf-8').read().split('\n')
sec = None
for i, l in enumerate(lines, 1):
    m = re.match(r'## (\d+) ', l)
    if m: sec = int(m.group(1)); continue
    if sec not in (4, 5, 7, 8, 9) or len(l.strip()) < 20: continue
    if sec in (8, 9):
        m = re.match(r'- (\d\d)\.(\d\d)\.', l)
        if not m or not win_dm(int(m.group(1)), int(m.group(2))): continue
    if l.strip() in seen: continue
    seen.add(l.strip())
    out.append(dict(q='R', ort=f'plan.md §{sec}:{i}', text=l.strip()))
# B Befunde, Rueckmeldungen (eindeutige Zeilen)
bf = glob.glob(f'{H}/aufgabenbank/bau/befunde-*.md') + [f'{H}/aufgabenbank/bau/rueckmeldung-bestellchat.md']
bf += glob.glob(f'{H}/aufgabenbank/bau/*/befunde-*.md') + glob.glob(f'{H}/aufgabenbank/bau/*/*/befunde-lehrer*.md')
bf += glob.glob(f'{H}/aufgabenbank-privat/bau/*/befunde-lehrer*.md')
for f in sorted(set(bf)):
    for i, l in enumerate(open(f, encoding='utf-8'), 1):
        l = l.strip()
        if len(l) < 20: continue
        out.append(dict(q='B', ort=os.path.relpath(f, H) + f':{i}', text=l))
# K anweisungen/archiv im Fenster
for f in sorted(glob.glob(f'{H}/anweisungen/archiv/**/*.md', recursive=True)):
    rel = os.path.relpath(f, H)
    if not win_iso(rel) or 'kandidaten-bis-' in rel: continue
    if os.path.basename(f) in ('global-final.md','global-kurz-A.md','global-kurz-B.md','umzug.md','zuordnung.md','auslagerung.md','modelle-nachtrag.md','auftrag.md','pruefauftrag.md','auftrag-kritiker.md'): continue
    for i, l in enumerate(open(f, encoding='utf-8'), 1):
        l = l.strip()
        if len(l) < 20: continue
        out.append(dict(q='K', ort=rel + f':{i}', text=l))
with open(f'{H}/runde-a/belege/korpus.jsonl', 'w', encoding='utf-8') as fh:
    for o in out: fh.write(json.dumps(o, ensure_ascii=False) + '\n')
from collections import Counter
print(Counter(o['q'] for o in out))

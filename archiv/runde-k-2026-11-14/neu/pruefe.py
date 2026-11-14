"""Selbstprüfung Runde K. Aufruf: python3 -I neu/pruefe.py   (Rückgabewert 1 bei Fehler)

Prüft: (1) Zeichenzahl alt/neu je Datei, global nicht länger als (f); (2) Stand-Zeilen; (3) jede Regel aus
regeln.csv hat genau eine Zeile in zuordnung.md, keine Zeile ohne Regel; (4) jeder Anker ⟨…⟩ steht wörtlich in der
genannten neuen Datei, bei „wörtlich“ auch im alten Text; (5) Übernahme nach Auftrag Nr. 6; (6) Wortlaut, der erhalten
bleiben muss (Kostenregel, Übergabe aus wege.md, Teil verbessereBlätter); (7) Pflichtinhalte aus Auftrag Nr. 1–5, 8.
Dazu als Auskunft: Sätze des alten Textes, die in keiner neuen Anweisung mehr wörtlich stehen.
"""
import csv
import re
import sys
from pathlib import Path

NEU = Path(__file__).resolve().parent
REPO = Path('/home/claude/anweisungen')
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
lies = lambda p: p.read_text(encoding='utf-8')
kop = lambda t: t.split('\n---\n', 1)[1].strip()
fehler = []

alt_g, alt_p = lies(REPO / 'global.md'), lies(REPO / 'projekt-verbessereBlaetter.md')
wege, modelle = lies(REPO / 'wege.md'), lies(REPO / 'modelle.md')
neu = {'global.md': lies(NEU / 'global.md'), 'projekt.md': lies(NEU / 'projekt-verbessereBlaetter.md'),
       'modelle-aenderung.md': lies(NEU / 'modelle-aenderung.md'), 'wege-aenderung.md': lies(NEU / 'wege-aenderung.md')}
neun = {k: norm(v) for k, v in neu.items()}
altn = {'G': norm(alt_g), 'P': norm(alt_p)}

# ---------- (1) Zeichenzahl ----------
print('(1) Zeichenzahl (Zeichen, nicht Bytes)')
for name, a, n in (('global.md, ganze Datei', alt_g, neu['global.md']),
                   ('global.md, kopierbarer Text', kop(alt_g), kop(neu['global.md'])),
                   ('projekt-verbessereBlaetter.md', alt_p, neu['projekt.md'])):
    print(f'    {name:32s} alt {len(a):6d}  neu {len(n):6d}  {(len(n) - len(a)) / len(a) * 100:+5.1f} %')
z_a = len(kop(alt_g)) + len(alt_p)
z_n = len(kop(neu['global.md'])) + len(neu['projekt.md'])
print(f'    {"beide Anweisungen zusammen":32s} alt {z_a:6d}  neu {z_n:6d}  {(z_n - z_a) / z_a * 100:+5.1f} %')
print(f'    modelle.md alt {len(modelle)} · modelle-aenderung.md {len(neu["modelle-aenderung.md"])}')
print(f'    wege.md    alt {len(wege)} · wege-aenderung.md    {len(neu["wege-aenderung.md"])}')
if len(kop(neu['global.md'])) > len(kop(alt_g)):
    fehler.append('global.md (kopierbar) ist länger als Stand (f)')

# ---------- (2) Stand-Zeilen ----------
if not kop(neu['global.md']).startswith('Stand: 2026-11-14 (g)\n'):
    fehler.append('global: kopierbarer Text beginnt nicht mit „Stand: 2026-11-14 (g)“')
if 'Stand 2026-11-14 (g).' not in neu['global.md'].split('\n---\n')[0]:
    fehler.append('global: Kopf nennt Stand (g) nicht')
if not neu['projekt.md'].startswith('Stand: 2026-11-14 (c)\n'):
    fehler.append('projekt: beginnt nicht mit „Stand: 2026-11-14 (c)“')
for name in ('global.md', 'projekt.md'):
    if re.search(r'2026-11-14 \((f|b)\)', neu[name]):
        fehler.append(f'{name}: alte Stand-Zeile noch im Text')

# ---------- (3) Kennungen ----------
regeln = list(csv.DictReader(open(REPO / 'archiv/runde-a-2026-11-14/regeln.csv', encoding='utf-8'), delimiter=';'))
soll = [r['kennung'] for r in regeln]
zeilen = {}
neue_regeln = []
for z in lies(NEU / 'zuordnung.md').split('\n'):
    m = re.match(r'^\| ([GPN]\d+) \|', z)
    if not m:
        continue
    sp = [s.strip() for s in z.strip().strip('|').split('|')]
    if m.group(1).startswith('N'):
        if len(sp) != 4:
            fehler.append(f'{m.group(1)}: {len(sp)} statt 4 Spalten')
        neue_regeln.append(sp)
        continue
    if len(sp) != 5:
        fehler.append(f'{m.group(1)}: {len(sp)} statt 5 Spalten')
        continue
    if sp[0] in zeilen:
        fehler.append(f'{sp[0]}: doppelt in zuordnung.md')
    zeilen[sp[0]] = sp
fehlt = [k for k in soll if k not in zeilen]
zuviel = [k for k in zeilen if k not in soll]
if fehlt or zuviel or list(zeilen) != soll:
    fehler.append(f'Kennungen: fehlt {fehlt} · zu viel {zuviel} · Reihenfolge gleich: {list(zeilen) == soll}')
print(f'(3) regeln.csv: {len(soll)} Regeln · zuordnung.md: {len(zeilen)} Zeilen alt, {len(neue_regeln)} neue Regeln')
for sp in neue_regeln:
    if not re.search(r'\d\d\.\d\d\.\d+|keine – Setzung', sp[3]):
        fehler.append(f'{sp[0]}: weder Registerzeile noch „keine – Setzung“')

# ---------- (4) Anker ----------
def anker(wo):
    datei = None
    for m in re.finditer(r'(global\.md|projekt\.md|modelle-aenderung\.md|wege-aenderung\.md)|⟨([^⟩]*)⟩', wo):
        if m.group(1):
            datei = m.group(1)
        else:
            yield datei, norm(m.group(2))


n_anker = 0
for k, sp in list(zeilen.items()) + [(s[0], [s[0], '', '', s[2], '']) for s in neue_regeln]:
    wo, wie = sp[3], sp[4]
    gefunden = list(anker(wo))
    if not gefunden and not wo.startswith('entfällt'):
        fehler.append(f'{k}: kein Anker')
    for datei, a in gefunden:
        n_anker += 1
        if datei is None or a not in neun[datei]:
            fehler.append(f'{k}: Anker nicht in {datei}: ⟨{a}⟩')
        elif wie.startswith('wörtlich') or ', wörtlich' in wie:
            if 'entfällt' not in wo and a not in altn[k[0]]:
                fehler.append(f'{k}: als wörtlich geführt, Anker steht nicht im alten Text: ⟨{a}⟩')
    if wo.startswith('entfällt') and not wie.startswith('gestrichen'):
        fehler.append(f'{k}: entfällt, aber nicht als gestrichen geführt')
print(f'(4) {n_anker} Anker geprüft')

# ---------- (5) Übernahme nach Auftrag Nr. 6 ----------
ZWEIFEL = {'G24', 'G48'}                                    # Abschnitt „Zweifelsfälle“ des Berichts
NR7 = {'P06', 'P10', 'P21', 'P23', 'P24', 'P35', 'P36'}     # Empfehlung Nr. 7 des Berichts
AUFTRAG1 = {'G49', 'G53'}                                   # bleiben global (Auftrag Nr. 1)
zahl = {}
for r in regeln:
    k, empf, schaden = r['kennung'], r['empfehlung'].split(' ')[0], r['schaden']
    if k not in zeilen:
        continue
    m = re.search(r'übernommen: (ja|nein|teils|–)', zeilen[k][2])
    ueb = m.group(1) if m else None
    if not zeilen[k][2].startswith(empf) or f'Schaden {schaden}' not in zeilen[k][2]:
        fehler.append(f'{k}: Spalte Regelprüfung weicht von regeln.csv ab ({empf}, {schaden})')
    if empf == 'behalten':
        erwartet = {'–'}
    elif empf in ('streichen', 'kürzen'):
        if k in ZWEIFEL or k in NR7:
            erwartet = {'nein'}
        elif schaden == 'gering':
            erwartet = {'ja'}
        else:
            erwartet = {'nein', 'teils'}
    else:  # verschieben
        nach_projekt = k.startswith('G') and 'Projekt verbessereBlätter' in r['empfehlung']
        if not nach_projekt or k in AUFTRAG1:
            erwartet = {'nein'}
        else:
            erwartet = {'ja', 'teils'}
    if ueb not in erwartet:
        fehler.append(f'{k}: {empf}/{schaden} – übernommen „{ueb}“, erwartet {sorted(erwartet)}')
    zahl[(empf, ueb)] = zahl.get((empf, ueb), 0) + 1
print('(5) Übernahme: ' + ' · '.join(f'{e} {u}: {n}' for (e, u), n in sorted(zahl.items())))

# ---------- (6) Wortlaut, der erhalten bleiben muss ----------
def absatz(text, anfang):
    t = [b for b in re.split(r'\n\s*\n', text) if b.startswith(anfang)]
    return norm(t[0]) if len(t) == 1 else None


if absatz(alt_g, 'Kostenregel:') != absatz(neu['global.md'], 'Kostenregel:') or not absatz(alt_g, 'Kostenregel:'):
    fehler.append('Kostenregel weicht vom Stand (f) ab')
ueb = wege.split('### Übergabe (alle Chats)')[1].split('### Teil verbessereBlätter')[0]
teil = wege.split('### Teil verbessereBlätter')[1].split('## Durchsicht am Handy')[0]
stuecke = []
for b in re.split(r'\n\s*\n', ueb.strip()):
    if re.match(r'^1\. ', b):
        stuecke += [norm(x) for x in re.split(r'\n(?=\d\. )', b)]
    else:
        stuecke.append(norm(b).rstrip(':'))
for s in stuecke:
    if s not in neun['global.md']:
        fehler.append(f'Übergabe (wege.md) fehlt in global: {s[:60]}…')
for s in ['Vorher prüfen, ob die Ergebnisse dort stehen, wo sie wirken, und per Skript',
          'ob Entscheidungsmarken („Lehrer TT.MM.“, „fest“, „beschlossen“) ohne Registerzeile neu sind – die Liste zeigst du mir',
          '`uebergabe.md` neu (nächster Schritt nur als Verweis auf plan.md „Jetzt“), alte datiert nach `archiv/`.',
          norm(teil.split('Im selben Zug')[1])]:
    assert s in norm(teil) or s == norm(teil.split('Im selben Zug')[1]), s
    if s not in neun['projekt.md']:
        fehler.append(f'Teil verbessereBlätter (wege.md) fehlt im Projekt: {s[:60]}…')
print(f'(6) Kostenregel, {len(stuecke)} Stücke der Übergabe, 4 Stücke Teil verbessereBlätter geprüft')

# ---------- (7) Pflichtinhalte ----------
PFLICHT = {
    'global.md': ['größten Nutzen', 'Anteilen der Woche', 'Rücklage', '„Pflicht“', '„Endspurt“',
                  'was ein Skript abnimmt oder Nacharbeit nachweislich spart', 'liest du die Nutzungsanzeige selbst ab',
                  '„Anzeige ablesen“', 'Qualität ist Bedingung, nicht Stellschraube', 'Blindvergleich',
                  'ohne Vergleich der bewährte Weg', 'Grenzen je Tag oder Stunde',
                  'stellst du den Rest bis nach dem Reset zurück', '`modelle.md` § 2', 'frag mich nie neu danach',
                  'etwa zur Wochenmitte vor einem großen Lauf',
                  'am Ende jedes Schritts, nie mitten in einem', 'halbem Kontextfenster',
                  'vor jeder automatischen Zusammenfassung', 'alles Entschiedene in Dateien steht',
                  'kein Entscheidungsgespräch offen', 'nur am Phasenende', 'mit der Rechnung in einer Zeile',
                  'Gibt es keine Auswertung, gilt der alte Weg', 'sonst erinnere ich', '„Umzug rechnen“',
                  '→ Anweisung, knapp', '„bei X lies Y“', '→ Register, nie Anweisung',
                  'Sprungmarken nur für Nachschlagestoff (Tabellen, Listen, Messwerte)', 'Regeltexte liest du immer ganz'],
    'projekt.md': ['zusätzlich zu global „Stichwort Umzug“', 'werkzeuge/entscheidungsmarken.py', 'roten Spalte',
                   'Kommentar mit seiner Stelle', 'Vergleiche nur die Stand-Zeile', '`kandidaten.md` kommt',
                   'Lies die Nutzungsanzeige ab', 'Abgebrochen wird nur auf mein Wort'],
    'modelle-aenderung.md': ['10.12.2026', '09.03.2027', '50 % der Woche', 'claude.ai/settings/usage',
                             "[...document.querySelectorAll('[role=dialog], dialog')].map(d=>d.innerText)",
                             '„Zurücksetz“', 'Bild der Anzeige beim Lehrer', '0,01 Wochenpunkten',
                             '| Fable | high |', 'Kritik kurzer Fragen', 'eigener Schritt',
                             '0,1 × (K − S) × N > U', 'Cache lesen ÷ Anfragen', '80 000', '0,35 Mio',
                             '89 Anfragen, 3,6 Mio gewichtet', 'Halbes Kontextfenster', 'werkzeuge/umzug_rechnung.py'],
    'wege-aenderung.md': ['abgelöst, steht wieder in global.md (g)'],
}
n_pf = 0
for datei, liste in PFLICHT.items():
    for s in liste:
        n_pf += 1
        if norm(s) not in neun[datei]:
            fehler.append(f'Pflichtinhalt fehlt in {datei}: {s}')
VERBOTEN = {'global.md': ['wege.md` §', 'Chatstart im Projekt', 'Kommentiertes PDF', 'roten Spalte', 'Recherche:',
                          'eine Tagesgrenze gibt es nicht', 'Nennen:', 'Vorausplanen:', 'Kontext klein:']}
for datei, liste in VERBOTEN.items():
    for s in liste:
        if s in neun[datei]:
            fehler.append(f'steht noch in {datei}: {s}')
print(f'(7) {n_pf} Pflichtinhalte geprüft')

# ---------- Auskunft: alte Sätze, die nirgends mehr wörtlich stehen ----------
def saetze(text):
    t = norm(re.sub(r'^#+ .*$', '', text, flags=re.M))
    return [s.strip() for s in re.split(r'(?<=[.?!:;])\s+(?=[A-ZÄÖÜ„(`*\d])', t) if len(s.strip()) > 12]


beide = neun['global.md'] + ' ' + neun['projekt.md']
print('\nAuskunft – Sätze und Satzteile des alten Textes, die in keiner neuen Anweisung wörtlich stehen:')
for name, text in (('global (f)', kop(alt_g)), ('projekt (b)', alt_p)):
    weg = [s for s in saetze(text) if s not in beide]
    print(f'  {name}: {len(weg)} von {len(saetze(text))}')
    for s in weg:
        print('     –', s[:150] + ('…' if len(s) > 150 else ''))

print()
if fehler:
    print(f'{len(fehler)} FEHLER')
    for f in fehler:
        print('  !', f)
    sys.exit(1)
print('0 Fehler')

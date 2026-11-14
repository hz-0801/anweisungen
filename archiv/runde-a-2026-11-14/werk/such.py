#!/usr/bin/env python3
"""such.py <regex> [n] – zaehlt Treffer je Quelle und zeigt n Fundstellen je Quelle."""
import re, json, sys
from collections import Counter, defaultdict
rx = re.compile(sys.argv[1], re.I | re.S); n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
c = Counter(); ex = defaultdict(list)
for l in open('/home/claude/runde-a/belege/korpus.jsonl', encoding='utf-8'):
    o = json.loads(l); m = rx.search(o['text'])
    if m:
        c[o['q']] += 1
        if len(ex[o['q']]) < n:
            s = max(0, m.start() - 70); ex[o['q']].append(o['ort'] + ' :: ' + o['text'][s:m.end() + 110].replace('\n', ' '))
print(dict(c))
for q in ex:
    for e in ex[q]: print(' ', q, e)

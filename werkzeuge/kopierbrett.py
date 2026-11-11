#!/usr/bin/env python3
"""brett.py – Kopierbrett: eine Seite mit allem, was der Lehrer aus dem Chat kopieren soll, je Eintrag ein Knopf.
Aufruf: python3 brett.py eintraege.json index.html   (eintraege.json: Liste aus titel, wohin, link, text oder datei, erledigt; {heute} im Text = Wochentag und Datum beim Öffnen)"""
import json, sys, html
E = json.load(open(sys.argv[1], encoding='utf-8'))
for e in E:
    if e.get('datei'):
        t = open(e['datei'], encoding='utf-8').read()
        if e.get('ab'): t = t[t.index(e['ab']):]
        e['text'] = t.rstrip() + '\n'
daten = json.dumps([e['text'] for e in E], ensure_ascii=False).replace('</', '<\\/')
teile = []
for i, e in enumerate(E):
    z = e['text'].count('\n') + (0 if e['text'].endswith('\n') else 1)
    wohin = html.escape(e['wohin']) + (' <a href="%s">Dorthin</a>' % html.escape(e['link']) if e.get('link') else '')
    teile.append('<li class="%s"><div class="kopf"><span class="t">%s</span><button type="button" data-i="%d">Kopieren</button></div>'
                 '<details><summary><span class="wohin">%s</span><span class="z">%d %s ▸</span></summary><pre>%s</pre></details></li>'
                 % ('fertig' if e.get('erledigt') else '', html.escape(e['titel']), i, wohin, z, 'Zeile' if z == 1 else 'Zeilen', html.escape(e['text'])))
open(sys.argv[2], 'w', encoding='utf-8').write('''<!DOCTYPE html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Zum Kopieren</title>
<style>
body{margin:0;font:16px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;color:#1c2530;background:#fff}
main{max-width:720px;margin:0 auto;padding:20px 16px 40px}h1{font-size:22px;margin:0 0 4px}p.s{color:#5d6875;font-size:13px;margin:0 0 16px}
ul{list-style:none;margin:0;padding:0}li{border:1px solid #d9dee4;border-left:4px solid #1f5fa8;border-radius:6px;padding:12px;margin-bottom:10px}
li.fertig{border-left-color:#9aa3ad;opacity:.6}.kopf{display:flex;justify-content:space-between;gap:10px;align-items:center}.t{font-weight:600}
.wohin{color:#5d6875;font-size:13px}a{color:#1f5fa8}
button{font:inherit;padding:6px 16px;border:1px solid #1f5fa8;background:#1f5fa8;color:#fff;border-radius:4px;cursor:pointer;white-space:nowrap}
button.ok{background:#2c7a4b;border-color:#2c7a4b}details{margin-top:2px;font-size:13px;color:#5d6875}summary{list-style:none;display:flex;justify-content:space-between;gap:10px;cursor:pointer}summary::-webkit-details-marker{display:none}.z{white-space:nowrap}li{padding:8px 12px}
pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f4f6f8;border-radius:4px;padding:10px;max-height:300px;overflow:auto;color:#1c2530;font:12px/1.4 ui-monospace,Consolas,monospace}
</style></head><body><main><h1>Zum Kopieren</h1><p class="s">%s · offen oben, Erledigtes grau</p><ul>%s</ul></main>
<script>const T=%s;
// {heute} im Text wird beim Öffnen durch Wochentag und Datum ersetzt („Mittwoch 11.11.26“) – für Startzeilen neuer Chats
(()=>{const d=new Date(),z=n=>String(n).padStart(2,"0"),h=["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"][d.getDay()]+" "+z(d.getDate())+"."+z(d.getMonth()+1)+"."+String(d.getFullYear()).slice(2);
T.forEach((t,i)=>{if(t.includes("{heute}")){T[i]=t.split("{heute}").join(h);const p=document.querySelectorAll("pre")[i];p.textContent=T[i];p.closest("details").open=true}})})();
document.querySelectorAll("button[data-i]").forEach(b=>b.addEventListener("click",()=>{
  const ok=()=>{b.textContent="Kopiert ✓";b.classList.add("ok");setTimeout(()=>{b.textContent="Kopieren";b.classList.remove("ok")},2500)};
  const hand=()=>{const d=b.closest("li").querySelector("details");d.open=true;const r=document.createRange();r.selectNodeContents(d.querySelector("pre"));const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent="Markiert – Strg+C"};
  try{navigator.clipboard.writeText(T[+b.dataset.i]).then(ok,hand)}catch(x){hand()}}));
</script></body></html>''' % (html.escape(sys.argv[3] if len(sys.argv) > 3 else ''), ''.join(teile), daten))
print('ok', len(E), 'Einträge', [len(e['text']) for e in E])

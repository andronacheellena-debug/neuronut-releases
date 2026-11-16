#!/usr/bin/env python3
"""Construiește licente.json din e-mailuri (un e-mail pe linie în emails.txt). Doar amprente ies din script."""
import hashlib, json, sys, time
emails = sorted({l.strip().lower() for l in open(sys.argv[1], encoding="utf-8") if "@" in l})
out = {"actualizat": time.strftime("%Y-%m-%d %H:%M"), "numar": len(emails),
       "licente": sorted(hashlib.sha256(e.encode()).hexdigest() for e in emails)}
json.dump(out, open("licente.json", "w"), indent=1)
print(len(emails), "licențe")

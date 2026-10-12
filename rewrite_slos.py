"""Rewrite each chapter's SLOS block from the authoritative syllabus.

Existing teaching metadata (simple/taught/activity/check) is preserved for
outcomes that survive; new outcomes get a placeholder that is filled in by hand.
"""
import importlib, pathlib, re, sys
sys.path.insert(0, "/workspace/Physics_Atlas")
exec(open("/workspace/Physics_Atlas/tools/smoke_app.py").read().split("failures = []")[0])
from physics import syllabus_xi as X

for n in range(1, 11):
    if n == 1:
        from physics import data as legacy
        old = {r["id"]: r for r in legacy.SLOS}
    else:
        path = pathlib.Path(f"/workspace/Physics_Atlas/physics/chapters/ch{n:02d}_data.py")
        src = path.read_text()
        mod = importlib.import_module(f"physics.chapters.ch{n:02d}_data")
        old = {r["id"]: r for r in mod.SLOS}
    rows = []
    for sid in X.chapter_ids(n):
        pub = X.outcome(sid)
        keep = old.get(sid, {})
        rows.append({
            "id": sid,
            "text": pub["text"],
            "simple": keep.get("simple", ""),
            "taught": keep.get("taught", pub["topic"]),
            "activity": keep.get("activity", ""),
            "check": keep.get("check", ""),
        })
    body = "SLOS = [\n"
    for r in rows:
        body += (f'    {{"id": "{r["id"]}", "text": "{r["text"]}",\n'
                 f'     "simple": "{r["simple"]}", "taught": "{r["taught"]}",\n'
                 f'     "activity": "{r["activity"]}", "check": "{r["check"]}"}},\n')
    body += "]"
    if n == 1:
        continue
    start = src.index("SLOS = [")
    end = src.index("\n]", start) + 2
    src = src[:start] + body + src[end:]
    path.write_text(src)
    missing = [r["id"] for r in rows if not r["simple"] or not r["activity"]]
    print(f"  ch{n:02d}: {len(rows):>2} outcomes rewritten"
          + (f"   {len(missing)} need content written" if missing else ""))

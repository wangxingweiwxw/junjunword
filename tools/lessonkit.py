"""Tiny helper for writing lesson.json from Python (used by ep04+ `lesson.py`).

Layout: you draw the *portrait* grid (3 columns, one string per row, '.' = empty);
landscape is its transpose (portrait rows become landscape columns), so a graph
that is tidy in one orientation is tidy in the other.

    L = Lesson("ep04", "birthday", "生日", 4, "birthday")
    L.node("cake", "cake", "/keɪk/", "蛋糕")             # icon defaults to id
    L.grid(["birthday party cake", "present match candle"])
    L.edge("party", "cake", "有")
    L.seg("map show:cake focus:cake", zh("……"), en("cake"))
    L.save()
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def zh(text, cue=""):
    return {"zh": text, **({"cue": cue.split()} if cue else {})}


def en(text, cue=""):
    return {"en": text, **({"cue": cue.split()} if cue else {})}


class Lesson:
    def __init__(self, ep, title, title_zh, num, title_icon):
        self.d = {"id": ep, "title": title, "titleZh": title_zh, "episode": f"第 {num} 集", "titleIcon": title_icon,
                  "voices": {"zh": {"voice": "zh-CN-XiaoxiaoNeural", "rate": "-5%"},
                             "en": {"voice": "en-US-JennyNeural", "rate": "-15%"}},
                  "stage": {}, "nodes": [], "edges": [], "script": []}
        self.byid = {}

    def node(self, id, word, ipa, zh_, icon=None, **kw):
        n = {"id": id, "word": word, "ipa": ipa, "zh": zh_, "icon": icon or id, **kw}
        self.d["nodes"].append(n); self.byid[id] = n
        return n

    def edge(self, a, b, label=None, dashed=False):
        e = {"from": a, "to": b}
        if label: e["label"] = label
        if dashed: e["dashed"] = True
        self.d["edges"].append(e)

    def seg(self, cue, *parts):
        self.d["script"].append({"cue": cue.split(), "parts": list(parts)})

    def grid(self, rows, flip=False, dy=340):
        rows = [r.split() for r in rows]
        R = len(rows)
        self.d["stage"] = {"landscape": [1800, 940], "portrait": [900, 300 + dy * (R - 1)]}
        for r, row in enumerate(rows):
            assert len(row) == 3, row
            for c, id in enumerate(row):
                if id == ".": continue
                n = self.byid[id]
                n["atP"] = [150 + 300 * c, 150 + dy * r]
                n["at"] = [round(1800 / R * (r + 0.5)), 150 + 320 * (2 - c if flip else c)]

    def review(self, items, outro):
        """items: list of (focus id, text to read)."""
        self.seg("focus:none", zh("最后，跟着我把今天的单词再读一遍吧！"))
        for fid, text in items:
            self.seg(f"focus:{fid}", en(text))
        self.seg("focus:none end", zh(outro))

    def save(self):
        ids = set(self.byid)
        for n in self.d["nodes"]:
            assert "at" in n, f"{n['id']} not placed in grid"
        for e in self.d["edges"]:
            assert e["from"] in ids and e["to"] in ids, e
        for s in self.d["script"]:
            for c in s["cue"] + [c for p in s["parts"] for c in p.get("cue", [])]:
                k, _, v = c.partition(":")
                for x in (v.split(",") if k == "focus" and v != "none" else [v] if k in ("show", "plural", "alt") else []):
                    assert x in ids, c
        out = os.path.join(ROOT, self.d["id"], "lesson.json")
        json.dump(self.d, open(out, "w"), ensure_ascii=False, indent=1)
        print(out, len(self.d["nodes"]), "nodes", len(self.d["script"]), "segments")

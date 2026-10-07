#!/usr/bin/env python3
"""lesson.json -> audio/lesson.mp3 + audio/words.mp3 + timeline.json

Usage: python3 tools/tts.py ep01
Clips are cached by (voice, rate, text) in <ep>/audio/cache, so editing one line
only re-synthesizes that line. Timings come from the exact PCM sample counts.
"""
import asyncio, hashlib, json, os, subprocess, sys, wave

import edge_tts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FFMPEG = os.path.join(ROOT, "tools", "ffmpeg")
SR = 24000
GAP_AFTER = {"zh": 0.25, "en": 0.5}   # pause after a part, inside a segment
GAP_SEGMENT = 0.6                     # extra pause between segments
GAP_WORD = 0.25                       # padding around each word in the sprite


def run(*args):
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


async def synth(text, voice, rate, cache):
    key = hashlib.sha1(f"{voice}|{rate}|{text}".encode()).hexdigest()[:16]
    wav = os.path.join(cache, key + ".wav")
    if os.path.exists(wav):
        return wav
    mp3 = os.path.join(cache, key + ".mp3")
    for attempt in range(4):
        try:
            await edge_tts.Communicate(text, voice, rate=rate).save(mp3)
            break
        except Exception as e:  # network hiccups
            if attempt == 3:
                raise
            print("  retry", text[:20], e)
            await asyncio.sleep(2)
    # mono 24k PCM, trim leading/trailing silence
    trim = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
            "silenceremove=start_periods=1:start_threshold=-45dB,areverse")
    run(FFMPEG, "-y", "-i", mp3, "-af", trim, "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", wav)
    os.remove(mp3)
    return wav


def pcm(path):
    with wave.open(path) as w:
        return w.readframes(w.getnframes())


def silence(sec):
    return b"\x00\x00" * int(round(sec * SR))


def encode(raw, out):
    tmp = out + ".wav"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(raw)
    run(FFMPEG, "-y", "-i", tmp, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
        "-ar", str(SR), "-c:a", "libmp3lame", "-b:a", "48k", out)
    os.remove(tmp)


async def main(ep):
    d = os.path.join(ROOT, ep)
    lesson = json.load(open(os.path.join(d, "lesson.json")))
    voices = lesson["voices"]
    cache = os.path.join(d, "audio", "cache")
    os.makedirs(cache, exist_ok=True)

    # collect every distinct (lang, text)
    jobs = {}
    for seg in lesson["script"]:
        for p in seg["parts"]:
            lang = "zh" if "zh" in p else "en"
            jobs[(lang, p[lang])] = None
    for n in lesson["nodes"]:
        for w in filter(None, [n["word"], n.get("alt"), n.get("plural")]):
            jobs[("en", w)] = None

    sem = asyncio.Semaphore(4)

    async def one(k):
        async with sem:
            v = voices[k[0]]
            jobs[k] = await synth(k[1], v["voice"], v["rate"], cache)

    await asyncio.gather(*(one(k) for k in jobs))

    # --- lesson track ---
    raw, t, parts = bytearray(), 0.0, []
    raw += silence(0.4); t = 0.4
    for si, seg in enumerate(lesson["script"]):
        for pi, p in enumerate(seg["parts"]):
            lang = "zh" if "zh" in p else "en"
            clip = pcm(jobs[(lang, p[lang])])
            dur = len(clip) / 2 / SR
            cue = (seg.get("cue", []) if pi == 0 else []) + p.get("cue", [])
            parts.append({"seg": si, "lang": lang, "text": p[lang], "t0": round(t, 3),
                          "t1": round(t + dur, 3), "cue": cue})
            raw += clip; t += dur
            g = GAP_AFTER[lang] + (GAP_SEGMENT if pi == len(seg["parts"]) - 1 else 0)
            raw += silence(g); t += g
    raw += silence(1.0); t += 1.0
    encode(bytes(raw), os.path.join(d, "audio", "lesson.mp3"))

    # --- word sprite (click a card to hear it) ---
    wraw, wt, words = bytearray(), 0.0, {}
    for n in lesson["nodes"]:
        # word and alt stay adjacent so a click can play "mother … mom" as one range
        for key, w in [(n["id"], n["word"]), (n["id"] + ":alt", n.get("alt")), (n["id"] + ":pl", n.get("plural"))]:
            if not w:
                continue
            clip = pcm(jobs[("en", w)])
            wraw += silence(GAP_WORD); wt += GAP_WORD
            dur = len(clip) / 2 / SR
            words[key] = [round(wt, 3), round(wt + dur, 3)]
            wraw += clip; wt += dur
    wraw += silence(GAP_WORD)
    encode(bytes(wraw), os.path.join(d, "audio", "words.mp3"))

    tl = {"duration": round(t, 3), "parts": parts, "words": words}
    json.dump(tl, open(os.path.join(d, "timeline.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{ep}: {len(parts)} parts, {t:.1f}s, {len(words)} word clips")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "ep01"))

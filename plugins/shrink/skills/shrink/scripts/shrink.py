#!/usr/bin/env python3
"""Algorithmic prompt compression via the LLMLingua-2 HuggingFace Space.

Zero dependencies — uses only the Python standard library.

Usage:
    python3 shrink.py --rate 0.5 < input.txt
    python3 shrink.py --rate 0.6 --force "API,token,2.1GB" --file prompt.md
    echo "long text" | python3 shrink.py

Compressed text -> stdout. Stats -> stderr.
"""
import argparse
import json
import sys
import time
import urllib.request
import urllib.error

BASE = "https://divkov-llmlingua-2.hf.space"
CALL = f"{BASE}/gradio_api/call/run"


def shrink(text: str, rate: float, force: str, wake_wait: int = 90) -> tuple[str, dict]:
    payload = json.dumps({"data": [text, rate, force]}).encode()
    deadline = time.time() + wake_wait
    warned = False
    while True:
        try:
            req = urllib.request.Request(
                CALL, data=payload, headers={"Content-Type": "application/json"}
            )
            event_id = json.loads(urllib.request.urlopen(req, timeout=30).read())["event_id"]
            break
        except urllib.error.HTTPError as e:
            # 503 = Space is cold/waking; retry until deadline
            if e.code in (503, 502) and time.time() < deadline:
                if not warned:
                    print("Space is waking up (cold start, ~30-60s)...", file=sys.stderr)
                    warned = True
                time.sleep(5)
                continue
            raise

    # Stream the SSE result
    with urllib.request.urlopen(f"{CALL}/{event_id}", timeout=120) as r:
        result = None
        for raw in r:
            line = raw.decode().rstrip()
            if line.startswith("data: "):
                result = json.loads(line[6:])
        if result is None:
            raise RuntimeError("no result returned from Space")
    return result[0], result[1]


def main():
    ap = argparse.ArgumentParser(description="Compress text via LLMLingua-2 (zero-dep)")
    ap.add_argument("--rate", type=float, default=0.3,
                    help="Retention rate 0.1-0.9 (0.3 = keep 30%% of tokens)")
    ap.add_argument("--force", default="",
                    help="Comma-separated tokens to never drop (numbers, IDs, paths)")
    ap.add_argument("--file", default=None, help="Read input from file instead of stdin")
    args = ap.parse_args()

    text = open(args.file).read() if args.file else sys.stdin.read()
    if not text.strip():
        sys.exit("error: empty input")

    compressed, stats = shrink(text, args.rate, args.force)

    sys.stdout.write(compressed)
    if not compressed.endswith("\n"):
        sys.stdout.write("\n")
    print(
        f"[{stats.get('original_tokens')} -> {stats.get('compressed_tokens')} tokens "
        f"| {stats.get('ratio')}x | {stats.get('saving_percent')}% saved]",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()

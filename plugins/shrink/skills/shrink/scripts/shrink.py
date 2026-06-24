#!/usr/bin/env python3
"""Algorithmic prompt compression via the LLMLingua-2 HuggingFace Space.

Usage:
    python3 shrink.py --rate 0.5 < input.txt
    python3 shrink.py --rate 0.6 --force "API,token,2.1GB" --file prompt.md
    echo "long text" | python3 shrink.py

Outputs the compressed text to stdout and stats to stderr.
Requires: pip install gradio_client
"""
import argparse
import sys

SPACE = "divkov/llmlingua-2"


def main():
    ap = argparse.ArgumentParser(description="Compress text via LLMLingua-2 Space")
    ap.add_argument("--rate", type=float, default=0.5,
                    help="Retention rate 0.1-0.9 (0.5 = keep 50%% of tokens)")
    ap.add_argument("--force", default="",
                    help="Comma-separated tokens/words to never drop (e.g. numbers, identifiers)")
    ap.add_argument("--file", default=None, help="Read input from file instead of stdin")
    args = ap.parse_args()

    text = open(args.file).read() if args.file else sys.stdin.read()
    if not text.strip():
        sys.exit("error: empty input")

    try:
        from gradio_client import Client
    except ImportError:
        sys.exit("error: pip install gradio_client")

    client = Client(SPACE)
    compressed, stats = client.predict(
        text=text, rate=args.rate, force_tokens=args.force, api_name="/run"
    )

    sys.stdout.write(compressed)
    if not compressed.endswith("\n"):
        sys.stdout.write("\n")
    print(
        f"[{stats.get('original_tokens')} → {stats.get('compressed_tokens')} tokens "
        f"| {stats.get('ratio')}x | {stats.get('saving_percent')}% saved]",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()

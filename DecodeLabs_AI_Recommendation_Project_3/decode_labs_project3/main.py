"""Command-line app for DecodeLabs AI Recommendation Logic."""
from __future__ import annotations

import argparse
from pathlib import Path

from recommender import load_items, recommend


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Recommend learning content based on your interests."
    )
    parser.add_argument(
        "--interests",
        help='Comma-separated interests, e.g. "python, AI, data science".',
    )
    parser.add_argument("--top", type=int, default=5, help="Number of results (default: 5).")
    parser.add_argument("--category", help="Optional category filter, e.g. Technology.")
    parser.add_argument(
        "--data",
        default=str(Path(__file__).parent / "data" / "items.json"),
        help="Path to the JSON item dataset.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.top < 1:
        print("Error: --top must be at least 1.")
        return 2

    try:
        items = load_items(args.data)
    except (OSError, ValueError) as exc:
        print(f"Could not load recommendation dataset: {exc}")
        return 2

    raw_interests = args.interests
    if raw_interests is None:
        print("=== DecodeLabs | AI Recommendation Logic ===")
        print("Enter interests separated by commas (e.g. Python, AI, design):")
        raw_interests = input("> ").strip()

    preferences = [part.strip() for part in raw_interests.split(",") if part.strip()]
    if not preferences:
        print("Please enter at least one interest.")
        return 1

    results = recommend(preferences, items, top_n=args.top, category=args.category)
    print("\nYour interests:", ", ".join(preferences))
    if args.category:
        print("Category filter:", args.category)
    print("\n=== Recommended for you ===")
    if not results:
        print("No matching items found. Try broader interests such as Python, AI, data science, or design.")
        return 0

    for number, item in enumerate(results, start=1):
        print(f"\n{number}. {item['title']} [{item['category']}]")
        print(f"   Match score: {item['score']:.0%}")
        print(f"   Why: matches {', '.join(item['matched_tags'])}")
        print(f"   {item['description']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

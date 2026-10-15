"""Core recommendation logic for DecodeLabs Project 3."""
from __future__ import annotations

import re
from typing import Any, Iterable


def normalize_terms(terms: Iterable[str]) -> set[str]:
    """Normalize comma-separated or individual terms into lowercase tokens."""
    normalized: set[str] = set()
    for term in terms:
        for piece in re.split(r"[,;]", str(term)):
            cleaned = re.sub(r"\s+", " ", piece.strip().lower())
            if cleaned:
                normalized.add(cleaned)
    return normalized


def jaccard_similarity(user_terms: set[str], item_terms: set[str]) -> float:
    """Return Jaccard similarity between two term sets (0.0 to 1.0)."""
    if not user_terms and not item_terms:
        return 0.0
    union = user_terms | item_terms
    return len(user_terms & item_terms) / len(union) if union else 0.0


def recommend(
    preferences: Iterable[str],
    items: list[dict[str, Any]],
    top_n: int = 5,
    category: str | None = None,
) -> list[dict[str, Any]]:
    """Rank items by Jaccard similarity and include match explanations."""
    user_terms = normalize_terms(preferences)
    if top_n < 1:
        raise ValueError("top_n must be at least 1")

    ranked: list[dict[str, Any]] = []
    for item in items:
        if category and item.get("category", "").casefold() != category.casefold():
            continue
        tags = normalize_terms(item.get("tags", []))
        matches = sorted(user_terms & tags)
        score = jaccard_similarity(user_terms, tags)
        if matches:
            ranked.append({
                **item,
                "score": score,
                "matched_tags": matches,
            })

    ranked.sort(key=lambda result: (-result["score"], result.get("title", "").casefold()))
    return ranked[:top_n]


def load_items(path: str = "data/items.json") -> list[dict[str, Any]]:
    """Load recommendation items from a JSON file."""
    import json
    from pathlib import Path

    file_path = Path(path)
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Dataset must be a JSON list")
    required = {"id", "title", "category", "description", "tags"}
    for index, item in enumerate(data):
        if not isinstance(item, dict) or not required.issubset(item):
            raise ValueError(f"Item at index {index} is missing required fields")
        if not isinstance(item["tags"], list):
            raise ValueError(f"Item at index {index} must have tags as a list")
    return data

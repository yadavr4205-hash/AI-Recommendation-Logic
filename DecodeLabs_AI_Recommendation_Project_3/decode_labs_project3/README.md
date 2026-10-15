# DecodeLabs — AI Recommendation Logic (Project 3)

A beginner-friendly content recommendation system built with Python. It asks users for interests, compares them with item tags using Jaccard similarity, ranks matching items, and explains why each result was recommended.

## Features
- Collect interests from interactive input or command-line arguments
- Normalize text and match user preferences to item tags
- Rank recommendations by similarity score
- Show matching interests as explanations
- Optional category filter and configurable number of results
- Unit tests and a small sample dataset

## Requirements
- Python 3.9+
- No third-party packages required

## Run

```bash
python main.py
```

Or provide interests directly:

```bash
python main.py --interests "machine learning, python, data science" --top 5
```

Filter by category:

```bash
python main.py --interests "AI, coding" --category Technology
```

## Algorithm

For user preference set `U` and item's tag set `I`, the system calculates Jaccard similarity:

`similarity(U, I) = |U ∩ I| / |U ∪ I|`

The score is between 0 and 1. A larger score means the item shares more tags with the user's interests. Results are sorted by score (highest first); items with no overlap are omitted by default.

## Project structure

```text
decode_labs_project3/
├── main.py
├── recommender.py
├── data/
│   └── items.json
├── tests/
│   └── test_recommender.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Customize
Edit `data/items.json` to add your own items. Each item should have `id`, `title`, `category`, `description`, and `tags`.

## GitHub upload

1. Create a new repository on GitHub, for example `decodelabs-ai-recommendation`.
2. Extract this project ZIP.
3. Open a terminal in the extracted folder and run:

```bash
git init
git add .
git commit -m "Complete DecodeLabs AI Recommendation Logic Project 3"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/decodelabs-ai-recommendation.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not upload passwords or access tokens.

import unittest

from recommender import jaccard_similarity, normalize_terms, recommend


SAMPLE_ITEMS = [
    {"id": 1, "title": "Python Basics", "category": "Technology",
     "description": "Python introduction", "tags": ["python", "coding"]},
    {"id": 2, "title": "Design Basics", "category": "Design",
     "description": "Design introduction", "tags": ["design", "creativity"]},
    {"id": 3, "title": "Python Data", "category": "Technology",
     "description": "Python and data", "tags": ["python", "data science"]},
]


class RecommendationTests(unittest.TestCase):
    def test_normalize_terms(self):
        self.assertEqual(normalize_terms([" Python, AI ", "python"]), {"python", "ai"})

    def test_jaccard_similarity(self):
        self.assertAlmostEqual(jaccard_similarity({"python", "ai"}, {"python", "data"}), 1 / 3)

    def test_empty_similarity(self):
        self.assertEqual(jaccard_similarity(set(), set()), 0.0)

    def test_recommendation_ranking(self):
        result = recommend(["python"], SAMPLE_ITEMS)
        self.assertEqual([item["title"] for item in result], ["Python Basics", "Python Data"])
        self.assertEqual(result[0]["matched_tags"], ["python"])

    def test_category_filter(self):
        result = recommend(["python", "design"], SAMPLE_ITEMS, category="design")
        self.assertEqual([item["title"] for item in result], ["Design Basics"])

    def test_top_n_validation(self):
        with self.assertRaises(ValueError):
            recommend(["python"], SAMPLE_ITEMS, top_n=0)

    def test_no_match(self):
        self.assertEqual(recommend(["cooking"], SAMPLE_ITEMS), [])


if __name__ == "__main__":
    unittest.main()

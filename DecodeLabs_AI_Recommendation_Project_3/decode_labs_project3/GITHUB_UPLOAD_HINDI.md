# GitHub पर Project Upload करने के Steps

1. GitHub पर login करें और **New repository** बनाएं।
2. Repository का नाम `decodelabs-ai-recommendation` रख सकते हैं।
3. इस ZIP को extract करें।
4. Project folder में terminal/CMD खोलें और नीचे commands चलाएं (YOUR-USERNAME बदलें):

```bash
git init
git add .
git commit -m "Complete DecodeLabs AI Recommendation Logic Project 3"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/decodelabs-ai-recommendation.git
git push -u origin main
```

अगर Git install नहीं है, तो GitHub repository में **Add file → Upload files** से extracted project की files upload कर सकते हैं।

## Run करने के लिए
Python 3 install होने के बाद:

```bash
python main.py
```

Interests लिखें: `python, AI, data science`

## Tests चलाने के लिए

```bash
python -m unittest discover -s tests -v
```

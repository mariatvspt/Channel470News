import json
import glob, os

total = 0

for fname in glob.glob("*.json"):
    with open(fname) as f:
        articles = json.load(f)
        total += len(articles)

print(total)

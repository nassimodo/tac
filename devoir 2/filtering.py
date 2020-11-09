"""Filter out stopwords for word cloud"""

import sys
import nltk
from nltk.corpus import stopwords
import json

tmp_path = "./tmp/"

with open('stopwords_fr.json') as json_file:
    external_sw = json.load(json_file)

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu"]
sw += external_sw['words']
sw += ["ville", "franc", "bruxelles", "conseil", "communale"]
sw = set(sw)

def filtering(year):
    path = f"{tmp_path}{year}.txt"
    output = open(f"{tmp_path}{year}_keywords.txt", "w")

    with open(path) as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)


if __name__ == '__main__':
    chosen_year = sys.argv[1]
    filtering(chosen_year)

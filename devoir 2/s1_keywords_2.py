"""Testing keyword extraction with YAKE"""

import os
import yake
print('Hello World!')
ignored = set(["conseil communal", "conseil général"])

kw_extractor = yake.KeywordExtractor(lan="fr", top=20)
data_path = "./tmp/"
files = os.listdir(data_path)
for f in sorted(files):
    # "Bxl_1855_Tome_I1_Part_1"
    if f.find("1855_ke") != -1:
        #print(f)
        text = open(data_path + f).read()
        keywords = kw_extractor.extract_keywords(text)
        kept = []
        for score, kw in keywords:
            words = kw.split()
            if len(words) > 1 and kw not in ignored: # only bigrams and more
                kept.append(kw)
        print(f"{f} mentions these keywords: {', '.join(kept)}...")

#print(keywords)
print(kept)
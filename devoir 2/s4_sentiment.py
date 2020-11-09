"""Sentiment analysis with Textblob-FR"""

#import sys

from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

data = open("tmp/set_sentiments.txt","r", encoding = "utf-8").read()
data2 = data.split(";")
#print(len(data2)) 
#print(data2[1])



#input_text = sys.argv[1]
sentiments = []
for sent in data2:
    #print(sent)
    blob = tb(sent)
    pola, subj = blob.sentiment
    perc = f"{100*abs(pola):.0f}"
    if pola > 0:
        sent = f"{perc}% positive"
    elif pola < 0:
        sent = f"{perc}% negative"
    else:
        sent = "neutral"
    if subj > 0:
        fact = f"{100*subj:.0f}% subjective"
    else:
        fact = "perfectly objective"
    sentiments.append(f"{sent} ({fact})") 
    print(f"This text is {sent} and {fact}.")
print(sentiments)
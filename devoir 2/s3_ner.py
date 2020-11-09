"""Named-entity recognition with SpaCy"""

from collections import defaultdict
import sys

import spacy
from spacy.lang.fr.examples import sentences 

nlp = spacy.load('fr_core_news_sm')

def test():
    """Basic test on sample sentences"""
    for sent in sentences:
        doc = nlp(sent)
        entities = []
        for ent in doc.ents:
            entities.append(f"{ent.text} ({ent.label_})")
        if entities:
            print(f"'{doc.text}' contains the following entities: {', '.join(entities)}")
        else:
            print(f"'{doc.text}' contains no entities")

def search():
    #text = open("tmp/1855_keywords.txt", encoding="utf-8").read()[:1000000]
    text = open("tmp/1855.txt", encoding= "utf-8").read()[:1000000]
    #text = open("../data/all.txt", encoding= "latin-1").read()[:1000000]
    doc = nlp(text)
    people = defaultdict(int) #cherche toutes les personnes
    organisation = defaultdict(int)
    lieu = defaultdict(int) 
    for ent in doc.ents:
        if ent.label_ == "PER" and len(ent.text) > 3:
            people[ent.text] += 1
        elif ent.label_ == "ORG" and len(ent.text) > 3:
            organisation[ent.text] += 1
        elif ent.label_ == "LOC" and len(ent.text) > 3:
            lieu[ent.text] += 1
    print("liste des personnes:")
    sorted_people = sorted(people.items(), key=lambda kv: kv[1], reverse=True) #trier et afficher les 10 premiers les plus récurrents
    for person, freq in sorted_people[:10]:
        print(f"{person} appears {freq} times in the corpus")
    print("liste des organisations:")
    sorted_organisation = sorted(organisation.items(), key=lambda kv: kv[1], reverse=True) 
    for organisation, freq in sorted_organisation[:10]:
        print(f"{organisation} appears {freq} times in the corpus")
    print("liste des lieux:")
    sorted_lieu = sorted(lieu.items(), key=lambda kv: kv[1], reverse=True) 
    for lieu, freq in sorted_lieu[:10]:
        print(f"{lieu} appears {freq} times in the corpus")


if __name__ == "__main__":
    try:
        if sys.argv[1] == "test":
            test()
        elif sys.argv[1] == "search":
            search()
        else:
            print("Unknown option, please use either 'test' or 'search'")
    except IndexError:
        print("No option, please specify either 'test' or 'search'")

from nltk.tokenize import *
from nltk.corpus import cmudict, wordnet as wn


d = cmudict.dict()

def parseFile(t):
	sentences = []
	with open(t) as text:
		for line in text:
			sentences.append(sent_tokenize(line))
	words = []
	for sentence in sentences:
		for s in sentence:
			words.append(word_tokenize(s))
	return words



def number_of_syllables(word):
	return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]] 


def find_synonyms(word):
	synset = wn.synset(word)
	hyponyms = synset.hyponyms()
	synonyms = sorted(lemma.name() for s in hyponyms for lemma in s.lemmas())
	return "\n".join(synonyms)
	
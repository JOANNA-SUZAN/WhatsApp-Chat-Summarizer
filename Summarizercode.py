import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
nlp = spacy.load('en_core_web_sm')
doc = nlp(required text) 
word_freq = {}
for word in doc:
    if word.text.lower() not in STOP_WORDS:
        if word.text.lower() not in word_freq:
            word_freq[word.text.lower()] = 1
        else:
            word_freq[word.text.lower()] += 1
  
sentence_scores = {}
for sentence in doc.sents:
    for word in sentence:
        if word.text.lower() in word_freq:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_freq[word.text.lower()]
            else:
                sentence_scores[sentence] += word_freq[word.text.lower()]
    
summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
  
summary = ' '.join([str(sentence) for sentence in summary_sentences])
print(summary) 

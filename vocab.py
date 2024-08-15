import numpy as np
from collections import defaultdict
import re

corpus = [
  'I love machine learning',
  'I love deep learning',
  'I love Natural Language Processing',
  'Deep learning is a subset of machine learning'
]

# Tokenize the text
def tokenize_corpus(corpus):
  tokens = [re.findall(r'\b\w+\b', sentence.lower()) for sentence in corpus]
  return tokens

def build_vocab(tokens):
  word_freq = defaultdict(int)
  for sentence in tokens:
    for word in sentence:
      word_freq[word] += 1
  vocab = { word: i for i, (word, _) in enumerate(word_freq.items())}
  return vocab
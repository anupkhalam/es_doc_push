#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:24:06 2018

@author: anup
"""

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


def tokenizer(corpus, params):
    for component in params:
        preprocessed_corpus = eval(component['tokenizer'])(corpus)
    return preprocessed_corpus


def replacer(corpus, params):
    for component in params:
        preprocessed_corpus = corpus.replace(component['replacer'][0], component['replacer'][1])
    return preprocessed_corpus

    
def joiner(corpus, params):
    for component in params:
        preprocessed_corpus = component['joiner'].join(corpus)
    return preprocessed_corpus


def stemmer(corpus, params):
    for component in params:
        stemmer = eval(component['stemmer'])()
        preprocessed_corpus = [stemmer.stem(token) for token in corpus]
    return preprocessed_corpus
    


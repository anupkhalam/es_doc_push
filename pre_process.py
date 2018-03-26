#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:27:04 2018

@author: anup
"""

from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import copy


class EsInputPreprocessing():
    def __init__(self, es_corpus, es_pre_processor):
        self.es_corpus = es_corpus
        self.es_pre_processor = es_pre_processor
    
    
    def es_input_pre_processing(self):
        self.es_pre_processor_sets = len(self.es_pre_processor)
        for es_pre_processor_count in range(1, self.es_pre_processor_sets + 1, 1):
            self.es_pre_processor_set = self.es_pre_processor[es_pre_processor_count]
            self.es_processed_corpus = copy.deepcopy(self.es_corpus)
            
            
            if self.es_pre_processor_set['tokenizer'] is not None:
                self.es_processed_corpus = self.es_token_processor()


            if self.es_pre_processor_set['stemmer'] is not None:
                self.es_processed_corpus = self.es_stemmer_processor()
                
                
            if self.es_pre_processor_set['joiner'] is not None:
                self.es_processed_corpus = self.es_joiner_processor()
                
            
            if self.es_pre_processor_set['replacer'] is not None:
                self.es_processed_corpus = self.es_replacer_processor()
        return self.es_processed_corpus
        
    
    def es_token_processor(self):
        if self.es_pre_processor_set['tokenizer'] == 'word_tokenize':
            self.es_processed_corpus = word_tokenize(self.es_processed_corpus)
            return self.es_processed_corpus


        if self.es_pre_processor_set['tokenizer'] == 'sent_tokenize':
            self.es_processed_corpus = sent_tokenize(self.es_processed_corpus)
            return self.es_processed_corpus


    def es_stemmer_processor(self):
        self.es_tokens = word_tokenize(self.es_corpus)
        if self.es_pre_processor_set['stemmer'] == 'porterstemmer':
            stemmer = PorterStemmer()
            self.es_processed_corpus = [stemmer.stem(token) for token in self.es_processed_corpus]
            return self.es_processed_corpus


        if self.es_pre_processor_set['stemmer'] == 'snowball':
            stemmer = SnowballStemmer("english")
            self.es_processed_corpus = [stemmer.stem(token) for token in self.es_tokens]
            return self.es_processed_corpus


    def es_joiner_processor(self):
        self.es_corpus_joiner = self.es_pre_processor_set['joiner'][0]
        self.es_processed_corpus = self.es_corpus_joiner.join(self.es_processed_corpus)
        return self.es_processed_corpus

    
    def es_replacer_processor(self):
        self.es_corpus_replacer = self.es_pre_processor_set['replacer']
        self.es_processed_corpus = self.es_processed_corpus.replace(self.es_corpus_replacer[0], self.es_corpus_replacer[1])
        return self.es_processed_corpus
        


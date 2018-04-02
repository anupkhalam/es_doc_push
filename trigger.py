#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:41:16 2018

@author: anup
"""

from html_indexer import *


files_location = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/002_tikka'
#files_location = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/001_libre'
#files_location = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/003_test'
index_1_names = ['index_11', 'doc_type_1']
index_2_names = ['index_12', 'doc_type_2']
pre_processor = pre_processor_04
es_index_create(files_location, index_1_names, index_2_names, pre_processor)




es_search_index = 'index_2'
es_search_doctype = 'doc_type_2'
es_user_query = 'What are the responsibilities of Bank Mandiri?'
es_query_pre_processor = {1:{'tokenizer' : 'word_tokenize', # Number '1' denotes first processor set. Any number of processor may be defined in the pipeline.
                             'stemmer' : 'porterstemmer', 
                             'joiner' : [' '], # 'joiner' must be a list with single element.
                             'replacer' : ['the', '$$$']}} # 'replacer' must be a list with two elements. First element: char to be replaced; Second element: Char to be placed.
#es_search_body = {"query": {"multi_match" : {"query": "What are the responsibilities of Bank Mandiri?", "fields": [ "Assumptions", "Scope of Work" ]}}}
es_search_body = {"query": {"multi_match" : {"query": "What are the responsibilities of Bank Mandiri?", "fields": [ "Full Text", "Sections.Section bullets.PART VII YOUR PRESCRIPTION DRUG BENEFITS" ]}}}
d = es_search_processor(es_search_index,es_search_doctype,es_search_body)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:41:16 2018

@author: anup
"""

from html_indexer import *
files_location = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/002_tikka'
index_1_names = ['index_1', 'doc_type_1']
index_2_names = ['index_2', 'doc_type_2']
pre_processor = pre_processor_03
es_index_create(files_location, index_1_names, index_2_names, pre_processor)

import json
import requests
response = requests.get('http://localhost:9200/index_2/_mapping?pretty')
data = response.content.decode()
parsed_data = json.loads(data)
import sys
filename  = open('out1.txt','w')
sys.stdout = filename
def myprint(d):
    for key, value in d.items():
        if key == 'properties':
            return list(value.keys())
        else:
            return myprint(value)
j = myprint(parsed_data)

for p in j:
    print(p)


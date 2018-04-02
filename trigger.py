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
index_1_names = ['index_1', 'doc_type_1']
index_2_names = ['index_2', 'doc_type_2']
pre_processor = pre_processor_03
es_index_create(files_location, index_1_names, index_2_names, pre_processor)


k='<p class="body_Text"><b>Note: Certain policies and contracts may not be covered or fully covered. </b>For example, coverage does not extend to any portion(s) of a policy or contract that the insurer does not guarantee, such as certain investment additions to the account value of a variable life insurance  policy  or  a variable  annuity  contract. There are also various residency requirements and other limitations under Colorado law.</p>'
j=BS(k)


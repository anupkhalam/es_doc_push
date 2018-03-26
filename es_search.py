#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 16:57:47 2018

@author: anup
"""

from elasticsearch import Elasticsearch
from pre_process import EsInputPreprocessing
import warnings
warnings.filterwarnings('ignore')


def es_search_processor(es_search_index, 
                        es_search_doctype, 
                        es_user_query, 
                        es_query_pre_processor, 
                        es_search_processor):
    es_search_instance = EsInputPreprocessing(es_user_query, es_query_pre_processor)
    es_preprocessed_user_query = es_search_instance.es_input_pre_processing()
    es_user_query_search_result = es.search(index = es_search_index, 
                                            doc_type = es_search_doctype, 
                                            body = es_search_processor)
    return es_user_query_search_result
    

    
    
    
    
    

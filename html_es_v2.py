#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:27:48 2018

@author: anup
"""


from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup as BS
import glob
from pre_process import EsInputPreprocessing
import warnings
warnings.filterwarnings('ignore')


def es_index_create(files_location, index_1_names, index_2_names, pre_processor):
    file_list = glob.glob(files_location + '/*.html')
    use_less_attribute_list = ["class", "id", "name", "style", "face", "size", "align", "width", "height", "cellspacing", "cellpadding", "start", "color", "bgcolor", "valign", "start"]
    use_less_tag_list = ['img','meta','title','head','style','table']
    headers_list = ['h1','h2','h3','h4','h5']
    for file_no in range(len(file_list)):
        with open(file_list[file_no]) as f:
            temp_html_file = [line.rstrip() for line in f]
            html_file = ''
            html_strip_file = ''
            for line in temp_html_file:
                html_file += (line + '\n')
                html_strip_file += (line)
            html = html_strip_file

            soup = BS(html)
            headers_indexing_list = []
            try:
                for headers_tag in headers_list:
                    first_tag = soup.find(headers_tag)
                    tag_list=first_tag.parent.findChildren(headers_tag)
                    headers_indexing_list.extend(tag_list)
            except AttributeError:
                pass
            headers_indexing_list = [i.get_text() for i in headers_indexing_list if i is not None]

            soup = BS(html)
            es_full_text = soup.get_text()
            
            for tag in soup():
                for attribute in use_less_attribute_list:
                    del tag[attribute]
            for use_less_tag in use_less_tag_list:
                while len(soup.find_all(use_less_tag)) > 0:
                    tag_string ='soup.' + use_less_tag + '.extract()'
                    exec(tag_string)
            for x in soup.find_all():
                if len(x.text) == 0:
                    x.extract()
    
            
            section_dict_full_text = {}
            section_dict_full_text['Full Text'] = es_full_text
            
            
            section_dict_h1 = {}
            first_h1_tag = soup.find("h1")
            h1_tag_list=first_h1_tag.parent.findChildren('h1')
            for h1_tag in h1_tag_list:
                h1_tag_count=0
                h1_tag_siblings=h1_tag.nextSiblingGenerator()
                h1_tag_sibling_list = []
                for h1_tag_sibling in h1_tag_siblings:
                    if h1_tag_sibling.name in ['h1']:
                        h1_tag_count += 1
                    if h1_tag_count > 0:
                        section_dict_h1[h1_tag.get_text()] = ' '.join(h1_tag_sibling_list)
                        break
                    h1_tag_sibling_list.append(h1_tag_sibling.get_text())
    
    
            section_dict_h2 = {}
            first_h2_tag = soup.find("h1")
            h2_tag_list=first_h2_tag.parent.findChildren('h2')
            for h2_tag in h2_tag_list:
                h1_h2_tag_count = 0
                h2_tag_siblings = h2_tag.nextSiblingGenerator()
                h2_tag_sibling_list = []
                for h2_tag_sibling in h2_tag_siblings:
                    if h2_tag_sibling.name in ['h1','h2']:
                        h1_h2_tag_count += 1
                    if h1_h2_tag_count > 0:
                        section_dict_h2[h2_tag.get_text()] = ' '.join(h2_tag_sibling_list)
                        break
                    h2_tag_sibling_list.append(h2_tag_sibling.get_text())
               
                
            section_dict_h3 = {}
            first_h3_tag = soup.find("h1")
            h3_tag_list=first_h3_tag.parent.findChildren('h3')
            for h3_tag in h3_tag_list:
                h1_h2_h3_tag_count = 0
                h3_tag_siblings = h3_tag.nextSiblingGenerator()
                h3_tag_sibling_list = []
                for h3_tag_sibling in h3_tag_siblings:
                    if h3_tag_sibling.name in ['h1','h2','h3']:
                        h1_h2_h3_tag_count += 1
                    if h1_h2_h3_tag_count > 0:
                        section_dict_h3[h3_tag.get_text()] = ' '.join(h3_tag_sibling_list)
                        break
                    h3_tag_sibling_list.append(h3_tag_sibling.get_text())
    
    
            section_dict_h4 = {}
            first_h4_tag = soup.find("h1")
            h4_tag_list=first_h4_tag.parent.findChildren('h4')
            for h4_tag in h4_tag_list:
                h1_h2_h3_h4_tag_count = 0
                h4_tag_siblings = h4_tag.nextSiblingGenerator()
                h4_tag_sibling_list = []
                for h4_tag_sibling in h4_tag_siblings:
                    if h4_tag_sibling.name in ['h1','h2','h3','h4']:
                        h1_h2_h3_h4_tag_count += 1
                    if h1_h2_h3_h4_tag_count > 0:
                        section_dict_h4[h4_tag.get_text()] = ' '.join(h4_tag_sibling_list)
                        break
                    h4_tag_sibling_list.append(h4_tag_sibling.get_text())
                  
                    
            section_dict = {**section_dict_full_text, **section_dict_h1, **section_dict_h2, **section_dict_h3, **section_dict_h4}
        
        
        for key, value in section_dict.items():
            value_instance = EsInputPreprocessing(value, pre_processor)
            section_dict[key] = value_instance.es_input_pre_processing()
        
        
        es = Elasticsearch()
        es.index(index=index_1_names[0], doc_type=index_1_names[1], id=(file_no + 1), body={"html": html_file, "headers" : headers_indexing_list})
        es.index(index=index_2_names[0], doc_type=index_2_names[1], id=(file_no + 1), body = section_dict)


def es_search_processor(es_sch_doctype, 
                        es_searcearch_index, 
                        es_searh_body):
    es_search = Elasticsearch()
    es_user_query_search_result = es_search.search(index = es_search_index, 
                                            doc_type = es_search_doctype, 
                                            body = es_search_body)
    return es_user_query_search_result



files_location = '/home/anup/03_test_scripts/08_elastic_search/kg'
index_1_names = ['index_1', 'doc_type_1']
index_2_names = ['index_2', 'doc_type_2']
pre_processor = {1:{'tokenizer' : 'word_tokenize', # Number '1' denotes first processor set. Any number of processor may be defined in the pipeline.
                    'stemmer' : 'porterstemmer', 
                    'joiner' : [' '], # 'joiner' must be a list with single element.
                    'replacer' : None}} # 'replacer' must be a list with two elements. First element: char to be replaced; Second element: Char to be placed.
es_index_create(files_location, index_1_names, index_2_names, pre_processor)


es_search_index = 'index_2'
es_search_doctype = 'doc_type_2'
es_user_query = 'What are the responsibilities of Bank Mandiri?'
es_query_pre_processor = {1:{'tokenizer' : 'word_tokenize', # Number '1' denotes first processor set. Any number of processor may be defined in the pipeline.
                             'stemmer' : 'porterstemmer', 
                             'joiner' : [' '], # 'joiner' must be a list with single element.
                             'replacer' : ['the', '$$$']}} # 'replacer' must be a list with two elements. First element: char to be replaced; Second element: Char to be placed.
#es_search_body = {"query": {"multi_match" : {"query": "What are the responsibilities of Bank Mandiri?", "fields": [ "Assumptions", "Scope of Work" ]}}}
es_search_body = {"query": {"multi_match" : {"query": "What are the responsibilities of Bank Mandiri?", "fields": [ "Full Text" ]}}}
d = es_search_processor(es_search_index,es_search_doctype,es_search_body)




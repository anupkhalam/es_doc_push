#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:56:00 2018

@author: anup
"""
import os
print (os.getcwd())
wdr = '/home/anup/03_test_scripts/08_elastic_search/kg'
os.chdir(wdr)
del wdr
print (os.getcwd())

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-09-2012')
print (date2.day)
is_date = Date.is_date_valid('11-09-2012')
print (is_date.day)

from abc import ABCMeta, abstractmethod
import abc
class Estimator(metaclass  = abc.ABCMeta):
    
    @abc.abstractmethod
    def abc1():
        """test 1"""

        
    @abc.abstractmethod
    def abc2():
        """test 2"""
        
#    @abstractmethod
#    def abc3():
#        pass
#    @abstractmethod
#    def abc4():
#        pass
#    
class testclass(Estimator):
    def abc1():
        print ("test1")
        return 42
    def abc2():
        print ("test2")
        return 45
    
    
    
w = Estimator()
p=testclass()
p.abc1

g = p.abc1()
k = p.abc2(1)



import abc

class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""



import abc
#from abc_base import PluginBase


class LocalBaseClass:
    pass


@PluginBase.register
class RegisteredImplementation(LocalBaseClass):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(RegisteredImplementation1,
                                  PluginBase))
    print('Instance:', isinstance(RegisteredImplementation1(),
                                  PluginBase))

class RegisteredImplementation1(PluginBase):

    def load(self, input):
        return input.read()

d = RegisteredImplementation1()

@PluginBase.register
class IncompleteImplementation(PluginBase):

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(IncompleteImplementation,
                                  PluginBase))
    print('Instance:', isinstance(IncompleteImplementation(),
                                  PluginBase))






from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup as BS
import glob
from preprocess_class import EsPreProcessor
import warnings
from html_processing import *

warnings.filterwarnings('ignore')

file = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/002_tikka/BA72-01012018-SOB.html'

with open (file) as f:
    temp_html_file = [line.rstrip() for line in f]
    html_file = ''
    html_strip_file = ''
    for line in temp_html_file:
        html_file += (line + '\n')
        html_strip_file += (line)
    html = html_strip_file


soup = BS(html)


headers_list = ['h1','h2','h3','h4','h5']
for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()
section_dict = {}

for header in range(len(headers_list)):
    header_tag = None
    header_tag = soup.find(headers_list[header])
    header_tag_list = []
    if header_tag is not None:
        header_tag_list = header_tag.parent.findChildren(headers_list[header])
    if len(header_tag_list) == 0:
        break
    for component_tag in header_tag_list:
        header_tag_count = 0
        header_tag_siblings = component_tag.nextSiblingGenerator()
        header_tag_sibling_list = []
        for header_tag_sibling in header_tag_siblings:
#            print (header_tag_sibling)
            if header_tag_sibling.name in (headers_list[:(header + 1)]):
                header_tag_count += 1
            if header_tag_count > 0:
                # may need to add exception for key error
                section_dict[component_tag.get_text()] = ' '.join(header_tag_sibling_list)
                break
            try:
                header_tag_sibling_list.append(header_tag_sibling.get_text())
            except AttributeError:
                pass
#    return section_dict




j = {'abc':{'a1':'b1','a2':'b2','a3':'b3'}}

es = Elasticsearch()
es.index(index='atsc',doc_type = 'sdfr', id = 2, body = j)




from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup as BS
import glob
from preprocess_class import EsPreProcessor
import warnings
from html_processing import *

warnings.filterwarnings('ignore')

file = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/002_tikka/BA72-01012018-SOB.html'

with open (file) as f:
    temp_html_file = [line.rstrip() for line in f]
    html_file = ''
    html_strip_file = ''
    for line in temp_html_file:
        html_file += (line + '\n')
        html_strip_file += (line)
    html = html_strip_file


soup = BS(html)


headers_list = ['h1','h2','h3','h4','h5']
for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()
section_dict = {}
section_dict_tag = {}

for header in range(len(headers_list)):
    header_tag = None
    header_tag = soup.find(headers_list[header])
    header_tag_list = []
    if header_tag is not None:
        header_tag_list = header_tag.parent.findChildren(headers_list[header])
    if len(header_tag_list) == 0:
        break
    for component_tag in header_tag_list:
        header_tag_count = 0
        header_tag_siblings = component_tag.nextSiblingGenerator()
        header_tag_sibling_list = []
        header_tag_sibling_tag_list = []
        #create a blank tag
        new_tag = BS('').new_tag('kgabcdefg')
        
        for header_tag_sibling in header_tag_siblings:
            if header_tag_sibling.name in (headers_list[:(header + 1)]):
                header_tag_count += 1
            if header_tag_count > 0:

                # may need to add exception for key error
                section_dict[component_tag.get_text()] = ' '.join(header_tag_sibling_list)
                section_dict_tag[component_tag.get_text()] = new_tag
                new_tag = BS('').new_tag('kgabcdefg')
                break
            try:
                print ("****************")
                header_tag_sibling_list.append(header_tag_sibling.get_text())
                new_tag.append(header_tag_sibling)
            except AttributeError:
                pass
#    return section_dict

soup = BS(' ')
k = soup.new_tag('kgabcdefg')
soup = BS(' ')
k = soup.new_tag('div')
new_tag.append(k)
new_tag.insert_after(header_tag_sibling)



soup.sometag.name = 'newtag'
soup.newtag.wrap(soup.new_tag('sometag'))





from elasticsearch import Elasticsearch
from bs4 import BeautifulSoup as BS
import glob
from preprocess_class import EsPreProcessor
import warnings
from html_processing import *

warnings.filterwarnings('ignore')

file = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/002_tikka/AMCS-N-G4-000562.html'

with open (file) as f:
    temp_html_file = [line.rstrip() for line in f]
    html_file = ''
    html_strip_file = ''
    for line in temp_html_file:
        html_file += (line + '\n')
        html_strip_file += (line)
    html = html_strip_file


soup = BS(html)


headers_list = ['h1','h2','h3','h4','h5']
for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()
section_dict = {}
section_dict_tag = {}

for header in range(len(headers_list)):
    header_tag = None
    header_tag = soup.find(headers_list[header])
    header_tag_list = []
    if header_tag is not None:
        header_tag_list = header_tag.parent.findChildren(headers_list[header])
    if len(header_tag_list) == 0:
        break
    for component_tag in header_tag_list:
        header_tag_siblings = component_tag.nextSiblingGenerator()
        header_tag_sibling_list = []
        header_tag_sibling_tag_list = []
        new_tag = BS('').new_tag('kgabcdefg')
        for header_tag_sibling in header_tag_siblings:
            if header_tag_sibling.name in (headers_list[:(header + 1)]):
                # may need to add exception for key error
                section_dict[component_tag.get_text()] = ' '.join(header_tag_sibling_list)
                new_tag = BS('').new_tag('kgabcdefg')
                for i in header_tag_sibling_tag_list:
                    new_tag.append(i)
                bundled_bullet_tag_list = []
                bundled_bullet_tag_list = new_tag.find_all('p', class_ = 'list_Paragraph')
                bundled_bullet_text_list = []
                try:
                    bundled_bullet_text_list = [j.get_text() for j in bundled_bullet_tag_list]
                except AttributeError:
                    pass
                if bundled_bullet_text_list:
                    section_dict_tag[component_tag.get_text()] = ' '.join(bundled_bullet_text_list)
                del new_tag
                break
            try:
                header_tag_sibling_list.append(header_tag_sibling.get_text())
                header_tag_sibling_tag_list.append(header_tag_sibling)
            except AttributeError:
                pass
#    return section_dict

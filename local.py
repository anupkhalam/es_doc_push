#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 09:56:00 2018

@author: anup
"""

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
class Estimator(object):
    __metaclass__  = abc.ABCMeta
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
    
    
    
w = Estimator()
p=testclass()
g = p.abc1()
k = p.abc2(1)
   
    
    

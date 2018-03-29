#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:50:08 2018

@author: anup
"""
import glob
import os
# Location of the files
files_location = '/home/anup/03_test_scripts/08_elastic_search/kg/converted/001_libre'

file_list = glob.glob(files_location + '/*.docx')
for file in file_list:
    file_location = file
    terminal_script = '/usr/bin/soffice --headless --convert-to html:HTML --outdir' + \
                      ' ' + files_location + ' ' + file_location
    os.system(terminal_script)

                      


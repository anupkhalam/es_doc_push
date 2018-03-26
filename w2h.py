#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:14:05 2018

@author: anup
"""

import mammoth

with open("Bank Mandiri-UST Global-FRMS_TechnicalProposal_v3.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
    
with open('test.html', 'w') as tht:
    tht.write(html)
    
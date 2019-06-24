# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:28:18 2019

@author: 一文 --最远的你们是我最近的爱
"""

import requests
import json

class Spider:  
    
    def get_html(self, url, encoding = None):
        
        r = requests.get(url)
            
        if encoding == None:
        
            r.encoding= r.apparent_encoding
        
        else:
            
            r.encoding = encoding
            
        return json.loads(r.text)

        
        
    

    
  
    
    
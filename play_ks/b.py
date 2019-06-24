# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:49:16 2019

@author: 一文 --最远的你们是我最近的爱
"""

import requests

import json

url = 'http://101.251.217.216/rest/n/feed/hot?isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=59942a6c1d534a51844dfda37e92afc3&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=23&refreshTimes=7&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=510e56b366931c4cb008c51ee44664c2'

a = requests.get(url).text

b = json.loads(a)

b = b['feeds']

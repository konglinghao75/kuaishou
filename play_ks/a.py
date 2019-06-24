# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:28:18 2019

@author: 一文 --最远的你们是我最近的爱
"""

import jpype
import os


jarpath = os.path.join(os.path.abspath("."), "E:\\play_ks\\")

jvmPath = r'E:\Java\jre1.8.0_101\bin\server\jvm.dll'

jpype.startJVM(jvmPath, "-ea","-Djava.class.path=%s" % (jarpath + 'ks_sig.jar'))  

javaClass = jpype.JClass("SingatureUtil")

t = javaClass()

a='isp=CMCC&mod=vivo%28vivo%20x5m%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_d1f47e9473209293&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560817030537&ver=6.1&retryTimes=1&max_memory=192&photoId=5228679183663739838&user_id=1295159539&pcursor102117525349&order=desc&count=10&photoPageType=0&client_key=3c2cd3f3&os=android'

sig = t.run(a)
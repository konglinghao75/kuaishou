# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:11:53 2019

@author: 一文 --最远的你们是我最近的爱
"""

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

import json

import time

import jpype

from play_ks.ks_spider import Ks_spider

import os

import multiprocessing

from play_ks.klh import kuaishou


def load_jar(q):# 加载jar包
    
    jarpath = os.path.join(os.path.abspath("."), "E:\\ks\\play_ks\\")
        
    jvmPath = r'E:\Java\jre1.8.0_101\bin\server\jvm.dll'
        
    jpype.startJVM(jvmPath, "-ea","-Djava.class.path=%s" % (jarpath + 'ks_sig.jar'))
    
    javaClass = jpype.JClass("SingatureUtil")
        
    info = kuaishou(javaClass).pro()
    
    q.put(info)



def index(request):#首页API随机加载20视频

    
    start=time.time()

    q = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=load_jar, args=[q])
    
    p.daemon = True
    
    p.start()
        
    info = q.get()
    
    index_info = []
        
    for i in info:
        
        try:
        
            if i['main_mv_urls'][1]['url'][0:13] == 'http://txmov2':
                                
                i['play_url'] = i['main_mv_urls'][1]['url']

                index_info.append(i)
                
            
            if i['main_mv_urls'][1]['url'][0:13] != 'http://txmov2':
                
                i['play_url'] = i['main_mv_urls'][0]['url']
                
                index_info.append(i)
                
        except KeyError:
            
            info.remove(i)
            
    index_info = [i for i in index_info if i['play_url'][0:13]=='http://txmov2']
        
       
            
    context = {'filmlist':index_info}
    
    p.terminate()
            
    print('耗时:',time.time()-start)

    
#    return JsonResponse(context)

    return render(request, 'myks/index.html',context)#, context




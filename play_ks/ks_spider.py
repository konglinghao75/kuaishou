# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:11:53 2019

@author: 一文 --最远的你们是我最近的爱
"""
from spider import Spider
from multiprocessing.dummy import Pool
import jpype
import os
#from klh import kuaishou


class Ks_spider:


    def __init__(self,javaClass):#初始化JVM, 
        
        '''
        args: sig_ls 存储破解sig a
              arg_ls 存储data参数
        '''
#        jarpath = os.path.join(os.path.abspath("."), "E:\\ks\\play_ks\\")
#        
#        jvmPath = r'E:\Java\jre1.8.0_101\bin\server\jvm.dll'
#        
#        jpype.startJVM(jvmPath, "-ea","-Djava.class.path=%s" % (jarpath + 'ks_sig.jar'))  
#        
#        self.javaClass = jpype.JClass("SingatureUtil")
        
        self.sig_ls = []
                
        self.t = javaClass()
        
        self.arg_ls = []
        
        self.arg = []
        
    def run(self,args):#破解快手sig码
    
        sig = self.t.run(args)
        
        return self.sig_ls.append(sig)
    
    def get_movies(self):#随机获取20个视频
        
        try:
            
            url = 'http://101.251.217.216/rest/n/feed/hot?isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=59942a6c1d534a51844dfda37e92afc3&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=23&refreshTimes=7&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=510e56b366931c4cb008c51ee44664c2'
            
            return Spider().get_html(url)
        
        except Exception as e :
            
            print(e.args)
    
    def get_first_comment_data(self,info):#获取视频第一次不带pcursor参数的args
        
        datas = []
        
        for i in info['feeds'] :
            
            args = (i['photo_id'],i['user_id'])
            
            datas.append(args)
            
        s_sig_ls = []
        
        for i in datas:
        
            sig_l = 'isp=CMCC&mod=vivo%28vivo%20x5m%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_d1f47e9473209293&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560817030537&ver=6.1&retryTimes=1&max_memory=192'
        
            sig_r = '&photoId='+str(i[0])+'&user_id='+str(i[1])+'&order=desc&count=10&photoPageType=0&client_key=3c2cd3f3&os=android'

            s_sig_ls.append(sig_l+sig_r)
        
        for i in range(len(s_sig_ls)):
            
            print(i)
            
            sig = self.t.run(s_sig_ls[i])
            
            data = (datas[i][0],datas[i][1],sig.lower())
            
            self.arg_ls.append(data)
        
        return self.arg_ls
        
    
    def get_comment(self,args):#获取评论
        
        comment_url = 'http://api.gifshow.com/rest/n/comment/list/v2?isp=CMCC&mod=vivo%28vivo%20x5m%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_d1f47e9473209293&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560817030537&ver=6.1&retryTimes=1&max_memory=192'    
        
        if len(args)==3:#获取作品的第一组评论
            
            sig_r = '&photoId={}&user_id={}&order=desc&count=10&photoPageType=0&client_key=3c2cd3f3&os=android&sig={}'.format(args[0],args[1],args[2])

            comment_url = comment_url + sig_r
            
            return Spider().get_html(comment_url)
        
        if len(args)==4:#获取带有pcursor参数的评论
            
            sig_r = '&photoId={}&user_id={}&order=desc&pcursor={}&count=10&photoPageType=0&client_key=3c2cd3f3&os=android&sig={}'.format(args[0],args[1],args[2],args[3])

            comment_url = comment_url + sig_r
            
            return Spider().get_html(comment_url)
            
    def comment_info(self,args):#多进程获取当前作品评论
        
        p = Pool(10)
        
        return p.map(self.get_comment,args)
    
    def get_all_comment_pro(self,args):
        
        if len(args)==3:#单个评论args参数
            
            info = self.get_comment(args)
            
            next_args = [(args[0],args[1],info['pcursor'])]

        else:#多个视频args参数列表
        
            p = Pool(10)
            
            info = p.map(self.get_comment,args)
        
            next_args = [(args[i][0],args[i][1],info[i]['pcursor'])for i in range(len(args))]
        
        s_sig_ls = []
        
        args_ls = []
        
        for i in next_args:
        
            sig_l = 'isp=CMCC&mod=vivo%28vivo%20x5m%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_d1f47e9473209293&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560817030537&ver=6.1&retryTimes=1&max_memory=192'
        
            sig_r = '&photoId='+str(i[0])+'&user_id='+str(i[1])+'&pcursor='+str(i[2])+'&order=desc&count=10&photoPageType=0&client_key=3c2cd3f3&os=android'

            s_sig_ls.append(sig_l+sig_r)
        
        for i in range(len(s_sig_ls)):
            
            print(i)
            
            sig = self.t.run(s_sig_ls[i])
            
            data = (next_args[i][0],next_args[i][1],next_args[i][2],sig.lower())
            
            args_ls.append(data)
            
            self.arg_ls.append(data)
            
        return args_ls
    
    def do_work(self,args):#构建评论参数队列
        
        while True:
            
            self.arg.append(args)
            
            args = self.get_all_comment_pro(args)
            
            for i in args:
                
                print(i)
                
                print('---------------------------')
                
                if i[2] == 'no_more':
                
                    args.remove(i)
                    
            if len(args) == 0:
                
                print('当前args长度',len(args))
                
                break
            
    def get_args(self,movies,userId):#通过用户ID获取用户当前作品的所有评论
        
        args = self.get_first_comment_data(movies)
        
        print(len(args))
        
        args = [i for i in args if i[1] == userId]
        
        queue = self.get_all_comment_pro(args)
    
        self.do_work(queue)
        
        args = [i[0] for i in self.arg]
                
        return self.comment_info(args)
    
    def close(self):
        
        jpype.shutdownJVM()
        
        print('关闭JVM')
        
    
    
    
if __name__ == '__main__':
    
    x = Ks_spider()
    
    
    
    
        
        






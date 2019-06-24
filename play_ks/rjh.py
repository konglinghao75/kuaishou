# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:55:16 2019

@author: dell
"""

import requests
import os
import jpype

class KuaiShou:

    def __init__(self,javaClass):  #初始化Java虚拟机参数  
        
#        jarpath=os.path.join(os.path.abspath('.'),"D:\\program\\workspace2\\testSolr\\commons-lang3-3.8.jar")
#    
#        jarpath2=os.path.join(os.path.abspath('.'),"D:\\program\\workspace2\\testSolr\\jiemi2.jar")
#        
#        # 使用jpype开启虚拟机（在开启jvm之前要加载类路径）
#        jpype.startJVM("D:\\program\\java\\jdk1.8.0_101\\jre\\bin\\server\\jvm.dll","-ea","-Djava.class.path=%s;%s"%(jarpath,jarpath2))
#        # 加载java类（参数是java的长类名）
#        jpype.JClass("org.apache.commons.lang3.StringUtils")
        
#        self.javaClass = jpype.JClass("test.SingatureUtil")
        
#        sign=javaClass.genSignature(javaClass.getMapFromStr(urlParams),javaClass.FANS_SALT)
        
        self.t=javaClass()
        
        self.ls={}
        
        self.ls2={}
        
        self.rst2=[]
        
        self.pcursor=None
    
    def java(self,srcStr):  #java虚拟机破解调用
        
        sig=self.t.run(srcStr)
        
#        sig=self.javaClass.genSignature(self.javaClass.getMapFromStr(srcStr),self.javaClass.FANS_SALT)
        
#        print(sig.lower())
        
        return sig
    
    def getResponse(self,url):  #联网获取数据,返回json
        
        resp=requests.get(url)
        
        resp.encoding=resp.apparent_encoding
    
        jso=resp.json()
        
        return jso
    
#    @property
#    def get_hot_production(self):  
#        
#        url='http://103.107.217.65/rest/n/feed/hot?isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=8285bb939fb45c67c865b8afb6419baf&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=107&refreshTimes=4&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=ac2716c6c7345d3bdcc8a1c8b5cdcd99'
#        
#        jso=self.getResponse(url)
#        
#        params=jso['feeds']
#        
#        for i in params:
#    
#            caption=i['caption'] #标题
#        
#            comment_count=i['comment_count'] #评论次数
#            
#            down_headUrls=i['headurls'][0]['url'] #封面图片下载地址
#            
#            play_headUrls=i['headurls'][1]['url'] #封面播放地址
#            
#            like_count=i['like_count'] #点赞
#            
#            if 'main_mv_urls' in i.keys():
#            
#                down_main_mv_urls=i['main_mv_urls'][0]['url'] #视频下载地址
#                
#                play_main_mv_urls=i['main_mv_urls'][1]['url'] #视频播放地址 手机app两个网址都可以播放
#            
#            else:
#            
#                down_main_mv_urls=''   
#            
#                play_main_mv_urls=''
#        
#            photo_id=i['photo_id']
#        
#            if 'soundTrack' in i.keys():
#                
#                soundTrack_music_url=i['soundTrack']['audioUrls'][0]['url'] #y音乐链接
#                
#                soundTrack_user_avatarUrls=i['soundTrack']['avatarUrls'][0]['url'] #背景音乐歌手图片地址
#                
#                soundTrack_id=i['soundTrack']['id'] #音乐id
#                
#                soundTrack_artist=i['soundTrack']['artist'] #背景音乐歌手
#                
#                soundTrack_name=i['soundTrack']['name'] #音乐名字
#                
#                soundTrack_type=i['soundTrack']['type'] #音乐类型
#                
#                try:
#                    
#                    soundTrack_user_eid=i['soundTrack']['user']['eid']
#                    
#                except KeyError:
#                    
#                    soundTrack_user_eid=''
#                
#                try :
#                    
#                    kwaiId  =i['kwaiId'] 
#                    
#                except KeyError:
#                    
#                    kwaiId='此账号无快手id'
#                
#            elif 'music' in i.keys():
#                
#                soundTrack_music_url=i['music']['audioUrls'][0]['url'] #y音乐链接
#                
#                soundTrack_user_avatarUrls=i['music']['avatarUrls'][0]['url'] #头像播放地址
#                
#                soundTrack_id=i['music']['id'] #音乐id
#                
#                soundTrack_artist=i['music']['artist'] #艺人
#                
#                soundTrack_name=i['music']['name'] #音乐名字
#                
#                soundTrack_type=i['music']['type'] #音乐类型
#                
#                try:
#                    
#                    soundTrack_user_eid=i['music']['user']['eid']
#                    
#                except KeyError:
#                    
#                    soundTrack_user_eid=''
#                    
#            user_name=i['user_name']
#             
#            user_sex=i['user_sex']
#            
#            user_id=i['user_id']
#            
#            if user_sex=='F':
#                
#                user_sex='女'
#                
#            elif user_sex=='M':
#                
#                user_sex='男'
#                
#            else:
#                
#                user_sex=''
#                
#            time=i['time'] #更新时间
#            
#            timestamp=i['timestamp'] #时间戳
#            
#            view_count=i['view_count'] #浏览次数
#        
#                
#            videoinfo={
#                    'caption':caption,'comment_count':comment_count,\
#                    'down_headUrls':down_headUrls,'play_headUrls':play_headUrls,\
#                    'like_count':like_count,'down_main_mv_urls':down_main_mv_urls,\
#                    'play_main_mv_urls':play_main_mv_urls,'photo_id':photo_id,'soundTrack_music_urls':soundTrack_music_url,\
#                    'soundTrack_user_avatarUrls':soundTrack_user_avatarUrls,'soundTrack_id':soundTrack_id,\
#                    'soundTrack_artist':soundTrack_artist,'soundTrack_name':soundTrack_name,'soundTrack_type':soundTrack_type,\
#                    'soundTrack_user_eid':soundTrack_user_eid,'user_id':user_id,'user_name':user_name,'user_sex':user_sex,'time':time,'timestamp':timestamp,'view_count':view_count
#                    }
#                
#               
#            self.ls2[play_main_mv_urls]=videoinfo
#            
#        return self.ls2
    
    
    def get_productionTop_url(self,url,vurl):
        
        sig=self.java(vurl)
        
        print(sig.lower())
        
        v_url=url+vurl+'&sig='+sig.lower() #获取到拼接的url
        
        print('拼接的url:'+v_url)
        
        jso=self.getResponse(v_url)
        
        return jso
    
#    def get_productionBelow_url(self,url,vurl):
#        
#        sig=self.java(vurl)
#        
#        v_url=url+vurl+'&sig='+sig.lower() #获取到拼接的url
#        
#        jso=self.getResponse(v_url)
#        
#        print(jso)
#        
#        self.rst2.append(jso['feeds'])
#        
#        return jso

    def parseUser1(self,user_id):  #获取用户主页信息(不包含主页发布的视频)
        
    #    url='http://103.107.217.165/rest/n/user/profile/v2?isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&retryTimes=1&max_memory=192&user=1212501318&client_key=3c2cd3f3&os=android&sig=a2247d9c8a44b47fbc45b5aaae92826b'
        
        url='http://103.107.217.165/rest/n/user/profile/v2?'
    
        vurl='isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&retryTimes=1&max_memory=192&user={}&client_key=3c2cd3f3&os=android'.format(user_id)
    
        jso=self.get_productionTop_url(url,vurl)
       
        up=jso['userProfile']
        
        user_name=up['profile']['user_name']
        
        if 'cityName' in jso['userProfile'].keys():
            
            user_cityName=up['cityName'] #城市名称
        
        else:
            
            user_cityName='此用户未填写城市名称'
        
        if 'user_profile_bg_urls' in up['profile'].keys():
            
            if len(up['profile']['user_profile_bg_urls']) > 1:
                
                user_backgroundImage=up['profile']['user_profile_bg_urls'][1]['url'] #用户主页背景图片
            
            else:
                
                user_backgroundImage=up['profile']['user_profile_bg_urls'][0]['url']
    
        else:
            
            user_backgroundImage=''
        
        if 'headurls' in up['profile'].keys():
            
            user_headUrl=up['profile']['headurls'][1]['url']#用户头像
        
        else:
            
            user_headUrl=''
        

        user_fans=up['ownerCount']['fan']  #粉丝量
        
        user_follow=up['ownerCount']['follow']  #关注人数
        
        user_sex=up['profile']['user_sex']  #用户性别
        
        if user_sex=='F':
        
            user_sex='女'
        
        elif user_sex=='M':
            
            user_sex='男'
            
        else:
            
            user_sex=''
        
        user_text=up['profile']['user_text']  #用户简介
        
        user_photo=up['ownerCount']['photo']  #发布视频个数
        
        userInfo={
                'user_name':user_name,'user_sex':user_sex,'user_headUrl':user_headUrl,'user_backgroundimage':user_backgroundImage,'user_fans':user_fans,'user_follow':user_follow,'user_photo':user_photo,
                'user_text':user_text,'user_cityName':user_cityName,
                }
        
        self.ls[user_name]=userInfo
        
        return self.ls
    
#    def parseUser2(self,user_id):
#        
#        url='http://103.107.217.2/rest/n/feed/profile2?'
#        
#        vurl='isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&max_memory=192&token=&user_id={}&lang=zh&count=30&privacy=public&referer=ks%3A%2F%2Fprofile%2F59719804%2F5194339237167842050%2F1_i%2F1636817716625289218_h86%2F8&client_key=3c2cd3f3&os=android'.format(user_id)
#        
#        jso=self.get_productionBelow_url(url,vurl)
#     
#        self.pcursor=jso['pcursor']
#        
#        print(jso['pcursor'])
#        
#        return jso
#    
#    def work(self,user_id,pcursor):
#        
#        url='http://103.107.217.65/rest/n/feed/profile2?'
#    
#        vurl='isp=CMCC&mod=samsung%28sm-g530h%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_e928f0db23263e87&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560816984874&ver=6.1&max_memory=192&token=&user_id={}&lang=zh&count=30&privacy=public&pcursor={}&referer=ks%3A%2F%2Fprofile%2F1212501318%2F5207568557927131014%2F1_i%2F1636761941840220164_h86%2F8&client_key=3c2cd3f3&os=android'.format(user_id,pcursor)
#        
#        try:
#            
#            jso=self.get_productionBelow_url(url,vurl)
#        
#            pcursor=jso['pcursor']
#            
#            print(jso['pcursor'])
#            
#        except Exception as e:
#            
#            print(e.args)
#            
#    def belowProduction(self,user_id):
#        
#        while True:
#            
#            self.work(user_id,self.pcursor)
#            
#            if self.pcursor=='no_more':
#                
#                break
        
if __name__=='__main__':
    
    kuaishou=KuaiShou()
      
#    ls2=kuaishou.get_hot_production 
    
    ls=kuaishou.parseUser1(1061241178)   #传入一个用户id可以查看用户相关信息(不包含个人发布视频)
    
#    one=kuaishou.parseUser2(1348593527)
#    
#    from multiprocessing.dummy import Pool
#    
#    p=Pool(5)
#    
#    two=p.map(kuaishou.belowProduction,[1348593527])
    
    
#    two=kuaishou.belowProduction(1348593527)









































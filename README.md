# kuaishou
爬取快手热门视频，每个视频评论，用户详情数据，用户所有个人作品
过程当中遇到评论，个人作品的签名加密，用的JAVA破解SIG加密在蟒蛇当中调用JAVA，遇到启动虚拟机错误，解决方法初始化类只用用类PUT方法删除只实例化一次JAVA虚拟机对象，ks_sig.JAR为调用JAVA解密的JAR包，ks_spider为评论代码，KLH为热门二十作品，个人所有作品代码，RJH为个人详细信息代码，在写评论和个人作品时遇到参数解密，获取问题，获取热门数据时遇到数据错误问题，解决通过作品ID去用户个人作品信息里找相同作品ID，拿到其中的正确数据，在展示数据时多些一条判断获取可播放正确数据

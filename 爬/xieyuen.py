# xieyuen 的 python 程序整合包
# -*- coding: utf-8 -*-

import requests
import jsonpath
import os

class Crawler: 
    '''
    爬虫类
    使用时要记得调用 main_program

    现有:
        1. Music
            - 音乐爬虫，支持网易云、QQ等平台
        2. Picture
            - 也许是最简单的图片爬虫了
    '''

    def __init__(self, _any):
        self.any = _any
        self.music = self.Music()
        self.picture = self.Picture()

    class Music:

        """
        音乐爬虫awa
        
        支持：
            1.网易云:netease
            2.QQ:qq
            3.酷狗:kugou
            4.酷我:kuwo
            5.百度:baidu
            6.喜马拉雅:ximalaya
        """

        """
        编程思路：
            1.url
            2.模拟浏览器请求
            3.解析网页源代码
            4.保存数据
        """

        def __init__(self, _music):
            self._music = _music

        def get_music_platfrom():
            print("1.网易云:netease\n2.QQ:qq\n3.酷狗:kugou\n4.酷我:kuwo\n5.百度:baidu\n6.喜马拉雅:ximalaya")
            _platfrom = input("输入音乐平台类型:")
            _inverted = Crawler.Music.invert_platfrom(_platfrom)
            return _inverted

        def invert_platfrom(platfrom):
            """
            检测并转换平台参数
            """
            
            match platfrom:
                
                # 网易云 netease
                case 'n'|'net'|'wy'|'wyy'|'wangyi'|'wangyiyun'|'netease':
                    return 'netease'
                
                # QQ qq
                case 'q'|'qq':
                    return 'qq'
                
                # 酷狗 kugou
                case 'kg'|'kugou':
                    return 'kugou'
                
                # 酷我 kuwo
                case 'kw'|'kuwo':
                    return 'kuwo'
                
                # 百度 baidu
                case 'bd'|'baidu':
                    return 'baidu'
                
                # 喜马拉雅 ximalaya
                case 'x'|'xi'|'xmly'|'xmla'|'ximalaya':
                    return 'ximalaya'
                
                # 无法识别
                case _:
                    print(f"【ERROR】\n无法识别到你输入的 '{ platfrom }' 平台，请重新输入.")
                    print("-------------------------------------------------------")
                    Crawler.Music.get_music_platfrom()

        def download_music(url, title, author):

            # 创建文件夹(如果不存在的话)
            if not os.path.exists('.\\music\\'): os.makedirs("music",exist_ok=True)

            path = '.\\music\\{}.mp3'.format(title)

            print('歌曲:{0}-{1},正在下载...'.format(title,author))

            # 下载（这种读写文件的下载方式适合少量文件的下载）
            content = requests.get(url).content
            with open(file = '.\\music\\' + title + ' ' + author + '.mp3',mode='wb') as f:
                f.write(content)
            
            print('下载完毕,{0}-{1},请试听'.format(title,author))
            return True

        def main_program():
            """
            搜索歌曲名称
            :return:
            """
            name = input("请输入歌曲名称:")
            platfrom = Crawler.Music.get_music_platfrom() # 获取搜索的平台
            print("-------------------------------------------------------")

            url = 'https://music.liuzhijin.cn/'
            headers = {
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
                # 判断请求是异步还是同步
                "x-requested-with":"XMLHttpRequest",
            }
            param = {
                "input":name,
                "filter":"name",
                "type": platfrom,
                "page": 1,
            }
            res = requests.post(url=url,data=param,headers=headers)
            json_text = res.json()

            title = jsonpath.jsonpath(json_text,'$..title')
            author = jsonpath.jsonpath(json_text,'$..author')
            url = jsonpath.jsonpath(json_text, '$..url')
            if title:
                songs = list(zip(title,author,url))
                for s in songs:
                    print(s[0],s[1],s[2])
                print("-------------------------------------------------------")
                index = int(input("请输入您想下载的歌曲版本:"))
                Crawler.Music.download_music(url[index],title[index],author[index])
            else:
                print("对不起，暂无搜索结果!")
                return False

    class Picture:

        """
        图片爬虫awa
        """

        def __init__(self, _picture):
            self._picture = _picture

        def main_program(_url: str, _root: str):
            _path = _root + _url.split('/')[-1]
            try:
                if not os.path.exists(_root):
                    os.mkdir(_root)
                if not os.path.exists(_path):
                    _req = requests.get(_url)
                    with open(path, 'wb')as f:
                        f.write(_req.content)
                        f.close()
                        print('图片已保存')
                        return True
                else:
                    print('文件爬取失败')
                    return False
            except:
                print('爬取失败')
                return False

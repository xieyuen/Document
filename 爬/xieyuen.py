# xieyuen 的 python 程序整合包
# -*- coding: utf-8 -*-

import requests
import jsonpath
import os

import fnmatch

# Please call "self.copyright_info()" to view copyright information



class Information:

    '''
        这个 python 文件的信息
    '''

    __license = 'MIT License\n\nCopyright (c) 2023 HIM049\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.'

    def __init__(self, _info): # 初始化，没得说
        self._info = _info
        self.help = self.Help()
    

    # LICENSE 开源协议
    def LICENSE():
        print(Information.__license)

    def license():
        Information.LICENSE()


    def author():
        print('Copyright from xieyuen')


    def help():
        Help.information()


    def copyright_info():
        Information.author()
        print('LICENSE：\n')
        Information.LICENSE()

class Help:

    def __init__(self, _help): # 初始化，没得说
        self._help = _help
        self.Crawler = self.Crawler()
        self.Tools = self.Tools()


    def printHelpMassage(_help_massage):
        print(_help_massage)


    def list():
        print('Help类中有以下函数/类：')
        for i in dir(Help):

            if fnmatch.fnmatch(i, '__*__'): continue

            if fnmatch.fnmatchcase(i, '[A-Z]*'):
                print('类:', end='')
            else:
                print('函数:', end='')
            print(f'{ i }()')


    class List:
        def __init__(self, _list):
            self.list = _list
        
        def Crawler():
            pass


    def information():
        print('这个python包的信息')


    def crawler():
        _help_massage = '一堆爬虫\n使用爬虫记得调用 main_program\n\n现有:\n    1. Music\n        - 音乐爬虫，支持网易云、QQ等平台\n   2. Picture\n        - 也许是最简单的图片爬虫了'
        Help.printHelpMassage(_help_massage)


    def help():
        _help_massage = '这是这个python包的帮助页面'
        Help.printHelpMassage(_help_massage)



    class Crawler:

        def __init__(self, _crawler): # 初始化，没得说
            self._crawler = _crawler


        def main_program():
            _help_massage = '爬虫的主程序，要使用的话请调用它'
            Help.printHelpMassage(_help_massage)


        def music():
            _help_massage = '音乐爬虫awa\n使用爬虫请调用`Crawler.Music.main_program()`这个函数awa\n\n支持:\n    1. 网易云\n    2.QQ\n    3.酷狗\n    4.酷我:kuwo\n    5.百度:baidu\n    6.喜马拉雅:ximalaya'
            Help.printHelpMassage(_help_massage)


        def picture():
            _help_massage = '图片爬虫awa\n使用爬虫请调用`Crawler.Picture.main_program()`这个函数awa'
            Help.printHelpMassage(_help_massage)


    def tools():
        _help_massage = '简单的小工具'
        Help.printHelpMassage(_help_massage)


    class Tools:
        
        def __init__(self, _tools):
            self._tools = _tools


        def chinese_count():
            _help_massage = '计算汉字数量并记录汉字位置\n返回值像这样：\n\n[{"汉字数量": 11,"字母数量": 45,"非字母汉字数量": 14},[1, 9, 19, 81 ...]]\n后面的列表是汉字所在字符串的索引'
            Help.printHelpMassage(_help_massage)

class Crawler: 

    '''
        一堆爬虫
        使用爬虫要记得调用 main_program

        现有:
            1. Music
                - 音乐爬虫，支持网易云、QQ等平台
            2. Picture
                - 也许是最简单的图片爬虫了
    '''

    def __init__(self, _crawler): # 初始化，没得说
        self._crawler = _crawler
        self.music = self.Music()
        self.picture = self.Picture()

    def help():
        Help.crawler()

    class Music:

        """
            音乐爬虫awa
            使用爬虫请调用`Crawler.Music.main_program()`这个函数awa
            
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

        def __init__(self, _music): # 初始化，没得说
            self._music = _music
        

        def help():
            Help.Crawler.music()


        def get_music_platfrom():
            print("1.网易云:netease\n2.QQ:qq\n3.酷狗:kugou\n4.酷我:kuwo\n5.百度:baidu\n6.喜马拉雅:ximalaya")
            _platfrom = input("输入音乐平台类型:")
            _inverted = Crawler.Music.invert_platfrom(_platfrom)
            return _inverted


        def invert_platfrom(platfrom):

            """
                检测并转换平台参数(大小写均可识别)
            """

            _platfrom = str.lower(platfrom) # 将所有的大写字母转化为小写 

            match _platfrom:

                # 网易云 netease
                case '1'|'n'|'net'|'wy'|'wyy'|'wangyi'|'wangyiyun'|'netease'|'网易'|'网易云'|'网易云音乐':
                    return 'netease'

                # QQ qq
                case '2'|'q'|'qq'|'qqmusic'|'qqyinyue'|'qq音乐'|'qq 音乐':
                    return 'qq'

                # 酷狗 kugou
                case '3'|'kg'|'ku'|'kou'|'gou'|'kugou'|'酷狗':
                    return 'kugou'

                # 酷我 kuwo
                case '4'|'kw'|'ko'|'wo'|'kuwo'|'酷我':
                    return 'kuwo'

                # 百度 baidu
                case '5'|'b'|'bd'|'bu'|'baidu'|'百度':
                    return 'baidu'

                # 喜马拉雅 ximalaya
                case '6'|'x'|'xi'|'xmly'|'xmla'|'ximalaya'|'喜马拉雅':
                    return 'ximalaya'

                # 无法识别
                case _:

                    print(f"【ERROR】\n无法识别到你输入的 '{ platfrom }' 平台")
                    __check = int(input('请选择操作：\n [1]重新输入参数\n [2]使用默认值'))
                    print("-------------------------------------------------------")
                    if __check == 1:
                        Crawler.Music.get_music_platfrom()
                    if __check == 2:
                        return 'netease'


        def download_music(url, title, author):

            # 创建文件夹(如果不存在的话)
            if not os.path.exists('.\\music\\'):
                os.makedirs("music",exist_ok=True)

            path = '.\\music\\{}.mp3'.format(title)

            print('歌曲:{0}-{1},正在下载...'.format(title,author))

            # 下载（这种读写文件的下载方式适合少量文件的下载）
            content = requests.get(url).content
            with open(file = '.\\music\\' + title + ' ' + author + '.mp3',mode='wb') as f:
                f.write(content)

            print('下载完毕,{0}-{1},请试听'.format(title,author))
            return True


        def main_program():

            '''
                音乐爬虫主程序
            '''

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
            使用爬虫请调用`Crawler.Picture.main_program()`这个函数awa
        """


        def __init__(self, _picture): # 初始化，没得说
            self._picture = _picture
        

        def help():
            Help.Crawler.picture()


        def main_program(_url: str, _root: str):

            '''
                图片爬虫主程序
            '''

            _path = _root + _url.split('/')[-1]

            try:
                # 创建文件夹（如果 { _root } 不存在的话）
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

class Tools:

    """
        简单的小工具
    """


    def __init__(self, _tools): # 初始化，没得说
        self._tools = _tools
        self.list_sort = self.ListSort()
        self.sysCmd = self.SysCmd()
        self.math = self.Math()


    def help():
        Help.tools()


    def isExistChinese(string):

        '''
            检测字符串内是否存在汉字
        '''

        for char in string:
            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字
                return True

        return False


    def chineseCount(string):

        '''
            计算汉字数量并记录汉字位置
            返回值像这样：

            >>> chinese_count('加油华为 加油China')
            {
                'count': {
                    'chinese': 6, 
                    'alpha': 5, 
                    '_': 1
                }, 
                'chineseIndex': [0, 1, 2, 3, 5, 6]
            }

            后面的列表是汉字所在字符串的索引
        '''
        
        __result = {
            'count': {
                'chinese': 0,
                'alpha': 0,
                '_': 0
            },
            'chineseIndex': []
        }
        __index = 0

        for char in string:

            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字，在isalpha()方法之前判断

                __result['count']['chinese'] += 1
                __result['chineseIndex'].append(__index)

            elif char.isalpha():  # ！汉字也返回 true

                # __result_1["字母数量"] += 1
                __result['count']['alpha'] += 1

            else:

                # __result_1["非字母汉字数量"] += 1
                __result['count']['_'] += 1

            __index += 1
        
        return __result


    def count(string):

        '''
            计算字符数量并记录字符位置

            返回值说明：
            >>>
            'count': 数量
            'index': 索引
            'chinese': 汉字
            'alpha': 字母
                'all': 全部字母
                'lowercase': 小写字母
                'uppercase': 大写字母
            ' ': 空格 space
            '_': 其他(相当于通配符)
            
            后面的列表是汉字所在字符串的索引

            返回值像这样：
            >>> count('加油华为 加油China')
            {
                'count': {
                    'chinese': 6,
                    'alpha': {
                        'all': 5, 
                        'lowercase': 4, 
                        'uppercase': 1, 
                        '_': 0
                    },
                    ' ': 1,
                    '_': 0
                },
                'index': {
                    'chinese': [0, 1, 2, 3, 5, 6],
                    'alpha': {
                        'all': [7, 8, 9, 10, 11],
                        'lowercase': [8, 9, 10, 11],
                        'uppercase': [7]
                    },
                    ' ': [4]
                }
            }
            >>> count('加油华为，加油China')
            {
                'count': {
                    'chinese': 6,
                    'alpha': {
                        'all': 5, 
                        'lowercase': 4, 
                        'uppercase': 1, 
                        '_': 0
                    },
                    ' ': 0,
                    '_': 1
                },
                'index': {
                    'chinese': [0, 1, 2, 3, 5, 6],
                    'alpha': {
                        'all': [7, 8, 9, 10, 11],
                        'lowercase': [8, 9, 10, 11],
                        'uppercase': [7]
                    },
                    '_': [4]
                }
            }
        '''

        __result = {
            'count': { # 数量
                'chinese': 0, # 汉字
                'alpha': { # 字母
                    'all': 0, # 全部
                    'lowercase': 0, # 小写
                    'uppercase': 0, # 大写
                    '_': 0 # 其他
                },
                ' ': 0, # 空格 space
                '_': 0 # 其他
            },
            'index': { # 索引，内容同上
                'chinese': [],
                'alpha': {
                    'all': [],
                    'lowercase': [],
                    'uppercase': [],
                    '_': []
                },
                ' ': [],
                '_': []
            }
        }

        # 开始处理并计数
        for __index in range(len(string)):
            char = string[__index]

            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字，在isalpha()方法之前判断
                __result['count']['chinese'] += 1
                __result['index']['chinese'].append(__index)

            elif char.isalpha():  # ！汉字也返回 true
                __result['count']['alpha']['all'] += 1
                __result['index']['alpha']['all'].append(__index)

                if char.islower(): # 小写字母
                    __result['count']['alpha']['lowercase'] += 1
                    __result['index']['alpha']['lowercase'].append(__index)

                elif char.isupper(): # 大写字母
                    __result['count']['alpha']['uppercase'] += 1
                    __result['index']['alpha']['uppercase'].append(__index)

                else:
                    __result['count']['alpha']['_'] += 1
                    __result['index']['alpha']['_'].append(__index)

            elif char == ' ': # 空格
                __result['count'][' '] += 1
                __result['index'][' '].append(__index)

            else: # 其他
                __result['count']['_'] += 1
                __result['index']['_'].append(__index)

        # 删除字典里值为 0 对应的索引
        for i in __result['count']:

            if isinstance(__result['count'][i], dict):
            
                for j in __result['count'][i]:
                    if __result['count'][i][j] == 0:
                        del __result['index'][i][j]
                        if j == 'all':
                            del __result['index'][i]
                            __result['count'][i] = 0
                            continue
            
            else:
            
                if __result['count'][i] == 0:
                    del __result['index'][i]

        return __result


    def listDedup(_list): # List dedup

        '''
            给列表不打乱顺序地去重
        '''

        result = []
        for i in _list:

            if i not in result:
                result.append(i)

        return result


    class Math:

        def __init__(self, _math): # 初始化，没得说
            self._math = _math
            self.constant = self.Constant()
        

        def sum(_expressions,_start,_stop):
            
            '''
                sum(关于x的表达式(需要定义成函数/方法), 起始值, 终值)
                起始值必须大于终值
            '''
            
            __sum = 0
            x = _start

            pass
            while x <= _stop:
                __sum += _expressions(x)
                x += 1
            
            return __sum

        
        class Constant:

            def __init__(self, _c): # 初始化，没得说
                self._c = _c

            def e():
                '''
                    Nature Constant
                    e = lim_{x \\to 0} ( 1 + \\frac{1}{x} ) ^{x}
                '''
                # lim_{x \to 0} ( 1 + \frac{1}{x} ) ^{x} = e
                __x = 2**52
                __e = (1 + 1/__x) ** __x
                return __e


    class ListSort:

            
        def __init__(self, _ListSort): # 初始化，没得说
            self._ListSort = _ListSort
            # self.list_sort = self.ListSort()
            # self.sysCmd = self.SysCmd()
        

        def bubble(numList):

            for i in range(len(numList)-1):

                for j in range(len(numList)-i-1):
                    if numList[j] > numList[j+1]:
                        numList[j], numList[j+1] = numList[j+1], numList[j]
            
            return numList
        
        def select(numList):
            for i in range(len(numList) - 1):
                _min = i
                for j in range(i+1, len(numList)):
                    if numList[j] < numList[_min]:
                        _min = j
                        numList[_min], numList[i] = numList[i], numList[_min]
            
            return numList
        

        def insertion(numList):

            for i in range(1,len(list)):

                j = i-1
                key = list[i]
                while j >= 0:
                    if numList[j] > key:
                        numList[j+1] = numList[j]
                        numList[j] = key
                    j -= 1

            return numList
        
        # def count(numList):
            
        #     clist = []
        #     clist[0] = []
        #     clist[1] = []

        #     for i in numList:
        #         if i not in clist[0]:
        #             clist


    class SysCmd:

        '''
            系统命令包
            仅限 Windows
        '''


        def __init__(self, _SysCmd): # 初始化，没得说
            self._SysCmd = _SysCmd


        def cmd(command):

            '''
                执行系统（cmd）命令
            '''

            os.system(command)


        def mkdir(_file_name):

            '''
                创建文件夹
            '''

            # os.makedirs(f'.\\{ _file_name }\\')
            Tools.SysCmd.cmd(f'mkdir ".\\{ _file_name }\\"')


        def md(_file_name):

            """
                mkdir 的别名
            """

            Tools.SysCmd.mkdir(_file_name)

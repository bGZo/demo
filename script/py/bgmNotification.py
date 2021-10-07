#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- author: bGZoCg -*-
# -*- update: 2021-08-12 -*-
# -*- third search enginee: https://www.agefans.cc/search?query=%s&page=1 -*-
# -*- NPM Json: https://github.com/bangumi-data/bangumi-data 
#               https://www.npmjs.com/package/bangumi-data -*-
# -*- Comic Wesite: https://m.manhuagui.com -*-
# -*- friend link:
#       - https://bgmlist.com
#       - https://www.agefans.cc
#       - https://m.manhuagui.com
#       - https://jsdelivr.com -*-

'function: get the daily animate, and the progress of comic'
__author__ = 'bGZoCg'

from tqdm import tqdm
import unicodedata
import requests
import datetime
import re
import json
import time

'''JSON Format Info
{'title': '平穏世代の韋駄天達', 'titleTranslate': 
{'zh-Hans': ['平稳世代的韦驮天们'], 'zh-Hant': ['平穩世代的韋駄天們']}, 
 'type': 'tv', 'lang': 'ja', 'officialSite': 'https://idaten-anime.com/', 
 'begin': '2021-07-22T15:55:00.000Z', 'broadcast': 'R/2021-07-22T15:55:00.000Z/P7D',
 'end': '', 'comment': '', 'sites': [{'site': 'bangumi', 'id': '312723'}, 
 {'site': 'gamer', 'id': '113084', 'begin': '2021-07-22T16:30:00.000Z', 
 'broadcast': 'R/2021-07-22T16:30:00.000Z/P7D'}]}
'''

def get_json_to_dict(url):
    r = requests.get(url, auth=('user', 'pass')) # Basic Auth
    data = json.loads(r.text)
    _ans = data['items']
    return _ans
    # TODO: dict how to trnasform json
    # 1. regex re.Match.groupdict(default=None)

def get_today_date(command):
    if command == 'y':
        return str(time.strftime('%Y',time.localtime(time.time())))
    if command == 'm':
        return str(time.strftime('%m',time.localtime(time.time())))
    if command == 'd':
        return str(time.strftime('%d',time.localtime(time.time())))
    if command == 'yy':
        return str(time.strftime('%y',time.localtime(time.time())))
    if command == 'date':
        return datetime.date.today()

def str2week(String):
    # NOTE: Data Format: 2021-07-16T16:00:00.000Z
    y = int(String[0:4])
    m = int(String[5:7])
    d = int(String[8:10])
    w = datetime.date(int(y),int(m),int(d))
    return w.weekday()

def get_unend_dict(Dict):
    unendDict = {}
    index = 0
    for i in Dict:
        if i['end'] == "":
            unendDict[index] = i
            # FIXME: how to add sub_dict don't use index???
            index += 1
    return unendDict

def get_doublet_list(bgmDict):
    T = get_today_date('date')
    Today = T.weekday()
    index = 0
    todayList = []
    tomorrowList = []
    for i in range(len(bgmDict)):
        data_string = bgmDict[index]['begin']
        data_week = str2week(data_string)
        if Today == data_week:
            if int(bgmDict[index]['begin'][11:13])+8 < 24:
                todayList.append(index)
            else:
                tomorrowList.append(index)
        index += 1
        '''
        # for i in bgmDict:
        Traceback (most recent call last):
        File "./ttttest.py", line 80, in <module>
            print(i['begin'])
        TypeError: 'int' object is not subscriptable
        '''
    return todayList, tomorrowList

def wide_chars(s):
    # return the extra width for wide characters
    # ref: http://stackoverflow.com/a/23320535/1276501
    # directly used from https://www.cxyzjd.com/article/m0_50794428/114491369
    return sum(unicodedata.east_asian_width(x) in ('F', 'W') for x in s)
def print_dict_refer_list(List, Dict):
    for i in List:
        if int(Dict[i]['begin'][11:13]) >= 16:
            Time = int(Dict[i]['begin'][11:13]) - 16
        else:
            Time = int(Dict[i]['begin'][11:13]) + 8
        # print('[%d%s]' % (Time,(Dict[i]['begin'][13:19])), end='')
        print('[{0}{1}]'.format(Time, Dict[i]['begin'][13:19]), end='')
        # NOTE:new print way via https://stackoverflow.com/questions/11146190/
        # python-typeerror-not-enough-arguments-for-format-string


        titleWordLimit = 40
        try:
            Title = Dict[i]['titleTranslate']['zh-Hans'][0]
        except:
            Title = Dict[i]['title']
        formerTitle = Title[0:titleWordLimit]
        fmt = '{0:<%s}' % (titleWordLimit - wide_chars(formerTitle))
        print(fmt.format(formerTitle), end='')
        # NOTE: a little counter- intuitive is table up and down align is called 
        # text-align(水平对齐), and a row align is called vertical align. 
        # TODO: I directly use code via https://blog.tankywoo.com/2017/01/21/
        # python-cli-chinese-align-and-encoding-continue.html, and also 
        # https://www.cxyzjd.com/article/m0_50794428/114491369 and 
        # https://stackoverflow.com/questions/23320148/
        # how-to-control-output-format-when-chinese-characters-and-ascii-mixed
        # give me importent ideas in formatting chinese, Japenese, English aligin.

        try:
            print('@https://'+ Dict[i]['sites'][0]['site']+'.tv/subject/'\
                + Dict[i]['sites'][0]['id'], end = '')
        except: pass
        print(' @https://www.agefans.cc/search?query='+ Title.replace(' ', '+') +'&page=1')

def get_comic_progress_ref_list(List):
    _ans = []
    root = 'https://m.manhuagui.com'

    s = requests.Session() # NOTE: # redirect
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    for i in tqdm(range(len(List)), leave=False):
        urlStr = root + '/comic/'+ List[i]
        r = s.get(urlStr)
        html = r.text
        Title = re.findall(r'<div class="main-bar bar-bg1"><h1>(.*?)<\/h1><\/div>', html)
        Chapter = re.findall(r'<a href=".*?"><b>(.*?)<\/b>', html)
        # FIXME: use BeautifulSoup make code to stronger, cause the tag isn't all same.

        time.sleep(2.5)
        _ans.append(Title[0] +' had Update '+ Chapter[0] + ' @ ' + urlStr)
    return _ans
    # soup = BeautifulSoup(html, features='lxml')
    # allChapterList = soup.find_all('div',{'class':'chapter-list'})
    # test = allChapterList.find_all('li')
    # print( allChapterList[0].get_text() )
    # try:
        # html = urllib.request.urlopen(urlStr, timeout=5).read().decode('utf-8')
    # response = requests.get(urlStr, headers=myheaders)
    # if response.status_code == 200:
        # print(response.text)
    # except:
        # print(urlStr)
    # print(html)
    # soup = BeautifulSoup(html, features='lxml')
    # allChapterList = soup.find_all('chapter-list')
    # print(allChapterList)

# def time_regex_filter_list(time, BgmList):
#     step = 0
#     regex = str(time) + '.*'
#     _ans = []
#     for i in BgmList:
#         if re.match( regex, i['begin']):
#             temp = ''
#             temp += ( str(step) + ', ' + i['begin'])
#             try: # is simple than is judge
#                 temp += (i['titleTranslate']['zh-Hans'][0])
#             except:
#                 temp += (i['title'])
#             _ans.append(temp)
#             step += 1
#     return _ans

if __name__ == '__main__':

    # Inital Config
    comicList = [
        '25878', # 枪之勇者重生录
        '26332', # 回复术士的重来人生
        '41059', # 平稳世代的韦驮天们
        '30037', # 异种族风俗娘评鉴指南
    ]
    itemsDict = get_json_to_dict('\
        https://cdn.jsdelivr.net/npm/bangumi-data@0.3/dist/data.json')


    bgmDict = get_unend_dict(itemsDict)
    # TODO: how to get the bgmDict ordered. Now I just used the index of index.
    # And which one is better. Directly former but really??? like following:
    # >>> bgmDict = bgmDict.sort(key = lambda x: x['begin'][11:19])
    # [error]AttributeError: 'dict' object has no attribute 'sort'

    (todayList, tomorrowList) = get_doublet_list(bgmDict)
    todayList.sort(key = lambda x: bgmDict[x]['begin'][11:19])
    tomorrowList.sort(key = lambda x: bgmDict[x]['begin'][11:19])
    # NOTE: not directly use time_string('brgin'), it will be order by year, month,
    # day, time and so on. we only need time order. 
    # Thx nice function: https://blog.csdn.net/stan_pcf/article/details/51969878
    
    print('今天准备放送:')
    print_dict_refer_list(todayList, bgmDict)
    print('明天预计放松:')
    print_dict_refer_list(tomorrowList, bgmDict)
    print('\n--漫画爬取进度:--')
    List = get_comic_progress_ref_list(comicList)
    for i in List: print(i)
    
    # FIXME: 多线程打印进度条?
    # FIXME: 现在调试只知道中间输出结果, 运行时无法调试....
    # NOTE: wsl line size: 4361-5383

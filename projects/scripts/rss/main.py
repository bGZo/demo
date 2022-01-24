import requests

loginUrl = 'https://rss.anyant.com/api/v1/user/login/'
favUrl = 'https://rss.anyant.com/api/v1/story/favorited'
data = {"account": "", "password": ""}

header = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    # 'cookie': ''
    }


r = requests.post(url, headers=header, )
c = requests.utils.dict_from_cookiejar(r.cookies)
header['cookie'] = 'sessionid='+c['sessionid']

fav = requests.get(favUrl, headers=header)

print(fav.text)
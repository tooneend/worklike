import requests
import json
import re
import pprint
from bs4 import BeautifulSoup

#实现b站视频获取
headers = { 
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'cookie': "",
    'referer': 'https://www.bilibili.com/video/BV1YA4y1R7RJ/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=6b8d0d4d6f716f69096850c4c4e05340'
    }                               #爬不到加cookie和referer，记得加cookie
url = 'https://www.bilibili.com/video/BV1YA4y1R7RJ'                                #自己换bv号
req = requests.get(url=url,headers=headers)
req.encoding = 'utf-8'
soup = BeautifulSoup(req.text,'lxml')
title = soup.find('h1',class_='video-title tit').string                                 #bs4查找，在最里层标签时.string直接取出标签内的文本
playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>',req.text)[0]           #查找，playinfo=.*?

playjson = json.loads(playinfo)
voice = playjson['data']['dash']['audio'][0]['baseUrl']
video = playjson['data']['dash']['video'][0]['baseUrl']

reqe1 = requests.get(headers=headers,url=voice)
sy = reqe1.content
reqe2 = requests.get(headers=headers,url=video)
sp = reqe2.content
with open('{}.mp3'.format(title),'wb') as f:
    f.write(sy)
    f.close
with open('{}.mp4'.format(title),'wb') as f:
    f.write(sp)
    f.close
#一个是视频一个是音频
#print(type(playjson))            #输出类型，验证是否转化成功
#pprint.pprint(playjson)         #格式化输出
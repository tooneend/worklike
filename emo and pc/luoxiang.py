import requests
import json
import re
import csv
import time

headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
           'cookie': ""}    #cookie是要自己加的
bvbecomeav = 'https://api.bilibili.com/x/web-interface/view'
centerapi = 'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&type=1&mode=3&plat=1'

def bvzhuangav(bv:str):
    res = requests.get(url=bvbecomeav,params={'bvid':bv},headers=headers)
    av = str(res.json()['data']['aid'])
    return av                                            #用于把bv转化为av号

def ismain(url:str):
    bv = url.split('/')[-1]
    av = bvzhuangav(bv)
    delter = re.compile(r'{.*}')        # 去除外层的jquery括号，让数据能被json解析
    params={'jsonp':'jsonp','type':1,'oid':av,'mode':3,'plat':1}     # 构造参数,可以在控制台里找到其他不需要改的参数的值
    headers['referer'] = url # 修改referer为当前视频url
    next = 0               # 初始值为0
    f = open('E:/pclx/emo and pc/reply.csv','w',encoding='utf-8',newline='')
    cvw = csv.writer(f)
    cvw.writerow(['用户名','评论'])
    while True:
        params['next'] = next
        response = requests.get(url=centerapi,params=params,headers=headers)
        json_text = delter.search(response.text).group(0)
        is_end = json.loads(json_text)['data']['cursor']['is_end']
        if is_end:                         # is_end为True就break
            break
        replies_info = json.loads(json_text)['data']['replies']
        for i in replies_info:
            zhenreply = i['content']['message']
            personname = i['member']['uname']
            cvw.writerow([personname,zhenreply])
        if next!=0:                       # 第一组next为0，第二组next为2，之后依次+1递增，next设为0和1返回数据一样。为了和实际保持一样，出此下策
            next+=1
        else:
            next+=2
        time.sleep(0.2)                   #调时间防止反爬
    f.close()
ismain('https://www.bilibili.com/video/BV1YA4y1R7RJ')
#出现报错， 爬取失败应该是ip问题，ip连续访问太多次被禁止了，过段时间或者换ip就可以，最好隔时间隔长一点，不然还是容易报错，还有视频评论多也容易报错
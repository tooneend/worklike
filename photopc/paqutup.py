from selenium import webdriver                                       #模拟浏览器
import requests
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains                    #模拟鼠标操作
from selenium.webdriver.common.keys import Keys                                    #模拟键盘操作

mosturl = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E7%88%B1%E8%8E%89%E5%B8%8C%E9%9B%85'
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')           #好像可以防止检测，加不加都行？
chromelink = webdriver.Chrome(chrome_options=options)                               #模拟谷歌浏览器
chromelink.get(mosturl)
time.sleep(3)

ele1 = chromelink.find_element(by=By.NAME,value='pn0')                      #查找位置，用name来找到位置
url = ele1.get_attribute('href')                                           #得到href内容，element可以用，elements不能
ActionChains(chromelink).move_to_element(ele1).perform()                #这里悬停，悬不悬都行，主要用来看反应看看找没找到位置
chromelink.get(url)                                                #打开新的网页，由于这里是href超链接，导致click失效，所以用这种方法
#chromelink.switch_to.window(chromelink.window_handles[1])                #这个用于切换窗口
time.sleep(3)                                                  #每次打开网页休息3秒
num = 20
imgname = 1
for i in range(1,num+1):
    ele2 = chromelink.find_element(By.CSS_SELECTOR,'img[log-rightclick]')                    #用css查找位置
    img = ele2.get_attribute('src')
    r = requests.get(img)
    with open('photo/{}.jpg'.format(imgname),'wb') as f:
        f.write(r.content)
        f.close
    imgname = imgname+1
    ele3 = chromelink.find_element(By.CLASS_NAME,'img-next')                  #用class找到切换按钮的位置
    ele3.click()                                                           #点击按钮打开下一张图片,这个时候有加载东西，为了防止网络波动都要休息一下
    time.sleep(1)                                                        #休息一秒加载东西
    

chromelink.quit()                                                  #关闭模拟浏览器
import cv2 as cv       
import numpy as np         

img = cv.imread('E:/pclx/faceshibie/liuhuaqiang.jpg')               #读取图片
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)                          #灰度处理
facemodel = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')     #导入模型，模型是opencv训练好的模型
face = facemodel.detectMultiScale(gray,1.01,5)                       #模型的detectMultiScale函数用于检测人脸，并用矩形保存人脸的坐标和大小
for x,y,w,h in face:
    cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=1)                 #在人脸处做矩形，（0，0，255）是红色
    cv.circle(img,center=(x+int(w/2),y+int(h/2)),radius=60,color=(255,0,0),thickness=1)  #做圆形


cv.imshow('photo',img)                        #''内是窗口标题,用于展示图片
cv.waitKey(0)
cv.destroyAllWindows()
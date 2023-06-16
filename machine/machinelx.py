import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
import jieba
from sklearn.model_selection import train_test_split
import numpy as np
import joblib

data = pd.read_csv('weibo_senti_100k.csv',encoding='utf-8')                        #读取数据
x_train,x_test,y_train,y_test = train_test_split(data['review'],data['label'],test_size=0.2)    #将数据分为训练集和测试集
with open('cn_stopwords.txt','r',encoding='utf-8') as f:
    stopwords = f.read()                                                        #读取停用词
with open('hit_stopwords.txt','r',encoding='utf-8') as f:
    stopwords2 = f.read()
stopwords = stopwords + stopwords2                   #两组停用词合成一组
def fengci(datatxt):
    mostword = []
    for i in datatxt:
        words = []
        word = jieba.cut(i)
        for j in word:
            if j not in stopwords:
                words.append(j)
        mostword.append(' '.join(words))          #这里join返回的是字符串，使得mostword是字符串形式
    return mostword                               #分词函数

tf_vect = TfidfVectorizer(analyzer='word')             #建立TF模型,lowercase默认为true，将大写转化为小写
train_tf = tf_vect.fit_transform(fengci(x_train))
test_tf = tf_vect.transform(fengci(x_test))                            #用TF模型处理训练集和测试集的自变量

lr = SGDClassifier(loss='log',penalty='l1')                         #建立SGD模型
lr.fit(train_tf,y_train)                                        #训练模型，注意这里用TF处理过的
y_pred = lr.predict(test_tf)                                  #预测，注意这里用TF处理过的
print(y_pred)

zhunque = sum(y_pred==y_test)/len(y_test)                        #判断准确率
print(zhunque)

joblib.dump(lr,'SGD.pkl')                          #保存模型
joblib.dump(tf_vect,'TFV.pkl')
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist                             #加载Fashion MNIST数据集，包含70,000张28x28像素的灰度图像和对应的标签
(x_train,y_train),(x_test,y_test) = data.load_data()             #分割训练集测试集

x_train = x_train/255.0
x_test = x_test/255.0                                    # 预处理数据，将像素值缩放到0到1之间

seq = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),          # 展平层，将图像从二维数组变成一维数组
    keras.layers.Dense(128, activation=tf.nn.relu),     # 全连接层，包含128个神经元，激活函数为ReLU
    keras.layers.Dense(10, activation=tf.nn.softmax)        #输出层，包含10个神经元，激活函数为Softmax，用于分类
])                                   #创建模型

seq.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)                                 # 编译模型，使用Adam优化器和稀疏分类交叉熵作为损失函数

seq.fit(x_train,y_train,epochs=5)                    #训练模型,epochs=5意思是迭代五次

seq.save('face.h5')                                   #保存模型

test_loss, test_acc = seq.evaluate(x_test, y_test)         # 评估模型，返回损失值和精度
print(test_acc)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:09:15 2018

@author: Gif
"""

from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
import numpy as np
X = [[4, 10], 
     [7, 10], 
     [4, 8], 
     [6, 8], 
     [3, 4], 
     [2, 2], 
     [5, 2], 
     [10, 5], 
     [12, 6], 
     [11, 4], 
     [9, 3], 
     [12, 3]]
# dataset = np.mat(X)
dataset = X
if __name__ == '__main__':
    estimator = KMeans(n_clusters=4)
    # fit_predict表示拟合+预测，也可以分开写
    res = estimator.fit_predict(dataset)
    # 预测类别标签结果
    lable_pred = estimator.labels_
    # 各个类别的聚类中心值
    centroids = estimator.cluster_centers_
    # 聚类中心均值向量的总和
    inertia = estimator.inertia_
    for i in range(len(dataset)):
        if int(lable_pred[i]) == 0:
            plt.scatter(dataset[i][0], dataset[i][1], color='red')
            # plt.scatter(centroids[i][0],centroids[i][1],color='blue')
        if int(lable_pred[i]) == 1:
            plt.scatter(dataset[i][0], dataset[i][1], color='black')
        if int(lable_pred[i]) == 2:
            plt.scatter(dataset[i][0], dataset[i][1], color='blue')
        if int(lable_pred[i]) == 3:
            plt.scatter(dataset[i][0], dataset[i][1], color='green')
    plt.show()

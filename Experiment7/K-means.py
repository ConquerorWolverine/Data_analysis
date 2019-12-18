# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:09:15 2018

@author: Gif
"""

from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
import sklearn.datasets as datasets
# import numpy as np

wine = datasets.load_wine()
wine_data = wine.data

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
dataset = wine_data
# print(dataset)
if __name__ == '__main__':
    estimator = KMeans(n_clusters=13)
    # fit_predict表示拟合+预测，也可以分开写
    res = estimator.fit(dataset)

    # print(res)
    # 预测类别标签结果
    lable_pred = estimator.labels_
    print(lable_pred)
    # 各个类别的聚类中心值
    centroids = estimator.cluster_centers_
    print(centroids)
    # 聚类中心均值向量的总和
    inertia = estimator.inertia_
    print(inertia)
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
        if int(lable_pred[i]) == 4:
            plt.scatter(dataset[i][0], dataset[i][1], color='aliceblue')
        if int(lable_pred[i]) == 5:
            plt.scatter(dataset[i][0], dataset[i][1], color='yellow')
        if int(lable_pred[i]) == 6:
            plt.scatter(dataset[i][0], dataset[i][1], color='chocolate')
        if int(lable_pred[i]) == 7:
            plt.scatter(dataset[i][0], dataset[i][1], color='darkgray')
        if int(lable_pred[i]) == 8:
            plt.scatter(dataset[i][0], dataset[i][1], color='azure')
        if int(lable_pred[i]) == 9:
            plt.scatter(dataset[i][0], dataset[i][1], color='hotpink')
        if int(lable_pred[i]) == 10:
            plt.scatter(dataset[i][0], dataset[i][1], color='lightsalmon')
        if int(lable_pred[i]) == 11:
            plt.scatter(dataset[i][0], dataset[i][1], color='mintcream')
        if int(lable_pred[i]) == 12:
            plt.scatter(dataset[i][0], dataset[i][1], color='orchid')
    plt.show()

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:04:58 2018

@author: Gif
"""

import scipy.cluster.hierarchy as hcluster 
import sklearn.datasets as datasets 
import matplotlib.pyplot as plt
iris = datasets.load_iris()  # iris 是一个有标签的数据集 

iris_data = iris.data  # 直接可以得到除去标签和其他内容而得到纯数据
# 生成点与点之间的距离矩阵,这里用的欧氏距离:
# disMat = hcluster.distance.pdist(iris_data,'euclidean')
# print(disMat)
# 进行层次聚类
# Z=hcluster.linkage(disMat,method='complete')
# Z=iris_data
# print (Z)
# P = hcluster.dendrogram(Z)
# plt.show()

# 根据linkage matrix Z得到聚类结果:
result = hcluster.fclusterdata(iris_data, criterion="maxclust", t=6)
print(iris_data)
print(result) 
for i in range(len(result)):
    if int(result[i]) == 4:
        plt.scatter(iris_data[i][0], iris_data[i][1], color='red')
        # plt.scatter(centroids[i][0],centroids[i][1],color='blue')
    if int(result[i]) == 1:
        plt.scatter(iris_data[i][0], iris_data[i][1], color='black')
    if int(result[i]) == 2:
        plt.scatter(iris_data[i][0], iris_data[i][1], color='blue')
    if int(result[i]) == 3:
        plt.scatter(iris_data[i][0], iris_data[i][1], color='green')
    if int(result[i]) == 5:
        plt.scatter(iris_data[i][0], iris_data[i][1], color='yellow')
    if int(result[i]) == 6:
        plt.scatter(iris_data[i][0], iris_data[i][1], color='purple')
plt.show()

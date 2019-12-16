import csv
import mmh3
from bitarray import bitarray
import math
import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

dictionary = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for k in range(5, 8):

	Malicious_URL = 1000000
	size = range(1000000, 10000000, 1000000)
	X = []
	Y = []

	for i in size:
		X.append(i // 1000000)
		'''
		k = ((i//Malicious_URL)*math.log(2,math.e))
		error_probability = (1 - math.e**(-k*Malicious_URL/i))**k
		if (k<1) or (k-(k//1)>0.5):
			k += 1
		int(k)
		'''
		# k = 7
		# k+=1
		# print(error_probability,'\t',int(k))
		bit_array = bitarray(i)
		bit_array.setall(0)
		r = csv.reader(open("G:\\学习资料\\2019年秋季学期\\数据分析\\Python试用\\2019_10_14\\Experiment4\\top1m.csv"))
		for row in r:
			url = row[1]
			# i1 = 0
			for i1 in range(0, k):
				b = mmh3.hash(url, 41 + i1) % i
				bit_array[b] = 1

		# 现在，已经得到了比特串

		r2 = csv.reader(open("G:\\学习资料\\2019年秋季学期\\数据分析\\Python试用\\2019_10_14\\Experiment4\\top2m.csv"))

		MaliciousURL_num = 10000
		for row in r2:
			url = row[1]
			# target = False
			# i2 = 0
			for i2 in range(0, k):
				probe = mmh3.hash(url, 41 + i2) % i
				if bit_array[probe] == 0:
					# target = True
					MaliciousURL_num -= 1
					break

		y = abs(MaliciousURL_num - 2000)
		Y.append(y)
	dictionary[k - 4] = X
	dictionary[k - 1] = Y

	# 开始画图
	plt.plot(dictionary[1], dictionary[4], color='red', label='5_hash_def')
	plt.plot(dictionary[2], dictionary[5], color='blue', label='6_hash_def')
	plt.plot(dictionary[3], dictionary[6], color='green', label='7_hash_def')
	plt.title("Just have a try. ", fontsize=26)
	plt.xlabel("X*1000000", fontsize=15)
	plt.ylabel("FP", fontsize=15)
	plt.legend()
	# plt.yticks([y1*0.02 for y1 in range(0, 50)])
	plt.show()

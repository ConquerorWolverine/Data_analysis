import matplotlib.pyplot as plt
import re

fp = open("G:\\学习资料\\2019年秋季学期\\数据分析\\Python试用\\2019_10_14\\Experiment2\\iris.data", "r")
data = fp.read()
# print(data)
pattern = re.compile(r"\d+\.\d*")
list1 = pattern.findall(data)
list2 = []
for i in list1:
    list2.append(float(i))

# print(list1)
list_x = []
list_y = []
for i in range(0, len(list2)):
    if i % 4 == 0:
        list_x.append(list2[i])
    elif i % 4 == 1:
        list_y.append(list2[i])

plt.scatter(list_x, list_y, color='m')
plt.title("Iris ", fontsize=26)
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)
plt.show()
fp.close()
# print(list_x, '\n', list_y)
'''
list = re.findall(r"\d+\.\d*", data)
print(re.findall(r"\d+\.\?\d*", data))
plt.scatter(5.1, 3.5, 25)
plt.show()
'''

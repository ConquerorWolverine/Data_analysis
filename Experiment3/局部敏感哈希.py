
# Some examples for MinHash

import re
from hashlib import sha1
from datasketch import MinHash, MinHashLSH

fp = open("G:\\学习资料\\2019年秋季学期\\数据分析\\实验3_相似项发现\\products.txt", 'r')

data2 = fp.readlines()
# print(data2)
data = []

for x in data2:
    i1 = 0
    # print(x)
    pattern = re.compile(r"\w+")
    temp = pattern.findall(x)
    temp.pop(0)
    data.append(temp)
print(data)
list_set = []   # set的集合
list_for_dictionary = []    # 字典键值
for i in range(0, len(data)):
    list_set.append(set(data[i]))
    list_for_dictionary.append(i)
dictionary = {}
dictionary = dictionary.fromkeys(list_for_dictionary)   # 用于储存变量的字典
for i in range(0, len(dictionary)):
    dictionary[i] = MinHash(num_perm=140)
    for d in list_set[i]:
        dictionary[i].update(d.encode('utf8'))

for i in range(0, len(dictionary)):
    lsh = MinHashLSH(threshold=0.3, num_perm=140)
    for j in range(0, len(dictionary)):
        if j != i:
            lsh.insert('m'+str(j+1), dictionary[j])
    result = lsh.query(dictionary[i])
    print("Approximate neighbours with Jaccard similarity > 0.3", result)

fp.close()
# print(dictionary)
# print(len(data))


'''
data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']


m1, m2 = MinHash(), MinHash()
for d in data1:
    m1.update(d.encode('utf8'))
for d in data2:
    m2.update(d.encode('utf8'))
print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

s1 = set(data1)
s2 = set(data2)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
print("Actual Jaccard for data1 and data2 is", actual_jaccard)
'''


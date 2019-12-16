from hashlib import sha1
from minhash import MinHash
import matplotlib.pyplot as plt
import numpy as np

x = range(100, 1025)
y = []
data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']

for i in x:
    m1, m2 = MinHash(num_perm=i), MinHash(num_perm=i)
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    '''print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))'''

    s1 = set(data1)
    s2 = set(data2)
    actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
    '''print("Actual Jaccard for data1 and data2 is", actual_jaccard)'''

    if actual_jaccard > m1.jaccard(m2):
        difference = actual_jaccard - m1.jaccard(m2)
    else:
        difference = m1.jaccard(m2) - actual_jaccard
    y.append(difference)


# 开始画图
plt.plot(x, y)
plt.title("Just have a try. ", fontsize=26)
plt.xlabel("X", fontsize=15)
plt.ylabel('Absolute Value ', fontsize=15)
# plt.yticks([y1*0.02 for y1 in range(0, 50)])
plt.show()

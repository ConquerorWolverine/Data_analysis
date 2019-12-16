# 我要先建立一个集合 done


def create_c1(data_set):
    c1 = set([])    # 里面要用一个列表？
    for item in data_set:
        c1 = c1.union(set(item))    # 并集，问题：item会不会被分离？   答：会被分离  所以说，给的事务集里面的事务还是要分成项，然后再凑项集
    return [frozenset([i]) for i in c1]


# 至此，单项集C1已完成
data_set1 = {'abcde': 0, 'abce': 0, 'abe': 0, 'bcd': 0, 'bc': 0}

# print(create_c1(data_set1))

# 接下来建立Lk


def get_lk(data_set, ck, support_threshold=3):
    lk = {}
    for item in data_set:
        for ci in ck:
            if ci.issubset(item):   # 如果该项是事务的子集，则该项的计数加一
                if ci not in lk:
                    lk[ci] = 1
                else:
                    lk[ci] += 1
    # 至此，计数已完毕
    lk_return = []
    for li in lk:
        if lk[li] >= support_threshold:
            lk_return.append(li)
    return lk_return


# 我可以借此函数得到Lk
# 下面如何一步步得到Ck

def get_ck(lk_1):
    ck = []
    for i in range(len(lk_1)-1):
        for j in range(i+1, len(lk_1)):
            if sorted(list(lk_1[i]))[0:-1] == sorted(list(lk_1[j]))[0:-1]:  # 这句话有什么意思？ 答：保证两项两项只生成三项而不会有四项
                ck.append(lk_1[i] | lk_1[j])
    return ck


# 至此，得到进一步的Ck也可以了，下面考虑循环


def is_empty(list1):
    if len(list1) == 0:
        return 1
    else:
        return 0


c = create_c1(data_set1)
lk_output = []
while (is_empty(get_lk(data_set1, c)) != 1):
    lk = get_lk(data_set1, c)
    c = get_ck(lk)
    for n in lk:
        lk_output.append(n)
for item in lk_output:
    print(item)
    print("")

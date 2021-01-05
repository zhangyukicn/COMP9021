from math import sqrt
#all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
#元素除了是 0,空、None、False 外都算 True。
#sqrt 方法返回数字x的平方根
#round() 方法返回浮点数x的四舍五入值。
#tuple 函数将列表转换为元组

def is_prime(n):
    L = []
    for d in range(3, round(sqrt(n)) + 1, 2):
        L.append(n % d)
    return all(L)

print('The solutions are:\n')
L =[]
for k in range(2, 13, 2):
    d = range(0, k, 2)
    sum_d = sum(d)
    L.append(sum_d)
good_leaps =tuple(L)
print(good_leaps)

L1 =[]
#method 1
for a in range(10001, 100000 - good_leaps[-1], 2):
    if all(((i in good_leaps) == is_prime(a + i)) for i in range(0, good_leaps[-1] + 1, 2)):
        print(' '.join((str(a + i) for i in good_leaps)))
#method 2




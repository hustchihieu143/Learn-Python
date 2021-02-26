# count()
# index()
# copy()
# clear()
# append(x) : them phan tu x vao cuoi list
# extend([1, 2]) them tung phan tu vao cuoi list
#insert(i, x) : them phan tu x vao vi tri i
a = [1, 2, 3]
a.insert(-20, 4)
print(a)

#pop(i)
a.pop(1)
print(a)

#remove(x): bo di phan tu dau tien trong list co gia tri x. Neu khong co phan tu thi bao loi

#reverse(): dao nguoc list

#sort(reverse=True): sap xep
kteam = [6, 8, 2, 5, 1, 10, 4]
kteam.sort(reverse=True)

print(kteam)

a = [1, 2, 3, 4]
print(a.index(4))
print(a)

a = "phan chi hieu"
print(a.partition('a'))

a = [1, 2, 3, 4, 5, 6, 7]


print(a[0::2])
ch = '*'
print(ch*20)

n = 9
show = [[x*y for x in range(1, 6)] for y in range(1, n+1)]
print(show)
num = []
smarties = ["Jane", "Bob", "Peter"]
cleveries = ["Oscar", "Lidia", "Ann"]
num += ([smarties[i], cleveries[i]] for i in range(len(smarties))) 
print(num)


def chessTeams(smarties, cleveries):
    return [[a, b] for a, b in zip(smarties, cleveries)]
def lengthOfName(name):
    return len(name)
print(list(map(lengthOfName, ['hieu', 'duong'])))    

import math
import functools
print(functools.reduce(lambda x, y: math.gcd(x, y), [12, 18, 30]))

a = ['a', 'o', 'c', 'b']
print(a.sort())



a = [87, 45]
b = [87, 45, 99]

print(set(a) <= set(b))

a = "coolcompany"
b = "nicecompany"  
c = "legendarycompany"
cmp1 = set(a)
cmp2 = set(b)
cmp3 = set(c)
word1 = "program"
word2 = "develop"
set_1 = set(word1)
set_2 = set(word2)
set1_result = (set_1|set_2) - set_2
print(str(sorted(set1_result)))
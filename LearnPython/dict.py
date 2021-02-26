# comprehension

info = {key:value for key,value in [('name', 'hieu'), ('age', 21)]}
print(info)
print(type(info))

#constructor: 4 cach: dict rong, iterable, mapping, keywordagurment
dic = dict()  # khoi tao dict rong
# su dung iterable
dic = (['name', 'hieu'], ['age', 21])
print(dict(dic))

# keyword arguments
name = 'SpaceX'
member = 696969
dic = dict(name='Kteam', member=69)
print(dic)
print(name) # => khong anh huong gi den cac bien ben ngoai

lis = [dict(dic)]
print(lis)
print(type(lis))

# fromkeys: khoi tao 1 dict voi cac key nam trong iterable
iter_ = ('name', 'age')
fk = dict.fromkeys(iter_)
print(fk)

# lay value trong dict bang key 
print(dic['name'])

# thay doi noi dung => them duoc

## cac phuong thuc

# copy()
# <dict>.get(key) : tra ve gia tri cua key. Neu khong co key thi tra ve default
# <dict>.items() : tra ve 1 gia tri thuoc lop dict_items. Cac gia tri cua dict_items se la mot tuple
# keys(): lay ra danh sach nhung key trong dict
# values(): lay ra danh sach value
# pop(key) : lay ra value cua key do va key, value se di mat di trong dict
# popitem() : tra ve 1 cap key va value
dic = dict(name='Kteam', member=69)
print(dic.popitem())
print(dic)
# setdefault(key, value): 
dic.setdefault('name')
print(dic.setdefault('name'))
dic.setdefault('okok', 'hieu')
print(dic)

# update(x): them x vao dict 
E = {'name1' : 'hieu', 'age' : 20}
dic.update(E)
print(dic)

d = {}
d.update(s = 3)
print(d)

n = 79
x = 5
print(int('560', 16))


a = [4, 5, 6, 7, 8]
b = ['hieu', 'duong', 'trung', 'lien', 'quan']

uniques = {i : j for i in a for j in b }

print(uniques)
print(type(uniques))
gen = enumerate(b, 1)
for item in gen:
    print(item)
    print(type(item))
E = {'name1' : 'hieu', 'age' : 20}
print([[key, E[key]] for key in E ])    
    
digits = [1, 2, 3, 4, 5]
from collections import deque
n = len(digits)
res = [deque(digits) for _ in range(n)]
deque(map(lambda x,y: x.rotate(-y) ,res,range(n)))
deque()
print([list(value) for value in res])

b = ['hieu', 'duong', 'trung', 'lien', 'quan']
gen = enumerate(b, 1)
for item in gen:
    print(item[0])
    print(type(item))


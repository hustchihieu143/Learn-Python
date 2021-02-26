tup = (1, 2)
print(type(tup))


 
a = tuple(i for i in range(10) if i % 2 == 0 )
print(a)

# indexing
tup = (1, 2, 'a', 'b', [3, 4])
print(tup[1])



a = tuple(i for i in range(10) if i % 2 == 0)
print(len(a))

# tuple va chuoi khong thay doi noi dung duoc

# id(x): xuat ra gia tri cua bo nho cua bien do.
# gia tri ben trong la int thi khong thay doi gia tri bien nho. Con cac kieu du lieu khac thi thay doi gia tri bien nho
'''
n = 70
print(n.__add__(2))
print(n.__sub__(3))
print(n.__mul__(0.5))
'''

tup = ([1, 3], (3, 4))
print(tup)

print(tup[0])
print(type(tup))

tup = tuple((1, 2, 3))
print(tup)
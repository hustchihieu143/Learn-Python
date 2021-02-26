set1 = {88, 69}
print(set1)

# trong set chi luu duoc cac gia tri hashable, khong luu duoc unhashable
# khong the tao 1 emptySet. Neu tao emptySet thi no se tao thanh Dict

a = set()
print(a)

# constructer Set
a = set((1, 2, 3))
print(a)

# trong set co ho tro cac toan tu: + - & | ^
# ^: loai phan giao nhau

# clear(): xoa tat ca cac gia tri trong set

# pop(x)

a = {1, 2, 3}
print(a.pop())
print(a)

# remove(x): Neu ko co gia tri x thi thong bao loi

# discard(value): loai bo value trong set. Neu khong co gia tri value thi se bo qua

# copy(): copy ban sao cua set

# add(value): them value vao trong set. Neu nhu da co gia tri value roi thi bo qua

# set la 1 hashable
a = {1, 2, 3, 4, 5}
print(id(a))
a.add(7)
print(id(a))

a = {1, 2}
b = a
b.clear()
print(a) # tại sao lại trở thành set rỗng?
# a tro thanh set rong boi vi: a la mot hashable, bien b tro vao dia chi cua a. Vi vay khi b clear thi a cung clear.
a = set("anh cahng")
print(a)

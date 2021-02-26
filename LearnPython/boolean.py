# ord: chuyen tu ki tu sang ma charAtCode
a = 'a'
print(ord(a))

# toan tu is
# is vs == khac nhau o : is la so sanh gia tri ham id() con tro, con == la so sanh gia tri 

a = [1, 2, 3]
b = [1, 2, 3]
a = b
print(id(a))
print(id(b))

print(bool([1, 2, 3]))
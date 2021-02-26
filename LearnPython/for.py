'''
x = (i for i in range(3))
c = 0
while c < 3:
    print(next(x))
    c+=1
    '''
iter_ = (x for x in range(5) if x % 2 == 0)
for value in iter_:
    print(value)

# for in dict
kteam = {'name' : 'hieu', 'age' : 21}
list_values = list(kteam.items())
print(list_values[0])
print(list_values[1])
for key, value in kteam.items():
    print(key, "=>", value)

# range(start, end, step)
for x in range(3, 30, 2):
    print(x)


# enumerate
list3 = ['long', 'giau', 'trung', 'thanh']
gen = enumerate(list3, 1)
print(type(gen))
print(list(gen)) 

list4 = []
list4.append([1, 2, 3, 4, 5])
list4.append([3, 4, 5, 6, 7])
print(list4[1][2])

answers = ['a', 'b', 'c']
gen = enumerate(answers, 1)
for i, ans in gen:
    if ans: print(i, " ", ans) 
num = [ord(c) - 96 for c in 'abcd']
print(type(num))
print(num) 
import random
a = [1]
print(a)
#List Comprehension
b = [number for number in range(3)]
print(b)
print(type(b))
c = random.randrange(1, 5)
print(c)

# list iterabale
a = list([1, 2, 3])
print(a)
a = list("Kteam")
print(a)

# toan tu cong
'''
a = [1, 2, 3]
a += [3, 4]
print(a)
a += "chi hieu"
print(a)


b = list("phan chi hieu")
b = 'a' in b
print(b)
'''
a = [1, 2, 3, 4, 5]
print(a[1])
a[1] = 'hieu'

print(a[-1])
a = list()
print(a)

s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
start = s.index('&')
end = s.index('%')
result = s[start+s.count('&'):end]
print(result)
print(sum(1, 2, 3))
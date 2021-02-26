password = "iamthebest"
table = password.maketrans("abcdefghijklmnopqrstuvwxyz", "zabcdefghijklmnopqrstuvwxy")
print(password.translate(table))

import itertools
# count
def countNumber(number, n) :
    gen = itertools.count(number)
    res = [next(gen) for _ in range(n)]
    print('gen ', gen)
    return res
print(countNumber(10, 6))    

# repeat
def repeatNumber(number, n) :
    gen = itertools.repeat(number)
    res = [next(gen) for _ in range(n)]
    print('gen ', gen)
    return res
print(repeatNumber(10, 6)) 

# cycle: "abcd" -> abcdabcdabc

# accumulated
# accumulate([1,2,3,4,5]) --> 1 3 6 10 15
# accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
# accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120  
def accumulatedNumber(arrayNumber) :
    gen = itertools.accumulate(arrayNumber, initial=100)
    res = [value for value in gen]
    return res
print(accumulatedNumber([1, 2, 3, 4, 5]))    

# compress() compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
def compressExampled(string, array) :
    gen = itertools.compress(string, array)
    res = [value for value in gen]
    return res
print(compressExampled('ABCDEF', [1,0,1,0,1,0]))    

# dropwhile(): dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1

# filterfalse(): filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
def filterfalseExample() : 
    gen = itertools.filterfalse(lambda x: x % 2 == 0, range(10))
    res = [value for value in gen]
    print('gen: ', gen)
    return res
print(filterfalseExample()) 

# dropwhile(): dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
#---> tra ve dang sau gia tri false dau tien
def dropwhileExample(arrayNumber) : 
    gen = itertools.dropwhile(lambda x: x % 2 == 1, arrayNumber)
    res = [value for value in gen]
    return res
print(dropwhileExample([1,2,3,4,5,6]))

# takewhile: takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4

# permutations(): permutations('ABCD', 2) = AB AC AD BA BC BD CA CB CD DA DB DC


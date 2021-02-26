# iteration: Kieu nhu thuc hien 1 vong lap
# iterable object trong python
a = [1, 2, (3, 4, 5)]
print(a)
print(a.__getitem__(2))

# iterator: cho ta lay lan luot gia tri cua chuoi chu ko lay duoc bat ki gia tri nao
a = (x for x in range(3))
print(a) # => iterator


# Mot so ham ho tro iterable
print(max(a))
print(sorted([1, 3, 2, 6, 5]))
b = [1, 2, 5, 4]
print(sorted(b, reverse=True))

for x in range(5):
    print(x,3, sep='??')

print("phan chi hieu", "phan trung duong", sep="??")    

# sleep
from time import sleep # nhập hàm sleep từ thư viện time

print('line 1', 'lin\ne2', end='')
sleep(3) # dừng chương trình 3 giây
print('end...')

# su dung ham print nhu phuong thuc ghi file trong write

# flush
from time import sleep # nhập hàm sleep từ thư viện time

print('start...\n', end='', flush=True)
sleep(3) # dừng chương trình 3 giây
print('end...')
# Nếu flush là True, nó sẽ yêu cầu bộ đệm xuất những gì có trong bộ đệm ra.
from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='\n', flush=True)
    sleep(1)
print()


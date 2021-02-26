

myString = "PhanChiHieu"
def main():
    print(myString)

main()
#print(myString[-1])
#cat chuoi tu trai sang phai
#print(myString[:3])

#cat chuoi tu phai sang
#print(myString[5:1:-1])

#thay doi gia tri ki tu
#a = myString[0:5] + 'k' + myString[6:]
#print(a) 
'''
a = "my name is %s" %("Phan Chi Hieu")
print(a)
name = "Phan Chi Hieu"
result = f"{name} is my name"
print(result)

#dinh dang format
info = "name:{}\naddress:{}\nsex:{}".format("hieu", "hanoi", "nam")
print(info)
'''

# can le
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)


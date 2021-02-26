a = "phan chi hieu"
#split(sep=None, maxsplit=-1): tach chuoi, tra va 1 list cac du lieu
# maxsplit: so lan tach duoc cung cap
print(a.split(' '))

#rsplit: cat tu phia ben phai qua

# partition(): Trả về một tuple với 3 phần tử. Các phần tử đó lần lượt là chuỗi trước chuỗi sep, sep và  chuỗi sau sep.
print(a.partition('c'))

#rpartition(): thuc hien tuong tu partition nhung tu ben phai qua

#<chuỗi>.count(sub, [start, [end]]): Trả về một số nguyên, chính là số lần xuất hiện của sub trong chuỗi. 
# Còn start và end là số kĩ thuật slicing (lưu ý không hề có bước).\
print(a.count('a'))

#starswith(prefix): tra ve true neu xuat hien prefix ở đầu
print(a.startswith('Ph'))

#endswith: tương tự với start nhưng end nó là ở cuối

#find(): tra ve vi tri dau tien nó tim thay chuoi truyen vao

#index(): nếu không tìm thấy thì nó sẽ quăng ra 1 cái lỗi

#islower(): co phai la chuoi viet thuong ko

#isupper(): co phai la chuoi viet hoa khong

#istitle(): co phai la title hay khong

#isdigit(): co phai so hay khong

#isspace(): co phai tat ca khong trang hay khong
s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
s = s.strip('aaaAAaaaooaa')
s += 'o'
print(s.title())

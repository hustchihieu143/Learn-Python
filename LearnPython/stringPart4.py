#cappitalize: Viet hoa ki tu dau tien cua chuoi
a = "phan chi hieu"
b = a.capitalize()
print(b)

#swapcase(): viet hoa thanh viet thuong, viet thuong thanh viet hoa.
name = "Phan Chi Hieu"
print(name.swapcase())

#title(): tra ve chuoi viet hoa chu cai dau
print(name.title())

#center(width, (fillchar)): Trả về một chuỗi được căn giữa với chiều rộng
print(name.center(30, '*'))

#rjust: Cách hoạt động tương tự như phương thức center, có điều là căn lề phải

# ljust: Cách hoạt động tương tự như phương thức center, có điều là căn lề trai

#encode: ma hoa 1 chuoi theo dung chuan
b = name.encode(encoding="utf-8", errors="strict")
print(b)

#join: ghep chuoi
a = "phan   "
b = "chi"
c = "hieu"
print(name.join(["1", "2", "3"]))

#replace()
print(name.replace("a", "d", 3))

#strip() loai bo cac khong cach, cat chu o hai dau
print(a.strip('p'))

#rstrip(), lstrip() tuong tu
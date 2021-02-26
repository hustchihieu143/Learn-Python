
# lay toan bo noi dung cua thu vien decimal
from decimal import*

# lay toi da 30 chu so phan nguyen va thap phan
getcontext().prec = 4

def main():
    d = str(Decimal(3.1415)).center(10)
    print(d)

if __name__ == "__main__":
    main()
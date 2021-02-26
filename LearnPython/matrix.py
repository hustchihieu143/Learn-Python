# cach 1:

n = int(input("enter a number: "))
matrix = [[None]*n for j in range(n)]
number, l, r = 1, 0, n - 1
value = n
while number <= value**2 :
    if number <= value**2 :
        for i in range(l, r+1):
            if matrix[l][i] == None :
                matrix[l][i] = number
            number += 1
    if number <= value**2 :
        for j in range(l+1, r+1):
            if matrix[j][r] == None :
                matrix[j][r] = number
            number += 1
    if number <= value**2 :
        for k in range(r-1, l-1, -1):
            if matrix[r][k] == None :
                matrix[r][k] = number
            number += 1  
    if number <= value**2 :
        for h in range(r-1, l, -1):
            if matrix[h][l] == None :
                matrix[h][l] = number
            number += 1    
    l+=1
    r-=1


for i in range(value) :
    for j in range(value) :
        print(matrix[i][j], end=' ')            
    print()    

# cach 2:

n = int(input('Enter size of matrix: '))
dx, dy = 1,0
x, y = 0,0
spiral_matrix = [[None] * n for j in range(n)]

for i in range(n ** 2):
    spiral_matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and spiral_matrix[nx][ny] == None:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x + dx, y + dy

for y in range(n):
    for x in range(n):
        print("%02i" % spiral_matrix[x][y], end=' ')
    print()

print()


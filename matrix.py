row = int(input("row:"))
col = int(input("col:"))

matrix = [[1 for j in range(col)] for i in range(row)]
num = 1
for i in range(row):
    for j in range(col):
        matrix[i][j] = num
        num += 1
for j in range(col):
    i = 0
    n = j
    while n >= 0:
        print(matrix[i][n], end=" ")
        i += 1
        n -= 1
    print()
for i in range(1, row):
    j = col - 1
    n = i
    while n < row:
        print(matrix[n][j], end=" ")
        n += 1
        j -= 1
 


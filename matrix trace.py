#The input to the program is a natural number n — the number of rows and columns in the matrix, 
#then the elements of the matrix (integers) line by line, 
#separated by a space
n,matr = int(input()),[]
for i in range(n):
    matr.append(input().split()) 
sled = 0
for i in range(n):
    sled+=int(matr[i][i])
print(sled) 

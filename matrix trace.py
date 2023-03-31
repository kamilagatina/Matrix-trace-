n,matr = int(input()),[]
for i in range(n):
    matr.append(input().split()) 
sled = 0
for i in range(n):
    sled+=int(matr[i][i])
print(sled) 

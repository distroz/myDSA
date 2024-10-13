coins=[2,3,5,10]
w=15
matrix=[[-1 for j in range(w+1)] for i in range(len(coins))]

matrix[0][0]=1
for j in range(1,w+1):
    if j%coins[0]==0:
        matrix[0][j]=1
    else:
        matrix[0][j]=0




for i in range(1,len(coins)):
    for j in range(w+1):
        if coins[i] > j:
            matrix[i][j]=matrix[i-1][j]
        else:
            matrix[i][j]=matrix[i-1][j]+matrix[i][j-coins[i]]

for i in range(len(coins)):
    for j in range(w+1):
        print(matrix[i][j])


        
            
            



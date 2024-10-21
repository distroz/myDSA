import math
def min_coin():
    coins=[1,5,6,9]
    w=10
    matrix=[[-1 for j in range(w+1)] for i in range(len(coins))]

        

    for j in range(w+1):
        if j%coins[0] == 0:
            matrix[0][j]= j/coins[0]
        else:
            matrix[0][j]=0


    for i in range(1,len(coins)):
        for j in range(w+1):
            if coins[i] > j:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=min(matrix[i-1][j],1 + matrix[i][j-coins[i]])

    for i in range(len(coins)):
        for j in range(w+1):
            print(matrix[i][j])    

min_coin()
#Bottom-up Approach
def fib(n):
    memo=[-1 for i in range(n+1)]
    memo[0]=0
    memo[1]=1
    if n==1:
        return memo[1]
    elif n==0:
        return memo[0]
    for i in range(2, n+1):
        memo[i]=memo[i-1] + memo[i-2]
    
    return memo[i]
print(fib(5))



        
    
def main(n):
    memo=[-1 for i in range(n+1)]
    print(memo)
    def fib(n):
        if memo[n]!= -1:
            return memo[n]
        if n==0:
            return 0
        elif n==1:
            return 1
        else:        
            memo[n]=fib(n-1)+fib(n-2)
            return memo[n]
    print(fib(n))

main(5)

    



def fib(n):

    if(n > 1):
        return fib(n-1) + fib(n-2)

    elif(n == 1 or n==0):
        return n


for i in range(12):
    print(fib(i))
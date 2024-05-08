def fib(n):
    a , b = 0,1
    c = 0
    if not n :
        return 0 
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(n-1):
            c = a+b
            a = b
            b = c
    return c    
print(fib(7))
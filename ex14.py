def fib(n):
    a = 0 #first number
    b = 1 #second number
    result = [0]
    print('The Fibonacci series is')
    for x in range(0,n):
        c = a + b # c = third number
        result.append(b)
        a = b
        b = c
    print(result)
    return
fib(20) # 20 interations

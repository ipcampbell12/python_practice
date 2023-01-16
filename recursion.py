def factorial(n):
    if n >= 1:
        return n*factorial(n-1)
    else:
        return 1


# print(factorial(3))

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(3))

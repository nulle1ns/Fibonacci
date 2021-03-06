def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result += [a]
        a, b = b, a+b
    return result


def fibonacci_generator(n):
    a, b = 0, 1
    counter = 0
    for _ in range(n):
        yield a
        a, b = b, a+b
        counter += 1
        if counter > n:
            return


# print(fibonacci(10))  
print(list(fibonacci_generator(10)))
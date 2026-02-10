def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
position = int(input("Fibonacci number? "))
print("Result:", fibonacci(position))   

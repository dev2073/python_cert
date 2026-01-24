def triangle(base, height):
    return base * height * 0.5

print("Area of triangle:")
print(triangle(3, 4))

print("\n")

def fibonacci(lenght):
    a, b, count = 0, 1, 0
    while count < lenght:
        count += 1
        a, b = b, a + b
        print(a, end=' ')

print("Fibonacci sequence:")
fibonacci(10)

print("\n")

def size(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print("Number of digits:")
print(size(123456789))      

print("\n")
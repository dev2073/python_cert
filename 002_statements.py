a=b=7
print(a, b)

print("")

x = 10
y = 20
x, y = y, x
print(x, y)

print("")

a=\
10\
+ 20
print(a)

print("")

x = (
    10
    + 25 
)
print(x)

print("")

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

print(add.__doc__)
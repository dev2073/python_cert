b = 8

def func1():
    a = 7
    print(a)
    print(b)

func1()
print("\n")

x = 0
def func2():
    print(x)
    x = 5
    print(x)

func2() # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
print("\n")

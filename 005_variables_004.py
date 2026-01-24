xyz=3

def func2():
  xyz=0
  xyz+=1
  print(xyz)

func2()
print("\n")

foo=1

def func2():
  global foo
  foo=3
  print(foo)

func2()

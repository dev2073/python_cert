for i in range(10):
     print(i) # 0,1,2,3,4,5,6,7,8,9
else:
     print("Reached else") # 'Reached else'

print("\n")

for i in range(10):
     print(i) # 0,1,2,3,4,5
     if i == 5:
          break
else:
     print("Reached else") # 'Reached else'



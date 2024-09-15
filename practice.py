import sys 
a =[]
for i in range(1,101):
    print(i,sys.getsizeof(a))
    a.append(i)
print(a)




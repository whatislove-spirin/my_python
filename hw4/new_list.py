import math
#решение на основе цикла for
lst1=[2,4,9,16,25]
lst=[]
for i in lst1:
    lst.append(math.sqrt(i))

print(lst)
print('\n')

#решение на основе функции map
def fun(x):
    return math.sqrt(x)

print(list(map(fun,lst1)))

print('\n')
#решение на основе генератора списка
print([math.sqrt(x) for x in lst1])

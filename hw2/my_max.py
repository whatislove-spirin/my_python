first = int(input('Введите первое число\n'))
second = int(input('Введите второе число\n'))
def my_max(first,second):
    if first > second:
        return first
    else:
        return second

print('Наибольшее из двух чисел:', my_max(first,second))   

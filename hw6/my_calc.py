#one run calculator
def calc(fir,sec,op):
    if op == "+":
        return fir+sec
    elif op == "-":
        return fir-sec
    elif op == "*":
        return fir*sec
    elif op == "/":
        return fir/sec
    
try:
    first = float(input("Введите первый операнд:\n"))
    second = float(input("Введите второй операнд:\n"))
    operator = input("Введите оператор:\n")
    print(calc(first,second,operator))
except ValueError:
    print("Ошибка в введённых данных")
except ZeroDivisionError:
    print("Ошибка деления на ноль")

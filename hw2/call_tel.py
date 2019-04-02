sity = int(input('Введите код города\n'))
time = float(input('введите длительность переговоров в минутах\n'))
if sity == 343:
    print(time*15,'руб')
elif sity == 381:
    print(time*18,'руб')
elif  sity == 473:
    print(time*13,'руб')
elif  sity == 485:
    print(time*11,'руб')
else:
    print('Введён неверный код города')

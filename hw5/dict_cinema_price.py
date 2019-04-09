films = {'Пятница' : {'12':250,'16':350,'20':450},
        'Чемпионы' : {'10':250,'13':350,'16':350},
        'Пернатая банда' : {'10':350,'14':450,'18':450}}

def dateDiscount(date):
    if date == 'завтра':
        return 0.05
    elif date == 'сегодня':
        return 0
    
def quantityDiscount(tAm):
    if tAm>=20:
        return 0.20
    else:
        return 0

def totalPrice(film,tAm,date,time):
    return tAm*film[time] - tAm*film[time]*(quantityDiscount(tAm) + dateDiscount(date))

film = input('Выберите фильм: ')
date = input('Выберите дату (сегодня, завтра): ')
time = input('Выберите время: ')
ticketAmount = input('Выберите количество билетов: ')

if film and date and time and ticketAmount:
    ticketAmount = int(ticketAmount)
    if film in films:
        if date == 'сегодня' or date == 'завтра':
            if time in films[film]:
                print('Фильм:',film,'Дата:',date,'Время:',time,'Количство билетов:',ticketAmount)
                print('Результат: ', totalPrice(films[film], ticketAmount, date, time))
            else:
                print('wrong time')
        else:
            print('wrong date')
    else:
        print('wrong film')
else:
    print('Ошибка ввода.')

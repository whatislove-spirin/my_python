film = str(input('Выберите фильм:'))
date = str(input('\nВыберите дату (сегодня, завтра):'))
time = int(input('\nВыберите время в часах:'))
t_count = int(input('\nВыберите количество билетов:'))
print('Выбрали фильм:',film,'\tдень:',date,'\tвремя:',time,'\tколичество билетов:',t_count) 
def cost(film,time):
    if film.lower() == 'пятница':
        if time == 12:
            return 250
        elif time == 16:
            return 350
        elif time == 20:
            return 450
    elif film.lower() == 'чемпионы':
        if time == 10:
            return 250
        elif time == 13:
            return 350
        elif time == 16:
            return 350
    elif film.lower() == 'пернатая банда':
        if time == 10:
            return 350
        elif time == 14:
            return 450
        elif time == 18:
            return 450
    else: return 0
            
price=cost(film,time)
def costall(date,t_count,price):
    if t_count >= 20 and date.lower() == 'завтра'.lower():
        return price*t_count*0.75
    elif t_count >= 20:
        return price*t_count*0.8
    elif date.lower() == 'завтра'.lower():
        return price*t_count*0.95
    else: return price*t_count

if costall(date,t_count,price) == 0:
    print('Ошибка ввода.')
else:
    print('\nРезультат:',costall(date,t_count,price),'руб.')

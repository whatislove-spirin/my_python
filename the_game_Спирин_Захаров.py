import random

# Создание персонажа

class Character:
    print('Игра дуэль')
    print()

#установка базовых атрибутов
  
    def __init__(self, name, hp, dmg, fd, x, y):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.ms = 6
        self.x = x
        self.y = y
        self.fd = fd
        print(' Игрок',self.name,'появился по координатам (',self.x,self.y,')')
        print()

#перемещение по полю

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y +=delta_y
        print(' Игрок', self.name, 'переместился на координаты (', self.x, self.y,')')
        print()

#атака

    def fire(self, enemy):
        if abs(self.x - enemy.x) + abs(self.y - enemy.y) <= self.fd:
            enemy.hp = enemy.hp - self.dmg
            print(self.name, 'нанес', enemy.name, self.dmg, 'единиц урона. Здоровье игрока', enemy.name, ': ', enemy.hp)
            print()
        else:
            print('Игрок', self.name, 'попытался атаковать игрока', enemy.name, ', но промахнулся')
            print()
        if enemy.hp <= 0:
            print ('Здоровье игрока', enemy.name, 'опустилось до нуля. Он выбывает из игры.')
            print('\nДуэль окончена.')

#поднятие предмета

    def pick(self,item):
        if self.x == item.x and self.y == item.y:
            self.hp += item.hpBonus
            self.dmg += item.dmgBonus
            self.ms += item.msBonus
            self.fd += item.fdBonus
            print('Игрок',self.name,'подобрал предмет:',item.name)
            print()

#появление предмета
            
class ItemAppear:
    def __init__(self, name, hpBonus, dmgBonus, fdBonus, msBonus, aX, aY):
        self.name = name
        self.hpBonus = hpBonus
        self.dmgBonus = dmgBonus
        self.fdBonus = fdBonus
        self.msBonus = msBonus
        self.x = aX
        self.y = aY
        print('  Предмет "',self.name, '" появился по координатам(',self.x, self.y,')')
        print()
    
#обретение способности летать

class FChar(Character):
    def __init__(self, name, hp, dmg, fd, x, y):
        super().__init__(name, hp, dmg, fd, x, y)
        print(' Игрок ', self.name, 'обрел способность летать')
        print()

#повление персонажей
hero0 = Character('Ranger',150,75,1, 1, 1)
hero1 = Character('Druid',250,40,1, 9, 10)

#1 ход
hero0.move(5,1)
hero1.move(-3,3)

#появление первого предмета
boots = ItemAppear('Boots of speed',0,0,0,3,3,4)

#2 ход
hero0.move(-3,2)
hero0.pick(boots)
hero1.move(-6,0)

#появление второго предмета
critz = ItemAppear('Daedalus', 0, 75,0,-1,1,7)

#3 ход
hero0.move(-2,3)
hero0.pick(critz)
hero1.move(1,-5)

#появление третьего предмета
health = ItemAppear('Health booster', 150,0,0,0,5,9)

#4 ход
hero0.move(4,2)
hero0.pick(health)
hero1.move(1,-5)

#появление четвертого предмета
wings = ItemAppear('Tsubasa wo kudasai', 50,20,2,1,8,2)

#5 ход
hero0.move(3,-7)
hero0.pick(wings)
hero0 = FChar(hero0.name, hero0.hp, hero0.dmg, hero0.fd, hero0.x, hero0.y)
hero1.move(5,1)

#6 ход
hero0.fire(hero1)
hero1.fire(hero0)

#7 ход
hero0.fire(hero1)

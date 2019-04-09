toDoList = []
while True:
    option = int(input(
        'Простой todo:\n\t1. Добавить задачу.\n\t2. Ввести список задач.\n\t3. Выход\nУкажите число:'))
    if option == 3:
        break
    if option == 2:
         for task in toDoList:
            for name in task:
                print(name+':', task[name])
            print()
    if option == 1:
        newTask = {}
        newTask['Задача'] = input('Сформулируйте задачу: ')
        newTask['Категория'] = input('Добавьте категорию к задаче: ')
        newTask['Время'] = input('Добавьте время к задаче: \n')
        toDoList.append(newTask)

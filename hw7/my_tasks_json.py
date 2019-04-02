def reader(filename):
    '''
    Чтение содержимого json файла 
    '''
    import json    
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

def writer(filename, numbers):    
    import json    
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)
    
toDoList = list(reader('tasks.json'))
taskList = {}
while True:
    option = int(input('Простой ToDo:\n1. Добавит задачу.\n2. Вывести список задач.\n3. Выход\n'))
    if option == 3:
        break
    elif option == 2:
        k = 0
        for i in toDoList:
            k+=1
            print(str(k)+' задача:')
            for j in i:
                print('\t'+j+':',i[j])
                print()
    elif option == 1:
        taskList['category'] = input('Добавить категорию к задаче: ')
        taskList['name'] = input('Сформулируйте задачу: ')
        taskList['time'] = input('Добавить время к задаче: ')
        toDoList.append(taskList)
        writer('tasks.json',toDoList)

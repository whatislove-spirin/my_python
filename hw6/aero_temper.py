with open('file_name.txt','r') as file: 
    contents = file.read()
contentSplit = contents.split()
temp = []
for i in contentSplit:
    temp.append(float(i))
k = 0
for i in temp:
    if temp.count(i) == 1:
        k += 1
print("\nМаксимальное значение температуры: ",max(temp),
      "\nМинимальное значение температуры: ",min(temp),
      "\nCредняя температура: ",sum(temp)/len(temp),
      "\nКоличество уникальных температур: ",k)
      

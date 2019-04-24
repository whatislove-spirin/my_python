from tkinter import *
from math import pi

def strFindSphericalVolume(r):
    return str(round((4/3)*pi*(r**3),3))

def file_write(string):
    try:
        with open("text_out.txt", 'w') as output_file:
            output_file.write(string)
    except Exception as e:
        return e
def web_write(string):
    try:
        with open("web_out.html", 'w') as output_file:
            output_file.write("<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t"+string+"\n\t</body>\n</html>")
    except Exception as e:
        return e
    
def ok():
    s = str(var.get())
    if s == "Текст":
        file_write(str(label['text']))
    elif s == "HTML":
        web_write(str(label['text']))

def click():
    try:
        label.config(text=strFindSphericalVolume(int(enter1.get())))
    except Exception:
        label.config(text="Ошибка ввода")
        
master = Tk()
master.geometry('400x200')

var = StringVar(master)
var.set("Выпадающий список") # initial value

option = OptionMenu(master, var,"Текст","HTML")
option.place(x=180,y=140)

label = Label(master,text="Программа для вычисления объема сферы")
label.place(x=75,y=10)

enter1=Label(master,text="Введите радиус:")
enter1.place(x=32,y=40)

enter1=Entry(master)
enter1.place(x=180,y=40)

enter2=Label(master,text="Результат\n вычислений")
enter2.place(x=32,y=70)
         
label = Label(master)
label.place(x=180,y=70)

button1 = Button(master,text="Вычислить",command=click)
button1.place(x=190,y=110)

button2 = Button(master, text="Save", command=ok)
button2.place(x=50,y=130)
mainloop()


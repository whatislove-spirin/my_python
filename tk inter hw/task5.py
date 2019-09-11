import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 
        self.radio_var = tkinter.IntVar()
 
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Дневное время (6:00-17:59)',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вечернее время (18:00-23:59)',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Непиковый период (00:00-5:59)',
                                       variable=self.radio_var,
                                       value=3)

        self.min_label = tkinter.Label(self.top_frame,
                    text='Введите количество минут:')
        self.min_entry = tkinter.Entry(self.top_frame,
                                        width=10)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.min_label.pack(side='left')
        self.min_entry.pack(side='left')

        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
 
        tkinter.mainloop()

    def show_choice(self):
        ch = int(self.radio_var.get())
        ent = float(self.min_entry.get())
        if ch == 1:
            value = ent*10/100
        elif ch == 2:
            value = ent*12/100
        elif ch == 3:
            value = ent*5/100
        tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты:' + str(value)
                                    )

my_gui = MyGUI()
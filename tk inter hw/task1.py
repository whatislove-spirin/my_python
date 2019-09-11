import tkinter

class MyGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()


        self.text = tkinter.StringVar()
        self.text.set('')
        
        self.info_text = tkinter.Label(self.top_frame, textvariable = self.text, justify=tkinter.LEFT)
        
        
        self.my_button = tkinter.Button(self.bottom_frame,
                                        text='Показать инфо',
                                command=self.inf_show)
        
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)
        
        
        self.info_text.pack(side = "left")
        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')
        
        
        self.my_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        tkinter.mainloop()
    
    def inf_show(self):
        self.text.set('Стивен Маркус\n274 Бейли\nУэйнзвиль, Северная Королина 27999')
        

my_gui = MyGUI()

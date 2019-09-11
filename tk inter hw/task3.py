import tkinter

class KiloConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame1 = tkinter.Frame()
        self.top_frame2 = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gal_label = tkinter.Label(self.top_frame1,
                    text='Введите количество галлонов:')
        self.gal_entry = tkinter.Entry(self.top_frame1,
                                        width=10)
        
        self.mile_label = tkinter.Label(self.top_frame2,
                    text='Введите количество миль:')    
        self.mile_entry = tkinter.Entry(self.top_frame2,
                                        width=10)

        self.gal_label.pack(side='left')
        self.mile_label.pack(side='left')
        self.gal_entry.pack(side='left')
        self.mile_entry.pack(side='left')

        
        self.descr_label = tkinter.Label(self.mid_frame,
                   text='Мили на галлон (MGP):')

        self.value = tkinter.StringVar()
        self.value.set('')
        
        self.mpg_label = tkinter.Label(self.mid_frame,
                   textvariable=self.value)

        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')


        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Вычислить MGP',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                   command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.top_frame1.pack()
        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()

    def convert(self):

        gal = float(self.gal_entry.get())
        mile = float(self.mile_entry.get())

        answ = mile/gal

        self.value.set(answ)

kilo_conv = KiloConverterGUI()
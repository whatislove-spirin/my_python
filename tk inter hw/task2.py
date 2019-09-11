import tkinter

class MyGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_subframe = tkinter.Frame(self.top_frame)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.text = tkinter.StringVar()
        self.text.set('')
        
        self.info_text = tkinter.Label(self.top_frame, textvariable = self.text)
        
        
        self.button_sinister = tkinter.Button(self.bottom_frame,
                                        text='sinister',
                                command = self.do_sinister)
        
        self.button_dexter = tkinter.Button(self.bottom_frame,
                                        text='dexter',
                                command = self.do_dexter)
        
        self.button_medium = tkinter.Button(self.bottom_frame,
                                        text='medium',
                                command = self.do_medium)
        
        self.info_text.pack()
        
        self.button_sinister.pack(side = "left")
        self.button_dexter.pack(side = "left")
        self.button_medium.pack(side = "left")
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    def do_sinister(self):
        self.text.set('левый')
                
    def do_dexter(self):
        self.text.set('правый')
                    
    def do_medium(self):
        self.text.set('средний')
                
my_gui = MyGUI()
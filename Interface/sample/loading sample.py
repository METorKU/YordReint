from time import sleep
from tkinter import *


class loading:
    def __init__(self):
        self.root = Tk()
        self.root.title("Loading")
        self.root.geometry("600x600")

        label1 = Label(self.root, text="Loading")
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        for i in range(4):
            Label(self.root, text="p", bg="black").place(x=(i + 22) * 22, y=450)
            
        self.root.update()
        self.play_animation()
        self.root.mainloop()


    def play_animation(self):
        for i in range(80):
            for j in range(4):
                Label(self.root, text="p", bg="grey").place(x=(j + 22) * 22, y=450)
                sleep(0.2)
                self.root.update_idletasks()

                Label(self.root, text="p", bg="black").place(x=(j + 22) * 22, y=450)
 
        else:
            self.root.destroy()

loading()
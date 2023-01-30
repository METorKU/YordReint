from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.master['bg']='green'
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300, background="black")
        self.frame1.pack()
        self.reg_txt = Label(self.frame1, text='login')
        self.reg_txt.pack()
        self.register_btn = Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.pack()
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300, background="yellow")
        self.frame2.pack()
        self.reg_txt2 = Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

root = Tk()
app(root)
root.mainloop()
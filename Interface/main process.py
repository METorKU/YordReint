from tkinter import *
import time
import random
from tkinter import ttk
from time import sleep
from PIL import ImageTk, Image
from tkinter import messagebox


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x800")
        #self.master['bg']='green'
        self.bg = PhotoImage(file = "Interface/image/bg image.png")
        self.label1 = Label(self.master, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.fourth_page()
    
    def click_5(self):
        self.fifth_page()

    def click_1(self):
        print("click")
    
    def random_ID(self):
        self.s = "1"
        for i in range (5):
            self.r1 = random.randint(0,9)
            print(self.r1)
            self.s = self.s + str(self.r1)
        return self.s

    def play_animation(self):
        for i in range(2):
            k=300
            for j in range(4):
                Label(self.frame5, bg="#79E8FF",width=5,height=3).place(x=(k+70), y=400)
                sleep(0.3)
                self.frame5.update_idletasks()
                sleep(0.3) 
                k+=100
            Label(self.frame5, bg="white",width=60,height=3).place(x=300, y=400)
            self.frame5.update_idletasks()

        else:
            self.sixth_page()

    def fourth_page(self):
        self.frame4 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame4.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame4, text="Have you put your clothes?", font=("Courier New", 20, "bold"),background="white")
        self.label1.place(relx=0.77, rely=0.25, anchor=CENTER)

        self.my_pic = Image.open("Interface/image/laundry-basket.png")
        self.resize = self.my_pic.resize((200,200),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resize)
        self.label1 = Label(self.frame4, image=self.img, width=200, height=200, background="white")
        self.label1.place(relx=0.77,rely=0.5, anchor=CENTER)

        self.label1 = Label(self.frame4, text="Add friend :)", font=("Courier New", 35, "bold"),background="white")
        self.label1.place(relx=0.3, rely=0.15, anchor=CENTER)

        self.label1 = Label(self.frame4, text="Name: น้องหยอด", font=("Courier New", 20, "bold"),background="white")
        self.label1.place(relx=0.27, rely=0.8, anchor=CENTER)

        self.label1 = Label(self.frame4, text="ID: "+self.random_ID(), font=("Courier New", 20, "bold"),background="white")
        self.label1.place(relx=0.27, rely=0.85, anchor=CENTER)

        self.my_pic2 = Image.open("Interface/image/qr.png")
        self.resize2 = self.my_pic2.resize((300,300),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(self.resize2)
        self.label1 = Label(self.frame4, image=self.img2, width=300, height=300)
        self.label1.place(relx=0.28,rely=0.47, anchor=CENTER)

        self.button1=Button(self.frame4, text = "Done", font=("Courier New", 20),height = 3, width = 10, command=self.click_5)
        self.button1.place(relx=0.77,rely=0.8, anchor=CENTER)

            
    def fifth_page(self):
        self.frame5 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame5.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame5, text="Loading", font=("Courier New", 120, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.play_animation()

    def countdown(self,t):
    
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            Label(self.frame6, text=timer, bg="white", font=("Courier New", 250)).place(relx=0.5,rely=0.5, anchor=CENTER)
            self.frame6.update()
            print(timer, end="\r")
            time.sleep(0.1)
            t -= 15
        
        self.seventh_page()


    def sixth_page(self):
        self.frame6 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame6.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.countdown(600)

    def seventh_page(self):
        self.frame7 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame7.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame7, text="Finished!", font=("Courier New", 120, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.27, anchor=CENTER)
        self.pic = Image.open("Interface/image/laundry.png")
        self.resize = self.pic.resize((250,250), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resize)
        self.label2 = Label(self.frame7, image=self.new_pic, background="white")
        self.label2.place(relx=0.5,rely=0.6, anchor=CENTER)
        self.label2.bind("<Button-1>", self.click)
        self.frame7.bind("<Button-1>", self.click)
        
        
        

root = Tk()
app(root)
root.mainloop()
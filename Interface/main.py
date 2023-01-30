from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from time import sleep
import random
import time
import _thread
import datetime
from mysql.connector import connect,Error
import RPi.GPIO as GPIO
import time
from time import sleep

max_amount = 0
label_coin = None
mode_type = 0
Id=1
mode=""
global left
global right
left = 7 #relay input 1
right = 1 #relay input 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(left, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(right,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.RISING)
onoff = "off"
a = 13
b = 26
c = 16
d = 21
e = 20
f = 19
g = 6
d1 = 24
d2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(a, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(b,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(c, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(d,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(e, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(f,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(g,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(d1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(d2,GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(17, GPIO.RISING) 
GPIO.add_event_detect(27,GPIO.RISING)
all7= [a,b,c,d,e,f,g]
dict1 = {0: [1,1,1,1,1,1,0], 1: [0,1,1,0,0,0,0], 2: [1,1,0,1,1,0,1], 
3: [1,1,1,1,0,0,1], 4: [0,1,1,0,0,1,1], 5: [1,0,1,1,0,1,1], 
6: [1,0,1,1,1,1,1,], 7: [1,1,1,0,0,0,0], 8: [1,1,1,1,1,1,1], 9: [1,0,1,0,0,1,1]}
GPIO.output(d2, 1)
for i in range(7):
    GPIO.output(all7[i], abs(dict1[1][i]-1) )

GPIO.output(5,GPIO.LOW)

#IMPORTANT
#WRITE HIGH TO STOP
def count(blink):
    for num in range(blink,0,-1):
        t = time.time()
        print(num)
        while time.time() - t < 1:
            GPIO.output(d1, GPIO.HIGH)
            ind = 0
            for i in all7:
                if num >= 10:
                    GPIO.output(i, abs(dict1[int(str(num)[0])][ind] - 1))
                    ind += 1
                if num < 10:
                    GPIO.output(i, 1)
                    ind += 1
            sleep(0.01)
            GPIO.output(d1, GPIO.LOW)
            ind = 0
            for i in all7:
                GPIO.output(i, 1)
                ind += 1
            GPIO.output(d2, GPIO.HIGH)
            ind = 0
            for i in all7:
                if num >= 10:
                    GPIO.output(i, abs(dict1[int(str(num)[1])][ind] - 1))
                    ind += 1
                if num < 10:
                    GPIO.output(i, abs(dict1[num][ind] - 1))
                    ind += 1
            sleep(0.01)
            GPIO.output(d2, GPIO.LOW)
            ind = 0
            for i in all7:
                GPIO.output(i, 1)
                ind += 1
def wash(m):
    t = time.time()
    print("mode", m)
    if m == "Power wash":
        stop = 0
        while stop <= 30:
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.LOW)
            sleep(7)
            stop = time.time() - t
            print(stop, "phase 2")
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.HIGH)
            sleep(2)
            stop = time.time() - t
            print(stop, "phase 3")
            GPIO.output(left, GPIO.LOW)
            GPIO.output(right,GPIO.HIGH)
            sleep(7)
            stop = time.time() - t
            print(stop, "phase 4")
            if stop >= 30:
                break
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.HIGH)
            sleep(2)
            stop = time.time() - t
            print(stop, "phase 1")
        GPIO.output(left, GPIO.HIGH)
        GPIO.output(right,GPIO.HIGH)
    if m == "Quick wash":
        stop = 0
        while stop <= 20:
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.LOW)
            sleep(5)
            stop = time.time() - t
            print(stop, "phase 2")
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.HIGH)
            sleep(2)
            stop = time.time() - t
            print(stop, "phase 3")
            if stop >= 20:
                break
            GPIO.output(left, GPIO.LOW)
            GPIO.output(right,GPIO.HIGH)
            sleep(5)
            stop = time.time() - t
            print(stop, "phase 4")
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.HIGH)
            sleep(2)
            stop = time.time() - t
            print(stop, "phase 1")
        GPIO.output(left, GPIO.HIGH)
        GPIO.output(right,GPIO.HIGH)
    if m == "Delicates wash":
        stop = 0
        while stop <= 25:
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.LOW)
            sleep(3)
            stop = time.time() - t
            print(stop, "phase 2")
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.HIGH)
            sleep(2)
            stop = time.time() - t
            print(stop, "phase 3")
            GPIO.output(left, GPIO.LOW)
            GPIO.output(right,GPIO.HIGH)
            sleep(3)
            stop = time.time() - t
            print(stop, "phase 4")
            GPIO.output(left, GPIO.HIGH)
            GPIO.output(right,GPIO.HIGH)
            sleep(2)
            stop = time.time() - t
            print(stop, "phase 1")
        GPIO.output(left, GPIO.HIGH)
        GPIO.output(right,GPIO.HIGH)
class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1280x800")
        #self.master['bg']='green'
        self.bg = PhotoImage(file = "Interface/image/bg image.png")
        self.label1 = Label(self.master, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.first_page()

    def click(self,event):
        self.second_page()

    def choose_power(self):
        global mode
        self.confirm = messagebox.askquestion("Power wash mode", "Are you sure?")
        if self.confirm == 'yes':
            print("Power wash")
            mode="Power wash"
            self.third_page("Power wash")

    def choose_quick(self):
        global mode
        self.confirm = messagebox.askquestion("Quick wash mode", "Are you sure?")
        if self.confirm == 'yes':
            print("Quick wash")
            mode="Quick wash"
            self.third_page("Quick wash")  
    
    def choose_deli(self):
        global mode
        self.confirm = messagebox.askquestion("Delicates wash mode", "Are you sure?")
        if self.confirm == 'yes':
            print("Delicates")
            mode="Delicates wash"
            self.third_page("Delicates") 

    def update_database0(self):
        val_tuple=('','available','','','',Id)
        try:
            with connect(
                host="192.168.1.121",
                user="toruser",
                password="64011340",
                database="project",
            ) as connection:
                update_query = "UPDATE yord SET password =%s,state =%s,time =%s, mode =%s, idline =%s WHERE refer=%s"
                with connection.cursor() as cursor:
                    cursor.execute(update_query,val_tuple)
                    connection.commit()  
        except Error as e:
            pass

    def first_page(self):
        _thread.start_new_thread(self.update_database0,())
        self.frame1 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame1.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1  = Label(self.frame1, text="Yordreint", font=("Courier New", 110, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.27, anchor=CENTER)
        self.pic = Image.open("Interface/image/washing-machine.png")
        self.resize = self.pic.resize((250,250), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resize)
        self.label2 = Label(self.frame1, image=self.new_pic, background="white")
        self.label2.place(relx=0.5,rely=0.6, anchor=CENTER)
        self.label2.bind("<Button-1>", self.click)
        self.frame1.bind("<Button-1>", self.click)
    
    def update_database1(self):
        val_tuple=("standby",Id)
        try:
            with connect(
                host="192.168.1.121",
                user="toruser",
                password="64011340",
                database="project",
            ) as connection:
                update_query = "UPDATE yord SET state =%s WHERE refer=%s"
                with connection.cursor() as cursor:
                    cursor.execute(update_query,val_tuple)
                    connection.commit()  
        except Error as e:
            pass

    def second_page(self):
        _thread.start_new_thread(self.update_database1,())
        self.frame2 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame2.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame2, text="Choose mode",font=("Courier New", 90, "bold"),background="white")
        self.label1.place(relx=0.5,rely=0.25, anchor=CENTER)
        self.button1=Button(self.frame2, text = "Power wash", font=("Courier New", 14),height = 10, width = 20, command=self.choose_power)
        self.button1.place(relx=0.25,rely=0.57, anchor=CENTER)
        self.button2=Button(self.frame2, text = "Quick wash", font=("Courier New", 14), height = 10, width = 20, command=self.choose_quick)
        self.button2.place(relx=0.5,rely=0.57, anchor=CENTER)
        self.button3=Button(self.frame2, text = "Delicates wash", font=("Courier New", 14), height = 10, width = 20, command=self.choose_deli)
        self.button3.place(relx=0.75,rely=0.57, anchor=CENTER)

    def coindetect(self,mode,me):
        def incoming(pin):
            global impulse
            global i
            impulse+=1
            i = 0
        global i,label_coin,max_amount
        i = 0
        global impulse
        impulse = 0
        total = 0
        GPIO.add_event_callback(4, incoming)
        while True:
            i+=1
            # print("i=", i, " impulses: ",impulse, " total ", total)  
            if i>=30 and impulse>7:
                me.coin()

                total+=10
                impulse = 0
                print(total)
                if total >= 30 and mode == "Power wash":
                    print('finish')
                    break
                elif total >= 20 and (mode == "Quick wash" or mode == "Delicates"):
                    print('finish')
                    break
            elif i>=30 and impulse<=7 and impulse>2:
                total+=5
                impulse = 0
    
            sleep(0.01)

    def coin(self):
        print("s")
        global max_amount, label_coin
        max_amount -= 10
        if(max_amount <= 0):
            self.fourth_page()
        label_coin = Label(self.frame3, text=max_amount,font=("Courier New", 25),width=5, background="#D9D9D9",justify=LEFT)
        label_coin.place(relx=0.37,rely=0.5, anchor=CENTER)

    def third_page(self,mode_c):
        _thread.start_new_thread(self.coindetect,(mode,self))
        global max_amount, label_coin, mode_type
        self.frame3 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame3.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame3, text="Payment",font=("Courier New", 60, "bold"),background="white")
        self.label1.place(relx=0.5,rely=0.15, anchor=CENTER)
        self.label1 = Label(self.frame3, text="Cycle\noptions",font=("Courier New", 25),background="white",justify=LEFT)
        self.label1.place(relx=0.18,rely=0.34, anchor=CENTER)
        self.frame1 = Frame(self.frame3, background="#D9D9D9", highlightthickness=1,width=200, height=55, bd= 0)
        self.frame1.place(relx=0.37,rely=0.33, anchor=CENTER)
        self.label1 = Label(self.frame3, text="Total\nprice",font=("Courier New", 25),background="white",justify=LEFT)
        self.label1.place(relx=0.174,rely=0.5, anchor=CENTER)
        self.frame1 = Frame(self.frame3, background="#D9D9D9", highlightthickness=1,width=170, height=55, bd= 0)
        self.frame1.place(relx=0.37,rely=0.50, anchor=CENTER)    
        self.label1 = Label(self.frame3, text=mode_c,font=("Courier New", 25),background="#D9D9D9",justify=LEFT)
        self.label1.place(relx=0.37,rely=0.33, anchor=CENTER)
        max_amount = 20
        mode_type = 300
        if mode_c == "Power wash":
            max_amount = 30
            mode_type = 1800
        label_coin = Label(self.frame3, text=max_amount,font=("Courier New", 25),background="#D9D9D9",justify=LEFT)
        label_coin.place(relx=0.37,rely=0.5, anchor=CENTER)
        self.my_pic = Image.open("Interface/image/"+mode_c+".png")
        self.resize = self.my_pic.resize((300,300),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resize)
        self.label1 = Label(self.frame3, image=self.img, width=300, height=300)
        self.label1.place(relx=0.78,rely=0.6, anchor=CENTER)

        self.button1=Button(self.frame3, text = "◀ Back ", font=("Courier New", 20),height = 2, width = 6, command=self.second_page)
        self.button1.place(relx=0.1,rely=0.8, anchor=CENTER)

        self.button2=Button(self.frame3, text = "Go >", font=("Courier New", 20),height = 2, width = 6, command=self.fourth_page)
        self.button2.place(relx=0.3,rely=0.8, anchor=CENTER)

    def click_5(self):
        self.fifth_page()

    def click_1(self,event):
        print("click")
        self.first_page()
    
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

    def update_database2(self,password,mode):
        print(password,mode)
        val_tuple=(password,"working",mode,Id)
        try:
            with connect(
                host="192.168.1.121",
                user="toruser",
                password="64011340",
                database="project",
            ) as connection:
                update_query = "UPDATE yord SET password = %s,state = %s,mode = %s WHERE refer=%s"
                with connection.cursor() as cursor:
                    cursor.execute(update_query,val_tuple)
                    connection.commit()  
        except Error as e:
            print(password,mode)
        
    
    def fourth_page(self):
        global mode
        pw=self.random_ID()
        _thread.start_new_thread(self.update_database2,(pw,mode))
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

        self.label1 = Label(self.frame4, text="ID: "+pw, font=("Courier New", 20, "bold"),background="white")
        self.label1.place(relx=0.27, rely=0.85, anchor=CENTER)

        self.my_pic2 = Image.open("Interface/image/qr.png")
        self.resize2 = self.my_pic2.resize((300,300),Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(self.resize2)
        self.label1 = Label(self.frame4, image=self.img2, width=300, height=300)
        self.label1.place(relx=0.28,rely=0.47, anchor=CENTER)

        self.button1=Button(self.frame4, text = "Done", font=("Courier New", 20),height = 3, width = 10, command=self.click_5)
        self.button1.place(relx=0.77,rely=0.8, anchor=CENTER)

    def circuit(self,mode):
        if mode=='Quick wash':
            count(20)
        elif mode=='Delicates wash':
            count(25)
        elif mode=='Power wash':
            count(30)
            
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
            time.sleep(1)
            t -= 15
        
        self.seventh_page()

    def update_database3(self):
        x=datetime.datetime.now()
        time=x.strftime("%X")
        val_tuple=(time,Id)
        try:
            with connect(
                host="192.168.1.121",
                user="toruser",
                password="64011340",
                database="project",
            ) as connection:
                update_query = "UPDATE yord SET time=%s WHERE refer=%s"
                with connection.cursor() as cursor:
                    cursor.execute(update_query,val_tuple)
                    connection.commit()  
        except Error as e:
            pass

    def sixth_page(self):
        global mode_type
        _thread.start_new_thread(wash,(mode,))
        _thread.start_new_thread(self.circuit,(mode,))
        _thread.start_new_thread(self.update_database3,())
        self.frame6 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame6.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.countdown(mode_type)

    def update_database4(self):
        val_tuple=('finish',Id)
        try:
            with connect(
                host="192.168.1.121",
                user="toruser",
                password="64011340",
                database="project",
            ) as connection:
                update_query = "UPDATE yord SET password =%s, state =%s, WHERE refer=%s"
                with connection.cursor() as cursor:
                    cursor.execute(update_query,val_tuple)
                    connection.commit()  
        except Error as e:
            pass

    def seventh_page(self):
        _thread.start_new_thread(self.update_database4,())
        self.frame7 = Frame(self.master, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
        self.frame7.place(relx=0.5,rely=0.5, anchor=CENTER)
        self.label1 = Label(self.frame7, text="Finished!", font=("Courier New", 120, "bold"),background="white")
        self.label1.place(relx=0.5, rely=0.27, anchor=CENTER)
        self.pic = Image.open("Interface/image/laundry.png")
        self.resize = self.pic.resize((250,250), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resize)
        self.label2 = Label(self.frame7, image=self.new_pic, background="white")
        self.label2.place(relx=0.5,rely=0.6, anchor=CENTER)
        self.label2.bind("<Button-1>", self.click_1)
        self.frame7.bind("<Button-1>", self.click_1)
        

root = Tk()                                                                   
app(root)
root.mainloop()
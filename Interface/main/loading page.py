from tkinter import *
from time import sleep

root = Tk()
root.title("Yordreint")
root.geometry("1280x800")

# Add image file
bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")

# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

# Create Frame
frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
frame1.place(relx=0.5,rely=0.5, anchor=CENTER)

def play_animation():
        for i in range(4):
            k=400
            for j in range(4):
                Label(root, bg="#79E8FF",width=5,height=3).place(x=(k+100), y=500)
                sleep(0.3)
                root.update_idletasks()
                sleep(0.3) 
                k+=100
            Label(root, bg="white",width=60,height=3).place(x=500, y=500)
            root.update_idletasks()

        else:
            root.destroy()

label1 = Label(root, text="Loading", font=("Courier New", 140, "bold"),background="white")
label1.place(relx=0.5, rely=0.4, anchor=CENTER)
play_animation()
root.mainloop()
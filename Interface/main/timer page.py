from tkinter import *
import time
root = Tk()
root.title("Yordreint")
root.geometry("1280x800")  # width and height of the window

# Add image file
bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")

# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

# Create Frame
frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
frame1.place(relx=0.5,rely=0.5, anchor=CENTER)


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        Label(root, text=timer, bg="white", font=("Courier New", 310)).place(relx=0.5,rely=0.5, anchor=CENTER)
        root.update()
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    root.destroy()

countdown(10) # call the function 

root.mainloop() 
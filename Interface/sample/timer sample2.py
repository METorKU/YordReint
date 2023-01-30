from tkinter import *
import time
root = Tk()
root.title("Timer")
root.geometry("300x200")  # width and height of the window


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        Label(root, text=timer, bg="white").place(x=100, y=100)
        root.update()
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    root.destroy()


countdown(700) # call the function 
root.mainloop() 
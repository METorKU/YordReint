# Import the required library
from tkinter import *
import time

# Create an instance of tkinter frame
win = Tk()

# Set the size of the window
win.geometry('700x350')

# Make the window fixed to its size
win.resizable(False, False)

# Configure the background
win.config(bg='skyblue4')

# Create Entry Widgets for HH MM SS
sec = StringVar()
Entry(win, textvariable=sec, width=2,
   font='Helvetica 14').place(x=380, y=120)
sec.set('00')

mins = StringVar()
Entry(win, textvariable=mins, width=2, font='Helvetica 14').place(x=346, y=120)
mins.set('00')

hrs = StringVar()
Entry(win, textvariable=hrs, width=2, font='Helvetica 14').place(x=310, y=120)
hrs.set('00')

# Define the function for the timer
def countdowntimer():
   times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
   while times > -1:
      minute, second = (times // 60, times % 60)
      hour = 0
      if minute > 60:
         hour, minute = (minute // 60, minute % 60)
      sec.set(second)
      mins.set(minute)
      hrs.set(hour)

      # Update the time
      win.update()
      time.sleep(1)
      if (times == 0):
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      times -= 1

# Create a Label widget
Label(win, font=('Helvetica bold', 22), text='Set the Timer', bg='skyblue4', fg="white").place(x=260, y=70)

# Button widget to set the timer
Button(win, text='START', bd='2', bg='IndianRed1', font=('Helvetica bold', 10), command=countdowntimer).place(x=335, y=180)

win.mainloop()

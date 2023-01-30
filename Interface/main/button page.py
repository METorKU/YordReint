from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Yordreint")
root.geometry("1280x800") # window size

def choose_power():
    confirm = messagebox.askquestion("Power wash mode", "Are you sure?")
    if confirm == 'yes':
        root.destroy()

def choose_quick():
    messagebox.askquestion("Quick wash mode", "Are you sure?")   
    
def choose_deli():
    messagebox.askquestion("Delicates wash mode", "Are you sure?")

# Add image file
bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")

# Show image using label
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

# Create frame
frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
frame1.place(relx=0.5,rely=0.5, anchor=CENTER)

# Text
label1 = Label(root, text="Choose mode",font=("Courier New", 90, "bold"),background="white")
label1.place(relx=0.5,rely=0.25, anchor=CENTER)

# Create button for "Power wash"
button1=Button(root, text = "Power wash", font=("Courier New", 14),height = 15, width = 20, command=choose_power)
button1.place(relx=0.25,rely=0.57, anchor=CENTER)

# Create button for "Quick wash"
button2=Button(root, text = "Quick wash", font=("Courier New", 14), height = 15, width = 20, command=choose_quick)
button2.place(relx=0.5,rely=0.57, anchor=CENTER)

# Create button for "Delicates wash"
button3=Button(root, text = "Delicates wash", font=("Courier New", 14), height = 15, width = 20, command=choose_deli)
button3.place(relx=0.75,rely=0.57, anchor=CENTER)

root.mainloop()
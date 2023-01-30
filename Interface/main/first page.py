from tkinter import *
from PIL import ImageTk, Image

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

label1 = Label(root, text="Yordreint", font=("Courier New", 140, "bold"),background="white")
label1.place(relx=0.5, rely=0.27, anchor=CENTER)

# Open image 
pic = Image.open("/Users/Onlyjune/Desktop/Yor/image/washing-machine.png")

# Resize image
resize = pic.resize((300,300), Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resize)

label2 = Label(root, image=new_pic, background="white")
label2.place(relx=0.5,rely=0.6, anchor=CENTER)

def click(event):
    print("click")

label2.bind("<Button-1>", click)
frame1.bind("<Button-1>", click)

root.mainloop()
from tkinter import *
from PIL import ImageTk, Image

def main(mode_c):
    root = Tk()
    root.title("Yordreint")
    root.geometry("1280x800") # window size

    # Add image file
    bg = PhotoImage(file = "/Users/Onlyjune/Desktop/Yor/image/bg image.png")

    # Show image using label
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)

    # Create frame
    frame1 = Frame(root, background="white", highlightthickness=1,width=1000, height=600, bd= 0)
    frame1.place(relx=0.5,rely=0.5, anchor=CENTER)

    # Payment Text
    label1 = Label(root, text="Payment",font=("Courier New", 60, "bold"),background="white")
    label1.place(relx=0.5,rely=0.2, anchor=CENTER)

    # Cycle options
    label1 = Label(root, text="Cycle\noptions",font=("Courier New", 25),background="white",justify=LEFT)
    label1.place(relx=0.18,rely=0.34, anchor=CENTER)

    # Pink box
    frame1 = Frame(root, background="#D9D9D9", highlightthickness=1,width=200, height=55, bd= 0)
    frame1.place(relx=0.35,rely=0.33, anchor=CENTER)

    # Total price 
    label1 = Label(root, text="Total\nprice",font=("Courier New", 25),background="white",justify=LEFT)
    label1.place(relx=0.174,rely=0.5, anchor=CENTER)

    # Pink box
    frame1 = Frame(root, background="#D9D9D9", highlightthickness=1,width=200, height=55, bd= 0)
    frame1.place(relx=0.35,rely=0.50, anchor=CENTER)

    price = 20
    if mode_c == "Power wash":
        price = 30
    label1 = Label(root, text=price,font=("Courier New", 25),background="#D9D9D9",justify=LEFT)
    label1.place(relx=0.345,rely=0.5, anchor=CENTER)

    my_pic = Image.open("/Users/Onlyjune/Desktop/Yor/image/"+mode_c+".png")
    resize = my_pic.resize((300,300),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize)
    label1 = Label(root, image=img, width=300, height=300)
    label1.place(relx=0.7,rely=0.6, anchor=CENTER)


    label1 = Label(root, text=mode_c,font=("Courier New", 25),background="#D9D9D9",justify=LEFT)
    label1.place(relx=0.345,rely=0.33, anchor=CENTER)

    root.mainloop()

a = input("Enter: ")
t=""
if a == '1':
    t = "Power wash"
elif a == '2':
    t = "Quick wash"
elif a == '3':
    t = "Delicates"

main(t)
from tkinter import *
from PIL import Image, ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("1350x700+0+0")

        self.bg = Image.open("images/bg.jpg")
        self.bg_icon = ImageTk.PhotoImage(self.bg)

        self.user_icon = ImageTk.PhotoImage(file="images/userman.png")
        
        self.logo_icon = PhotoImage(file="")


        self.bg_lbl = Label(self.root, image=self.bg_icon)
        self.bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


        title = Label(self.root, text="Sistema de Login", font=("times new roman", 40, "bold"), bg="white", fg="black")
        title.place(x=0, y=0, width=1350, height=70)

        self.root.bind("<Configure>", self.resize_bg)

    def resize_bg(self, event):

        new_width = event.width
        new_height = event.height
        resized_bg = self.bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.bg_icon = ImageTk.PhotoImage(resized_bg)
        
        self.bg_lbl.config(image=self.bg_icon)
        
        Login_Frame = Frame(self.root, bg="White").place(x=400)
        
        logolbl = Label(Login_Frame, image=self.user_icon).grid(row=0, column=0,pady=20)

root = Tk()
obj = Login_System(root)
root.mainloop()

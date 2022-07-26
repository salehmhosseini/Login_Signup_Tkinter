from time import strftime
from tkinter import *



class ForgetPassword:
    def __init__(self):
        root = Tk()
        # icon image
        iconImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures/logo.png")
        root.iconphoto(False, iconImage)
        root.config(bg='LightCyan2')
        root.geometry("1000x650")
        root.title("Forger password Page")
        root.resizable(False, False)

        # logo image
        logoImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures/logo.png")
        logoImage = logoImage.subsample(3, 3)

        # logo label
        logoLabel = Label(root, image=logoImage, bg='LightCyan2')
        logoLabel.pack(pady=15)

        # help label
        helpLabel = Label(root, text="Forget password", font=("segoe print", 25, "bold"), bg='LightCyan2')
        helpLabel.pack()






        root.mainloop()
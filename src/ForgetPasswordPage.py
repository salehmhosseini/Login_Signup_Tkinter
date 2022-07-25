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




        root.mainloop()
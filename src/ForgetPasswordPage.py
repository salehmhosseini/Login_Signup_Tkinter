import re
from time import strftime
from tkinter import *

import ForgetPasswordEmailConfirmPage
import LoginPage


class ForgetPassword:
    emailVariable = StringVar
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

        # back to login page button handler function
        def backToLoinPageButtonHandler():
            root.destroy()
            LoginPage.LoginPage()

        # back to log in page button
        BackToLoginPageButton = Button(root, text="Back to login", font=("plain", 13),
                                       width=12, bd=3, bg="#E4CDEF", cursor="hand2",
                                       command=backToLoinPageButtonHandler)

        BackToLoginPageButton.place(x=10, y=10)

        # forget password page explain
        myFont = ("plain" , 20 , "bold")
        explainLabel1 = Label(root , bg='LightCyan2', text="\nare you forgot your password ?\n\n enter your email in below text field " , font=myFont )
        explainLabel1.pack()

        #forget password entry
        forgetPasswordEntry = Entry(root , width=25 , font=myFont , bd=3)
        forgetPasswordEntry.pack(pady=10)

        #sendcode button handler
        def sendCodeButtonHandler():
            root.destroy()
            ForgetPasswordEmailConfirmPage.ForgetPasswordComfrim()

        #send verify code into email
        sendCodeButton = Button(root, text="send" , font=myFont  , bg="#E4CDEF" , state=DISABLED , command=sendCodeButtonHandler)
        sendCodeButton.pack(pady=7)

        # email controller bye regex (regular expression)
        EmailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        def checkEmail(email):

            if (re.search(EmailRegex, email)):
                return True
            else:
                return False

        def emailController(event):

            self.emailStatus = checkEmail(forgetPasswordEntry.get())

            if (self.emailStatus):
                forgetPasswordEntry.config(bg="white")

                ForgetPassword.emailVariable = forgetPasswordEntry.get()
                sendCodeButton.config(state=NORMAL)

            else:
                forgetPasswordEntry.config(bg="#ffe1e1")
                sendCodeButton.config(state=DISABLED)

        forgetPasswordEntry.bind('<Return>', emailController)















        root.mainloop()
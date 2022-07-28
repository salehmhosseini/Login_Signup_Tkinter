import re
from tkinter import *

import LoginPage


class CahngePassword:
    def __init__(self):
        root = Tk()
        # icon image
        iconImage = PhotoImage(file="logo.png")
        root.iconphoto(False, iconImage)
        root.config(bg='LightCyan2')
        root.geometry("1000x650")
        root.title("Change password page")
        root.resizable(False, False)

        # logo image
        logoImage = PhotoImage(file="logo.png")
        logoImage = logoImage.subsample(3, 3)

        # logo label
        logoLabel = Label(root, image=logoImage , bg='LightCyan2' )
        logoLabel.pack(pady=15)

        # explain label
        explain = Label(root , text="Cahnge your password" , font=("segoe print" , 25 , "bold") , bg='LightCyan2' )
        explain.pack()

        #pssword label
        passwordLabel = Label(root, text="password", font=("plain", 17), bg='LightCyan2')
        passwordLabel.pack(pady=10)

        #password enrty
        # password text field
        passwordTextField = Entry(root, width=18, font=("plain", 17, "bold"), bd=2)
        passwordTextField.pack(pady=10)
        # password controller

        PasswordRegex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$"

        def checkPassword(password):

            if (re.search(PasswordRegex, password)):
                return True
            else:
                return False

        def passwordController(event):



            if ( checkPassword(passwordTextField.get())):
                passwordTextField.config(bg="white")
                confirmPasswordTextField.focus_set()

            else:
                passwordTextField.config(bg="#ffe1e1")

        passwordTextField.bind('<Return>', passwordController)

        # confirm password label
        confirmPasswordLabel = Label(root, text="Confirm password", font=("plain", 17), bg='LightCyan2')
        confirmPasswordLabel.pack()

        # confirm password field
        confirmPasswordTextField = Entry(root, width=18, font=("plain", 17, "bold"), bd=2)
        confirmPasswordTextField.pack(pady=10)

        # confirm password controller
        def confirmPasswordHandler():
            if (confirmPasswordTextField.get() == passwordTextField.get()):
                return True
            else:
                return False

        def confirmPasswordController(event):

            self.cnfirmPasswordStatus = confirmPasswordHandler()

            if (self.cnfirmPasswordStatus):
                confirmPasswordTextField.config(bg="white")

            else:
                confirmPasswordTextField.config(bg="#ffe1e1")

        confirmPasswordTextField.bind('<Return>', confirmPasswordController)

        #change password button handler
        def changePasswordButtonHadler():
            passwordTextField = ""
            confirmPasswordTextField = ""






        #change button
        changeButton = Button(root , text="Change" , font=("plain" , 15 ),width=12 ,  bd=3, bg="#E4CDEF" )
        changeButton.pack(pady=10)

        # back to loin page button
        def backToLoginPageButtonHandler():
            root.destroy()
            LoginPage.LoginPage()

        # back to loin page button
        backToLoginPageButton = Button(root, text="Login ", font=("plain", 13),
                                       width=15, bd=3, bg="#E4CDEF", cursor="hand2",
                                       command=backToLoginPageButtonHandler)
        backToLoginPageButton.place(x=10, y=10)

        root.mainloop()
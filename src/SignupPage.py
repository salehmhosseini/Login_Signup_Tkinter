from tkinter import *
import re
import HelpPage


import LoginPage


class SignUp:
    def __init__(self):
        root = Tk()
        iconImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures\logo.png")
        root.iconphoto(False, iconImage)
        root.geometry("1000x650")
        root.title("Signup Page")
        root.resizable(False, False)
        root.config(bg='LightCyan2')

        #statuses
        self.firstNameStatus=False
        self.lastNameStatus =False
        self.phoneNumberStatus=False
        self.emailStatus=False
        self.usernameStatus = False
        self.passwordStatus= False
        self.cnfirmPasswordStatus=False




        #sign up label
        signupLabel = Label(text='Sign up' ,font=("Georgia " , 24 , "bold"), bg='LightCyan2')
        signupLabel.pack(pady=10)

        #first name label
        firstNameLabel= Label(root , text = "First name" , font=("plain" ,13), bg='LightCyan2')
        firstNameLabel.pack()


        #first name text field
        firstNameTextField = Entry(root , width=18, font=("plain" ,13,  "bold") , bd=2 )
        firstNameTextField.pack(pady=10)

        # first name controller
        def lenController( string, length):
            if (len(string) < length or len(string) == 0):
                return False
            else:
                return True

        def firstNameController(event):

            self.firstNameStatus = lenController(firstNameTextField.get(), 3)

            if(self.firstNameStatus):
                firstNameTextField.config(bg="white")
                lastNameTextField.focus_set()

            else :
                firstNameTextField.config(bg="#ffe1e1")



        firstNameTextField.bind('<Return>', firstNameController)




        # last name label
        lastNameLabel = Label(root, text="Last name", font=("plain", 13), bg='LightCyan2')
        lastNameLabel.pack()

        # last name text field
        lastNameTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        lastNameTextField.pack(pady=10)

        #last name controller

        def lastNameController(event):

            self.lastNameStatus = lenController(lastNameTextField.get(), 3)

            if (self.lastNameStatus):
                lastNameTextField.config(bg="white")
                phoneNumberTextField.focus_set()

            else:
                lastNameTextField.config(bg="#ffe1e1")


        lastNameTextField.bind('<Return>', lastNameController)

        # phone number label
        phoneNumberLabel = Label(root, text="Phone number", font=("plain", 13), bg='LightCyan2')
        phoneNumberLabel.pack()

        # phone number text field
        phoneNumberTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        phoneNumberTextField.pack(pady=10)

        #phone number handler

        def phoneNumberNameController(event):


            def lenController(string, length):
                if (len(string) != length or len(string) == 0):
                    return False
                else:
                    return True
            self.phoneNumberStatus = lenController(phoneNumberTextField.get() , 11)
            def overriding():
                if(phoneNumberTextField.get()[0]=="0" and
                phoneNumberTextField.get()[1]=="9" and phoneNumberTextField.get().isnumeric()):
                    return True
                else :
                    return False

            if(self.phoneNumberStatus and overriding()):
                phoneNumberTextField.config(bg="white")
                emailTextField.focus_set()

            else :
                phoneNumberTextField.config(bg="#ffe1e1")


        phoneNumberTextField.bind('<Return>', phoneNumberNameController)

        # email label
        emailLabel = Label(root, text="Email", font=("plain", 13), bg='LightCyan2')
        emailLabel.pack()

        # emailtext field
        emailTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        emailTextField.pack(pady=10)

        # email controller bye regex (regular expression)
        EmailRegex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        def checkEmail(email):

            if (re.search(EmailRegex, email)):
                return True
            else:
                return False

        def emailController(event):

            self.emailStatus = checkEmail(emailTextField.get())

            if (self.emailStatus):
                emailTextField.config(bg="white")
                userNameTextField.focus_set()

            else:
                emailTextField.config(bg="#ffe1e1")

        emailTextField.bind('<Return>', emailController)
        # user name label
        userNameLabel = Label(root, text="Username", font=("plain", 13), bg='LightCyan2')
        userNameLabel.pack()

        # user name field
        userNameTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        userNameTextField.pack(pady=10)

        #username controller

        def usernameController(event):

            self.usernameStatus = lenController(userNameTextField.get(), 5)

            if (self.usernameStatus):
                userNameTextField.config(bg="white")
                passwordTextField.focus_set()

            else:
                userNameTextField.config(bg="#ffe1e1")

        userNameTextField.bind('<Return>', usernameController)
        # password label
        passwordlLabel = Label(root, text="Password", font=("plain", 13), bg='LightCyan2')
        passwordlLabel.pack()

        # password text field
        passwordTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        passwordTextField.pack(pady=10)

        #password controller

        PasswordRegex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$"

        def checkPassword(password):

            if (re.search(PasswordRegex, password)):
                return True
            else:
                return False
        def passwordController(event):

            self.passwordStatus = lenController(passwordTextField.get(), 8)


            if (self.passwordStatus and checkPassword(passwordTextField.get())):
                passwordTextField.config(bg="white")
                confirmPasswordTextField.focus_set()

            else:
                passwordTextField.config(bg="#ffe1e1")

        passwordTextField.bind('<Return>', passwordController)

        # confirm password label
        confirmPasswordLabel = Label(root, text="Confirm password", font=("plain", 13), bg='LightCyan2')
        confirmPasswordLabel.pack()

        # confirm password field
        confirmPasswordTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        confirmPasswordTextField.pack(pady=10)

        #confirm password controller
        def confirmPasswordHandler():
            if(confirmPasswordTextField.get()==passwordTextField.get()):
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


        #sign up button
        signUpButton = Button(root  , text="Sign up" , font=("plain" , 13 ) , width=12 , bd = 3 ,
                              bg="#E4CDEF", state=DISABLED)
        signUpButton.pack()
        def signUPButtonHandler(event):

            if(self.firstNameStatus and self.lastNameStatus and
            self.emailStatus and self.usernameStatus and
            self.phoneNumberStatus and self.passwordStatus and
            self.cnfirmPasswordStatus):
             signUpButton.config(cursor="hand2" , state=NORMAL)
            else :
                signUpButton.config(state=DISABLED)
        root.bind('<Return>', signUPButtonHandler)



        #back to login page button handler function
        def backToLoinPageButtonHandler():
            root.destroy()
            LoginPage.LoginPage()

        #back to log in page button
        BackToLoginPageButton = Button(root  , text="Back to login" , font=("plain" , 13 ) ,
                                       width=12 , bd = 3 ,bg="#E4CDEF", cursor="hand2" ,command= backToLoinPageButtonHandler)
        # BackToLoginPageButton.bind("<Button-1>" , backToLoinPageButtonHandler())
        BackToLoginPageButton.place(x=10 , y=10)

        #help button handler
        def helpButtonHandler(event):
            root.destroy()
            HelpPage.Help()



        #help button
        helpButton = Button(root  , text="Help (Ctrl+h)" , font=("plain" , 13 ) , width=12 , bd = 3 ,
                            bg="#E4CDEF" , cursor="hand2" , command=helpButtonHandler)
        helpButton.place(x = 870 , y =10)
        root.bind('<Control-h>' , helpButtonHandler)



        root.mainloop()


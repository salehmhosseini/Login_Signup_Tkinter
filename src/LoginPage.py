import re
from time import strftime
from tkinter import *
import tkinter as tk
from tkinter import messagebox


from captcha.image import ImageCaptcha
import SignupPage
import ForgetPasswordPage
import random
import string
import webbrowser
class LoginPage:


    emailvar = StringVar
    passwordvar = StringVar

    def __init__(self):

        # creat an object from Tkinter
        root = Tk()

        # icon image
        iconImage = PhotoImage(file="logo.png")

        root.iconphoto(False, iconImage)
        root.config(bg='LightCyan2')

        root.geometry("1000x650")
        root.title("Login Page")
        root.resizable(False, False)

        #statuses
        self.captchaStatus = False
        self.emailStatus = False
        self.passwordStatus = False

        self.email = StringVar
        self.password = StringVar

        # logo image
        logoImage = PhotoImage(file="logo.png")
        logoImage = logoImage.subsample(3, 3)

        # logo label
        logoLabel = Label(root, image=logoImage, bg='LightCyan2')
        logoLabel.pack()

        # xatrock label
        xatrockLabel = Label(root, text="Xatrock", fg="black", font=("segoe print", 20, "bold"), bg='LightCyan2')
        xatrockLabel.pack(fill="none" )

        # login Label
        loginLabel = Label(root, text="Login", fg="black", font=("segoe print", 20, "bold") , bg='LightCyan2')
        loginLabel.pack()

        # email label
        emailLabel = Label(root, text="Email", fg="black", font=("segoe print", 17, "bold") , bg='LightCyan2')
        emailLabel.pack()

        # email entry
        emailTextField = Entry(root , width=26, font=("plain", 13, "bold") , bd = 2)
        emailTextField.pack()

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
                passwordTextField.focus_set()
                LoginPage.emailVariable = emailTextField.get()
                self.email = emailTextField.get()
                self.emailStatus=True

            else:
                emailTextField.config(bg="#ffe1e1")
                self.emailStatus=False

        emailTextField.bind('<Return>', emailController)

        # password label
        passLabel = Label(root, text="Password", fg="black", font=("segoe print", 17, "bold") , bg='LightCyan2')
        passLabel.pack()

        # password entry
        passwordTextField = Entry(root, width=26, show="*", font=("plain", 13, "bold") , bd=2)
        passwordTextField.pack()

        # password controller

        PasswordRegex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$"

        def checkPassword(password):

            if (re.search(PasswordRegex, password)):
                return True
            else:
                return False

        def lenController( string, length):
            if (len(string) < length or len(string) == 0):
                return False
            else:
                return True

        def passwordController(event):

            self.passwordStatus = lenController(passwordTextField.get(), 8)

            if (self.passwordStatus and checkPassword(passwordTextField.get())):
                passwordTextField.config(bg="white")

                LoginPage.passwordvar = passwordTextField.get()


            else:
                passwordTextField.config(bg="#ffe1e1")

        passwordTextField.bind('<Return>', passwordController)

        #function of switch to forget password page
        def switchToForgetPasswordPage(self):
            root.destroy()
            ForgetPasswordPage.ForgetPassword()
        # foreget password hyper link


        forgetPasswordHyper = Label(root, text="Forgot password", fg="blue",
                                    cursor="hand2" , font=("plain", 12) , bg='LightCyan2')
        forgetPasswordHyper.pack(pady=5)
        forgetPasswordHyper.bind("<Button-1>",switchToForgetPasswordPage)

        #login logic function


        def loginLogic():
            pass
            # SQL.insertSQL()

            # if(SQL.updateSQL()):
            #     messagebox.showinfo("salam" , "ok")
            # else:
            #     messagebox.showinfo("salam" , "NOk")






       # catcha generator

        self.image = ImageCaptcha(width=200, height=60)

        self.x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase
                                       + string.digits) for _ in range(5))
        self.captcha_text = self.x

        self.image.write(self.captcha_text, 'CAPTCHA.png')

        self.captchaImage = PhotoImage(
            file="CAPTCHA.png")
        self.captchaImage.subsample(80, 80)
        self.captchaLabel = Label(root, image=self.captchaImage)
        self.captchaLabel.pack(pady=10)


        #captcha entry controller
        def captchaEntryController(event):
            if(captchaEntry.get()==self.x):
                captchaEntry.config(bg="white")
                self.captchaStatus=True
            else:
                captchaEntry.config(bg="#ffe1e1")
                self.captchaStatus = False


        #captcha entry
        captchaEntry = Entry(root ,width=20 , font=("plain" ,13,  "bold") , bd=2 )
        captchaEntry.pack()
        captchaEntry.bind("<Return>" , captchaEntryController)



        # change the captcha code by cliking on return button

        returnImage = PhotoImage(file="return.png")
        returnButton = Button(root , image=returnImage , cursor="hand2" , bd=0 , bg = "LightCyan2"  )

        returnButton.place(x=610 , y=392)


        # login button hedler fuction
        def loginButtonHandler():

            if(self.captchaStatus==False):
                messagebox.showerror("warning ", "Enter the correct captcha code!")

            if(self.passwordStatus==False):
                messagebox.showerror("warning ", "Enter the correct password!")

            #TODO
            # if(SQL.selectSQL()==False):
            #     messagebox.showerror("warning ", "your input email is not match the password!")

            else:
                messagebox.showinfo("Login status ", "You are successfully loged in!")




        #check robot label
        checkRobotLabel = Label(text="Im NOT a robot " , font=("plain" ,12) , bg="LightCyan2")

        checkRobotLabel.place(x=438 , y=480)


        # check button
        tk.Checkbutton(root,
             text='',
             onvalue='agree',
             offvalue='disagree' , bg='LightCyan2' , fg="green").place(x=548 , y=480)



        # login button
        loginButton = Button(root, width=14, height=-10, text="Login", fg="red", bg="#E4CDEF",
                             font=("plain", 12),
                             command=loginButtonHandler, cursor="hand2")
        loginButton.pack(pady=35)

        #dont have an account label
        dontHaveAccountLabel = Label(root , text = "Dont have an account?" , font=("plain" , 12)
                                     , bg='LightCyan2')
        dontHaveAccountLabel.pack()

        #function of switch to cignup page
        def switchToSignUpPage(self):
             root.destroy()
             SignupPage.SignUp()

        #signuo hyper link label
        signUpHyperLabel = Label(root , text = "sign up here" , font=("plain" , 12) , fg="blue"
                                 , cursor="hand2" , bg='LightCyan2')
        signUpHyperLabel.pack(pady=5)
        signUpHyperLabel.bind("<Button-1>",switchToSignUpPage)

        #show local time

        def my_time():
            time_string = strftime('%H:%M:%S %p\n %Y / %b / %d')  # time format
            l1.config(text=time_string)
            l1.after(1000, my_time)  # time delay of 1000 milliseconds

        my_font = ('times', 20, 'bold')  # display size and style

        l1 =Label(root, font = my_font , bg='LightCyan2')
        l1.place(x=20 , y=20)

        my_time()

        root.mainloop()

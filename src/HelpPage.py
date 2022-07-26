
from tkinter import *
import LoginPage
import SignupPage



class Help:
    def __init__(self):
        root = Tk()
        # icon image
        iconImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures/logo.png")
        root.iconphoto(False, iconImage)
        root.config(bg='LightCyan2')
        root.geometry("1000x650")
        root.title("Help")
        root.resizable(False, False)

        # logo image
        logoImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures/logo.png")
        logoImage = logoImage.subsample(3, 3)

        # logo label
        logoLabel = Label(root, image=logoImage, bg='LightCyan2')
        logoLabel.pack(pady=15)

        # help label
        helpLabel = Label(root , text="Help" , font=("segoe print" , 25 , "bold") ,bg='LightCyan2' )
        helpLabel.pack()

        # help explain

        helpExplainLabel = Label(root , bg='LightCyan2' ,font=("plain" , 13) , text="This is explanations for each of text fields in sign up page "
                                                                  "to understand how to have to fill the entries , read the following :)\n\n"
                                                                  "First name : should be input a first name that has more than 3 character.\n\n"
                                                                  "Last name : Same of the first name \n\n"
                                                                  "Phone number:should be input a phone number that it first character be 0 and seconds be 9 and "
                                                                  "it should be has 11 numeric characters \n\n"
                                                                  "Email : you should input the valid email . because that email entry logic has been implemented via regex\n"
                                                                  "Username:should be input at least 5 characters\n\n"
                                                                  "password : It has been implemented by regex and you should input a password that \n"
                                                                  " at least 8 characters and"
                                                                  "it has at least one capital and small alphabet and one number and one special character"
                                                                  "example \"@#$%*&\" \n\n"
                                                                  "confirm password : it shoud be right equal to password entries\n\n"
                                                                  "***************************************************************************\n\n"
                                                                  "Hint 1 : The signup button is disable and when you fill all of the entries correctly if will be enable\n\n"
                                                                  "Hint 2 : For confident filling and check your input , you should press enter after each time of fill")



        helpExplainLabel.pack()

        # back to signup page Button handler
        def backToSignUpPageButton():
            root.destroy()
            SignupPage.SignUp()

        # back to loin page button
        def backToLoginPageButtonHandler():
            root.destroy()
            LoginPage.LoginPage()


        # back to signup page Button
        backToSignUpPageButton = Button(root, text="Back To Signup ", font=("plain", 13),
                                       width=15, bd=3, bg="#E4CDEF", cursor="hand2" , command=backToSignUpPageButton)
        backToSignUpPageButton.place(x=15 , y=10)

        # back to loin page button
        backToLoginPageButton = Button(root, text="Login ", font=("plain", 13),
                                    width=15, bd=3, bg="#E4CDEF", cursor="hand2" , command=backToLoginPageButtonHandler)
        backToLoginPageButton.place(x=840, y=10)

        root.mainloop()


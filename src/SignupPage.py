from tkinter import *

class singUp:
    def __init__(self):
        root = Tk()
        iconImage = PhotoImage(file=r"C:\Users\HUAWEI\Desktop\FirstProject/logo.png")
        root.iconphoto(False, iconImage)
        root.geometry("1000x650")
        root.title("Signup Page")
        root.resizable(False, False)

        #sign up label
        signupLabel = Label(text='Sign up' ,font=("segoe print" , 24 , "bold") )
        signupLabel.pack(pady=10)

        #first name label
        firstNameLabel= Label(root , text = "First name" , font=("plain" ,13))
        firstNameLabel.pack()

        #first name text field
        firstNameTextField = Entry(root , width=18, font=("plain" ,13,  "bold") , bd=2 )
        firstNameTextField.pack(pady=10)

        # last name label
        lastNameLabel = Label(root, text="Last name", font=("plain", 13))
        lastNameLabel.pack()

        # last name text field
        lastNameTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        lastNameTextField.pack(pady=10)

        # phone number label
        phoneNumberLabel = Label(root, text="Phone number", font=("plain", 13))
        phoneNumberLabel.pack()

        # phone number text field
        phoneNumberTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        phoneNumberTextField.pack(pady=10)

        # email label
        emailLabel = Label(root, text="Email", font=("plain", 13))
        emailLabel.pack()

        # emailtext field
        emailTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        emailTextField.pack(pady=10)

        # user name label
        userNameLabel = Label(root, text="Username", font=("plain", 13))
        userNameLabel.pack()

        # user name field
        userNameTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        userNameTextField.pack(pady=10)

        # password label
        passwordlLabel = Label(root, text="Password", font=("plain", 13))
        passwordlLabel.pack()

        # password text field
        passwordTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        passwordTextField.pack(pady=10)

        # confirm password label
        confirmPasswordLabel = Label(root, text="Confirm password", font=("plain", 13))
        confirmPasswordLabel.pack()

        # confirm password field
        confirmPasswordTextField = Entry(root, width=18, font=("plain", 13, "bold"), bd=2)
        confirmPasswordTextField.pack(pady=10)

        #sign up button
        signUpButton = Button(root  , text="Sign up" , font=("plain" , 13 ) , width=12 , bd = 3 ,
                              bg="#E4CDEF", cursor="hand2")
        signUpButton.pack()

        #back to log in page button
        BackToLoginPageButton = Button(root  , text="Back to login" , font=("plain" , 13 ) ,
                                       width=12 , bd = 3 ,bg="#E4CDEF", cursor="hand2")
        BackToLoginPageButton.place(x=10 , y=10)

        #help button
        helpButton = Button(root  , text="Help" , font=("plain" , 13 ) , width=12 , bd = 3 ,
                            bg="#E4CDEF" , cursor="hand2")
        helpButton.place(x = 870 , y =10)


        root.mainloop()


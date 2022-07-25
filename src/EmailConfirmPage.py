from tkinter import *
import time
from tkinter import messagebox


class EmailConfirm:
    def __init__(self):
        root = Tk()

        # icon image
        iconImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures/logo.png")
        root.iconphoto(False, iconImage)
        root.config(bg='LightCyan2')
        root.geometry("1000x650")
        root.title("Confirm email Page")
        root.resizable(False, False)

        # logo image
        logoImage = PhotoImage(file=r"D:\Learn\programming\python\project1\The-first-python-project\pictures/logo.png")
        logoImage = logoImage.subsample(3, 3)

        # logo label
        logoLabel = Label(root, image=logoImage, bg='LightCyan2')
        logoLabel.pack(pady=15)

        # explain label
        explainLabel= Label(root , text="Wee need to verify your\n email adderess",
                            font=("plain" , 22),bg='LightCyan2')
        explainLabel.pack()

        # explain2 label
        explainLabel2 =  Label(root , text="Please enter the 6-digit code we sent to:",
                               font=("plain" , 12) , state=DISABLED,bg='LightCyan2')
        explainLabel2.pack(pady=37)

        # explain3 label
        explainLabel3 =  Label(root , text="Your 6-digit code", font=("plain" , 17)
                               ,bg='LightCyan2')
        explainLabel3.pack()

        # verify entry
        verifyEntry = Entry(root , width=10, font=("plain", 20, "bold"), bd=2)
        verifyEntry.pack(pady=10)

        #verifyButton
        verifyButton = Button(root , text="Verify" , width=10 , height=2 , font=("plain" , 13 )  ,
                              bd = 3 , bg="#E4CDEF")
        verifyButton.pack()

        ###########################


        # declaration of variables

        minute = StringVar()
        second = StringVar()

        # setting the default value as 0

        minute.set("00")
        second.set("02")

        # Using Entry class to take input from the user


        mins_box = Entry(
            root,
            width=3,
            font=("Arial", 18, ""),
            textvariable=minute ,
        state=DISABLED ,
        bd=3)

        mins_box.place(x=450, y=450)

        sec_box = Entry(
            root,
            width=3,
            font=("Arial", 18, ""),
            textvariable=second ,
            state=DISABLED ,
            bd=3)

        sec_box.place(x=500, y=450)

        # button widget
        resendButton = Button(root, text='Resend code', bd=3,
                              state=DISABLED, bg="#E4CDEF" )
        resendButton.place(x=456, y=499)

        def countdowntimer():
            resendButton.config(state=DISABLED)
            global user_input
            try:
                # store the user input
                user_input = int( int(minute.get()) * 60 + int(second.get()))
            except:
                messagebox.showwarning('', 'Invalid Input!')
            while user_input > -1:

                # divmod(firstvalue = user_input//60, secondvalue = user_input%60)
                mins, secs = divmod(user_input, 60)
                # store the value up to two decimal places
                # using the format() method

                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                # updating the GUI window
                root.update()
                time.sleep(1)

                # if user_input value = 0, then a messagebox pop's up
                # with a message
                if (user_input == 0):
                    messagebox.showinfo("Time Countdown", "Time of input is over . click resend code to be send you a new code ")
                    minute.set("00")
                    second.set("02")
                    resendButton.config(state=NORMAL , command=countdowntimer)

                # decresing the value of temp
                # after every one sec by one
                user_input -= 1
        countdowntimer()






        root.mainloop()
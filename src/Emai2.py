import random
import smtplib

import ForgetPasswordPage
import SignupPage

class Email2:
    verifyCodeVariable = int

    def __init__(self):
        def makeRandomNumber(self):
           Email2.verifyCodeVariable= random.randrange(100000, 999999)
           return Email2.verifyCodeVariable


        def getEmail(self):
            return SignupPage.SignUp.emailVariable
        def getEmail2(self):
            return ForgetPasswordPage.ForgetPassword.emailVariable

        def sendMail(self):
            emailHost = "smtp.gmail.com"
            emailHostUser = "salehtest2002@gmail.com"
            emailPortSSL = 465
            emailHostPassword = "indryqehepsntkem"

            with smtplib.SMTP_SSL(emailHost, emailPortSSL) as server:
                server.login(emailHostUser, emailHostPassword)
                server.sendmail(emailHostUser, getEmail2(self) ,
                                f" the verify code : {makeRandomNumber(self)}")

        sendMail(self)



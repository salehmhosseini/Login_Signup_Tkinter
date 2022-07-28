import random
import smtplib

import ForgetPasswordPage
import SignupPage

class Email:
    verifyCodeVariable = int

    def __init__(self):
        def makeRandomNumber(self):
           Email.verifyCodeVariable= random.randrange(100000, 999999)
           return Email.verifyCodeVariable

        # email : salehteset2002@gmail.com
        #password : "indryqehepsntkem"



        def getEmail(self):
            return SignupPage.SignUp.emailVariable
        def getEmail2(self):
            return ForgetPasswordPage.ForgetPassword.emailVariable

        def sendMail(self):
            emailHost = "smtp.gmail.com"
            emailHostUser = "salehtest22002@gmail.com"
            emailPortSSL = 465
            emailHostPassword ="vshyekedzycrdyre"

            with smtplib.SMTP_SSL(emailHost, emailPortSSL) as server:
                server.login(emailHostUser, emailHostPassword)
                server.sendmail(emailHostUser, getEmail2(self) ,
                                f" the verify code : {makeRandomNumber(self)}")

        sendMail(self)


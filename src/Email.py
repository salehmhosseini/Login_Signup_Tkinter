import random
import smtplib
import SignupPage

class Email:
    verifyCodeVariable = int

    def __init__(self):
        def makeRandomNumber(self):
           Email.verifyCodeVariable= random.randrange(100000, 999999)
           return Email.verifyCodeVariable


        def getEmail(self):
            return SignupPage.SignUp.emailVariable

        def sendMail(self):
            emailHost = "smtp.gmail.com"
            emailHostUser = "salehtest2002@gmail.com"
            emailPortSSL = 465
            emailHostPassword = "indryqehepsntkem"

            with smtplib.SMTP_SSL(emailHost, emailPortSSL) as server:
                server.login(emailHostUser, emailHostPassword)
                server.sendmail(emailHostUser,"salehmhosseini2002@gmail.com",
                                f" the verify code : {makeRandomNumber(self)}")

        sendMail(self)



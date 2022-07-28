
import mysql.connector
import SignupPage
import LoginPage
def insertSQL():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python_signup"
    )
    # preparing a cursor object
    cursorObject = conn.cursor()
    sql = "INSERT INTO python_signup (firstName, lastName , phone , email , username , password) VALUES (%s, %s ,%s, %s ,%s, %s )"
    val = (SignupPage.SignUp.inputFirstName, SignupPage.SignUp.inputLastName,SignupPage.SignUp.inputPhone, SignupPage.SignUp.inputEmail, SignupPage.SignUp.inputUername, SignupPage.SignUp.inputPassword)
    cursorObject.execute(sql, val)
    conn.commit()

def selectSQL():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python_signup"
    )

    # preparing a cursor object
    cursorObject = conn.cursor()
    query = "SELECT password FROM python_signup WHERE email = %s"
    var = [LoginPage.LoginPage.emailvar]


    cursorObject.execute(query , var)
    myresult = cursorObject.fetchal()
    conn.commit()
    global a

    for x in myresult:
        a = x[0]

    if (str(a) == str(LoginPage.LoginPage.passwordvar)):
        return True
    else:
        return False






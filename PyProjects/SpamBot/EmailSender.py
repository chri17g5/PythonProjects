from email import message
import smtplib, ssl

email = "klementhuskatbad@gmail.com"
password = ""

receiver = email
theMessage = """\
    Husk at gaa i bad! klement Du lugter!!!
    """

port = 465
sslcontext = ssl.create_default_context()

try:
    for x in range(1):
        connection = smtplib.SMTP_SSL("smtp.gmail.com", port, context=sslcontext)
        connection.login(email, password)
        connection.sendmail(email, receiver, theMessage)

        print("Message Sent!")

except Exception as ex:
    print(ex)


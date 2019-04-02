import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(from_email, password, to_email, subject, message):
    # setup the parameters of the message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    try:

        # set up the SMTP server
        # host and port, you can leave port empty as 465 is the default anyway
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something went wrong: ' + str(e))
        return False

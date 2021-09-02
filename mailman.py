import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(from_email, name, password, to_email, subject, message, filename):
    # setup the parameters of the message
    msg = MIMEMultipart()
    msg['From'] = name + ' <' + from_email + '>'
    msg['To'] = to_email
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # attaching file
    # We assume that the file is in the directory where you run your Python script from
    with open(filename, "rb") as attachment:
        # The content type "application/octet-stream" means that a MIME attachment is a binary file
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(part)

    # Add header
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    msg.attach(part)
    try:

        # set up the SMTP server
        # host and port, you can leave port empty as 465 is the default anyway
        server = smtplib.SMTP_SSL('smtp.gmaill.com', 465)
        server.ehlo()
        server.login(from_email, password)
        server.sendmail(from_email, msg['To'], msg.as_string())
        server.close()
        return True
    except Exception as e:
        print('Something went wrong: ' + str(e))
        return False

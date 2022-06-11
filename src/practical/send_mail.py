import smtplib, ssl
"""
If found SSL Error, run /Applications/Python*/Install\\ Certificates.command
"""
print(ssl.OPENSSL_VERSION)

# we dont need to expose credential in the repo, so prompt it
port = 587  # For SSL
smtp_server = input("Type your smtp server and press enter: ") # Enter smtp server
sender_email = input("Type your sender email: ")  # Enter your address
receiver_email = input("Type destination email and press enter: ")  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Mail Test

This message is sent from python tutorial."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
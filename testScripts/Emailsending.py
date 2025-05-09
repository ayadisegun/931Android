import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import pytest


#this script works to send normal email from my personal account.
# def sendEmail(senderEmail, receiverEmail, content):
#     server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     server.login(senderEmail, "apwh wvav mqja iifx")
#     server.sendmail(senderEmail,receiverEmail,content)
#     server.quit()



# def send_mail(sender_address, sender_pass, receiver_address, subject, mail_content, attach_file_name,
#               ):
#     # sender_pass = 'Selenium@234'
#
#     # setup the MIME
#     message = MIMEMultipart()
#     message['From'] = sender_address
#     message['To'] = receiver_address
#     message['Subject'] = subject
#
#     # The subject line
#     # The body and the attachments for the mail
#     message.attach(MIMEText(mail_content, 'plain'))
#     attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
#     payload = MIMEBase('application', 'octate-stream')
#     payload.set_payload((attach_file).read())
#     encoders.encode_base64(payload)  # encode the attachment
#     # add payload header with filename
#     payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
#     message.attach(payload)
#
#     # Create SMTP session for sending the mail
#     session = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     session.login(sender_address, sender_pass)  # login with mail_id and password
#     text = message.as_string()
#     session.sendmail(sender_address, receiver_address, text)
#     session.quit()
#     print('Mail Sent')
#
#
# send_mail("ayadisegun02@gmail.com", "apwh wvav mqja iifx", "aitunuayo@gmail.com", "Rapture Testing", "Did you get this email, give feedback if you got the attachment too", "C:\\Users\\Segun\\PycharmProjects\\Android931\\testScripts\\report\\htmlreport.html")








import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()

message["From"] = "ozgur968@gmail.com" # define sender

message["To"] = "" # define to person who will recieve our mail

message["Subject"] = "Smpt deneme" # content name

content = """
  I'm trying to sent email with python my babe , but also i just want to say I LOVE YOU
  
  Your love
  """

messagePlace = MIMEText(content, "plain")
message.attach(messagePlace) # define our content to message object

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587) # google service connection
    mail.ehlo()
    mail.starttls()
    mail.login("", "") # our email address and password
    mail.sendmail(message["From"], message["To"], message.as_string()) # sent
    print("Mail has been sent ...")
    mail.close()
except:
    sys.stderr.write("error has been occured")
    sys.stderr.flush()

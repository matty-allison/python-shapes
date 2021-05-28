import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


senders_email = "mattymallison@gmail.com"
receiver_email = "mattymallison@gmail.com, thapelo@lifechoices.co.za"
password = input("Enter senders password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg["From"] = senders_email
msg["To"] = receiver_email
msg["Subject"] = subject

message = "hi there"
message = message + " hope this sends"
msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()

s.login(senders_email, password)

s.sendmail(senders_email, receiver_email, text)
s.quit()


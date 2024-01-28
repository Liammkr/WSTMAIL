import smtplib
from email.message import EmailMessage
a = 1
t = 0
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "liamkrubin@gmail.com"
    msg['from'] = user
    password = "xbedywkocqyhkjnh"
    #vqkjdjnwtzyszfdi
  
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

toEmail= input("Recieving Email: ") 

if toEmail.lower() == ' ': 
   exit

while a == 1:
    email_alert("Not Liam","Hi",str(toEmail))
    t+=1
    print("Emails Sent: "+ str(t))

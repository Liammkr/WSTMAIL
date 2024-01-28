mport smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "lr14@smmk12.org"
    msg['from'] = user
    password = "vqkjdjnwtzyszfdi"
  
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

import smtplib
from email.message import EmailMessage
from colorama import Fore
from colorama import init
import os
from time import sleep
import re
import requests
from random import randint
init()
start = True
while start == True:
    os.system('cls')
    print(
    Fore.MAGENTA +
    """                                                                                        
                                                                                       
                          .                .,                                ., G:        
                         ;W               ,Wt j.                            ,Wt E#,    :
            ;           f#E GEEEEEEEL    i#D. EW,                   ..     i#D. E#t  .GE
          .DL         .E#f  ,;;L#K;;.   f#f   E##j                 ;W,    f#f   E#t j#K;
  f.     :K#L     LWLiWW;      t#E    .D#i    E###D.              j##,  .D#i    E#GK#f  
  EW:   ;W##L   .E#fL##Lffi    t#E   :KW,     E#jG#W;            G###, :KW,     E##D.   
  E#t  t#KE#L  ,W#;tLLG##L     t#E   t#f      E#t t##f         :E####, t#f      E##Wi   
  E#t f#D.L#L t#K:   ,W#i      t#E    ;#G     E#t  :K#E:      ;W#DG##,  ;#G     E#jL#D: 
  E#jG#f  L#LL#G    j#E.       t#E     :KE.   E#KDDDD###i    j###DW##,   :KE.   E#t ,K#j
  E###;   L###j   .D#j         t#E      .DW:  E#f,t#Wi,,,   G##i,,G##,    .DW:  E#t   jD
  E#K:    L#W;   ,WK,          t#E        L#, E#t  ;#W:   :K#K:   L##,      L#, j#t     
  EG      LE.    EG.            fE         jt DWi   ,KK: ;##D.    L##,       jt  ,;     
  ;       ;@     ,               :                       ,,,      .,,                   
                           
                                                                              liamm --
                                                                                        """
)
    with open('settings.txt', 'r') as file:
        # Read the file line by line
        lines = file.readlines()
        # Iterate over the lines
        for i in range(0, len(lines), 4):
            if i + 3 < len(lines):  # Check if there are enough lines left in the file
                sender_email_match = re.search(r'senderemail="(.*?)"', lines[i])
                sender_apppass_match = re.search(r'senderapppass="(.*?)"', lines[i + 1])
                body_match = re.search(r'body="(.*?)"', lines[i + 2])
                subject_match = re.search(r'subject="(.*?)"', lines[i + 3])
                if sender_email_match and sender_apppass_match and body_match and subject_match:
                    sender_email = sender_email_match.group(1)
                    sender_apppass = sender_apppass_match.group(1)
                    pre_body = body_match.group(1)
                    pre_subject = subject_match.group(1)
    if sender_email == '':
        senderEmail = input(Fore.LIGHTBLUE_EX +"Sender Email: ")
    else: 
        senderEmail = sender_email
    if sender_apppass == '':
        senderPass = input(Fore.LIGHTBLUE_EX +"Sender App Password: ")
    else:
        senderPass = sender_apppass 
    toEmail = input(Fore.LIGHTBLUE_EX +"Recieving Email: ")
    if pre_subject == '': 
        subjectInput = input(Fore.LIGHTBLUE_EX +"Subject: ")
    else:
        subjectInput = pre_subject
    if pre_body == '':
        bodyInput = input(Fore.LIGHTBLUE_EX +"Body: ")
    else:
        bodyInput = pre_body
    a = input(Fore.LIGHTBLUE_EX +"Ammount Of Emails: ")
    def email_alert(subject, body, to):
       msg = EmailMessage()
       msg.set_content(body)
       msg['subject'] = subject
       msg['to'] = to
       user = str(senderEmail)
       msg['from'] = user
       password = str(senderPass)
       server = smtplib.SMTP("smtp.gmail.com", 587)
       server.starttls()
       server.login(user, password)
       server.send_message(msg)
       server.quit()
    aInt = int(a)
    t=0
    while aInt > 0:
        if pre_body == 'random':
            bodyInput = randint(10000000000000000000000000000000000,999999999999999999999999999999999999999999999999999)
        if pre_subject == 'random':
            subjectInput = randint(10000000000000000000000000000000000,999999999999999999999999999999999999999999999999999)
        def measure_response_time(url):
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    ping = response.elapsed.total_seconds() * 1000
                    print(Fore.GREEN + "Emails Sent: "+ str(t)+ "| STATUS: [201] ACCEPTED"+ " | Ping To www.gmail.com : " + str(response.elapsed.total_seconds() * 1000))
                else:
                    print(f"Failed to fetch {url}, status code: {response.status_code}")
            except Exception as e:
                print(f"Error while fetching {url}: {e}")
        email_alert(str(subjectInput),str(bodyInput),str(toEmail))
        t+=1
        measure_response_time("https://www.gmail.com")
        aInt-=1
    else:
        print(Fore.YELLOW+"FINISHED")
        restart = input(Fore.LIGHTCYAN_EX+"More Emails (y/n)")
        if restart == 'y':
            start = True
        else:
            print(Fore.RED+"Closing Program in 2s")
            sleep(2)
            start = False

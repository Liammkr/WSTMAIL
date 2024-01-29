import smtplib
from email.message import EmailMessage
from colorama import Fore
from colorama import init
import os
from time import sleep
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
    senderEmail = input(Fore.LIGHTBLUE_EX +"Sender Email: ") 
    senderPass = input(Fore.LIGHTBLUE_EX +"Sender App Password: ") 
    toEmail = input(Fore.LIGHTBLUE_EX +"Recieving Email: ") 
    subjectInput = input(Fore.LIGHTBLUE_EX +"Subject: ")
    bodyInput = input(Fore.LIGHTBLUE_EX +"Body: ")
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
        email_alert(str(subjectInput),str(bodyInput),str(toEmail))
        t+=1
        print(Fore.GREEN + "Emails Sent: "+ str(t)+ " STATUS: [201] ACCEPTED")
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

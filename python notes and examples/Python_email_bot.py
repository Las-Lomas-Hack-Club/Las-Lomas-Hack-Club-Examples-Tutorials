#sorry, was too lazy to make a gui with tkinter or wx python :(
import smtplib
import time
#need correct password to use email
enter_pass = input("Type in password: ")
#subject of message
subject = input("Type header message you want to send, warning, this will go to all hack club members: ")
body = input("Type the message you want to send, warning, this will go to all hack club members: ")
email_bot_server = smtplib.SMTP("smtp.EMAIL PROVIDER HERE.com",PORT NUMBER HERE)
email_bot_server.ehlo()
#starts ttls encryption.  Not required but recommended
email_bot_server.starttls()
email_bot_server.ehlo()
# do not put passwords in source code
email_bot_server.login('EMAIL HERE',enter_pass)
try:
    with open ('FILE NAME HERE') as file:
        for line in file: 
            name_with_email = line.split()
            final_message = (subject, name_with_email[1],body )
            email_bot_server.sendmail('llhackclub@gmail.com',name_with_email[0],final_message)
            print(name_with_email[0])
            #names
            print(name_with_email[1])
    email_bot_server.quit()
finally:
    print("process finished")

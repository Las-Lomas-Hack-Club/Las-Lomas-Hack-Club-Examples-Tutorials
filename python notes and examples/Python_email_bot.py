#sorry, was too lazy to make a gui with tkinter or wx python :(

import smtplib

import time

#need correct password to use email

enter_pass = input("Type in password: ")

#think before you email kids
print("Please do not butt dial all of LL hack club")
time.sleep(10)
greeting = input("Type greeting message you want to send, warning, this will go to all hack club members: ")

body = input("Type the message you want to send, warning, this will go to all hack club members: ")

subject = input("Enter subject:")
#set up connection
#ex email_bot_server = smtplib.SMTP("smtp.gmail.com",587)
email_bot_server = smtplib.SMTP("smtp.EMAIL PROVIDER HERE.com",YOURPORTHERE)
#testing server
email_bot_server.ehlo()

#starts ttls encryption.  Not required but recommended
email_bot_server.starttls()
#testing server
email_bot_server.ehlo()

# do not put passwords in source code
#note, if using gmail you might need to get a special app key.  Contact me if u need help :)
#ex email_bot_server.login("sumdude@gmail.com",enter_pass)
email_bot_server.login('YOUR EMAIL HERE',enter_pass)

try:
#note this only takes txt files in the form of EMAIL NAME \n
    with open ('YOUR TEXT FILE HERE') as file:

        for line in file: 

            name_with_email = line.split()

            final_body = ("Subject:{}\n\n{}{}{}".format(subject,greeting,name_with_email[1],body))

            email_bot_server.sendmail('llhackclub@gmail.com',name_with_email[0],final_body)

            print("Done emailing ",name_with_email[1]," at" ,name_with_email[0])


    email_bot_server.quit()

finally:
    print("process finished")
#Keep coding!  

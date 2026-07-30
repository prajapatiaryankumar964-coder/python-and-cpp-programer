import smtplib
import math, random


print("welcome to mail Application")

receivers_email=input('Enter your Email Address:')
name=input('Enter your name:')

subject=input('Enter your Subject:')
msg=input('Enter your Message:')


digits = "0123456789"
OTP = ""
 
for i in range(4):
    OTP += digits[math.floor(random.random() * 10)]
 


message="Name="+name+"\nSubject="+subject+"\nYour OTP="+OTP+"\nYour Message="+msg


try:
    sender_mail="prajapatialpa989@gmail.com"

    password="gkyt xsmj kuml wiid"
    smtpObj=smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.starttls()
    smtpObj.login(sender_mail,password)

    smtpObj.sendmail(sender_mail,receivers_email,message)
    print("success mail")

except Exception as ex:
    print(ex)
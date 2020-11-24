import smtplib

sender_email = input("nhap email cua ban: ")
rec_email = input("nhap email nhan: ")
password = input(str("pass: "))
message = input("nhap noi dung: ")
n = int(input("so lan ban muon gui: "))
for i in range(n):
 sever = smtplib.SMTP('smtp.gmail.com',587)
 sever.starttls()
 sever.login(sender_email,password)
 print("thanh cong")
 sever.sendmail(sender_email,rec_email,message)
 print("da gui den:",rec_email)
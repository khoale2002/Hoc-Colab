import os,string,random

capa = 1000
limit = int(input("NHAP GIOI HAN DU LIEU 1-1024MB: "))
if limit >= 1 and limit <= 1024:
 for i in range(int(limit * 1024 / capa)):
    file = open('file' + str(i + 1) + '.txt', 'w')
    file.write(random.choice(string.ascii_letters))
 if int(limit* 1024 % capa) >0 :
    file = open('file end ' + '.txt', 'w')
    file.write(random.choice(string.ascii_letters))
 if file.seek(0):
    os.remove(file)
 file.close()
 print("thanh cong")
else:
    print("Sai gioi han")





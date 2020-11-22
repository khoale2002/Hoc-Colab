import random
x = int(input("nhap gioi han dau cua list: "))
y = int(input("nhap gioi han sau cua list: "))
n = int(input("nhap so gia tri trong list: "))
if n <= 0 :
    print("khong co gia tri nho nhat")
else:
 list = random.sample(range(x,y),n)
 print ("List random la  : ",(list))
 min = list[0]
 for i in list:
    if i < min:
        min = i
 print ("min = ",min)

import random
import string

def text(): 
    k=''.join(random.sample(sstring,one_file))
    return k 

dlmax = int(input('nhap gioi han du lieu (MB): '))
while (dlmax<1 or dlmax>1024):
	dlmax = int(input('nhap lại gioi han du lieu (1->1024MB): '))

one_file = 1000*1024 

m = dlmax*(2**20)//(one_file) 
n = dlmax*(2**20)%(one_file)
sstring= string.ascii_lowercase*39385

print('số file có kích thước 1KB là: ',m)
print('file cuối cùng có kích thước: ',n/1024,"KB")
for i in range(m):
	file=open('file'+str(i+1)+'.txt' ,'w')
	file.write(text())

	file.close()
if n>0: 
    file=open('file cuoi cung'+'.txt' ,'w')
    file.write(''.join(random.sample(sstring,n)))
file.close()
print('done')




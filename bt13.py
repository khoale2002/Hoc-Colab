import os
list1=list()
list2=list()
for (root,dirs,files) in os.walk('C:'):
    print("thu muc o dia C:",root)
    print("thu muc con",dirs)
    print("tap tin ",files)
for (root,dirs,files) in os.walk('C:'):
    for i in files:
        list1.append(i)
    for x in dirs:
        list2.append(x)
print("list tap tin ",list1)
print("list thu muc con ",list2)
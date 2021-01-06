import os

x=input("ten thu muc: ")
y=input("ten file: ")
z=input("noi ban muon luu: ")
os.chdir(z)
os.mkdir(x)
e= z + x
os.chdir(e)
f= open(y,"w")
f.close()

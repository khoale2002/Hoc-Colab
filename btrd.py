import random
List = []
List2 = []
List.append(random.randint(50, 1000))
print('gia tri cua list: ',List)
x = random.sample(range(-1000,1000),10)
print ("List 10 so nguyen random la  : ",(x))
for i in range(0, 10):
    x = round(random.uniform(-1000.0, 1000.0), 2)
    List2.append(x)
print('list 10 so thuc: ',List2)
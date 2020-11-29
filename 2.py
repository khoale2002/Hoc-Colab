import string,random
list = []
letters = string.ascii_letters
for i in range((random.randint(50,100))) :
 dict = {}
 dict['name'] =''.join(random.choice(letters) for i in range(random.randint(1, 10)))
 dict["age"] = random.randint(0,100)
 list.append(dict)
print(list)

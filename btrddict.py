import string,random
dict = {}
letters = string.ascii_letters
dict['name'] =''.join(random.choice(letters) for i in range(random.randint(1,10)))
dict["age"] = random.randint(0,100)
print(dict)
list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}),
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}),
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}),
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]
for index,value in enumerate(list2, 1):
    print(f'{index}: {value}')
    for i in value:
        print(i)
        for x in i :
            print(x, ": ", i.get(x))
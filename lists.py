list1 = [3, 5, 7, 9, 10.5]
print(list1)
list1.append('Python')
print(len(list1))
print(list1)
print(list1[0])
print(list1[5])
del list1[5]
print(list1)
dict1 = {"city": "Москва", "temperature": 20}
print(dict1["city"])

dict1["temperature"] = dict1["temperature"] - 5
print(dict1)
print(dict1.get('country', 'Россия'))
dict1['date']='27.05.2019'
print(dict1)
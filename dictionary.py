my_dict = {'name': 'Arif', 'age': 25}

print(my_dict.get('name'))  # Output: Arif

# keys()
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# update()
my_dict.update({'age': 26, 'city': 'Delhi'})
print(my_dict)  # Output: {'name': 'Arif', 'age': 26, 'city': 'Delhi'}

# pop()
my_dict.pop('city')
print(my_dict)  # Output: {'name': 'Arif', 'age': 26}
print(type(my_dict))  # Output: <class 'dict'>
# d={}
# print(type(d))  # Output: <class 'dict'>
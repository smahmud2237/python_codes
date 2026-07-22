'''
There are many data types in PYTHON like: 
1. int => Integers = Whole numbers such as 3, 350, 1000
2. float => Floating Point = Numbers with a decimal point such as 2.3, 4.5, 100.0
3. str => Strings = Ordered sequence of characters: "Hello", 'sammy', "2000"
4. list => Lists = Ordered sequence of objects: [10, "Hello", 300.5]
5. dict => Dictionaries = Unordered Key: Value pairs: {"mykey":"value", "name":"Farhan"}
6. tup => Tuples = Ordered immutable sequence of objects: (10, "hello", 100.23)
7. set => Sets = Unordered collection of unique objects: {"a", "b"}
8. Booleans => bool = Logical value indicating True or False
<----------------------------------================------------------------------------>
Rules for variables names:
1. Names can not start with a Number.
2. There can be no spaces in the name of the variable, use _varName insted.
3. Can't use any of these symbols: ",<>/?|()!@ # $ % ^ & * ~ - +

Best Practices for variable names:
1. It's considered best practice (PEP8) that names are lowercase.
2. Avoid using words that have special meaning in python like "list" and "str"
'''


my_pet = 2
print(f'I have {my_pet} pets')
print(type(my_pet))
# in python reassign new data type in existing variable is totally okay. Cause python is dynamic Language.
my_pet = ["Jack", "Don"]
print(f'My pets name is {my_pet}')
print(type(my_pet))



'''
1. Lists are ordered sequences of object types which is mutable.
2. They use [] brackets and commas to separate objects in the list like [1, 2, 3, 4, 5]
3. Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.
'''
my_list = [1, 3, 4, 2, 5, 6]
my_list.sort()
print(my_list)
my_list[2] = 'three'
# pop and append can remove and add items from last elements in a list
my_list.pop()  # my_list.pop(5)  
print(my_list[::])
print(my_list[::2])
# python list are very flexible. They can hold any data type in lists
new_list = ['STRING', 100, 23.5]
print(len(new_list))
print(new_list[0])
new_list.append('six')
# let's concatenate my_list and new_list and print them
result = my_list + new_list
print(result)

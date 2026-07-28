'''
1. Tuples: Ordered sequence of objects which is immutable.
2. Tuples are very similar to lists. However they have one key difference - immutability (can't be changed).
3. Once an element is inside a tuple, it can not be reassigned.
4. Tuples use parenthesis like: (1, 2, 3)
5. So in a nutshell, we use tuple where we will use continuous values and it will never be changed.
'''
# list and tuple diff
my_list = [1, 2, 3]
print(type(my_list))
my_list[2] = 'three'
print(my_list)
# Here the big diff between list and tuple. we can update list(mutable) but can't update tuple(immutable).  
my_tuple = (1, 2, 3)
print(type(my_tuple))
print(len(my_tuple))
# if we ever try to update value in tuple what happens see below output
'''
my_tuple[1] = 'two'  
print(my_tuple)
# TypeError: 'tuple' object does not support item assignment
''' 






'''
Many objects in Python are "iterable", meaning we can iterate over every element in the object. Such as every
element in a list or every character in a string. We can use for loops to execute a block of code for every iteration.
The term "iterable" means you can iterate over the objects. For example, you can iterate over every character in a string,
iterate over every item in a list, iterate over every key in a dictionary.
*** Syntax of a for loop:
                my_iterable = [1, 2, 3]
                for item_name in my_iterable:
                    print(item_name)

'''
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    # check for even 
    if num % 2 == 0:
        print(f"Even Number: {num}")
    else:
        print(f"{num} is a Odd Number")
#---------------------------=========================---------------------------#
my_list = [(1,2), (3, 4), (5, 6), (7, 8)]
print(f"The total length of my_list is {len(my_list)}")
for (a,b) in my_list:
    # to get the even num from tuples as b
    print(b)



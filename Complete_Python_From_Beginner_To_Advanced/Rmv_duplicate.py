"""
*** Access SET items:
Create a fruits Set items of orange, apple, banana, apple. Firstly, remove duplicates and show original fruits list. 
Then, access set items(show fruits name one by one) from the original list.
"""

fruits = {'orange', 'apple', 'banana', 'apple'}
#Show original fruits list here
print('Original Fruits: ', fruits) 

#Now show them one by one
for fruit in fruits:
    print(f'Fruit: {fruit}')

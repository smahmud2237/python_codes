'''
List comprehensions are a unique way of quickly creating a list with Python. If you find yourself using a for loop
along with .append() to create a list, List Comprehensions are a good alternative!
To do this, let's go to the playground!
'''
mystring = 'Hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
print(mylist) 
# or we can just do it in one line code below
mylist1 = [letter for letter in mystring]
print(mylist1)
# another example
mylist2 = [x for x in 'Goodbye']
print(mylist2)
# another exp with numbers
mylist3 = [num for num in range(0, 11) if num%2 == 0]
print(mylist3)
# if we wants to get the square version 
mylist4 =[num**2 for num in range(2, 26)]
print(mylist4)
#---------------------------=========================---------------------------#
celcius = [0, 10, 20, 30, 44.5]
'''
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5) * temp + 32))
'''
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)
#---------------------------=========================---------------------------#
newlist = []
for x in [2, 4, 6]:
    for y in [10, 20, 30]:
        newlist.append(x*y)
# we can do it in just one line below
# newlist = [x*y for x in [2, 4, 6] for y in [10, 20, 30]]
print(newlist)
#---------------------------=========================---------------------------#




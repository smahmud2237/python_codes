'''
Strings: Ordered sequence of characters
'''
new_str = "Hello world"
# showing string len
print(len(new_str))
# print on a new line using \n
print("I am here \n to tell you \n  about string length")
# indexing with string
my_string = "Hey Buddy"
print(my_string[0]) #print(my_string[-9])
print(my_string[1]) #print(my_string[-8])
print(my_string[2]) #print(my_string[-7])
print(my_string[3]) #print(my_string[-6])
print(my_string[4]) #print(my_string[-5])
print(my_string[5]) #print(my_string[-4])
print(my_string[6]) #print(my_string[-3])
print(my_string[7]) #print(my_string[-2])
print(my_string[8]) #print(my_string[-1])
# slicing with string
my_new_str = 'safdsgfdgsg'
print(my_new_str[::3])
print(my_new_str[::-1])  #reverse the string
# After reversing show this in uppercase
print(my_new_str.upper())
# concatenation in string
print(my_string + '!' + " How are you?")
print('2' + '3') 
# formatting with .format() method
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {f} {b} {q}'.format(f = 'fox', q = 'quick', b = 'brown'))












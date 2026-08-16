'''
1. Creating clean repeatable code is a key part of becoming an effective programmer.
2. Functions allow us to create blocks of code that can be easily executed many times, without needing to constantly rewrite the entire 
block of code.
3. Functions will be a huge leap forward in your capabilities as a python programmer.
4, This means that the problems you are able to solve can also be a lot harder!
5. It's very important to get practice combining everything you've learned so far(control flow, loops, etc) with functions to become an 
effective programmer.
6. This may be a point in your progress where you may get discouraged or frustrated, don't worry, this is completely normal and very common!
7. We will go step by step, be patient with yourself and practice, practice and practice!!!
#---------------------------=========================---------------------------#
Syntax:
    def name_of_function():
        # Docstring explains function. It helps reader to understand the code quickly.
        print("Hello")
Output:
    >> name_of_function()
    >> Hello
#---------------------------=========================---------------------------#
Another Syntax:
    def name_of_function(name):
        # Docstring explains function.
        print("Hello " + name)
Output:
    >> name_of_function('Jose')
    >> Hello Jose
#---------------------------=========================---------------------------#
Typically we will use the return keyword to send back the result of the function,instead of just printing it out.
return allows us to assign the output of the function to a new variable.
Syntax:
    def add_function(num1, num2):
        return num1+num2
Output:
    >> result = add_function(1, 2)
    >> print(result)
    >> 3

'''
def say_hello(name ='Name'):
    return 'Hello ' + name

result = say_hello('Mahmud')
print(result)
#---------------------------=============>O<============---------------------------#
def add(n1, n2):
    return n1 + n2
result1 = add(2, 3)
print(result1) 
#---------------------------=============>O<============---------------------------#
def even_check(number):
    return number % 2 == 0
num1 = even_check(20)
num2 = even_check(21)
print(num1)
print(num2)
#---------------------------=============>O<============---------------------------#
# Find out if the word 'dog' is in a string
def dog_check(myString):
    return 'dog' in myString.lower()
myStr = dog_check('Dog run away')
print(myStr)
#---------------------------=============>O<============---------------------------#
'''
PIG LATIN: If word starts with a vowel, add 'ay' to end. If word doesn't start with a vowel, put first letter at the end, then add 'ay'.
Exp: word --> ordway; apple --> appleay
'''
def pig_latin(word):
    first_letter = word[0] 
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

r1 = pig_latin('word')
r2 = pig_latin('apple')
print(r1)
print(r2)
#---------------------------=============>O<============---------------------------#
# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
mylist = check_even_list([3, 5, 7, 9, 10])
print(mylist)


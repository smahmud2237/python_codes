'''
Given, st = 'Sam Print only the words that start with s in this sentence'.
Use for, .split() and if to create a statement that will print out words that start with 's'.
'''
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':  # if word[0] == 's' or word[0] == 'S':
        print(word)
'''
Use range() to print all the even numbers from 0 to 10.
'''
mynum = list(range(0, 11, 2)) # for mynum in range(0, 11, 2):
print(mynum)
'''
Use a list comprehension to create a list of all numbers between 1 to 50 that are divisible by 3.
'''
myList = [x for x in range(1, 51) if x%3 == 0]
print(myList)
'''
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''
for num in range(1, 101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)

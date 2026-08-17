'''
Learning functions increases your Python skills exponentially. This also means that the difficulties of problems
you can solve also increases drastically. Let's get some practice with converting problem statements into Python 
code. We'll go through a series of Function Practice Exercises. After this lecture we will go through the solutions.
'''
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both 
# numbers are even, But returns the greater if one or both numbers are odd.
def lesser_of_two_evens(a, b):
    if a%2==0 and b%2==0:
        # both are even 
        # return min(a, b) 
        if a < b:
            result = a
        else: 
            result = b
    else:
        # one or both are odd
        # return max(a, b) 
        if a > b:
            result = a
        else:
            result = b
    return result
r1 = lesser_of_two_evens(2, 4)
r2 = lesser_of_two_evens(2, 5)
print(r1)
print(r2)
#---------------------------=============>O<============---------------------------#
'''
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter.
'''
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')
#---------------------------=============>O<============---------------------------#
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name.
def old_macdonald(name):
    first_letter = name[0].upper()
    inbetween = name[1:3]
    fourth_letter = name[3].upper()
    rest = name[4:]
    return first_letter + inbetween + fourth_letter + rest
'''
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()
'''
mac = old_macdonald('macdonald')
print(mac)
#---------------------------=============>O<============---------------------------#
# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') -->> 'home am I' ; master_yoda('We are ready') -->> 'ready are We'
def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return ' '.join(reverse_word_list)
rev1 = master_yoda('I am home')
rev2 = master_yoda('We are ready')
print(rev1)
print(rev2)
#---------------------------=============>O<============---------------------------#
'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90)  -->> True; almost_there(104) -->> True; almost_there(150) -->> False; almost_there(209) -->> True
'''
def almost_there(number):
    return (abs(100 - number) <= 10) or (abs(200 - number) <= 10)
at1 = almost_there(90)
at2 = almost_there(104)
at3 = almost_there(150)
at4 = almost_there(209)
print(at1)
print(at2)
print(at3)
print(at4)
#---------------------------=============>O<============---------------------------#
'''
MAKES TWENTY: Given two integers, return True if the sum of the integers if 20 or if one of the integers is 20.
if not return False
makes_twenty(20,10) -->> True; makes_twenty(2,3) -->> False; makes_twenty(12,8) -->> True
'''
def makes_twenty(n1, n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20
''' if n1 + n2 == 20:
        return True
    elif (n1 == 20) or (n2 == 20):
        return True
    else:
        return False'''
m1 = makes_twenty(20,10)
m2 = makes_twenty(2,3)
m3 = makes_twenty(12,8)
print(m1)
print(m2)
print(m3)
#---------------------------=============>O<============---------------------------#






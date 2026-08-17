'''
Find 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) ->> True; has_33([1, 3, 1, 3]) ->> False; has_33([3, 1, 3]) ->> False;
'''
def has_33(nums):
    for i in range(0, len(nums) - 1):
        # if nums[i:i+1] == [3,3]:
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
num1 = has_33([1, 3, 3])
num2 = has_33([1, 3, 1, 3])
num3 = has_33([3, 1, 3])
print(num1)
print(num2)
print(num3)
#---------------------------=============>O<============---------------------------#
'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters.
paper_doll('Hello') -->> 'HHHeeellllllooo'
paper_doll('Mississippi') -->> 'MMMiiissssssiiippppppiii'
'''
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
t1 = paper_doll('Hello')
t2 = paper_doll('Mississippi')
print(t1)
print(t2)
#---------------------------=============>O<============---------------------------#
'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and
there's an eleven, reduce the total sum by 10. Finally, if the sum(even after adjustment) exceeds 21, return 'BUST'.
black_jack(5, 6, 7) -->> 18; black_jack(9, 9, 9) -->> 'BUST'; black_jack(9, 9, 11) -->> 19
'''
def black_jack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif sum([a, b, c]) > 21 and (a == 11 or b == 11 or c == 11):  # elif 11 in [a, b, c] and sum([a, b, c]) - 10 <= 21: # sum([a, b, c]) <= 31
        return sum([a, b, c]) - 10
    else: 
        return 'BUST'
j1 = black_jack(5, 6, 7)
j2 = black_jack(9, 9, 9)
j3 = black_jack(9, 9, 11)
print(j1)
print(j2)
print(j3)
#---------------------------=============>O<============---------------------------#
'''
SUMMER OF '69': Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the 
next 9(every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) -->> 9
summer_69([4, 5, 6, 7, 8, 9]) -->> 9
summer_69([2, 1, 6, 9, 11]) -->> 14
'''
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num!= 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
s1 = summer_69([1, 3, 5])
s2 = summer_69([4, 5, 6, 7, 8, 9])
s3 = summer_69([2, 1, 6, 9, 11])
print(s1)
print(s2)
print(s3)
#---------------------------=============>O<============---------------------------#
'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order.
spy_game([1, 2, 4, 0, 0, 7, 5]) -->> True
spy_game([1, 0, 2, 4, 0, 5, 7]) -->> True
spy_game([1, 7, 2, 0, 4, 5, 0]) -->> False
'''
def spy_game(nums):
    code = [0, 0, 7, 'x']
    # [0, 7, 'x']
    # [7, 'x']
    # ['x'] Length = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
sp1 = spy_game([1, 2, 4, 0, 0, 7, 5]) # True
sp2 = spy_game([1, 0, 2, 4, 0, 5, 7]) # True
sp3 = spy_game([1, 7, 2, 0, 4, 5, 0]) # False
print(sp1)
print(sp2)
print(sp3)
#---------------------------=============>O<============---------------------------#
'''
COUNT PRIMES: Writes a function that returns the number of prime numbers that exist up to and including a given 
number. By convention, we'll treat 0 and 1 as not prime.
# count_primes(100) -->> 25
'''
def count_primes(number):
    # First check 0 or 1 input
    if number < 2:
        return 0
    ################
    # For 2 or greater
    ################
    # Store our prime numbers
    primes = [2]
    # Counter going up to the input num
    x = 3
    # x is going through every number up to input num
    while x <= number:
        # Check if x is prime
        for y in primes: # for y in range(3, x, 2):
            if x%y == 0: 
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes) # to show the prime numbers
    return (f'In {number}, there are total {len(primes)} prime numbers')
p1 = count_primes(100)
p2 = count_primes(200)
print(p1)
print(p2)
#---------------------------=============>O<============---------------------------#





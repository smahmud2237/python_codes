for num in range(10):
    print(num)
#---------------------------=========================---------------------------#
print('Range 3 to 9 output: ')
for n in range(3, 10):
    print(n)
#---------------------------=========================---------------------------#
print('Print 0 to 10 even numbers: ')
for number in range(0, 11, 2):
    print(number)
#---------------------------=========================---------------------------#
print("if wants to use range in list: ")
evenlist = list(range(0, 11, 2))
print(evenlist)
oddlist = list(range(1, 10, 2))
print(oddlist)
#---------------------------=========================---------------------------#
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1
#---------------------------=========================---------------------------#
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1, mylist2):
    print(item)


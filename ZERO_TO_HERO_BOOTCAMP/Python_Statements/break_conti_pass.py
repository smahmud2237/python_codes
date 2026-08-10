'''
break => breaks out of the current closest enclosing loop.
continue => Goes to the top of the closest enclosing loop.
pass => Does nothing at all.
'''
x = [1, 2, 3]
for i in x:
    # don't want to show anything so I will use pass
    pass
print('End of my pass script')
#---------------------------=========================---------------------------#
print('This is an example of continue:')
myString = 'Sammy'
for letter in myString:
    if letter == 'a':
        continue
    print(letter)
#---------------------------=========================---------------------------#
print('This is an example of break:')
newString = 'Summy'
for let in newString:
    if let == 'm':
        break
    print(let)


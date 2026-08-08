'''
1. Let's begin to learn about control flow
2. We often only want certain code to execute when a particular condition has been met.
3. For example, if my dog is hungry (some condition), then I will feed the dog(some action).
4. For control this flow of logic we use some keywords: if, elif, else
5. Syntax of an if statement: 
                if some_condition:
                    #execute_some_code
                elif anothor_condition:
                    #do_something_different
                elif anothor_condition:
                    #do_something_diff_like_this
                else:
                    #do_these
'''
hungry = True
if hungry:
    print("IT'S TRUE! HE'S VERY HUNGRY. GIVE HIM FOOD RIGHT NOW.")
else:
    print("HE'S NOT HUNGRY!")
#---------------------------=========================---------------------------#
loc = 'Game'
if loc == 'Auto shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money are cool!")
elif loc == 'Game':
    print("Games are cool!")
else:
    print("I don't know much")
#---------------------------=========================---------------------------#
name = 'Jose'
if name == 'Frankie':
    print("Hello Frankie!")
elif name == 'Sammy':
    print("Hello Sammy!")
else:
    print("What is your name?")


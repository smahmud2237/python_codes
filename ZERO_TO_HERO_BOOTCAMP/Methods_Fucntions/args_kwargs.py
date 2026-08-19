def myfunc(a, b, c=0, d=0, e=0):
    # Returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05
res = myfunc(40, 60, 100, 200)
print(res)
#---------------------------=============>O<============---------------------------#
# same work we can do by using args below
def myfunc1(*args):
    return sum(args) * 2
res1 = myfunc1(10, 20, 30)
print(res1)
# args give tuple output(keep it in mind)
#---------------------------=============>O<============---------------------------#
# kwargs or keywordargs always give dictionary output
def myfunc2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didnot find any fruit here')
myfunc2(fruit='apple', veggie='lettuce')
#---------------------------=============>O<============---------------------------#
# we can use both args and kwargs in a func
def myfunc_both(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))
    print(f'I wold like {args[1]} {kwargs['fruit']}')
myfunc_both(10, 20, 30, fruit='orange', food='eggs', animal='dog')




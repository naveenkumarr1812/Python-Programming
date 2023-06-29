# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args):          # (*) is important instead of args,we can also change the name like (stuff) in place of args
    sum = 0
    # args = list(args)  # How to assign values in args
    # args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
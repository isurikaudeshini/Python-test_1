def unlimited_arguments(*args):   #star syntax is used to convert function arguments to a tuple of arguments #Unpacking
    print(args)
    for argument in args:
        print(argument)

unlimited_arguments(1,2,3,4) # a tuple
unlimited_arguments([1,2,3,4])
unlimited_arguments(*[1,2,3,4])
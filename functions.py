def unlimited_arguments(*args, **keyword_args):   #star syntax is used to convert function arguments to a tuple of arguments #Unpacking
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)

unlimited_arguments(1,2,3,4, name = 'Isurika', age =29) # a tuple
#unlimited_arguments([1,2,3,4])
#unlimited_arguments(*[1,2,3,4])
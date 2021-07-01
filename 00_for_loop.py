# for (int a = 0; a < 10 ; a ++)


# for loop can be applied on iterable object 
# (string, list, tuple, set, frozenset, dictionary, iterator, generator) only

language = "python programming"
l = len(language)

for index, number in enumerate(language): 
    print( ' \r{0}'.format(language[0:index]), end = '')


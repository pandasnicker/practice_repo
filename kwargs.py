# Display the use of **kwargs


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("kwarg items {0} = {1}".format(key, value))

greet_me(name="yasoob")
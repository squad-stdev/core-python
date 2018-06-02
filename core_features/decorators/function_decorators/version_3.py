#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Multiple Decorators V3.


import functools


def asterisked(func):
    @functools.wraps(func)
    def wrapper(text):
        print("******************************************")
        func(text)
        print("******************************************")

    return wrapper


def doted(func):
    @functools.wraps(func)
    def wrapper(text):
        print("..........................................")
        func(text)
        print("..........................................")

    return wrapper


@doted
@asterisked
def text_printer(text):
    print(text)

# Same as this:
# text_printer = doted(asterisked(text_printer))

if __name__ == '__main__':
    text_printer("Hello Cruel World!")
    # Name, docstring, metadata of the function is 'cached'.

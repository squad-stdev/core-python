#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Class Methods Decorator V3.


def asterisked(func):
    def wrapper(self, text):
        print("********************************")
        func(self, text)
        print("********************************")

    return wrapper


def doted(func):
    def wrapper(*args, **kwargs):
        print("................................")
        func(*args, **kwargs)
        print("................................")

    return wrapper


@doted
def destruct(x):
    print("We are destructing: {}".format(x))


class Test(object):

    @asterisked
    def action(self, x):
        print("We are testing: {}".format(x))

    @doted
    def hack(self, x):
        print("We are hacking: {}".format(x))


# Same as this:
# Test.action = asterisked(Test.action)

if __name__ == '__main__':
    t = Test()
    t.action("Hadron Collider")
    t.hack("Hadron Collider")
    destruct("Hadron Collider")

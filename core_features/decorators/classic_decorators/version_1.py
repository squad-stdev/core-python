#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Classic Decorator V1.


class Asterisk(object):
    def __call__(self, *args, **kwargs):
        print("AT CALL: ", args, kwargs)
        print("****************************")
        self.func(*args, **kwargs)
        print("****************************")
 
    def __init__(self, func, *args, **kwargs):
        print("AT INIT: ", func, args, kwargs)
        self.func = func


@Asterisk
def test(x):
    print("Testing: {}".format(x))


if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~~~ Before TEST ~~~~~~~~~~~~~~~~~~~~~")
    print()
    test("Mira")

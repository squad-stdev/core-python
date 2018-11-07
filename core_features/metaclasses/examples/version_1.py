#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Classic Decorator V1.


class SimpleMetaclass(type):
    def __call__(cls, *args, **kwargs):
        print("! AT CALL !")
        print(cls)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")

    def __init__(cls, *args, **kwargs):
        print("! AT INIT !")
        print(cls)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")

    def __new__(mcs, *args, **kwargs):
        print("! AT NEW !")
        print(mcs)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")

        return type.__new__(mcs, *args, **kwargs)


class MetaclassUser(metaclass=SimpleMetaclass):
    pass


if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~~~ Before TEST ~~~~~~~~~~~~~~~~~~~~~")
    m = MetaclassUser()

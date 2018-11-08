#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Classic Decorator V1.


class SimpleClass(object):
    def __call__(self, *args, **kwargs):
        print("! AT CALL !")
        print(self)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")

    def __init__(self, *args, **kwargs):
        print("! AT INIT !")
        print(self)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")

    def __new__(cls, *args, **kwargs):
        print("! AT NEW !")
        print(cls)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")

        return cls.__new__(cls, *args, **kwargs)


class SimpleMetaclass(type):
    def __call__(cls, *args, **kwargs):
        print("! AT CALL !")
        print(cls)
        print(args)
        print(kwargs)
        print("****************************\n\n\n")
        type.__call__()

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

        return super(SimpleMetaclass, mcs).__new__(mcs, *args, **kwargs)


class MetaclassUser(object, metaclass=SimpleMetaclass):
    pass


if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~~~ Before TEST ~~~~~~~~~~~~~~~~~~~~~")
    m = MetaclassUser()

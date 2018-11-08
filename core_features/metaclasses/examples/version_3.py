#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Classic Decorator V1.


class MultitonReceiver(type):
    """
    Implements "Multiton" pattern.
    """
    _instances = {}

    def __call__(cls, host, port=None, *args, **kwargs):
        signature = (cls, host, port, )
        if signature not in cls._instances:
            cls._instances[signature] = super().__call__(host, port, *args, **kwargs)

        return cls._instances[signature]


class BaseReceiver(object):
    """
    Base receiver class.
    """

    name = 'RTM Receiver'

    def __init__(self, host, port=502, timeout=0.5):
        self.host = host
        self.port = port
        self.timeout = timeout


class MultitonBaseReceiver(BaseReceiver, metaclass=MultitonReceiver):
    """
    Base receiver with "Multiton" pattern.
    """
    pass

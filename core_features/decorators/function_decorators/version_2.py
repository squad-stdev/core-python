#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Commutative Binary Operations Decorator V2.


import functools


def cache(action):
    cached_calculations = dict()

    def improved_cache(func):
        # @functools.wraps(func)
        def cached(x, y):
            code = "{}${}".format(max(x, y), min(x, y))

            if code not in cached_calculations:
                print("{} performed between: {} and {}.".format(action, x, y))
                cached_calculations[code] = func(x, y)

            return cached_calculations[code]

        return cached

    return improved_cache


@cache("Addition")
def sigma(x, y):
    return x + y

# It is the same as this:
# sigma = cache("Addition")(sigma)


@cache("Multiplication")
def pi(x, y):
    return x * y


if __name__ == '__main__':
    print("Sum is: ", sigma(5, 10))
    print("Sum is: ", sigma(10, 5))
    print()
    print("Pi is: ", pi(5, 10))
    print("Pi is: ", pi(10, 5))
    print()
    print("Name of SUM function is: ", sigma.__name__)
    print("Name of PI function is: ", pi.__name__)
    # Name, docstring, metadata of the function is 'cached' if functools.wraps is not used.

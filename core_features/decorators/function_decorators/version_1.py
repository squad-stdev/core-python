#!/usr/bin/python3
# Author: Hovhannes Dabaghyan
# Matter: Commutative Binary Operations Decorator V1.


def cache(func):
    cached_calculations = dict()

    def cached(x, y):
        code = "{}${}".format(max(x, y), min(x, y))

        if code not in cached_calculations:
            print("Addition performed between: {} and {}.".format(x, y))
            cached_calculations[code] = func(x, y)

        return cached_calculations[code]

    return cached


@cache
def sigma(x, y):
    return x + y

# It is the same as this:
# sigma = cache(sigma)


@cache
def pi(x, y):
    return x * y


if __name__ == '__main__':
    print("Sum is: ", sigma(5, 10))
    print("Sum is: ", sigma(10, 5))
    print()
    print("Pi is: ", pi(5, 10))
    print("Pi is: ", pi(10, 5))
    # For both message is "Addition performed between".

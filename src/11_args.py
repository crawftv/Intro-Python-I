# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

from functools import reduce

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(x, y):
    return x, y


print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum. Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*args):
    a = []
    for i in args:
        if type(i) in [int, float]:
            a.append(i)
        elif type(i) in [list, tuple]:
            a.extend(i)
    s = reduce(lambda x, y: x + y, a)
    return s


print(f2(1))  # Should print 1
print(f2(1, 3))  # Should print 4
print(f2(1, 4, -12))  # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# What thing do you have to add to make this work?
print(f2(a))  # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments. Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(x=0, y=0):
    return x + y


print(f3(1, 2))  # Should print 3
print(f3(8))  # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Google "python keyword arguments".

# YOUR CODE HERE
def f4(**kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    for i in range(len(kwargs)):
        print(f"key: {keys[i]}, value: {values[i]}")


# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {"monster": "goblin", "hp": 3}

# What thing do you have to add to make this work?
f4(**d)

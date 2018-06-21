#!/usr/bin/python
# Filename: lambda.py

def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)

print (twice('word'))
print (twice(5))
print ('word'*5)

def powersum(power, *args):
    """Return the sum of each argument raised to specified power."""
    total = 0
    for i in args:
        total += pow(i, power)
    return total
powersum(2, 3, 4)


powersum(2, 10)
#100
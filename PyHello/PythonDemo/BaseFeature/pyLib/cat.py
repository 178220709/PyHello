import sys
import os

class ShortInputException(Exception):
    """A user-defined exception class."""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    pa = os.path
    pn = os.name
    help(sys)
    t=input('Enter t --> ')
    print ('t is %s.'  % (t))

    s = input('Enter s --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
    # Other work can continue as usual here
except EOFError:
    print ('\nWhy did you do an EOF on me?')
except ShortInputException as x:
    print( 'ShortInputException: The input was of length %d, \
          was expecting at least %d' %  (x.length, x.atleast))
else:
    print ('No exception was raised.')
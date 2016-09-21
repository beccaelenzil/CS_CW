import math

"""
Arithmetic Processing
"""

def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)

def sq(x):
    """
    output: sq returns the square of its input
    input x: a number (int or float)
    """
    return x*x
print 'sq(5) is', sq(5)

def interp(low,high,fraction):
    """
    :param low: the lower input
    :param high: the higher input
    :param fraction: the fraction of the way between the high and the low
    :return: The difference between the high and the low multiplied by the fraction. This output is added to the low.
    """
    return (high-low)*(fraction)+low
print 'interp(1,3,.25) is', interp(1,3,.25)


"""
String functions
"""
def checkends(s):
    """
    :param string: any string of letters or numbers in quotations
    :return: True, if the beginning and end of the string are the same; False if otherwise.
    """
    if s[0]==s[-1]:
        return True
    else:
        return False
print 'checkends(colin) is', checkends('colin')
print 'checkends(calc) is', checkends('calc')

def flipside(s):
    """
    :param s: a string of numbers of letters
    :return: The first half of the string and the second half of the string switch positions.
     If the length of the string is odd, the first half of the input string will have one fewer
     variable than the second half of the input.
    """
    remainder = len(s)%2
    if remainder == 0:
        return s[len(s)/2:]+s[0:len(s)/2]
    else:
        return s[(len(s)/2):]+s[0:(len(s)/2)]

print 'flipside(maddting) is', flipside('maddting')
print 'flipside(madting) is', flipside('madting')

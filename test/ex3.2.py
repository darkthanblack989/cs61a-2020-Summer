from operator import add,mul,truediv

def invert(x):
    y = 1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled',e)
        return 0

def divide_all(n,ds):
    try:
        return reduce(truediv,ds,n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f,s,initial):
    """Combine elements of s using f starting with initial.
    >>> reduce(mul,[2,4,8],1)
    64
    >>> reduce(add,[1,2,3,4],0)
    10
    """
    for x in s:
        initial = f(initial,x)
    return initial
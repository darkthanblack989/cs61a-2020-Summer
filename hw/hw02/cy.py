from operator import add, mul, sub
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1
def accumulate(combiner, base, n, term):
    acc,i = base,1
    while i <= n:
        acc,i = combiner(acc,term(i)),i+1
    return acc
accumulate(lambda x, y: x + y + 1, 2, 3, square)
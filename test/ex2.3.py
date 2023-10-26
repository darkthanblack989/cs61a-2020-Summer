def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def path(m,n):
    if m == 1 or n == 1:
        return 1
    else:
        return path(m-1,n) + path(m,n-1)

def knap(n,k):
    if n == 0:
        return k== 0
    last = knap(n//10,k-n%10)
    digit_without_last = knap(n//10,k)
    return last or digit_without_last

def count_partitions(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m < 0:
        return 0
    else:
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
    return with_m + without_m

def all_nums(k):
    def h(k,prefix):
        if k == 0:
            print(prefix)
        return h(k-1,prefix*10) and h(k-1,prefix*10+1)
    return h(k,0)

def remove(n,digit):
    kept,digits = 0,0
    while n > 0:
        n,last = n//10,n%10
        if last != digit:
            kept = kept + last*10**digits
            digits = digits+1
    return kept

def lens(prev = lambda x:0):
    def put(k,v):
        def get(k2):
            if k2 == k:
                return v
            else:
                return prev(k2)
        return get,lens(get)
    return put

def storeroom(helium,fn_even,fn_odd):
    evens_defined,odds_defined = False,False
    evens,odds = None,None
    while helium > 0:
        digit,helium = helium%10,helium//10
        if digit % 2 == 0:
            if not evens_defined:
                evens = digit
                evens_defined = True
            else:
                evens = fn_even(evens,digit)
        else:
            if not odds_defined:
                odds = digit
                odds_defined = True
            else:
                odds = fn_odd(odds,digit)
    return evens > odds

def sculptural(ruler,k):
    if k == 0 or ruler == 0:
        return 0
    a = (ruler%10)+sculptural(ruler//10,k-1)*10 #ues last digit
    b = sculptural(ruler//10,k)                 #don't use last digit
    return max(a,b)
    
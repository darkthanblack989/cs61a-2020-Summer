def split(n):
    return n//10,n%10
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last,last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10 :
        return n
    else:
        all_but_last,last = split(n)
        return luhn_sum_double(all_but_last)+last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum +last
    return digit_sum

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow,print,n//10)
shrink =lambda n : f_then_g(print,shrink,n//10)

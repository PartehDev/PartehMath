import random
def rand(min,max):
    return random.randrange(min,max)
def add(addend1,addend2):
    return addend1 + addend2
def sub(x,y):
    return x - y
def mul(factor1,factor2):
    return factor1 * factor2
def div(x,y):
    return x / y
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
def dot(vec1,vec2):
    return sum(x*y for x, y in zip(vec1,vec2))
def square_root(num):
    if num < 0:
        return None
    else:
        return num**0.5
def Power(k, n):
    return k**n
def DoubleNum(n):
    return n + n
def modulo(spam, eggs): 
    print(str(spam % eggs))
def percent(spam, eggs): 
    return str((spam * eggs) / 100.0)

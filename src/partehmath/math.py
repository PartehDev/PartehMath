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
    value = 0
    value = sum( [vec1[i][0]*vec2[i] for i in range(len(vec2))])
    return value
def square_root(num):
    if num < 0:
        return None
    else:
        return num**0.5

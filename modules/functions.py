import math

def a(x):
    sum = 0
    for i in range(0, len(x)) :
        sum = sum + x[i]
    avg = sum/len(x)
    if (avg - math.floor(avg) < 0.5) :
        return math.floor(avg)
    else :
        return math.ceil(avg)
    
def f(x, y) :
    return math.ceil((y - 1) * (x/y))

def h(x, y) :
    return math.floor(x/y)

def g(x, y) :
    return f(x, y) - (y - 1) * h(x, y)

def sse (x) :
    sum = 0
    for i in range(0, len(x)) :
        sum = sum + pow(x[i] - a(x), 2)
    return sum

def mse(x, k) :
    return pow((pow(2, k) - 1), 2) * sse(x)/len(x)

def Cm(x, k, avg, yn) :
    x_belongs_to_cm = True
    for i in range(0, len(x) - 1) :
        if not ((0 <= (x[i] - f(avg, pow(2, k))) <= pow(2, 8 - k) - 1)) :
            x_belongs_to_cm = False
            break
    if not (0 <= yn <= 255) :
        x_belongs_to_cm = False
    return x_belongs_to_cm

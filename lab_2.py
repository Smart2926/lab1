## Завдання 1
import math
a = 6
b = 9
h = 0.2
x = a
while x <= b:
    if x<7:
        print(math.log10(x*math.log(x)+math.sin(x)))
    elif x>=7 and x<8:
        print(math.log((math.sin(x)+4),3))
    else:
        print(1/(16+1/math.cos(x)))
    x += h


## Завдання 2
a = 0
b = 0.5
h = 0.05
d = 0.001
m = 9
x = a 
while x<=b:
    n = 1
    sum_value = 1
    term = (-1)**n*math.prod([m+i for i in range(n)]) * (x**n)/math.factorial(n)
    while abs(term) > d:
        sum_value += term
        n += 1
        term = ((-1)**n*math.prod([m+i for i in range(n)]) * (x**n)/math.factorial(n))
    print("x = ", x, "f(x) =", sum_value)
    x += h
import math
a = 6
b = 9
h = 0.2
x=a
while x<=b:
    if x<7:
        print(math.log10(x*math.log(x)+math.sin(x)))
    elif x>=7 and x<8:
        print(math.log((math.sin(x)+4),3))
    else:
        print(1/(16+1/math.cos(x)))
    x+=h


    
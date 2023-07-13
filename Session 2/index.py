import math

def D(a, b, c):
     d = a ** 2 - (4 * a * c)
     x1 = (-b + math.sqrt(d) / (2 * a))
     x2 = (-b - math.sqrt(d) / (2 * a))
     print(x1)
     print(x2)

D(1,2,3)

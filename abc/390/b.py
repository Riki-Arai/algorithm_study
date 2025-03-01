import math

X = int(input())

for n in range(10000000000000000):
    if math.factorial(n) == X:
        print(n)
        break

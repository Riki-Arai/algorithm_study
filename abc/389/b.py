import math

X = int(input())

for i in range(100000000000000000):
    if math.factorial(i) == X:
        print(i)
        break

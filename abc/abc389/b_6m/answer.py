import math

X = int(input())

for i in range(2, X+1):
    if math.factorial(i) == X:
        print(i)
        exit()
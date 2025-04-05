X, Y = map(int, input().split())

if X >= Y:
    print(0)
else:
    num = 0
    while X < Y:
        X += 10
        num += 1
    print(num)
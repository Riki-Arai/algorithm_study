X = int(input())

if X == 0:
    print(X)
elif X % 10 == 0:
    print(int(str(X)[:-1]))
elif -10 < X < 10:
    print(int(X // 10) + 1)
else:
    if X >= 0:
        print(int(str(X)[:-1])+1)
    else:
        print(int(str(X)[:-1]))
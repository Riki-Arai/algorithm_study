R, C = map(int, input().split())
max_dis = max(abs(R - 8), abs(C - 8))
if max_dis % 2 == 0:
    print("white")
else:
    print("black")
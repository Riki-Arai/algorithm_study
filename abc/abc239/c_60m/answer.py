x1, y1, x2, y2 = map(int, input().split())

move_lists = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
for i in range(8):
    xx1 = x1 + move_lists[i][0]
    yy1 = y1 + move_lists[i][1]
    if pow(xx1-x2, 2) + pow(yy1-y2, 2) == 5:
        print("Yes")
        exit()

for i in range(8):
    xx2 = x2 + move_lists[i][0]
    yy2 = y2 + move_lists[i][1]
    if pow(x1-xx2, 2) + pow(y1-yy2, 2) == 5:
        print("Yes")
        exit()

print("No")
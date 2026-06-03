N, X, Y = map(int, input().split())
A_list = list(map(int, input().split()))

x_set, y_set = set(), set()
x_set.add(0)
x_set.add(A_list[0])
y_set.add(0)
for i, a in enumerate(A_list[1:], 1):
    if i%2 == 0:
        tmp_x_set = set()
        for x in x_set:
            tmp_x_set.add(x+a)
            tmp_x_set.add(x-a)
        x_set = tmp_x_set
    else:
        tmp_y_set = set()
        for y in y_set:
            tmp_y_set.add(y+a)
            tmp_y_set.add(y-a)
        y_set = tmp_y_set

if X in x_set and Y in y_set:
    print("Yes")
else:
    print("No")
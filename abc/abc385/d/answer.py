from sortedcontainers import SortedList, SortedDict
from collections import defaultdict

N, M, Sx, Sy = map(int, input().split())
x2y_dict = defaultdict(SortedList)
y2x_dict = defaultdict(SortedList)
for _ in range(N):
    X, Y = map(int, input().split())
    x2y_dict[X].add(Y)
    y2x_dict[Y].add(X)

res = 0
move_dict = {"L":(-1, 0), "U":(0, 1), "R":(1, 0), "D":(0, -1)}
cur_x, cur_y = Sx, Sy
for _ in range(M):
    X, Y = input().split()
    mx, my = move_dict[X]
    n_x, n_y = cur_x+mx*int(Y), cur_y+my*int(Y)
    if X in ("U", "D"):
        if cur_x in x2y_dict and len(x2y_dict[cur_x]):
            y_list = x2y_dict[cur_x]
            if cur_y >= n_y:
                cur_i = y_list.bisect_right(cur_y)
                n_i = y_list.bisect_left(n_y)
            else:
                cur_i = y_list.bisect_left(cur_y)
                n_i = y_list.bisect_right(n_y)
            delete_list = []
            n = len(y_list)
            for i in range(min(cur_i, n_i), min(max(cur_i, n_i), n)):
                delete_list.append(y_list[i])
            for d in delete_list:
                y_list.discard(d)
                y2x_dict[d].discard(cur_x)
            res += abs(cur_i-n_i)
            x2y_dict[cur_x] = y_list

        cur_x, cur_y = n_x, n_y
    else:
        if cur_y in y2x_dict and len(y2x_dict[cur_y]):
            x_list = y2x_dict[cur_y]
            if cur_x >= n_x:
                cur_i = x_list.bisect_right(cur_x)
                n_i = x_list.bisect_left(n_x)
            else:
                cur_i = x_list.bisect_left(cur_x)
                n_i = x_list.bisect_right(n_x)
            delete_list = []
            n = len(x_list)
            for i in range(min(cur_i, n_i), min(max(cur_i, n_i), n)):
                delete_list.append(x_list[i])
            for d in delete_list:
                x_list.discard(d)
                x2y_dict[d].discard(cur_y)
            res += abs(cur_i-n_i)
            y2x_dict[cur_y] = x_list

        cur_x, cur_y = n_x, n_y

print(cur_x, cur_y, res)
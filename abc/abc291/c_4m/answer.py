N = int(input())
S = input().strip()

# 上、右、下、左
move_dict = {"L":(-1, 0), "U":(0, 1), "R":(1, 0), "D":(0, -1)}
cur_pos = (0, 0)
res_set = set([(0, 0)])
for s in S:
    mw, mh = move_dict[s]
    w, h = cur_pos[0], cur_pos[1]
    new_pos = (w+mw, h+mh)
    if new_pos in res_set:
        print("Yes")
        exit()
    res_set.add(new_pos)
    cur_pos = new_pos

print("No")
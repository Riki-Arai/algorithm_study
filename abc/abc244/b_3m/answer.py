N = int(input())
S = input().strip()

res = [0, 0]
idx = 0
move_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for s in S:
    if s == "R":
        idx = (idx + 1) % 4
    else:
        res[0] = res[0] + move_list[idx][0]
        res[1] = res[1] + move_list[idx][1]

print(res[0], res[1])
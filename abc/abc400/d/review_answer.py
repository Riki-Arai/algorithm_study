# 0-1BFSという手法で解く
from collections import deque

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1
B -= 1
C -= 1
D -= 1
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
dis_lists = [[float("INF")]*W for _ in range(H)]
dq = deque([(0, A, B)])
dis_lists[A][B] = 0
while len(dq):
    dis, i, j  = dq.popleft()
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "." and dis < dis_lists[ii][jj]:
            dis_lists[ii][jj] = dis
            dq.appendleft((dis, ii, jj))

    for w in range(1, 3):
        for mi, mj in move_lists:
            ii = i + mi*w
            jj = j + mj*w
            if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "#" and dis+1 < dis_lists[ii][jj]:
                dis_lists[ii][jj] = dis+1
                dq.append((dis+1, ii, jj))

print(dis_lists[C][D])
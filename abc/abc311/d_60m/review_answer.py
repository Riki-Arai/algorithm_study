from collections import deque

N, M =map(int,input().split())
s_lists = [list(input()) for _ in range(N)]

move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
dq = deque([(1, 1)])
res_lists = [[False]*M for _ in range(N)]
res_lists[1][1] = True
seen_sets = set([(1, 1)])
while len(dq):
    i, j = dq.popleft()
    for mi, mj in move_lists:
        ii, jj = i, j
        while True:
            if not(0 <= ii+mi < N) or not(0 <= jj+mj < M):
                break
            if not(0 <= ii+mi < N and 0 <= jj+mj < M and s_lists[ii+mi][jj+mj] == "."):
                break
            ii += mi
            jj += mj
            res_lists[ii][jj] = True

        if (ii, jj) not in seen_sets:
            dq.append((ii, jj))
            seen_sets.add((ii, jj))

res = 0
for i in range(N):
    for j in range(M):
        if res_lists[i][j]:
            res += 1

print(res)
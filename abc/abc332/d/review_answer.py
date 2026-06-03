from itertools import permutations

H, W = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(H)]
B_lists = [list(map(int, input().split())) for _ in range(H)]

def f(p_list):
    count = 0
    n = len(p_list)
    for i in range(n):
        for j in range(i + 1, n):
            if p_list[i] > p_list[j]:
                count += 1
    return count

res = float("INF")
for p1 in permutations(list(range(H))):
    for p2 in permutations(list(range(W))):
        new_A_lists = [[None]*W for _ in range(H)]
        for i, pi in enumerate(p1):
            for j, pj in enumerate(p2):
                new_A_lists[i][j] = A_lists[pi][pj]

        if new_A_lists == B_lists:
            res = min(f(p1)+f(p2), res)

if res == float("INF"):
    print(-1)
else:
    print(res)

from itertools import permutations


# 転倒数をカウント
# ソートした順序に並び替えるための入れ換え回数と転倒数は一致するという法則がある
def count(p):
    cnt = 0
    for i in range(len(p) - 1):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                cnt += 1
    return cnt


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = float("inf")
# 純烈全探索
for p_h in permutations(range(H)):
    for p_w in permutations(range(W)):
        new_B = [[A[r][c] for c in p_w] for r in p_h]
        # Bと一致するのであればp_hとp_wにするための入れ替え回数(転倒数)をカウント
        if new_B == B:
            ans = min(ans, count(p_h) + count(p_w))

print(ans if ans != float("inf") else -1)
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
A = [deque() for _ in range(M)]   # 各列（スタック）を表すキュー
mem = [[] for _ in range(N)]      # 先頭にある色 -> その色が先頭の列の番号リスト

for i in range(M):
    k = int(input())
    arr = list(map(int, input().split()))
    for a in arr:
        A[i].append(a - 1)        # 0-index化
    mem[A[i][0]].append(i)        # 先頭色の列番号を記録

que = deque()
for i in range(N):
    if len(mem[i]) == 2:
        que.append(i)

while que:
    now = que.popleft()
    # now 色が先頭にある2つの列を処理
    for p in mem[now]:
        A[p].popleft()            # 先頭のボールを取り除く
        if A[p]:
            top = A[p][0]
            mem[top].append(p)
            if len(mem[top]) == 2:
                que.append(top)
    mem[now].clear()              # 再利用防止（C++の挙動と同等）

for p in A:
    if p:
        print("No")
        exit()
print("Yes")
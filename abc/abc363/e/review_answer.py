'''
※C++に変換してAC
(1) ひとまず優先度付きキューに格納し、条件を満たした時にpopするという方法をやったことがあったのでそれをすぐに思いつけた
(2) 方針はすぐにできたが、pythonでTLEとなってしまってC++だとACするケースだった
(3) ロジックが合っているとしか思えない時は、setをなるべく使用しない実装に変更をしてC++で試すケースが大事であることを学べた
'''
import sys
import heapq

input = sys.stdin.buffer.readline

H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 訪問済みかどうか
seen = [[False] * W for _ in range(H)]

# 優先度付きキュー
# (マスの高さ, i, j)
pq = []

# 海に面しているマスを最初に登録
for i in range(H):
    for j in range(W):
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            if not seen[i][j]:
                seen[i][j] = True
                heapq.heappush(pq, (A[i][j], i, j))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 沈んだマスの数
sunk = 0

for y in range(1, Y + 1):

    while pq and pq[0][0] <= y:
        _, i, j = heapq.heappop(pq)

        # このマスが沈んだ
        sunk += 1

        for di, dj in moves:
            ni = i + di
            nj = j + dj

            if 0 <= ni < H and 0 <= nj < W and not seen[ni][nj]:
                seen[ni][nj] = True
                heapq.heappush(pq, (A[ni][nj], ni, nj))

    print(H * W - sunk)
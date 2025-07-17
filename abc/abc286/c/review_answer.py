N, A, B = map(int, input().split())
S = input()

res = float("INF")
# 一見するとO(N^3)にみえるが、三重ループの構造でないのでO(N^2)+O(N^2)=O(N^2)で済む
for i in range(N):
    cost = 0
    for j in range(N//2):
        if S[j] != S[N-j-1]: # S[-j]だとj=0の時に反対の位置を指定できないのでN-j-1の形に落ち着く
            cost += B
    res = min(res, cost+A*i)
    # この処理があると三重ループになるように思えるが、実際にはそうならない
    S = S[1:] + S[0]

print(res)
import sys; sys.setrecursionlimit(10**7)

N, V = map(int, input().split()) # 取得例：1 2
W_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (i+1)+(j+1)+(k+1) <= V:
                res = max(W_list[i]+W_list[j]+W_list[k], res)

print(res)
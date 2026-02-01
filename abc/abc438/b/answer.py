N, M = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"
T = input().strip() # 取得例："A"

res = float("INF")
for i in range(N-M+1):
    tmp_res = 0
    for j in range(M):
        t = T[j]
        while True:
            if S[i+j] == t:
                break
            t = str((int(t)+1)%10)
            tmp_res += 1
    res = min(tmp_res, res)

print(res)
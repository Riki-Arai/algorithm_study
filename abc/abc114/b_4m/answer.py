import sys; sys.setrecursionlimit(10**7)

S = input().strip() # 取得例："A"

res = float("INF")
base = 753
for i in range(len(S)-2):
    if res > abs(base-int(S[i:i+3])):
        res = abs(base-int(S[i:i+3]))

print(res)

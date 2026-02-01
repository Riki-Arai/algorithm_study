N, X = map(int, input().split()) # 取得例：1 2

res = float("INF")
min_b = float("INF")
tmp_res = 0
for i in range(1, N+1):
    A, B = map(int, input().split()) # 取得例：1 2
    if X < i:
        break
    tmp_res += (A+B)
    min_b = min(B, min_b)
    res = min(tmp_res+(X-i)*min_b, res)

print(res)

#N, X = map(int, input().split()) # 取得例：1 2
#
#res = float("INF")
#tmp_res = 0
#for i in range(1, N+1):
#    A, B = map(int, input().split()) # 取得例：1 2
#    if X < i:
#        break
#    tmp_res += (A+B)
#    res = min(tmp_res+(X-i)*B, res)
#
#print(res)
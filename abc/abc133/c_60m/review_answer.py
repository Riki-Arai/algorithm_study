# 2019 個以上の整数が連続すると2019の倍数が存在し、そうでなければLとR内の数は2019個未満だと気づくことがポイント
L, R = map(int, input().split()) # 取得例：1 2

if (R//2019) - ((L-1)//2019) > 0:
    print(0)
    exit()

res = float("INF")
for i in range(L, R+1):
    for j in range(i+1, R+1):
        res = min(i*j%2019, res)

print(res)
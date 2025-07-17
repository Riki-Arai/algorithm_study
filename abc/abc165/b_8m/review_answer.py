X = int(input()) # 取得例：1

res = 0
m = 100
while m < X:
    m = (m * 101) // 100
    res += 1

print(res)
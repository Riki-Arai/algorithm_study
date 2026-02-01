N = int(input()) # 取得例：1

res = 0
for a in range(1, 10**6+1):
    if N % a == 0:
        res += N//a - 1
    else:
        res += N//a

print(res)
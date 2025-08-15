N = int(input()) # 数値

res = 0
for a in range(1, 10**6+1):
    w_a = int(str(a) * 2)
    if w_a > N:
        break
    res += 1

print(res)
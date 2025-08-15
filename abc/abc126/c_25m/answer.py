N, K = map(int, input().split()) # 取得例：1 2

res = 0
for i in range(1, N+1):
    score = i

    if score >= K:
        res += 1/N
        continue

    for j in range(1, 21):
        score *= 2
        if score >= K:
            break
    res += (1/N) * ((1/2)**j)

print(res)
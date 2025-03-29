m = int(input())
ans = []

for _ in range(20):
    for i in range(10, -1, -1):
        while 3**i <= m:
            m -= 3**i
            ans.append(i)
print(len(ans))
print(*ans)
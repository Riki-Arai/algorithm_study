m = int(input())
ans = []

for i in range(20, -1, -1):
  while 3**i <= m:
    m -= 3**i
    ans.append(i)
print(len(ans))
print(*ans)

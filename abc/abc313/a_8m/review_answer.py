n = int(input())
p = list(map(int, input().split()))
m = 0
for i in range(1, n):
    m = max(m, p[i])
print(max(0, m + 1 - p[0]))
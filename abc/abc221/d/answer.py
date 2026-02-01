from collections import defaultdict

N = int(input().strip())

res_lists = [[0, 0]]
for _ in range(N):
    A, B = map(int, input().split())
    res_lists.append([A, 1])
    res_lists.append([A+B, -1])

n = 0
days = 0
res_lists.sort()
res_list = [0]*(N+1)
for i in range(len(res_lists)-1):
    x, y = res_lists[i]
    xx, yy = res_lists[i+1]
    days = xx-x
    n += y
    res_list[n] += days

print(*res_list[1:])
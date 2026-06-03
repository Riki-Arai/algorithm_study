from collections import defaultdict

N, K = map(int, input().split())
A_list = list(map(int, input().split()))

cum = 0
counter = defaultdict(int)
counter[0] = 1
res = 0
for a in A_list:
    cum += a
    res += counter[cum - K]
    counter[cum] += 1

print(res)
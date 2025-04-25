N = int(input())

res = 0
i = 2 ** res
while i <= N:
    res += 1
    i = 2 ** res

print(max(0, res-1))
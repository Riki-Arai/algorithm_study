N, M = map(int, input().split())
A_list = list(map(int, input().split()))

res = 0
for a in A_list:
    if M - a >= 0:
        res += 1
        M -= a
    else:
        break

print(res)
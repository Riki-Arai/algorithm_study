N = int(input())

res = ""
div_list = sorted(list(filter(lambda x: 1 <= x <= 9, [i for i in range(1, N+1) if N % i ==0])))
for i in range(N+1):
    for j in div_list:
        if i % (N / j) == 0:
            res += str(j)
            break
    else:
        res += "-"

print(res)
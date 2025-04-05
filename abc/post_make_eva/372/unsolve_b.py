M = int(input())
a_list = list(reversed([3**x for x in range(10)]))
n = 0
res_list = []
for i, a in enumerate(a_list):
    if n > 20:
        break

    j = 10 - i
    if M == 0:
        break
    elif a > M:
        continue
    elif a <= M:
        for _ in range(100000000):
            if a > M: 
                break
            if M == 0:
                break
            if n == 20:
                break
            M -= a
            res_list.append(j)
            n += 1

print(n)
print(*res_list)

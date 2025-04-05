N, C = list(map(int, input().split()))
t_list = list(map(int, input().split()))

res = 0
last_time = 0
count = 0
for t in t_list:
    if count == 0:
        res += 1
        last_time = t
        count = 1
    else:
        if t - last_time >= C:
            res += 1
            last_time = t

print(res)

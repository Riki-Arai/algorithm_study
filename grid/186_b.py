H, W = map(int, input().split())

all_a_list = []
for _ in range(H):
    a_list = map(int, input().split())
    all_a_list.extend(a_list)

min_v = min(all_a_list)
res = 0
for a in all_a_list:
   res += a - min_v

print(res)

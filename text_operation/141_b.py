s_list = list(input())

count = 0
for i, s in enumerate(s_list, 1):
    if i % 2 == 0 and s in ("L", "U", "D"):
        count += 1
    elif i % 2 == 1 and s in ("R", "U", "D"):
        count += 1

print('NYoe s'[len(s_list) == count::2])

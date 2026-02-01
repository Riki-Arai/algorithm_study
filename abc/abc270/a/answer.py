A, B = map(int, input().split())

res_dict = {0: [0], 1: [1], 2: [2], 4:[4], 3:[1,2], 5:[1,4], 6:[2,4], 7:[1,2,4]}
res = 0
for x in res_dict[A]+res_dict[B]:
    res |= x

print(res)
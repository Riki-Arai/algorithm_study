from collections import defaultdict

N, M = map(int, input().split()) # 取得例：1 2

res = 0
r2c_dict = defaultdict(int)
c2r_dict = defaultdict(int)
for _ in range(M):
    R, C = map(int, input().split()) # 取得例：1 2
    if R in r2c_dict and C in c2r_dict:
        c = r2c_dict.pop(R)
        c2r_dict.pop(c)
        if C in c2r_dict:
            r = c2r_dict.pop(C)
            r2c_dict.pop(r)
            res -= 1
        r2c_dict[R] = C
        c2r_dict[C] = R
    elif R in r2c_dict and C not in c2r_dict:
        c = r2c_dict.pop(R)
        c2r_dict.pop(c)
        r2c_dict[R] = C
        c2r_dict[C] = R
    elif R not in r2c_dict and C in c2r_dict:
        r = c2r_dict.pop(C)
        r2c_dict.pop(r)
        r2c_dict[R] = C
        c2r_dict[C] = R
    else:
        r2c_dict[R] = C
        c2r_dict[C] = R
        res += 1

print(res)
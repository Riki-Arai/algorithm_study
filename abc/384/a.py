N, c_1, c_2 = input().split()
S = input()

res = ""
for s in S:
    if s != c_1:
        res += c_2
    else:
        res += s

print(res)

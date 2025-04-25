S_list = [input() for _ in range(3)]
T = input().strip()

res = ""
for t in T:
    res += S_list[int(t)-1]

print(res)
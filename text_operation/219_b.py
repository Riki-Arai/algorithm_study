s_list = [input() for _ in range(3)]
t_list = list(input())

res = ""
for t in t_list:
    res += s_list[int(t)-1]

print(res)

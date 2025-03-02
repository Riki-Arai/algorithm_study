N, D = list(map(int, input().split()))
S = input()

s_list = []
for s in S:
    s_list.append(s)

s_list.reverse()
for _ in range(D):
    c_idx = s_list.index("@")
    s_list[c_idx] = "."

s_list.reverse()
print("".join(s_list))

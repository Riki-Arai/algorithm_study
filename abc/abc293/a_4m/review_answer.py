S_list = list(input().strip())

c_S_list = S_list.copy()
for i in range(len(S_list)//2):
    c_S_list[2*i+1] = S_list[2*i]
    c_S_list[2*i] = S_list[2*i+1]

print("".join(c_S_list))
S_list = list(input().strip())
T_list = list(input().strip())

if S_list == T_list:
    print("Yes")
    exit()

c_S_list = S_list.copy()
for i in range(len(S_list)-1):
    c_S_list[i] = S_list[i+1]
    c_S_list[i+1] = S_list[i]
    if c_S_list == T_list:
        print("Yes")
        exit()

    c_S_list = S_list.copy()

print("No")
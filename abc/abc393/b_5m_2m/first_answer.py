S = input().strip()

a_list, b_list, c_list = [], [], []
for i in range(len(S)):
    if S[i] == "A":
        a_list.append(i+1)
    elif S[i] == "B":
        b_list.append(i+1)
    elif S[i] == "C":
        c_list.append(i+1)

res = 0
for i in b_list:
    for j in a_list:
        for k in c_list:
            if i > j and k > j and 2 * i == j + k: 
                res += 1
print(res)
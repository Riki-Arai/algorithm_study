S, T = input().split()

for w in range(1, len(S)):
    for c in range(w):
        res_list = []
        for i in range(0, len(S), w):
            if i+w > len(S):
                break
            res_list.append(S[i:i+w][c])

    if "".join(res_list) == T:
        print("Yes")
        exit()

print("No")
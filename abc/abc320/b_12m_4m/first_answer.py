S = input().strip()

for i in range(len(S), -1, -1):
    for j in range(len(S)):
        if j + i <= len(S):
            sub_S = S[j:j+i]
            if sub_S == sub_S[::-1]:
                print(i)
                exit()
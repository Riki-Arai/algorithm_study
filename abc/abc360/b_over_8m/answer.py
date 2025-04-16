S, T = input().split()

for w in range(1, len(S)):
    for c in range(w):
        res = ""
        for i in range(c, len(S), w):
            res += S[i]

        if res == T:
            print("Yes")
            exit()

print("No")
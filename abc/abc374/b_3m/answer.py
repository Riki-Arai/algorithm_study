S = input().strip()
T = input().strip()

max_l = max(len(S), len(T))
for i in range(max_l):
    if i == len(S) or i == len(T):
        print(i+1)
        exit()
    if S[i] != T[i]:
        print(i+1)
        exit()

print(0)
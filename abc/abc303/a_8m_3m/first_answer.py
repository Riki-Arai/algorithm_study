N = int(input())
S = input()
T = input()

for i in range(N):
    s = S[i]
    t = T[i]
    if s != t and s + t not in ("1l", "l1") and s + t not in ("o0", "0o"):
        print("No")
        exit()
print("Yes")
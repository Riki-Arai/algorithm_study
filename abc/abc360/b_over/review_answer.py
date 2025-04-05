s, t = input().split()
for w in range(1, len(s)):
    for c in range(w):
        p = ""
        for i in range(c, len(s), w):
            p += s[i]
        if p == t:
            print("Yes")
            exit()
print("No")
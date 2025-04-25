s = input()

n = len(s)
v = []
for k in range(0, n):
    v.append(s[k:] + s[:k])

print(min(v))
print(max(v))
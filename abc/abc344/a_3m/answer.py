S = input().strip()

count = 0
res = ""
for s in S:
    if s == "|":
        count += 1
    elif count != 1:
        res += s
print(res)
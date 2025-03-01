N = int(input())
S = input()

x = "" 
count = 0
for s in S:
    x += s
    print(x)
    if x == "A":
        continue
    elif x == "AB":
        continue
    elif x == "ABC":
        count += 1
        x = ""
        continue
    else:
        x = ""

print(count)

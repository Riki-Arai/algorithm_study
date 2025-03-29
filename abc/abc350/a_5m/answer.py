S = input().strip()

if S[:3] == "ABC" and 1 <= int(S[3:]) <= 349 and int(S[3:]) != 316:
    print("Yes")
else:
    print("No")
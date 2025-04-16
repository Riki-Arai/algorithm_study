N = int(input())
S = input().strip()

if S.count("o") > 0 and S.count("x") == 0:
    print("Yes")
else:
    print("No")
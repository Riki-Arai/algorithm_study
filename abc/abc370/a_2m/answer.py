L, R = map(int, input().split())

if L == 1 and R == 0:
    print("Yes")
elif L == R:
    print("Invalid")
else:
    print("No")
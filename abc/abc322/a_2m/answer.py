N = int(input())
S = input().strip()

if "ABC" in S:
    print(S.index("ABC") + 1)
else:
    print(-1)
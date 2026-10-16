import sys; sys.setrecursionlimit(10**7)

S = input().strip() # 取得例："A"

if S.count("E") > S.count("W"):
    print("East")
else:
    print("West")
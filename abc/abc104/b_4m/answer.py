import sys; sys.setrecursionlimit(10**7)

S = input().strip() # 取得例："A"

if S[0] == "A" and S[2:-1].count("C") == 1:
    for s in S:
        if s not in ("A", "C") and s.isupper():
            print("WA")
            exit()
    else:
        print("AC")
else:
    print("WA")
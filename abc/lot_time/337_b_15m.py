S = input().strip()

res = "A" * S.count("A") + "B" * S.count("B") + "C" * S.count("C") 
if S == res:
    print("Yes")
else:
    print("No")
S = input().strip()

if "A" * S.count("A") + "B" * S.count("B") + "C" * S.count("C") == S:
    print("Yes")
else:
    print("No")
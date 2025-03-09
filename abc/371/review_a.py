S_ab, S_ac, S_bc = input().split()

# BAC or CAB
if (S_ab == "<" and S_ac == ">" and S_bc == ">") or (S_ab == ">" and S_ac == "<" and S_bc == "<"):
    print("A")
# CBA or ABC
elif (S_ab == "<" and S_ac == "<" and S_bc == "<") or (S_ab == ">" and S_ac == ">" and S_bc == ">"):
    print("B")
# ACB or BCA
else:
    print("C")

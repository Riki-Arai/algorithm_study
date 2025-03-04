S_1, S_2, S_3 = input().split()

a_older_b = None
a_older_c = None
b_older_c = None

if S_1 == "<":
    a_older_b = False
elif S_1 == ">":
    a_older_b = True

if S_2 == "<":
    a_older_c = False
elif S_2 == ">":
    a_older_c = True

if S_3 == "<":
    b_older_c = False
elif S_3 == ">":
    b_older_c = True

# BAC or CAB
if (not a_older_b and a_older_c and b_older_c) or (a_older_b and not a_older_c and not b_older_c):
    print("A")
# ABC or CBA
elif (a_older_b and a_older_c and b_older_c) or (not a_older_b and not a_older_c and not b_older_c):
    print("B")
# BCA or ACB
elif (not a_older_b and not a_older_c and b_older_c) or (a_older_b and a_older_c and not b_older_c):
    print("C")

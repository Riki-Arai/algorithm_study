A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)
if C % 2 == 0:
    if abs(A) == abs(B):
        print("=")
    elif abs(A) > abs(B):
        print(">")
    else:
        print("<")
else:
    if A < 0 and B >= 0:
        print("<")
    elif A >= 0 and B < 0:
        print(">")
    elif A < 0 and B < 0:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
            print("<")
        else:
            print(">")
    else:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
            print(">")
        else:
            print("<")
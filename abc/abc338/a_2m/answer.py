S = input().strip()

if len(S) == 1 and S[0].isupper():
    print("Yes")
elif len(S) != 1 and S[0].isupper() and S[1:].islower():
    print("Yes")
else:
    print("No")
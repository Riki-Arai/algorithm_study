S = input()

if len(S) == 8:
    tmp = S[0] + S[-1]
    if tmp.isalpha() and tmp.isupper():
        if S[1:-1].isdecimal() and 100000 <= int(S[1:-1]) <= 999999:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
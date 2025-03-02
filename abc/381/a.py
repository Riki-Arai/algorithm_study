N = input()
S = input()

def sakura():
    if len(S) % 2 == 1:
        one_str = "1" * ((len(S)+1)//2 -1)
        if S[:((len(S)+1)//2 -1)] == one_str:
            if "/" == S[((len(S)+1)//2 -1)]:
                two_str = "2" * (len(S) - ((len(S)+1)//2))
                if S[((len(S)+1)//2):] == two_str:
                    return "Yes"
    return "No"

print(sakura())

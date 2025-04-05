N = int(input())
S = input().strip()

f_idx = S.index("|")
s_idx = len(S) - S[::-1].index("|")
if "*" in S[f_idx:s_idx]:
    print("in")
else:
    print("out")
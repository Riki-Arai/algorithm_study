N = int(input())
S_list = [input() for _ in range(N)]

res = "Yes"
for S in S_list:
    if not ((S[0] in ("H", "D", "C", "S") and S[1] in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"))):
        print("No")
        exit()

if len(S_list) == len(set(S_list)):
    print("Yes")
else:
    print("No")
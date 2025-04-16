W, B = map(int, input().split())
S = "wbwbwwbwbwbw" * 100

for i in range(len(S) - (W+B)):
    sub_s = S[i:i+(W+B)]
    if sub_s.count("w") == W and sub_s.count("b") == B:
        print("Yes")
        exit()

print("No")
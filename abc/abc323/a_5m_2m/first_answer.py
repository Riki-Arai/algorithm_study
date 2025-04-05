S = input().strip()

for i in range(2, len(S)+1):
    if (i) % 2 == 0 and S[i-1] != "0":
        print("No")
        exit()

print("Yes")
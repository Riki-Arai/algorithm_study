S = input().strip()

for i in range(1, len(S)):
    if int(S[i-1]) <= int(S[i]):
        print("No")
        exit()
print("Yes")
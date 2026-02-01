S = input().strip() # 取得例："A"
T = input().strip() # 取得例："A"

for i in range(1, len(S)):
    if S[i].isupper():
        if S[i-1] not in T:
            print("No")
            exit()

print("Yes")
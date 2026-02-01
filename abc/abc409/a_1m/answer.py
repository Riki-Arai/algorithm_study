N = int(input()) # 数値：1
S = input().strip() # 取得例："A"
T = input().strip() # 取得例："A"

for i in range(N):
    if S[i] == "o" and T[i] == "o":
        print("Yes")
        exit()

print("No")
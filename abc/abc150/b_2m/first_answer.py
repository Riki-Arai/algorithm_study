N = int(input()) # 取得例：1
S = input().strip() # 取得例：A

res = 0
sub_s = "ABC"
for i in range(N):
    if S[i:i+3] == sub_s:
        res += 1

print(res)
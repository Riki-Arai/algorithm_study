S = input().strip() # 取得例：A

n = len(S)
sub_s = S[:(n-1)//2]
sub_s_2 = S[(n+3)//2-1:n]
if S == S[::-1] and sub_s == sub_s[::-1] and sub_s_2 == sub_s_2[::-1]:
    print("Yes")
else:
    print("No")
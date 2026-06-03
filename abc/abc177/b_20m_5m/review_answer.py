S, T = map(int, input().split())

ans = len(T)

# S のどの位置から T を重ねるかを全探索
for start in range(len(S) - len(T) + 1):
    diff = 0
    # T の文字と S[start + i] の文字を比較し、異なる個数を数える
    for i in range(len(T)):
        if T[i] != S[start + i]:
            diff += 1
    ans = min(ans, diff)

print(ans)


## first
#S = input().strip() # 取得例：A
#T = input().strip() # 取得例：A
#
#res = 0
#for i in range(len(S)):
#    s = S[i:i+len(T)]
#    if len(s) == len(T):
#        tmp_res = 0
#        for j in range(len(s)):
#            if s[j] == T[j]:
#                tmp_res += 1
#
#        res = max(res, tmp_res)
#
#print(len(T)-res)
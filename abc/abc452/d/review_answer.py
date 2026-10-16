import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

res = (1 + len(S)) * len(S) // 2
# dp_lists[j] = いままで見た範囲で T[:j+1] を部分列として作れるときの開始位置の最大値
dp_lists = [-1] * len(T)
for i in range(len(S)):
    for j in range(len(T) - 1, -1, -1):
        if S[i] != T[j]:
            continue
        if j == 0:
            dp_lists[j] = max(dp_lists[j], i)
        elif dp_lists[j - 1] != -1:
            dp_lists[j] = max(dp_lists[j], dp_lists[j - 1])

    if dp_lists[-1] != -1:
        res -= dp_lists[-1] + 1

print(res)






#import sys; sys.setrecursionlimit(10**7)
#
#S = input().strip() # 取得例："A"
#T = input().strip() # 取得例："A"
#
## 構成できない場合は -1 とするため、初期値を -1 に変更します
#dp_lists = [[-1]*(len(T)+1) for _ in range(len(S)+1)]
#
#for i in range(len(S)+1):
#    # Tの0文字目（空文字列）を作るための最大の開始インデックスは、現在の位置 i になります
#    dp_lists[i][0] = i
#
#for i in range(1, len(S)+1):
#    ii = i - 1
#    for j in range(1, len(T)+1):
#        jj = j - 1
#        if S[ii] == T[jj]:
#            # 文字が一致する場合、直前の文字を使う場合と使わない場合の開始インデックスの最大値をとります
#            dp_lists[i][j] = max(dp_lists[ii][jj], dp_lists[ii][j])
#        else:
#            # 一致しない場合、直前の結果（使わない場合）をそのまま引き継ぎます
#            dp_lists[i][j] = dp_lists[ii][j]
#
## 全部分文字列の総数から、「Tを含む部分文字列の総数」を引きます
#print((1+len(S))*len(S)//2 - sum(dp_lists[i][len(T)] + 1 for i in range(1, len(S)+1)))



## 失敗例
#import sys; sys.setrecursionlimit(10**7)
#
#S = input().strip() # 取得例："A"
#T = input().strip() # 取得例："A"
#
#dp_lists = [[0]*(len(T)+1) for _ in range(len(S)+1)]
#for i in range(len(S)+1):
#    dp_lists[i][0] = 1
#
#for i in range(1, len(S)+1):
#    ii = i - 1
#    for j in range(1, len(T)+1):
#        jj = j - 1
#        if S[ii] == T[jj]:
#            dp_lists[i][j] = dp_lists[ii][jj]+dp_lists[ii][j]
#        else:
#            dp_lists[i][j] = dp_lists[ii][j]
#
#print((1+len(S))*len(S)//2-dp_lists[len(S)][len(T)])
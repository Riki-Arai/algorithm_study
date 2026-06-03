N = int(input()) # 数値：1
S = input().strip() # 取得例："A"

ai_list = []
bi_list = []
for i in range(2*N):
    if S[i] == "A":
        ai_list.append(i)
    else:
        bi_list.append(i)

# 左から順番に入れ替えるわけではなく、差異的に入れ替えた時と距離の和が編集距離に一致することがポイント
a_res = 0
for i, ai in enumerate(ai_list):
    ii = 2*i
    a_res += abs(ii-ai)

b_res = 0
for i, bi in enumerate(bi_list):
    ii = 2*i
    b_res += abs(ii-bi)

print(min(a_res, b_res))
# スライスを利用してmaxを計算する場合ならもうout of indexは気にしない方が良さそう

S = input().strip()

res = 0
for s in range(1, len(S)+1):
    tmp_res = 0
    for i in range(len(S)):
        if S[i:i+s] == S[i:i+s][::-1]:
            tmp_res = max(len(S[i:i+s]), tmp_res)

    res = max(tmp_res, res)

print(res)


S = input().strip()

res = 0
for i in range(len(S)):
    for j in range(len(S)-i+1):
        if S[i:i+j] == S[i:i+j][::-1]:
            res = max(len(S[i:i+j]), res)

print(res)

## first
#S = input().strip()
#
#for i in range(len(S), -1, -1):
#    for j in range(len(S)):
#        if j + i <= len(S):
#            sub_S = S[j:j+i]
#            if sub_S == sub_S[::-1]:
#                print(i)
#                exit()
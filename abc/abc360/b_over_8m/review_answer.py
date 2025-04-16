S, T = input().split()

for w in range(1, len(S)): # wは区切り文字なので問題文と同じ領域に合わせる
    for s in range(w): # sはインデックスの役割なので0ベース
        res = ""
        for i in range(s, len(S), w):
            res += S[i]
        if res == T:
            print("Yes")
            exit()

print("No")
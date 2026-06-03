import sys; sys.setrecursionlimit(10**7)

H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

res = 0
for h1 in range(H):
    for h2 in range(h1, H):
        for w1 in range(W):
            for w2 in range(w1, W):
                res_flag = True
                # range(h1, h2)だとh2を含まれなくなってしまうので、h2+1の補正を行う
                for i in range(h1, h2+1):
                    for j in range(w1, w2+1):
                        if S_lists[i][j] != S_lists[h1+h2-i][w1+w2-j]:
                            res_flag = False
                            break

                if res_flag:
                    res += 1

print(res)
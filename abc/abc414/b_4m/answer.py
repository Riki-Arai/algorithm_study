N = int(input()) # 数値：1
A_lists = [list(input().split()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

res = ""
count = 0
for c, l in A_lists:
    l = int(l)
    count += l
    if count > 100:
        print("Too Long")
        exit()
    res += c*l

print(res)
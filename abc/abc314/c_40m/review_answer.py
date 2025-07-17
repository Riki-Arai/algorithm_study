N, M = map(int, input().split())
S = input().strip()
C_list = list(map(int, input().split()))

# 文字列を可変リストとして扱う（Pythonの文字列は変更不可のため）
ans = list(S)

# グループごとに所属インデックスをまとめるリスト
groups = [[] for _ in range(M)]
for i, c in enumerate(C_list):
    # c は 1～M の範囲なので、c-1 をインデックスに
    groups[c - 1].append(i)

# 各グループで「1つ右へシフト」する形で文字を入れ替える
for g in groups:
    length = len(g)
    # 要素が1つ以下ならシフト不要
    if length <= 1:
        continue

    # 古い文字を一時的に退避しておき、1つ先の位置にコピー
    old_chars = [ans[idx] for idx in g]
    for j in range(length):
        ans[g[(j + 1) % length]] = old_chars[j]

# 最終的に文字列に戻して出力
print("".join(ans))

# 以下は2回目に解答したもの（模範解答よりもコードが短い）
#N, M = map(int, input().split())
#S = input().strip()
#C_list = list(map(int, input().split()))
#
#idx_lists = [[] for _ in range(M)]
#for i, c in enumerate(C_list):
#    idx_lists[c-1].append(i)
#
#s_list = list(S)
#res_list = [""] * N
#for idx_list in idx_lists:
#    for i in range(len(idx_list)):
#        res_list[idx_list[(i+1)%len(idx_list)]] = s_list[idx_list[i]]
#
#print("".join(res_list))

#N, M = map(int, input().split())
#S = input().strip()
#C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#alp_lists = [[] for _ in range(M)]
#idx_lists = [[] for _ in range(M)]
#for j, c in enumerate(C_list):
#    alp_lists[c-1].append(S[j])
#    idx_lists[c-1].append(j)
#
#res_dict = {}
#for i in range(M):
#    alp_list = alp_lists[i]
#    idx_list = idx_lists[i]
#    for k in range(1, len(alp_list)+1):
#        res_dict[idx_list[k%len(idx_list)]] = alp_list[k-1]
#
#res_list = []
#for i in range(N):
#    res_list.append(res_dict[i])
#
#print("".join(res_list))
# 問題自体は事前に用意したリストに出現回数を記録する典型
# 出現回数が2回に達した時点で答えのリストに追加すればよかったが、自分の場合は無駄な処理を挟んでしまっている
# またこの手の問題はいい加減慣れてきているので、ただ解くのではなく5分くらいでの回答を目指したい
n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(3 * n)]
ans = []
for i in a:
    cnt[i] += 1
    if cnt[i] == 2:
        ans.append(i)
print(*ans)

#N = int(input())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#idx_lists = []
#oc_list = [0] * (N+1)
#for i, a in enumerate(A_list):
#    oc_list[a] += 1
#    if oc_list[a] == 2:
#        idx_lists.append([i, a])
#
#idx_lists.sort(key=lambda x: x[0])
#res_list = list(map(lambda x: x[1], idx_lists))
#print(*res_list)
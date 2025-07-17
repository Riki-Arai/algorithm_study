# リスト化できないのでめぐる式で探索していくが、正解が必ず存在するかどうかをチェックしておくと無難
# ソートしたリスト同士で常にB_listの要素がA_listの要素よりも大きい値でなくてはならない

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
ok = 1 << 30
ng = 0

def can_fit(x):
    c_B_list = B_list[:]
    c_B_list.append(x)
    c_B_list.sort()
    for i in range(N):
        if A_list[i] > c_B_list[i]:
            return False
    # Trueが成立するということはA_list[x(mid)] >= B_list[i]
    # 最小を求める場合はmid >= i(閾値)の条件となるらしいが、確かに今回もそのケースに該当している
    return True

# あえて一番最大値を入れて回答が必ず存在するかをチェック
if not can_fit(ok):
    print(-1)
    exit()

while ok - ng > 1:
    mid = (ok + ng) // 2
    if can_fit(mid):
        ok = mid
    else:
        ng = mid

print(ok)
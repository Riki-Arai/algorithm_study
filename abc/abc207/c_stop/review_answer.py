# 補正の値が小さすぎることが原因で判定が失敗しているだけだった。。。。
# ただ着想自体は合っていたのでそこはポジティブ
# 判定に影響が出るとはあまり認知していないところがあったので今後気をつける
N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

def f(t, l, r):
    if t == 1:
        return l, r
    elif t == 2:
        return l, r-0.05
    elif t == 3:
        return l+0.05, r
    elif t == 4:
        return l+0.05, r-0.05

check_set = set()
res = 0
for i in range(N):
    for j in range(i+1, N):
        t1, l1, r1 = A_lists[i]
        t2, l2, r2 = A_lists[j]
        l1, r1 = f(t1, l1, r1)
        l2, r2 = f(t2, l2, r2)

        if not(r1 < l2 or l1 > r2):
            res += 1

print(res)
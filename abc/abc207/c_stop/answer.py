N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

def f(l, r, x):
    if l <= x <= r:
        if x == l and x == r and isinstance(x, float):
            return False
        return True
    else:
        return False

def g(t, l, r):
    if t == 1:
        return l, r
    elif t == 2:
        return l, r-0.00000001
    elif t == 3:
        return l+0.00000001, r
    elif t == 4:
        return l+0.00000001, r-0.00000001

check_set = set()
res = 0
for i in range(N):
    for j in range(i, N):
        if i != j:
            t1, l1, r1 = A_lists[i]
            t2, l2, r2 = A_lists[j]
            l1, r1 = g(t1, l1, r1)
            l2, r2 = g(t2, l2, r2)

            if (f(l1, r1, r2) or f(l1, r1, l2)) or (f(l2, r2, r1) or f(l2, r2, l1)):
                res += 1

print(res)
def is_ok(i):
    return i > 5 #大きい側がTrue

ok,ng = 10,-1 # さっきと逆なので注意
while ok-ng > 1: # さっきと逆なので注意。abs(ok-ng)のように汎用的に書く流派もある
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok,ng) # "6 5" が出力される

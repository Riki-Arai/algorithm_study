N = int(input().strip())

res_lists = [[0, 0]]
for _ in range(N):
    A, B = map(int, input().split())
    res_lists.append([A, 1])
    res_lists.append([A+B, -1])

n = 0
days = 0
res_lists.sort()
res_list = [0]*(N+1)
for i in range(len(res_lists)-1):
    x, y = res_lists[i]
    xx, yy = res_lists[i+1]
    days = xx-x
    n += y
    res_list[n] += days

print(*res_list[1:])


n = int(input().strip())
x = []  # list of events (position, +1 or -1)
for _ in range(n):
    a, b = map(int, input().split())
    x.append((a,  1))
    x.append((a + b, -1))

x.sort()
# ans[i] := “重なっている区間の長さが i のとき” の合計長さ
# C++ では固定長配列 N=200010 でしたが、Pythonでは必要分だけ確保または dict でも良い
ans = [0] * (n + 2)  # 安全に n+1 まで使えるように n+2 頂きます
cnt = 0
for i in range(len(x) - 1):
    cnt += x[i][1]
    length = x[i+1][0] - x[i][0]
    # cnt が 0 のときも length を足しても問題ないが、
    # “重なっている区間の長さが cnt のとき”という定義なので cnt が 0 のときは ans[0] に入る。
    # ただ C++ コードでは ans[0] を使って出力しないので、ここも同様に扱います。
    ans[cnt] += length

# 出力: ans[1], ans[2], …, ans[n]
# C++ では rep(i, n-1) cout << ans[i+1] ... 最後に cout << ans[n]
res = []
for i in range(1, n+1):
    res.append(str(ans[i]))
print(" ".join(res))
## 文字列を2倍にしたものも加算してしまうことに気づけば全探索でいける
N = int(input()) # 数値

res = 0
for i in range(1, 10**6+1):
    if N < i:
        break

    d = len(str(i))
    if d%2 == 0 and str(i)[:d//2] == str(i)[d//2:]:
        res += 1

    if 10**6 < int(str(i)*2) <= N:
        res += 1

print(res)

#N = int(input()) # 数値
#
#res = 0
#for a in range(1, 10**6+1):
#    w_a = int(str(a) * 2)
#    if w_a > N:
#        break
#    res += 1
#
#print(res)
# 反転前と反転後の文字列を同列に扱う時はminを取る方法が有効らしい（gptによるとメジャーな方法）
# この方法を使えば自分の最初の実装のように考慮漏れを防ぎやすくなる
N = int(input())
t = set()
for _ in range(N):
    S = input()
    t.add(min(S, S[::-1]))

print(len(t))

## first
#N = int(input())
#
#res_set = set()
#for _ in range(N):
#    S = input().strip()
#    res_set.add(S)
#
#double_num = 0
#for res in res_set:
#    if res[::-1] in res_set and res[::-1] != res:
#        double_num += 1
#
#print(len(res_set)-(double_num//2))
N, Q = map(int, input().split())
A_lists = [[s, int(x)] for s, x in (input().split() for _ in range(Q))]

# 右回転をした時に壁がある場合は左回転をするかどうかを判断できればいい
# 左回転をした時のことも考えても上の反対のことをやるだけで意味がない
def f(s, g, w):
    if s < w < g:
        return s+N-g
    return abs(g-s)

res = 0
l, r = 1, 2
for h, t in A_lists:
    if h == "R":
        # 右回転をできるかの判断ができればいいので、パーツとtの位置が反対になっても構わない
        res += f(min(r, t), max(r, t), l)
        r = t
    else:
        res += f(min(l, t), max(l, t), r)
        l = t

print(res)


#N, Q = map(int, input().split())
#A_lists = [[s, int(x)] for s, x in (input().split() for _ in range(Q))]
#
#def f(s, g, w):
#    if s > g:
#        g, s = s, g
#    if s < w < g:
#        return N-g+s
#    else:
#        return g - s
#
#res = 0
#l = 1
#r = 2
#for h, t in A_lists:
#    if h == "R":
#        res += f(r, t, l)
#        r = t
#    else:
#        res += f(l, t, r)
#        l = t
#
#print(res)
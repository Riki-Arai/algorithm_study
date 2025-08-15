N, Q = map(int, input().split())
A_lists = [[s, int(x)] for s, x in (input().split() for _ in range(Q))]

def f(s, g, w):
    if s > g:
        g, s = s, g
    if s < w < g:
        return N-g+s
    else:
        return g - s

res = 0
l = 1
r = 2
for h, t in A_lists:
    if h == "R":
        res += f(r, t, l)
        r = t
    else:
        res += f(l, t, r)
        l = t

print(res)
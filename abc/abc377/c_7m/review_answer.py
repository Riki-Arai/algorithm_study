# 最初の回答は少々コードが煩雑だったが、以下のように工夫を入れておくべきだった
n,m = map(int,input().split())
s = set()
for _ in range(m):
    a,b = map(int,input().split())
    s.add((a,b))
    for i in [-1,1]:
        for j in [-2,2]:
            s.add((a+i,b+j))
            s.add((a+j,b+i))
ans = n*n
for i,j in s:
    if 1<=i<=n and 1<=j<=n:
        ans-=1
print(ans)


## first
#N, M = map(int, input().split())
#
#res_set = set()
#for _ in range(M):
#    a, b = map(int, input().split())
#    res_set.add((a, b))
#    if a + 2 <= N and b + 1 <= N:
#        res_set.add((a + 2, b + 1))
#    if a + 1 <= N and b + 2 <= N:
#        res_set.add((a + 1, b + 2))
#    if a - 1 >= 1 and b + 2 <= N:
#        res_set.add((a - 1, b + 2))
#    if a - 2 >= 1 and b + 1 <= N:
#        res_set.add((a - 2, b + 1))
#    if a - 2 >= 1 and b - 1 >= 1:
#        res_set.add((a - 2, b - 1))
#    if a - 1 >= 1 and b - 2 >= 1:
#        res_set.add((a - 1, b - 2))
#    if a + 1 <= N and b - 2 >= 1:
#        res_set.add((a + 1, b - 2))
#    if a + 2 <= N and b - 1 >= 1:
#        res_set.add((a + 2, b - 1))
#
#print(N*N-len(res_set))
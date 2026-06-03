N = int(input())
A_list = list(map(int, input().split()))

l_list = [0]*(N+1)
r_list = [0]*(N+1)
for i, a in enumerate(A_list, 1):
    if l_list[i-1]+1 <= a:
        l_list[i] = l_list[i-1]+1
    else:
        l_list[i] = a

for i, a in enumerate(A_list[::-1], 2):
    i *= -1
    if r_list[i+1]+1 <= a:
        r_list[i] = r_list[i+1]+1
    else:
        r_list[i] = a

res = 1
for i in range(N-1):
    res = max(min(l_list[i+1], r_list[i]), res)

print(res)


n=int(input())
a=list(map(int,input().split()))
l=[0]*(n+1)
r=[0]*(n+1)
for i in range(1,1+n):
    l[i]=min(l[i-1]+1,a[i-1])

for i in range(n-1,-1,-1):
    r[i]=min(r[i+1]+1,a[i])

ans = -1
for i in range(n):
    ans=max(min(l[i+1],r[i]),ans)

print(ans)
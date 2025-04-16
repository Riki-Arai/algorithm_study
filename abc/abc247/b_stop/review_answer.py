N=int(input())

s=[""]*N; t=[""]*N
for i in range(N):
    s[i],t[i]=input().split()

Ans=1
for i in range(N):
    f=g=1
    for j in range(N):
        if i==j:
            continue
        if s[i]==s[j] or s[i]==t[j]:
            f=0
        if t[i]==s[j] or t[i]==t[j]:
            g=0
    if f==g==0:
        Ans=0
        break

print("Yes" if Ans else "No")

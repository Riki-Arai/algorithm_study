N = int(input())
H_list = list(map(int,input().split()))

ans=1
for i in range(N):
    for w in range(1,N-i):
        cnt=1
        while i+cnt*w<N and H_list[i] == H_list[i+cnt*w]:
            cnt+=1
            ans=max(ans,cnt)

print(ans)
N, S = list(map(int, input().split()))
A_list = list(map(int, input().split()))

dp_list = [False]*(S+1)
dp_list[0] = True
for a in A_list:
    for i in range(S, a-1, -1):
        if dp_list[i-a]:
            dp_list[i] = True

if dp_list[S]:
    print("Yes")
else:
    print("No")

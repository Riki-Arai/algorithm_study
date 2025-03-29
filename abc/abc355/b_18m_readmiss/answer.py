N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

tmp_A_list = A_list.copy()
A_list.extend(B_list)
A_list.sort()
for i in range(1, N+M):
    if A_list[i-1] in tmp_A_list and A_list[i] in tmp_A_list: 
        print("Yes")
        exit()
print("No")
N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

C = sorted(A_list + B_list)
for i in range(1, len(C)):
    if C[i-1] in A_list and C[i] in A_list:
        print("Yes")
        exit()

print("No")
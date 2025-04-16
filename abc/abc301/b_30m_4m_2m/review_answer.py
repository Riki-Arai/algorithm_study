N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N-1):
    ans.append(A[i])
    if not abs(A[i] - A[i+1]) == 1:
        if A[i] < A[i+1]:
            for j in range(A[i]+1, A[i+1]):
                ans.append(j)
        else:
            for j in range(A[i]-1, A[i+1], -1):
                ans.append(j)
ans.append(A[-1])
print(*ans)

####　以下はfirst
#N = int(input())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#while True:
#    count = 0
#    M = len(A_list)
#    for i in range(1, M):
#        f_idx = A_list[i-1]
#        s_idx = A_list[i]
#        if abs(s_idx-f_idx) == 1:
#            count += 1
#        else:
#            if f_idx < s_idx:
#                A_list = A_list[:i] + [j for j in range(f_idx+1, s_idx)] + A_list[i:]
#                break
#            else:
#                A_list = A_list[:i] + [j for j in range(f_idx-1, s_idx, -1)] + A_list[i:]
#                break
#    if count == M - 1:
#        break
#
#print(*A_list)
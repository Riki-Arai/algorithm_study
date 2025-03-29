N, L, R = map(int, input().split())
A_list = [i for i in range(1, N+1)]

tmp_A_list = list(reversed(A_list[L-1:R]))
print(*A_list[:L-1] + tmp_A_list + A_list[R:])
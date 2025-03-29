N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
print(*a_list[-K:] + a_list[:-K])
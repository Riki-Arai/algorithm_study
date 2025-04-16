N = int(input())
A_lists = [input().split() for _ in range(N)]

name_list = sorted(list(map(lambda x: x[0], A_lists)))
rate_sum = sum(list(map(lambda x: int(x[1]), A_lists)))
print(name_list[(rate_sum%N)])
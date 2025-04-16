import statistics

A, B, C = map(int, input().split())
res_list = [A, B, C]
res = statistics.median(res_list)
if res == B:
    print("Yes")
else:
    print("No")
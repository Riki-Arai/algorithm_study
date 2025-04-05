from collections import Counter

N = int(input())
a_list = list(map(int, input().split()))
counter = Counter(a_list)
dup_a_list = [x for x in a_list if counter[x] > 1]

res = 1000000000000
for a in set(dup_a_list):
    first = a_list.index(a)
    second = a_list.index(a, first+1)
    diff = (second - first) + 1
    if diff < res:
        res = diff

if res == 1000000000000:
    print(-1)
else:
    print(res)
import collections

card_list = list(map(int, input().split()))
card_kind_count = collections.Counter(card_list)

tmp = sorted(list(card_kind_count.values()))

if tmp[0] == 1 and tmp[1] == 3:
    print("Yes")
elif tmp[0] == 2 and tmp[1] == 2:
    print("Yes")
else:
    print("No")

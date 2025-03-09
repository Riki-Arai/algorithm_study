N = int(input())
a_list = list(map(int, input().split()))
sorted_a_list = sorted(a_list, reverse=True)
print(a_list.index(sorted_a_list[1])+1)

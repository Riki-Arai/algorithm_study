N = input()
a_list = list(map(int, input().split()))
sorted_a_list = sorted(a_list)
if a_list == sorted_a_list and len(a_list) == len(set(a_list)):
    print("Yes")
else:
    print("No")

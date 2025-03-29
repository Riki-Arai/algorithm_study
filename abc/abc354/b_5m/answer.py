N = int(input())
A_lists = [input().split() for _ in range(N)]

user_list = [a[0] for a in A_lists]
c_sum = sum([int(a[1]) for a in A_lists])
mod = c_sum % N
user_list.sort()
print(user_list[mod])
S_list = list(input())
a, b = map(int, input().split())
c_S_list = S_list[::]
c_S_list[a-1] = S_list[b-1]
c_S_list[b-1] = S_list[a-1]
print("".join(c_S_list))
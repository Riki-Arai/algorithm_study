K, N = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

r_dis_list = []
for i in range(len(A_list)-1):
    r_dis_list.append(A_list[i+1]-A_list[i])

r_dis_list.append(K - A_list[-1] + A_list[0])

l_a_list = []
rev_a_list = A_list[::-1]
for a in rev_a_list:
    l_a_list.append(K - a)

l_dis_list = []
for i in range(len(A_list)-1):
    l_dis_list.append(l_a_list[i+1]-l_a_list[i])

l_dis_list.append(K - l_a_list[-1] + l_a_list[0])
print(min(sum(r_dis_list)-max(r_dis_list), sum(l_dis_list)-max(l_dis_list)))
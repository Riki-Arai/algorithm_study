N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
s_a_list = sorted(list(set(A_list)))
for i, a in enumerate(s_a_list, 1):
    if i > K:
        break
    if res == a:
        res = a+1
    else:
        break

print(res)

#N, K = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#a_set = set(A_list)
#for i in range(K):
#    if i not in a_set:
#        print(i)
#        exit()
#
#print(K)
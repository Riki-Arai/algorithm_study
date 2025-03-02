N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

pair_dic = {}
bib_dic = {}
for n in range(N):
    pair_dic[n] = [p_list[n], q_list[p_list[n]-1]]
    bib_dic[q_list[n]] = n

res_list = []
for i in range(1, N+1):
    p = bib_dic[i]
    res_list.append(str(pair_dic[p][1]))

print(" ".join(res_list))

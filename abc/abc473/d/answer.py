import sys; sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2

sum_ = 0
res_list = []
def dfs(i):
    global sum_
    for j in range((K-sum_)//i+1):
        if sum_+i*j < K and (K-(sum_+i*j))%(i+1):
            sum_ += i*j
            res_list.append(j)
            dfs(i+1)
        elif sum_ + i*j == K:
            res_list.append(j)
            print(*res_list)
            res_list.pop()

dfs(1)
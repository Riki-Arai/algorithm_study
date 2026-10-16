N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list = [0] + A_list
c_list = [0]*(N+1)
k = 0
seen_set = set([1])
a = 1
while k < K:
    a = A_list[a]
    k += 1
    if a in seen_set:
        break
    c_list[a] = k
    seen_set.add(a)

if k == K:
    print(a)
else:
    K -= c_list[a]
    K %= (k-c_list[a])
    for _ in range(K):
        a = A_list[a]
    print(a)
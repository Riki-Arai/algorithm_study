N = int(input())

l_list, r_list = [], []
for _ in range(N):
    L, R = map(int, input().split())
    l_list.append(L)
    r_list.append(R)

# 最初はコメントアウトの条件にしていたが、notの方が直感的に理解しやすい
# if sum_l > 0 or sum_r < 0:
if not (sum(l_list) <= 0 <= sum(r_list)):
    print("No")
    exit()

sum_ = sum(l_list)
for i in range(N):
    # 1ずつ探索するのではなく、差分を用いていく
    # 差分がなくなった場合はminを取ることで毎回0になる
    diff = min(r_list[i]-l_list[i], -sum_)
    sum_ += diff
    l_list[i] += diff

print("Yes")
print(*l_list)
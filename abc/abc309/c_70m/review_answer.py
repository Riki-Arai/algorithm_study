# 日にちの導出方法が原因で苦戦してしまった
# 薬の量は累積和で良いが、日にちは累積和にしてはいけない
# また初日を1としてカウントしている関係から、最終的な解答に+1する必要がある
N, K = map(int, input().split())

sum_ = 0
res_lists = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    res_lists.append([a, b])
    sum_ += b

if sum_ <= K:
    print(1)
    exit()

res_lists.sort(key=lambda x: x[0])
sum_d = 0
res = 0
for res_list in res_lists:
    a, b = res_list
    res = a
    sum_ -= b
    if sum_ <= K:
        print(res+1)
        exit()
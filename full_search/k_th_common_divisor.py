A, B, K = list(map(int, input().split()))

def divisor(N):
    set_ = set()
    for x in range(1, N+1):
        if N % x == 0:
            set_.add(x)

    return set_

common_dev_set = divisor(A) & divisor(B)
list_ = [x for x in common_dev_set]
list_.sort(reverse=True)
print(list_[K-1])

# gptの回答
'''
def find_kth_divisor(A, B, K):
    # AとBの公約数を格納するリスト
    common_divisors = []

    # 最小の数を基準に素朴に公約数を探します
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            common_divisors.append(i)

    # 降順にソート
    common_divisors.sort(reverse=True)

    # K番目の公約数を返す
    return common_divisors[K - 1]

# 入力の取得
A, B, K = map(int, input().split())

# 答えの出力
print(find_kth_divisor(A, B, K))
'''

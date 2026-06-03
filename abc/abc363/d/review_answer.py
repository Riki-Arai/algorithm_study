N = int(input())

# 1番目の回文数は 0
if N == 1:
    print(0)
    exit()

# 0 を除いた中で何番目かにする
N -= 1
for digit in range(1, 40):
    half_len = (digit + 1) // 2

    # digit 桁の回文数の個数
    count = 9 * (10 ** (half_len - 1))

    if N > count:
        N -= count
        continue

    # 前半部分を作る
    half = str(10 ** (half_len - 1) + N - 1)

    # 前半から回文を作る
    if digit % 2 == 1:
        ans = half + half[-2::-1]
    else:
        ans = half + half[::-1]

    print(ans)
    break
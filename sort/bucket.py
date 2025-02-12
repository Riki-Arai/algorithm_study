def bucket_sort(a):
    n = len(a)
    max_val = 22
    num = [0] * max_val
    for x in a:
        num[x] += 1

    sum_ = [0] * max_val
    for x in range(0, len(num)):
        sum_[x] = sum_[x-1] + num[x] 

    a_2 = [0] * n
    print(sum_)
    for x in range(len(a) - 1, -1, -1):
        t = a[x]
        sum_[t] -= 1
        pos = sum_[t]
        a_2[pos] = t

    return a_2

if __name__ == "__main__":
    a = [0, 21, 10, 8, 2, 9, 9, 3, 0, 1, 1]

    # バケットソート実行
    sorted_a = bucket_sort(a)

    # 結果表示
    print(" ".join(map(str, sorted_a)))

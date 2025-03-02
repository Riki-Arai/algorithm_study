import bisect

INF = 20000000  # 十分大きな値に

def main():
    N = 5
    K = 11
    A = [1, 2, 3, 4, 5]
    B = [6, 7, 8, 9, 10]

    B.sort()
    # 暫定最小値を格納する変数
    min_value = INF
    for a in A:
        index = bisect.bisect_left(B, K-a)
        if len(B) > index:
            if min_value > a + B[index]:
                min_value = a + B[index]

    print(min_value)


if __name__ == "__main__":
    main()

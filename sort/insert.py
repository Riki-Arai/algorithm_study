def insertion_sort(a):
    N = len(a)
    for i in range(1, N):
        v = a[i]
        j = i
        while j > 0 and a[j - 1] > v:
            a[j] = a[j - 1]
            j -= 1
        a[j] = v

def main():
    a = [4, 2, 7, 6, 9]

    insertion_sort(a)

    # 結果を出力
    print(" ".join(map(str, a)))

if __name__ == "__main__":
    main()

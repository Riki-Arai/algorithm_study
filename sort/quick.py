def quick_sort(a, left, right):
    if right - left <= 1:
        return

    piv_idx = (left + right) // 2
    piv_val = a[piv_idx]
    a[piv_idx], a[right-1] = a[right-1], piv_val
    i = left
    for j in range(left, right-1):
        if a[j] <= piv_val:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[right-1] = piv_val, a[i]
    quick_sort(a, left, i)
    quick_sort(a, i + 1, right)

if __name__ == "__main__":
    a = [13, 20, 1, 19, 5, 3, 12, 10, 9]

    quick_sort(a, 0, len(a))

    print(" ".join(map(str, a)))

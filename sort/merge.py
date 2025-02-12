def merge_sort(a, left, right):
    if right - left <= 1:
        return

    mid = left + (right - left) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid, right)

    buf = []
    for x in range(left, mid):
        buf.append(a[x])
    for x in range(right-1, mid-1, -1):
        buf.append(a[x])

    l_idx = 0
    r_idx = len(buf) - 1
    for x in range(left, right):
        if buf[r_idx] >= buf[l_idx]:
            a[x] = buf[l_idx]
            l_idx += 1
        else:
            a[x] = buf[r_idx]
            r_idx -= 1

if __name__ == "__main__":
    a = [8, 5, 3, 7, 4]
    merge_sort(a, 0, len(a))
    print(" ".join(map(str, a)))

def heapify(a, i, n):
    if i >= n:
        return

    j = i * 2 + 1
    print(a)
    if j + 1 < n and a[j+1] > a[j]:
        a[j], a[j+1] = a[j+1], a[j]
    print(a)
    if j < n and a[j] > a[i]:
        a[i], a[j] = a[j], a[i]
        heapify(a, j, n)
    print(a)
    print()
    print()

def heap_sort(a):
    n = len(a)
    i = n // 2
    for j in range(i, -1, -1): 
        heapify(a, j, n)

    for j in range(n-1, -1, -1):
        print(j)
        a[0], a[j] = a[j], a[0]
        heapify(a, 0, j)
    

if __name__ == "__main__":
    a = [10, 7, 12, 1, 3]
    heap_sort(a)
    print(" ".join(map(str, a)))

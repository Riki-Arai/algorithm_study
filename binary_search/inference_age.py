N = 8
A = [3, 5, 8, 10, 14, 17, 21, 39]
key = 50

def binary_search(A, key, left, right):
    if left > right:
        return -1
    mid = left + (right-left) // 2
    if A[mid] == key:
        return mid
    elif A[mid] > key:
        return binary_search(A, key, left, mid-1)
    elif A[mid] < key:
        return binary_search(A, key, mid+1, right)

print(binary_search(A, key, 0, N-1))

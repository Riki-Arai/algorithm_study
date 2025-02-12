def fib(arr, n):
    if arr[n] != 0:
        return arr[n]
    elif n == 0:
        arr[0] = 1
        return arr[0]
    elif n == 1:
        arr[1] = 1
        return arr[1]
    else:
        arr[n] = fib(arr, n - 1) + fib(arr, n - 2)
        return arr[n]

n = 8
arr = [0] * n
print(fib(arr, n - 1))

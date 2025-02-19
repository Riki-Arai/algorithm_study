N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
a_result, b_result = 0, 0
for i, a in enumerate(A, 1):
    if i % 2 == 1:
        a_result += a

    elif i % 2 == 0:
        b_result += a

print(a_result - b_result)

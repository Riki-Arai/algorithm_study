N = int(input())
W = int(input())
A = list(map(int, input().split()))

def bit_search():
    for bit in range(1 << N):
        w_sum = 0
        for i in range(N):
            if bit & 1 << i:
                w_sum += A[i]
            if w_sum == W:
                return True
    return False

print(bit_search())

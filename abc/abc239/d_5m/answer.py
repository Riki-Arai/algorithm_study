A, B, C, D = map(int, input().split())

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            break
    else:
        print("Takahashi")
        exit()

print("Aoki")
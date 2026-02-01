K = int(input())

def legendre_formula(N, p):
    count = 0
    power = p
    while power <= N:
        count += N // power
        power *= p
    return count
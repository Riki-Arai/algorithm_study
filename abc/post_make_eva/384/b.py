N, R = list(map(int, input().split()))

for _ in range(N):
    D, A = list(map(int, input().split()))
    if D == 1 and R >= 1600 and R <= 2799:
        R += A
    if D == 2 and R >= 1200 and R <= 2399:
        R += A

print(R)

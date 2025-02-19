A = int(input())
B = int(input())
C = int(input())
X = int(input())

result = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            sum_ = 500 * a + 100 * b + 50 * c
            if sum_ == X:
                result += 1

print(result)

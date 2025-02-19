N, A, B = list(map(int, input().split()))

def find_digit(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

result = 0
for n in range(1, N+1):
   if int(A) <= find_digit(n) <= int(B): 
       result += n

print(result)

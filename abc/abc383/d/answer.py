N = int(input())

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


p_list = []
for i in range(2*10**6+1):
    if is_prime(i):
        p_list.append(i)

res = 0
for i in range(len(p_list)):
    if pow(p_list[i], 8) <= N:
        res += 1
    for j in range(i+1, len(p_list)):
        if pow(p_list[i], 2)*pow(p_list[j], 2) <= N:
            res += 1
        else:
            break

print(res)
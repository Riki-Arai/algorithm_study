n, k = map(int, input().split())

def convert_to_base_num(n, k):
    # 符号を考慮
    if n == 0:
        return "0"
    sign = ""
    if n < 0:
        sign = "-"
        n = -n
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    while n > 0:
        r = n % k
        n //= k
        result.append(digits[r])

    return sign + "".join(reversed(result))

print(len(convert_to_base_num(n, k)))
N = int(input()) # 取得例：1

def convert_base(num_str: str, from_base: int, to_base: int) -> str:
    decimal_value = int(num_str, from_base)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_value == 0:
        return "0"
    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value //= to_base
    return result

res = 0
for i in range(1, N+1):
    k = convert_base(str(i), 10, 8)
    if "7" not in str(i) and "7" not in k:
        res += 1

print(res)
N = int(input())

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

res = convert_base(str(N), 10, 16)
print(f"{res:02}")
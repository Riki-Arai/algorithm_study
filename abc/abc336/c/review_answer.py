'''
5進数であることをまずは見抜く。
以下のような関係になっており、N番目のものはN-1の5進数に対して2倍することで求められる
0, 1, 2, 3, 4, 10, 11, 12, ・・・
0, 1, 2, 3, 4, 5, 6, 7・・・
'''
N = int(input())

n = N - 1
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

print(int(convert_base(str(n), 10, 5))*2)
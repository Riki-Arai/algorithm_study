from decimal import Decimal

A, B = input().split()
A_dec = Decimal(A)
B_dec = Decimal(B)

result = A_dec * B_dec
print(int(result))
N = int(input()) # 数値
s = str(N).strip("0")

if s == s[::-1]:
    print("Yes")
else:
    print("No")
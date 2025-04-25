X = input().strip() # 文字列

res = ""
for x in X:
    if x == ".":
        break
    else:
        res += x

print(res)
S = input().strip() # 文字列

for i, s in enumerate(list(S), 1):
    if i % 2 == 0 and s.isupper():
        continue
    elif i % 2 != 0 and s.islower():
        continue
    else:
        print("No")
        exit()

print("Yes")
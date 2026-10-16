X = int(input()) # 取得例：1

for a in range(-200, 201, 1):
    for b in range(-200, 201, 1):
        if pow(a, 5)-pow(b, 5) == X:
            print(a, b)
            exit()
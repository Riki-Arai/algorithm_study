N = int(input())

result = 0
for x in range(1, N+1):
    count = 0
    if x % 2 != 0:
        for y in range(1, x+1):
            if x % y == 0: 
                count += 1
        if count == 8:
            result += 1
print(result)

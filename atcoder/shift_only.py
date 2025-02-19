n = int(input())
a_list = list(map(int, input().split()))

count = 0
while len(a_list) >= n:
    for i, a in enumerate(a_list):
        if a % 2 == 0:
            a_list[i] = int(a // 2)
        elif a % 2 != 0:
            a_list.remove(a)

        if i == n - 1:
            count += 1

print(count)

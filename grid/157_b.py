row_list = [input().split() for _ in range(3)]
col_list = [col for col in zip(*row_list)]
diagonal_list = [[row_list[0][0], row_list[1][1], row_list[2][2]], [row_list[0][2], row_list[1][1], row_list[2][0]]]

N = int(input())
num_set = set([input() for _ in range(N)])
for row in row_list:
    if set(row) <= num_set:
        print("Yes")
        exit()

for col in col_list:
    if set(col) <= num_set:
        print("Yes")
        exit()

for diagonal in diagonal_list:
    if set(diagonal) <= num_set:
        print("Yes")
        exit()

print("No")

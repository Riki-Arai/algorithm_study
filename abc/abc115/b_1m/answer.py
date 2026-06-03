import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
p_list = [int(input().strip()) for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用

p_list.sort(reverse=True)
print(p_list[0]//2+sum(p_list[1:]))
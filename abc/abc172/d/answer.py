N = int(input()) # 取得例：1

def count_divisors_all(n):
   # 約数の個数を記録する配列（初期値 1）
   div_count = [1] * (n + 1)
   # エラトステネスの篩の要領で更新
   for i in range(2, n + 1):
       for j in range(i, n + 1, i):
           div_count[j] += 1
   return div_count

div_list = count_divisors_all(N)

res = 0
for x in range(1, N+1):
    res += x*div_list[x]

print(res)
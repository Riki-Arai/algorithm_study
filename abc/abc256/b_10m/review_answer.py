N = int(input())
A = list(map(int, input().split()))
P = 0
field = [0, 0, 0, 0]        # マスの状態を管理する list
for x in A:
  next_field = [0, 0, 0, 0] # 次のマスの状態を管理する list
  field[0] = 1              # マス 0 にコマを置く
  for i in range(4):
    if field[i] == 1:
      if i + x >= 4:        # i + x >= 4 かどうかに応じて場合分け
        P += 1
      else:
        next_field[i + x] = 1
  field = next_field
print(P)

#N = int(input())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#res = 0
#res_list = []
#for a in A_list:
#    res_list.append(0)
#    res_list = list(map(lambda x: x+a, res_list))
#    while res_list[0] > 3:
#        res_list.pop(0)
#        res += 1
#        if len(res_list) == 0:
#            break
#
#print(res)
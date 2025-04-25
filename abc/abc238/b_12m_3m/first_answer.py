N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [0]
for a in A_list:
    res_list = list(map(lambda x: (x + a) % 360, res_list))
    res_list.append(0)

res = 0
res_list.sort()
for i in range(len(res_list)-1):
    res = max(res, abs(res_list[i]-res_list[i+1]))

print(max(res, abs(360-res_list[-1])))
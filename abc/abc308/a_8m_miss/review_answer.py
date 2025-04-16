S_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for i in range(len(S_list)-1):
    if not(S_list[i] <= S_list[i+1] and 100 <= S_list[i] <= 675 and S_list[i] % 25 == 0):
        print("No")
        exit()

print("Yes")


## first
#S_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#for i in range(len(S_list)-1):
#    if S_list[i] > S_list[i+1]:
#        print("No")
#        exit()
#    if not(100 <= S_list[i] <= 675 and 100 <= S_list[i+1] <= 675):
#        print("No")
#        exit()
#    if not( S_list[i] % 25 == 0 and S_list[i+1] % 25 == 0):
#        print("No")
#        exit()
#
#print("Yes")
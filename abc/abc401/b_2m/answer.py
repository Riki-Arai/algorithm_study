N = int(input()) # 数値：1
S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用

res = 0
login_flag = False
for s in S_list:
    if s == "login":
        login_flag = True
    if s == "logout":
        login_flag = False
    if not login_flag and s == "private":
        res += 1

print(res)
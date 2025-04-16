N = int(input())
W_list = input().split() # 取得例：["a", "b", "c"]、1行の入力用

for w in W_list:
    if w in ("and", "not", "that", "the", "you"):
        print("Yes")
        exit()

print("No")
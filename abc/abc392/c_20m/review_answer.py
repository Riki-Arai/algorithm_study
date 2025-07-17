N = int(input())
p_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

res_list = [0] * N
#　ゼッケン番号iがどのゼッケン番号を見たかという観点で捉えてみると、この処理の意味がわかりやすくなるかも
# 例の出力の3 4 1 2でも、1のゼッケンは3、2のゼッケンは4、3のゼッケンは1・・のように見ることが可能
for i in range(N):
    # 1番目の人はゼッケン2をつけているので、res_listの1に着目
    # 1番目の人は4の人(p_list[i])を見ている。そして4の人はq_listによるとゼッケン4をつけている
    # よってres_list[1] = 4となる
    res_list[q_list[i]-1] = q_list[p_list[i]-1]

print(*res_list)
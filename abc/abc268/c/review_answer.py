N = int(input())
P_list = list(map(int, input().split()))

res_list = [0]*(N+1)
for i, p in enumerate(P_list):
    ii = (p-i)%N - 1
    for k in range(0, 3):
        res_list[(ii+k)%N] += 1

print(max(res_list))


N = int(input())
P_list = list(map(int, input().split()))

cnt = [0] * N
for i in range(N):
    # P_list[i]の料理をiの左隣にたた持ってための回転数を導出している
    # P_list[i] - iでは正面に持っていくまでの回転数（例：i=1、P_list[i]=2であれば1回転必要）
    # 左隣にしたいので、正面にするために必要な回転数に-1する
    j = (P_list[i] - i - 1) % N
    for k in range(3):
        # j回転数+k回転させた時に喜ぶので+1する
        # 他のiでもj+kで一致した時に+1できるので、結果的に累積することができる
        cnt[(j + k) % N] += 1

ans = max(cnt)
print(ans)

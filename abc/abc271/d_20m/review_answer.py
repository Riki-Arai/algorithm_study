'''
(1) 過去の状態を常に残して全探索で間に合うのであれば良いが、今回の場合だとTLE
(2) O(N*S)とやっても間に合いそうなのでDPが良さそうだが構築問題でもある
(3) ペンディングができず、必ず1つを選択するタイプの問題なので、常に新しいリストを作成する方法のDPを使う
(4) インデックスをSの情報、中身を構築した文字列を格納していけばいい
(5) ペンディングができずに必ず1つ選択するタイプの問題は、新しいリストを作るDPが使えるかもという意識が大事
'''
N, S = map(int, input().split())

dp_lists = [[False, ""]] * (10**4+1)
dp_lists[0] = [True, ""]
for _ in range(N):
    a, b = map(int, input().split())
    # n回後に到着しているかの判定をしたいときは途中経過のものを記録に残さないためにこのようなリストを用意
    new_dp_lists = [[False, ""]] * (10**4+1)
    for i in range(10**4, -1, -1):
        if i-a >= 0 and dp_lists[i-a][0]:
            new_dp_lists[i] = [True, dp_lists[i-a][1]+"H"]
        if i-b >= 0 and dp_lists[i-b][0]:
            new_dp_lists[i] = [True, dp_lists[i-b][1]+"T"]

    dp_lists = new_dp_lists.copy()

if dp_lists[S][0]:
    print("Yes")
    print(dp_lists[S][1])
else:
    print("No")
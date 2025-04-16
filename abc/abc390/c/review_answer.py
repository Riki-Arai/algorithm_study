# マスの範囲(h行w列)
h,w = map(int, input().split())

# 作成する長方形のxの範囲
range_x = [1000,0]

# 作成する長方形のyの範囲
range_y = [1000,0]

# 白マスの座標を格納するリスト
white = []

# マスの入力
for i in range(h):
  s = input()

  for j in range(w):
    # マスが黒(#)の場合
    if s[j] == "#":
      # xの範囲を更新
      range_x[0] = min(range_x[0],j)
      range_x[1] = max(range_x[1],j)

      # yの範囲を更新
      range_y[0] = min(range_y[0],i)
      range_y[1] = max(range_y[1],i)

    # マスが白(.)の場合
    elif s[j] == ".":
      # 白マスの座標を格納
      white.append([j,i])

#　白マスが作成される長方形の外にあるか確認
for w in white:
  if(range_x[0] <= w[0] <= range_x[1] and range_y[0] <= w[1] <= range_y[1]):
    print("No")
    exit()

print("Yes")
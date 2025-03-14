# 文字列の位置探索
S = 'ab0ab0'
print(S.find('ab'))  # 0
print(S.find('c'))  # -1
print(S.rfind('ab')) # 3
print(S.rfind('c')) # -1

# 文字列の計算評価
eval("3 * 1")

# 3, 5, 7のいずれであればindexが1となるのでYes
print(['NO', 'YES'][[7, 5, 3].count(int(input()))])

# 8 4と入力されていれば2.0と返却
string = input().replace(' ', '/')
print(eval(string))

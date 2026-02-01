X, Y = input().split() # 取得例："A" "B"

v_dict = {"Ocelot":1, "Serval":2, "Lynx":3}
if v_dict[X] >= v_dict[Y]:
    print("Yes")
else:
    print("No")
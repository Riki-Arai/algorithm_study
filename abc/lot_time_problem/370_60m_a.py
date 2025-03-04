## 愚直に実装をしすぎ、6パターンしかないのであれば6パターンごとの記号で振り分ければ済む話

S = input()
if S == "< > >" or S == "> < <":
    print("A")
elif S == "> > >" or S == "< < <":
    print("B")
else:
    print("C")

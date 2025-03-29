S = input().strip()
if S[0] == "A":
    if "C" in S[2:-1] and S[2:-1].count("C") == 1:
        for s in S:
            if s!= "A" and s != "C" and s.lower() != s:
                print("WA")
                exit()


        print("AC")
    else:
        print("WA")

else:
    print("WA")
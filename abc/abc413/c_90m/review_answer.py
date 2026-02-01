from collections import deque

q = deque()

for _ in range(int(input())):
    t, *p = (int(x) for x in input().split())
    if t == 1:
        c, x  = p
        q.append((x, c))
    else:
        c = p[0]
        result = 0
        while c:
            x, d = q.popleft()
            # この処理が何度もありそうにみえるが、最大でもappendした数しか処理が発生しない
            # appendとpopleftを交互に繰り返す場合はQ+Q=O(Q)
            # appendをQ-1行ない、最後にwhileのif条件が続いてもappend分しか処理が発生しないので、2*(Q-1)=O(Q)に収まる
            if d <= c:
                c -= d
                result += x * d
            else:
                result += x * c
                q.appendleft((x, d - c))
                break
        print(result)
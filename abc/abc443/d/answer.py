import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        R = list(map(int, input().split()))

        ans = 0

        # 左→右
        for i in range(1, N):
            if R[i] > R[i-1] + 1:
                diff = R[i] - (R[i-1] + 1)
                ans += diff
                R[i] = R[i-1] + 1

        # 右→左
        for i in range(N-2, -1, -1):
            if R[i] > R[i+1] + 1:
                diff = R[i] - (R[i+1] + 1)
                ans += diff
                R[i] = R[i+1] + 1

        print(ans)

if __name__ == "__main__":
    solve()
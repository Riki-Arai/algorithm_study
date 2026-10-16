import sys
import math

def solve():
    # 入力の読み込み
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    
    # K=1の場合は無数に直線を引けるので Infinity
    if K == 1:
        print("Infinity")
        return
        
    # 点の座標を取得
    points = []
    idx = 2
    for _ in range(N):
        points.append((int(data[idx]), int(data[idx+1])))
        idx += 2
        
    # 辞書: { (傾きdy, 傾きdx, 切片の分子) : {その直線に乗っている点のインデックスの集合} }
    lines = {}
    
    # 全ての2点の組み合わせを探索
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            
            dx = x2 - x1
            dy = y2 - y1
            
            # 垂直な直線 (x = x1) の場合
            if dx == 0:
                dy = 1
                dx = 0
                b_num = x1 # 垂直な場合はx座標を切片の代わりとする
            else:
                # 常に dx が正になるように符号を調整 (直線の同一性判定のため)
                if dx < 0:
                    dx = -dx
                    dy = -dy
                
                # 最大公約数で割って既約分数にする
                g = math.gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                
                # 切片 b = y1 - (dy/dx)*x1 の分子部分
                b_num = y1 * dx - x1 * dy
            
            # 傾きと切片の情報を一意なキーとする
            line_key = (dy, dx, b_num)
            
            # 辞書にセットを作成し、点 i と j を追加
            if line_key not in lines:
                lines[line_key] = set()
            lines[line_key].add(i)
            lines[line_key].add(j)
            
    # K個以上の点を含む直線の数を数え上げる
    ans = 0
    for key, pts_set in lines.items():
        if len(pts_set) >= K:
            ans += 1
            
    print(ans)

if __name__ == '__main__':
    solve()
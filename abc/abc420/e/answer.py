import sys

def main():
    # 入力を一括で取得して高速化
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    Q = int(input_data[1])

    # 1-indexedで配列を確保
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    black_count = [0] * (N + 1)  # グループ（代表元）ごとの黒頂点の数
    color = [0] * (N + 1)        # 頂点の色（0: 白, 1: 黒）

    # 非再帰による経路縮約付きfind
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    # ランク論理に基づく結合と黒頂点数の合算
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            black_count[root_i] += black_count[root_j]
            if rank[root_i] == rank[root_j]:
                rank[root_i] += 1

    idx = 2
    results = []

    for _ in range(Q):
        query_type = input_data[idx]
        
        if query_type == '1':
            u = int(input_data[idx + 1])
            v = int(input_data[idx + 2])
            union(u, v)
            idx += 3
            
        elif query_type == '2':
            v = int(input_data[idx + 1])
            root = find(v)
            # 反転（白→黒 または 黒→白）してグループの黒の数を更新
            if color[v] == 0:
                color[v] = 1
                black_count[root] += 1
            else:
                color[v] = 0
                black_count[root] -= 1
            idx += 2
            
        elif query_type == '3':
            v = int(input_data[idx + 1])
            root = find(v)
            if black_count[root] >= 1:
                results.append("Yes")
            else:
                results.append("No")
            idx += 2

    # まとめて出力
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    main()
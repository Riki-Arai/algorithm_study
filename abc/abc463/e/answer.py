'''
(1) 最小の重みで到達する問題なのでダイクストラ法を適用できるが、愚直にワープの辺を張ろうとするとTLEになる
(2) そのためワープの扱いをどうするかが肝となるが、ワープの始点となるものが1つに決まるのではないかと思い始める
    →ダイクストラで先に辿りついた後の頂点から、すでに到達図の頂点に改めてワープするのは明らかにコストが無駄
    →よって現時点よりも前の頂点からワープすることによってコストが低くなる可能性があるとわかる
    →その前の頂点についても始点となる箇所は常に1つに決まるので、そこがどこかを求めてあげればいい
(3) そこが求めることができれば辺を張ってダイクストラを実行すればいい
(4) 図を用いた分析と辺の貼り方に着目できたことは良かったが、解説の方がだいぶスマート
(5) 頂点を追加する発想を持った上で式を分解できないか、多数の頂点に接続できそうかなどを考える工程が大事だと学んだ
    →多数の頂点と接続する必要があるときに有効そう
'''
import heapq as hq

N, M, Y = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, T = map(int, input().split()) # 取得例：1 2
    g_lists[u].append((T, v))
    g_lists[v].append((T, u))

X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

hq_list = [(0, 1)]
hq.heapify(hq_list)
res_list = [float("inf")] * (N + 1)
res_list[1] = 0
min_wc = X_list[0] + Y
ws_n = 1
while hq_list:
    w, u = hq.heappop(hq_list)
    if w > res_list[u]:
        continue

    for c, v in g_lists[u]:
        ww = w + c
        if res_list[v] > ww:
            res_list[v] = ww
            if min_wc > X_list[v-1]+Y+res_list[v]: 
                ws_n = v
                min_wc = X_list[v-1]+Y
            hq.heappush(hq_list, (ww, v))

for n in range(1, N+1):
    if n != ws_n:
        g_lists[ws_n].append((min_wc+X_list[n-1], n))

hq_list = [(0, 1)]
hq.heapify(hq_list)
res_list = [float("inf")] * (N + 1)
res_list[1] = 0
while hq_list:
    w, u = hq.heappop(hq_list)
    if w > res_list[u]:
        continue

    for c, v in g_lists[u]:
        ww = w + c
        if res_list[v] > ww:
            res_list[v] = ww
            hq.heappush(hq_list, (ww, v))

print(*res_list[2:])
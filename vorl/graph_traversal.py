# 隣接リストのBFS/DFSと、4近傍グリッドBFS。各探索は O(V + E) または O(HW)。

from collections import deque


# TODO: graphとstartを問題に合わせて用意する。頂点番号は0-indexにそろえる。
# 各辺の重みが1のグラフの距離を返す。到達不能は -1。
def bfs_distances(graph: list[list[int]], start: int) -> list[int]:
    distances = [-1] * len(graph)
    distances[start] = 0
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return distances


# TODO: graphとstartを問題に合わせて用意する。頂点番号は0-indexにそろえる。
# startから到達できる頂点を、再帰を使わず深さ優先順で返す。
def dfs_order(graph: list[list[int]], start: int) -> list[int]:
    visited = [False] * len(graph)
    visited[start] = True
    order = [start]
    stack = [iter(graph[start])]

    while stack:
        for neighbor in stack[-1]:
            if not visited[neighbor]:
                visited[neighbor] = True
                order.append(neighbor)
                stack.append(iter(graph[neighbor]))
                break
        else:
            stack.pop()

    return order


# TODO: 開始座標は0-indexの通行可能マスにする。
# 4近傍の距離を返す。# は壁、到達不能は -1。
def grid_bfs(grid: list[str], start_row: int, start_col: int) -> list[list[int]]:
    height = len(grid)
    width = len(grid[0])
    distances = [[-1] * width for _ in range(height)]
    distances[start_row][start_col] = 0
    queue = deque([(start_row, start_col)])
    # TODO: 8方向移動などなら方向差分を変更する。
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue:
        row, col = queue.popleft()
        for row_step, col_step in directions:
            next_row = row + row_step
            next_col = col + col_step
            if 0 <= next_row < height and 0 <= next_col < width:
                # TODO: 壁文字が#以外なら比較する値を変更する。
                if grid[next_row][next_col] != "#" and distances[next_row][next_col] == -1:
                    distances[next_row][next_col] = distances[row][col] + 1
                    queue.append((next_row, next_col))

    return distances

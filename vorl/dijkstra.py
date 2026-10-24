# 非負整数重みの単一始点最短路。多重辺ありで O(V + E log(E + 1))。

import heapq


# TODO: graph[u]に(行き先, 非負整数重み)を追加する。頂点番号とstartを0-indexにそろえる。
# 到達不能な頂点は float('inf')。単純グラフなら O((V + E) log V)。
def dijkstra(
    graph: list[list[tuple[int, int]]], start: int
) -> list[int | float]:
    distances: list[int | float] = [float("inf")] * len(graph)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        distance, vertex = heapq.heappop(queue)
        if distance != distances[vertex]:
            continue

        for neighbor, weight in graph[vertex]:
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                heapq.heappush(queue, (candidate, neighbor))

    return distances

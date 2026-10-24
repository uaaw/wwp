# 0-index頂点の集合を併合・判定する。各操作は償却 O(α(n))。


# TODO: nには頂点数を渡す。入力番号が1-indexなら各呼び出しで1引く。
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.sizes = [1] * n

    def find(self, vertex: int) -> int:
        while self.parent[vertex] != vertex:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex

    def union(self, first: int, second: int) -> bool:
        first_root = self.find(first)
        second_root = self.find(second)
        if first_root == second_root:
            return False

        if self.sizes[first_root] < self.sizes[second_root]:
            first_root, second_root = second_root, first_root
        self.parent[second_root] = first_root
        self.sizes[first_root] += self.sizes[second_root]
        return True

    def size(self, vertex: int) -> int:
        return self.sizes[self.find(vertex)]

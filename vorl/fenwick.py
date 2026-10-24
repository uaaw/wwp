# 整数の一点加算と半開区間和を扱う。各操作 O(log n)、メモリ O(n)。


# TODO: nは要素数。addの位置は0-indexなので、1-index入力なら呼び出し時に1引く。
class Fenwick:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    # 0-indexの位置にdeltaを加える。0 <= index < n。
    def add(self, index: int, delta: int) -> None:
        index += 1
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    # 半開区間 [0, end) の和を返す。0 <= end <= n。
    def prefix_sum(self, end: int) -> int:
        total = 0
        while end > 0:
            total += self.tree[end]
            end -= end & -end
        return total

    # 半開区間 [left, right) の和を返す。
    # TODO: 1-indexの閉区間 [l, r] は range_sum(l - 1, r) に直す。
    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left)

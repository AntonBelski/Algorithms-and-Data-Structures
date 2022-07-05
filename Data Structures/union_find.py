class UnionFind:
    def __init__(self, n):
        # Time Complexity - O(n)
        self.nodes = []
        self.sizes = []

        for i in range(n):
            self.nodes.append(i)
            self.sizes.append(1)

    def union(self, p, q):
        # Time Complexity - O(log*(n)), * -> iterated logarithm, veryyy close to constant O(1)
        p_root = self.root(p)
        q_root = self.root(q)

        if p_root == q_root:
            return

        if self.sizes[q_root] > self.sizes[p_root]:
            self.nodes[p_root] = q_root
            self.sizes[q_root] += self.sizes[p_root]
        else:
            self.nodes[q_root] = p_root
            self.sizes[p_root] += self.sizes[q_root]

    def root(self, e):
        # Time Complexity - O(log*(n)), * -> iterated logarithm, veryyy close to constant O(1)
        # Tarjan and Van Leeuwen one-pass improvement, Here is - Path splitting
        # Good description - https://en.wikipedia.org/wiki/Disjoint-set_data_structure
        while e != self.nodes[e]:
            e, self.nodes[e] = self.nodes[e], self.nodes[self.nodes[e]]
        return e

    def connected(self, p, q):
        # Time Complexity - O(log*(n)), * -> iterated logarithm, veryyy close to constant O(1)
        return self.root(p) == self.root(q)


if __name__ == '__main__':
    union_find = UnionFind(6)
    union_find.union(1, 5)
    union_find.union(0, 5)
    union_find.union(4, 5)
    union_find.union(4, 4)
    union_find.union(4, 5)
    print(union_find.nodes)
    print(union_find.sizes)

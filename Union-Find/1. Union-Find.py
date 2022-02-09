class UnionFind:
    def __init__(self, n):
        # Time Complexity - O(n)
        self.nodes = {}
        self.sizes = {}

        for i in range(n):
            self.nodes[i] = i
        for i in range(n):
            self.sizes[i] = 1

    def union(self, p, q):
        # Time Complexity - O(log*(n)), * -> this function veryyy close to constant O(1)
        p_node_root = self.root(p)
        q_node_root = self.root(q)
        if self.sizes[q_node_root] > self.sizes[p_node_root]:
            self.nodes[p_node_root] = q_node_root
            self.sizes[q_node_root] += self.sizes[p_node_root]
        else:
            self.nodes[q_node_root] = p_node_root
            self.sizes[p_node_root] += self.sizes[q_node_root]

    def root(self, e):
        # Time Complexity - O(log*(n)), * -> this function veryyy close to constant O(1)
        while e != self.nodes[e]:
            self.nodes[e] = self.nodes[self.nodes[e]]
            e = self.nodes[e]
        return e

    def connected(self, p, q):
        # Time Complexity - O(log*(n)), * -> this function veryyy close to constant O(1)
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

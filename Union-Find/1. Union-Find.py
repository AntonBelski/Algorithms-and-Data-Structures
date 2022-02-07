class UnionFind:
    def __init__(self, n):
        # Time Complexity - O(n)
        self.nodes = []
        self.sizes = []

        for i in range(n):
            self.nodes.append(i)
        for i in range(n):
            self.sizes.append(1)

    def union(self, p, q):
        # Time Complexity - O(log(n))
        p_node_root = self.root(p)
        q_node_root = self.root(q)
        if self.sizes[q_node_root] > self.sizes[p_node_root]:
            self.nodes[p_node_root] = q_node_root
            self.sizes[q_node_root] += self.sizes[p_node_root]
        else:
            self.nodes[q_node_root] = p_node_root
            self.sizes[p_node_root] += self.sizes[q_node_root]

    def root(self, e):
        # Time Complexity - O(log(n))
        while e != self.nodes[e]:
            self.nodes[e] = self.nodes[self.nodes[e]]
            e = self.nodes[e]
        return e

    def connected(self, p, q):
        # Time Complexity - O(log(n))
        return self.root(p) == self.root(q)


if __name__ == '__main__':
    pass

# graph_utilities.py

import numpy as np
import random

class DisjointSet:
    """
    A 'disjoint set' data structure (also known as 'union-find') to keep track
    of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1
            return True
        return False

def generate_random_adjacency_matrix(n, m):
    assert 1 <= m <= n, "number of components must be between 1 and n to be consistent"
    ds = DisjointSet(n)
    adjacency_matrix = np.zeros((n, n), dtype=int)

    while ds.components > m:
        a, b = random.sample(range(n), 2)
        if ds.union(a, b):
            adjacency_matrix[a, b] = 1
            adjacency_matrix[b, a] = 1

    return adjacency_matrix

def is_valid_adjacency_matrix(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return False
    if not np.all(np.diag(matrix) == 0):
        return False
    if not np.all(matrix == matrix.T):
        return False
    return True

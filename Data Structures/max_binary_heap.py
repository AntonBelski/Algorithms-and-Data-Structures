class BinaryMaxHeap:
    def __init__(self, array):
        self.heap = [0] + array
        self.heapify()

    def heapify(self):
        # Build a max heap
        # Time Complexity - O(n), sift_down approach
        n = len(self.heap)

        for i in range(n - 1, 0, -1):
            self.sift_down(i)

    def sift_up(self, i):
        # Move a node up in the tree, as long as needed; used to restore heap condition after insertion
        # Time Complexity - O(log(n))
        while i // 2 > 0 and self.heap[i // 2] < self.heap[i]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def sift_down(self, i):
        # Move a node up in the tree, as long as needed; used to restore heap condition after insertion
        # Time Complexity - O(log(n))
        while i * 2 < len(self.heap):
            largest = i
            if self.heap[i * 2] > self.heap[largest]:
                largest = i * 2
            if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] > self.heap[largest]:
                largest = i * 2 + 1

            if i != largest:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def insert(self, val):
        # Insert a node into the heap
        # Time Complexity - O(log(n))
        self.heap.append(val)
        self.sift_up(len(self.heap) - 1)

    def extract_max(self):
        # Return the max value, removing node with this value
        # Time Complexity - O(log(n))
        if len(self.heap) > 1:
            max_value = self.heap[1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self.sift_down(len(self.heap) - 1)
            return max_value

    def get_max(self):
        # Return the max value
        # Time Complexity - O(1)
        if len(self.heap) > 1:
            return self.heap[1]

    def get_size(self):
        # Return the heap size
        # Time Complexity - O(1)
        return len(self.heap) - 1

    def is_empty(self):
        # Return true if heap contains no elements
        # Time Complexity - O(1)
        return not bool(len(self.heap) - 1)


if __name__ == '__main__':
    array = [3, 9, 2, 1, 4, 5]
    binary_max_heap = BinaryMaxHeap(array)
    print(binary_max_heap.heap)
    binary_max_heap.insert(6)
    print(binary_max_heap.heap)
    print(binary_max_heap.extract_max())
    print(binary_max_heap.heap)
    print(binary_max_heap.get_max())
    print(binary_max_heap.heap)
    print(binary_max_heap.get_size())
    print(binary_max_heap.is_empty())

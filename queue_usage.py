from singly_linked_list import SinglyLinkedList
from collections import deque
from queue import Queue


if __name__ == '__main__':
    print('Queue implementation using Singly Linked List (TC add_tail() - O(1), TC remove_head() - O(1))')
    test_queue = SinglyLinkedList()
    print(test_queue)
    test_queue.add_tail(1)
    test_queue.add_tail(2)
    test_queue.add_tail(3)
    print(test_queue)
    test_queue.remove_head()
    print(test_queue)
    test_queue.remove_head()
    test_queue.remove_head()
    print(test_queue)

    print()
    print('Queue implementation using collections.deque (TC append() - O(1), TC popleft() - O(1))')
    test_queue = deque()
    print(test_queue)
    test_queue.append(1)
    test_queue.append(2)
    test_queue.append(3)
    print(test_queue)
    test_queue.popleft()
    print(test_queue)
    test_queue.popleft()
    test_queue.popleft()
    print(test_queue)

    print()
    print('Queue implementation using queue.Queue (TC put() - O(1), TC get() - O(1))')
    test_queue = Queue()
    print(test_queue.qsize())
    test_queue.put(1)
    test_queue.put(2)
    test_queue.put(3)
    print(test_queue.qsize())
    test_queue.get()
    print(test_queue.qsize())
    test_queue.get()
    test_queue.get()
    print(test_queue.qsize())

from singly_linked_list import SinglyLinkedList
from collections import deque
from queue import LifoQueue


if __name__ == '__main__':
    print('Stack implementation using Python list (TC append() - O(1), TC pop() - O(1))')
    test_stack = list()
    print(test_stack)
    test_stack.append(1)
    test_stack.append(2)
    test_stack.append(3)
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.pop()
    test_stack.pop()
    print(test_stack)

    print()
    print('Stack implementation using Singly Linked List (TC add_tail() - O(1), TC remove_tail() - O(1))')
    test_stack = SinglyLinkedList()
    print(test_stack)
    test_stack.add_tail(1)
    test_stack.add_tail(2)
    test_stack.add_tail(3)
    print(test_stack)
    test_stack.remove_tail()
    print(test_stack)
    test_stack.remove_tail()
    test_stack.remove_tail()
    print(test_stack)

    print()
    print('Stack implementation using collections.deque (TC append() - O(1), TC pop() - O(1))')
    test_stack = deque()
    print(test_stack)
    test_stack.append(1)
    test_stack.append(2)
    test_stack.append(3)
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.pop()
    test_stack.pop()
    print(test_stack)

    print()
    print('Stack implementation using queue.LifoQueue (TC put() - O(1), TC get() - O(1))')
    test_stack = LifoQueue()
    print(test_stack.qsize())
    test_stack.put(1)
    test_stack.put(2)
    test_stack.put(3)
    print(test_stack.qsize())
    test_stack.get()
    print(test_stack.qsize())
    test_stack.get()
    test_stack.get()
    print(test_stack.qsize())

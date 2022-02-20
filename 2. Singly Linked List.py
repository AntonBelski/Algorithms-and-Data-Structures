class Node:
    def __init__(self, value=None, nexxt=None):
        self.value = value
        self.nexxt = nexxt


class SinglyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __str__(self):
        result = []
        node = self.first

        if node is not None:
            result.append(str(node.value))
            node = node.nexxt
        while node is not None:
            result.append('->')
            result.append(str(node.value))
            node = node.nexxt

        return "[" + ''.join(result) + "]"

    def size(self):
        # returns number of data elements in list
        # Time Complexity - O(1)
        return self.size

    def is_empty(self):
        # bool returns true if empty, Time Complexity - O(1)
        return self.first is None

    def add_head(self, value):
        # adds an item to the head of the list, Time Complexity - O(1)
        node = Node(value)
        self.size += 1
        if self.first is None and self.last is None:
            self.first = node
            self.last = node
        else:
            first = self.first
            self.first = node
            self.first.nexxt = first

    def add_tail(self, value):
        # adds an item at the tail, Time Complexity - O(1)
        node = Node(value)
        self.size += 1
        if self.first is None and self.last is None:
            self.first = node
            self.last = node
        else:
            self.last.nexxt = node
            self.last = node

    def insert(self, index, value):
        # insert value at index, so current item at that index is pointed to by new item at index,Time Complexity - O(n)
        if not 0 <= index < self.size:
            return None

        if index == 0:
            self.add_head(value)
        elif index == self.size - 1:
            self.add_tail(value)
        else:
            self.size += 1
            prev_node = self.first
            index -= 1
            while index:
                prev_node = prev_node.nexxt
                index -= 1
            new_node = Node(value=value, nexxt=prev_node.nexxt)
            prev_node.nexxt = new_node

    def get_head(self):
        # get value of head item, Time Complexity - O(1)
        if self.first is not None:
            return self.first.value
        else:
            return None

    def get_tail(self):
        # get value of tail item, Time Complexity - O(1)
        if self.last is not None:
            return self.last.value
        else:
            return None

    def remove_head(self):
        # remove head item and return its value, Time Complexity - O(1)
        node = self.first
        if self.first is not None:
            self.size -= 1
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.nexxt
        return node

    def remove_tail(self):
        # removes tail item and returns its value, Time Complexity - O(n)
        node = self.last
        if self.last is not None:
            self.size -= 1
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                curr_node = self.first
                while curr_node.nexxt != self.last:
                    curr_node = curr_node.nexxt
                curr_node.nexxt = None
                self.last = curr_node
        return node

    def remove_value(self, value):
        # removes the first item in the list with this value, Time Complexity - O(n)
        if self.first is None:
            return None

        if self.first.value == value:
            self.remove_head()
        elif self.last.value == value:
            self.remove_tail()
        else:
            prev_node = self.first
            while prev_node.nexxt is not None and prev_node.nexxt.value != value:
                prev_node = prev_node.nexxt
            if prev_node.nexxt is not None:
                next_node = prev_node.nexxt.nexxt
                prev_node.nexxt.nexxt = None
                prev_node.nexxt = next_node
                self.size -= 1

    def erase(self, index):
        # removes node at given index, Time Complexity - O(n)
        if not 0 <= index < self.size:
            return None

        if index == 0:
            self.remove_head()
        elif index == self.size - 1:
            self.remove_tail()
        else:
            prev_node = self.first
            index -= 1
            while index:
                prev_node = prev_node.nexxt
                index -= 1
            next_node = prev_node.nexxt.nexxt
            prev_node.nexxt.nexxt = None
            prev_node.nexxt = next_node
            self.size -= 1

    def value_at(self, index):
        # returns the value of the nth item (starting at 0 for first), Time Complexity - O(n)
        if self.first is None or not 0 <= index < self.size:
            return None

        node = self.first
        while index:
            node = node.nexxt
            index -= 1
        return node.value

    def value_n_from_end(self, index_from_end):
        # returns the value of the node at nth position from the end of the list (starts from 0), Time Complexity - O(n)
        if self.first is None or not 0 <= index_from_end < self.size:
            return None

        node = self.first
        index = self.size - 1 - index_from_end
        while index:
            node = node.nexxt
            index -= 1
        return node.value

    def reverse_list(self):
        # reverses the linked list, Time Complexity - O(n)
        if self.size < 2:
            return None

        prev_node = None
        node = self.first
        next_node = self.first.nexxt
        node.nexxt = prev_node
        self.tail = self.first

        while next_node is not None:
            prev_node = node
            node = next_node
            next_node = next_node.nexxt
            node.nexxt = prev_node

        self.first = node


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    print(linked_list)
    linked_list.remove_head()
    linked_list.remove_tail()
    linked_list.remove_value(1)
    linked_list.erase(0)
    linked_list.value_at(1)
    linked_list.value_n_from_end(0)
    print(linked_list.is_empty())
    print(linked_list.size)
    linked_list.add_tail(3)
    linked_list.add_tail(2)
    linked_list.add_tail(1)
    print(linked_list)
    print(linked_list.size)
    print(linked_list.is_empty())
    linked_list.add_head(4)
    linked_list.add_head(5)
    linked_list.add_head(6)
    print(linked_list)
    print(linked_list.value_at(1))
    print(linked_list.value_n_from_end(1))
    print(linked_list.value_at(0))
    print(linked_list.value_n_from_end(0))
    print(linked_list.get_head())
    print(linked_list.get_tail())
    linked_list.insert(1, 5.5)
    print(linked_list)
    linked_list.insert(0, 6.5)
    print(linked_list)
    linked_list.remove_value(5)
    print(linked_list)
    linked_list.erase(1)
    print(linked_list)
    linked_list.reverse_list()
    print(linked_list)

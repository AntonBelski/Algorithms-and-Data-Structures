class Node:
    def __init__(self, value=None, nexxt=None):
        self.value = value
        self.nexxt = nexxt


class SinglyLinkedList:
    # head - (голова) элемент, на которого нет ссылки
    # tail - (хвост) элемент, который ссылается на None
    def __init__(self):
        self.first = None
        self.last = None
        self.length = None

    def __str__(self):
        out = 'empty'
        if self.first is not None:
            current = self.first
            out = str(current.value)
            while current.nexxt is not None:
                current = current.nexxt
                out += ' ' + str(current.value)
        return out

    def clear(self):
        self.__init__()

    def lenn(self):
        len_list = 0
        if self.first is not None:
            len_list += 1
            current = self.first
            while current.nexxt is not None:
                len_list += 1
                current = current.nexxt
        return len_list

    # add
    def add_head(self, value):
        if self.first is None:
            self.first = Node(value=value, nexxt=None)
            self.last = self.first
        else:
            self.first = Node(value=value, nexxt=self.first)

    def add_tail(self, value):
        if self.first is None:
            self.first = Node(value=value, nexxt=None)
            self.last = self.first
        elif self.first == self.last:
            self.last = Node(value=value, nexxt=None)
            self.first.nexxt = self.last
        else:
            new_last = Node(value=value, nexxt=None)
            self.last.nexxt = new_last
            self.last = new_last

    def add(self, value, ind):
        if self.first is None:
            self.first = Node(value=value, nexxt=None)
            self.last = self.first
            return
        if ind == 0:
            self.first = Node(value=value, nexxt=self.first)
            return
        current = self.first
        position = 1
        while current is not None:
            if position == ind:
                current.nexxt = Node(value=value, nexxt=current.nexxt)
                if current.nexxt.nexxt is None:
                    self.last = current.nexxt
                break
            current = current.nexxt
            position += 1


if __name__ == '__main__':
    slist = SinglyLinkedList()
    
from typing import TypeVar, Generic
T = TypeVar('T')

class DLinkedList (Generic [T]):

    def __init__(self):
        self.head = Node (None)
        self.tail = Node (None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front (self, data):
        n = Node[T] (data)
        n.set_prev(self.head)
        self.size += 1

    def add_back (self, data):
        n = Node[T] (data)
        n.set_prev(self.tail.prev)
        self.size += 1

    def remove (self, nPos):
        current = self.head.next
        cont = 0
        while (current.data != None):
            if (cont == nPos):
                current.next.prev = current.prev
                current.prev.next = current.next
                break

            current = current.next
            cont+=1

        self.size -=1

    def set_element (self, nPos, data):
        current = self.head.next
        cont = 0
        while (current.data != None):
            if (cont == nPos):
                current.data = data
                break

            current = current.next
            cont+=1

    def get_element (self, nPos):
        current = self.head.next
        cont = 0
        while (current.data != None):
            if (cont == nPos):
                return current.data

            current = current.next
            cont+=1

    def get_size (self):
        return self.size

    def print (self):
        current = self.head.next
        while (current.data != None):
            print(str(current))
            current = current.next


class Node (Generic [T]):

    def __init__(self, data : T):
        self.next = None
        self.prev = None
        self.data = data

    def set_prev (self, prevNode):
        self.prev = prevNode
        self.next = prevNode.next
        prevNode.next.prev = self
        prevNode.next = self

    def __str__(self):
        return "" + str (self.data)    
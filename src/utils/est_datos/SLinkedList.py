# Creado por JABM
# Creado el 02 de marzo de 2020
# Objetivo: aprender sobre generics, listas y python

from typing import TypeVar, Generic
T = TypeVar('T')

class SLinkedList (Generic [T]):

    def __init__(self):
        self.head = None
        self.size = 0

    def add_first (self, data : T):
        if self.head == None:
            self.head = Node (data)

        else:
            new_node = Node (data)
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def add_last (self, data : T):
        if self.head == None:
            self.head = Node (data)

        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            
            temp.next = Node (data)

        self.size += 1

    def get (self, index : int):
        cont = 0
        temp = self.head
        while temp is not None:
            if cont == index:
                return temp
            temp = temp.next
            cont += 1
        
        return None

    def find (self, data : T):
        cont = 0
        temp = self.head
        while temp is not None:
            if data == temp.data:
                return cont
            temp = temp.next
            cont += 1
        
        return -1

    def delete_node (self, data : T):
        index = self.find (data)

        if index == -1:
            return False
        else:
            if index == 0:
                self.head = self.head.next
            else:
                self.get(index-1).next = self.get(index+1)

            return True

    def delete_from_index (self, index : int):

        if index >= 0 and index <= self.size:
            if index == 0:
                self.head = self.head.next
            else:
                self.get(index-1).next = self.get(index+1)
            
            return True

        else:
            return False

    def update_node (self, index : int, new_data : T):
        if index >= 0 and index <= self.size:
            self.get(index).data = new_data # falta validacion de null
        else:
            print(f"\nIndex {index} no se encunetra dentro del rango [0, {self.size-1}]\n")
        
    def get_size (self):
        return self.size
    
    def display_sll (self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def __str__(self) :
        acum = ""
        temp = self.head
        while temp is not None:
            acum += str(temp.data) + ", "
            temp = temp.next

        return f"[{acum[:len(acum)-2]}]"

    def __iter__(self):
        return LinkedListIterator (self.head)


class Node (Generic [T]):

    def __init__(self, data : T):
        self.data = data
        self.next = None

    def __str__(self):
        return "" + str(self.data)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

if __name__ == '__main__':
    sll = SLinkedList [int] ()
    sll.add_first(12)
    sll.add_first(13)
    sll.add_first(14)
    sll.add_first(15)
    sll.add_last(11)
    sll.add_last(10)
    sll.add_last(9)

    print(sll)

    print("\nfind function")
    print ("find " + str(sll.find(12)))
    print ("find " + str(sll.find(10)))

    print("\nget function")
    print ("get " + str(sll.get(0)))
    print ("get " + str(sll.get(1)))

    print("")
    sll.update_node(0, 300)
    print(sll)

    print("")
    sll.delete_from_index(1)
    sll.delete_node(300)
    print(sll)
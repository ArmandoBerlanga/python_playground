from typing import TypeVar, Generic

E = TypeVar('E')
T = TypeVar('T')

class BinaryTree (Generic [E]):

    def __init__(self):
        self.root = None
        self.size = 0

    def add_node (self, data : E):
        self.root = self.__acom_node(self.root, data)
        self.size += 1

    def __acom_node (self, current, data : E):
        if current == None:
            return Node (data)

        else:
            if current.__gt__(data):
                current.rigth = self.__acom_node(current.rigth, data)
            elif current.__lt__(data):
                current.left = self.__acom_node(current.left, data)
            else:
                return current
                
        return current

    def display_tree (self):
        self.__rec_display(self.root)

    def __rec_display (self, node):
        if node != None:
            print (node.data)
            self.__rec_display(node.left)
            self.__rec_display(node.rigth)

    def get_root (self):
        return self.root

class Node (Generic [T]):

    def __init__(self, data : T):
        self.rigth = None
        self.left = None
        self.data = data    
        
    def __gt__ (self, data : T):
        return self.data < data

    def __lt__ (self, data : T):
        return self.data > data
import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)
# sys.path.append("/Users/armandoberlanga/VSC-workspace/python_playground/src")

from utils.LinkedList import DLinkedList

ll = DLinkedList[str] ()

ll.add_back("vaca")
ll.add_back("gato")
ll.add_back("perro")
ll.add_back("delfin")
ll.add_back("cerdito")
ll.add_back("mamut")

# print("\nLista de animales\n")
# ll.print()
# print("\nSize: " + str(ll.size))

# print("\nNueva lista de animales\n")
# ll.remove(3)
# ll.print()
# print("\nNew size: " + str(ll.size))

ll.get_element(2)
ll.set_element(2, "oso")
ll.print()



import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.SLinkedList import SLinkedList
from utils.Fecha import Fecha

sll = SLinkedList [Fecha] ()
sll.add_first (Fecha (12, 12, 2020))
sll.add_first (Fecha (11, 11, 2020))
sll.add_first (Fecha (12, 9, 2019))

print("\nFechas en forma de lista compacta")
print(sll)

print("\nFechas en forma de lista iterable")
for s in sll:
    print(s)
    
print("")
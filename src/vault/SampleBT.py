import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.BinaryTree import BinaryTree

bt = BinaryTree [int] ()
bt.add_node(12)
bt.add_node(90)
bt.add_node(11)
bt.add_node(97)
bt.add_node(10)
bt.add_node(9)

bt.display_tree()
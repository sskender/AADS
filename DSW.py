import math
from SimpleBinaryTree import SimpleBinaryTree


def DSW_rotates(tree: SimpleBinaryTree, rcount):
    node, A = tree.root, None
    while rcount > 0:
        A1 = node.R
        node.leftrotate(tree)
        rcount -= 1
        A = A1
        node = A.R


def DSW(tree: SimpleBinaryTree, n: int):
    if tree.root is None:
        return None

    tree.rightbackbone()

    h = math.ceil(math.log2(n+1))  # height of tree
    i = 2**(h-1) - 1  # number of internal nodes

    DSW_rotates(tree, n-i)  # makes one leaf on the left side

    while i > 1:
        i = math.floor(i / 2)
        DSW_rotates(tree, i)

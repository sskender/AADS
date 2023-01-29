from SimpleBinaryTree import Node

def createBalBT(vs):
    n = len(vs)
    if n > 0:
        i = (n // 2) + (n % 2)
        root = Node(vs[i-1])
        root.setLeftChild(createBalBT(vs[0:i-1]))
        root.setRightChild(createBalBT(vs[i:n]))
        return root
    else:
        return None

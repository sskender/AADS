from SimpleBinaryTree import SimpleBinaryTree


class AVLTree(SimpleBinaryTree):

    def updateHeights(self, lst):
        for n in lst:
            n.updateHeight()

    def AVLDetectRotate(self, n):
        if n.balance_factor() == 2:
            n1 = n.R
            n1bf = n1.balance_factor()
            if n1 is not None and n1bf in [0, 1]:
                n.leftrotate(self)
                self.updateHeights([n, n1])
            elif n1 is not None and n1bf == -1:
                n1.rightrotate(self)
                n.leftrotate(self)
                self.updateHeights([n1, n, n.P])
        else:
            n1 = n.L
            n1bf = n1.balance_factor()
            if n1 is not None and n1bf in [0, -1]:
                n.rightrotate(self)
                self.updateHeights([n, n1])
            elif n1 is not None and n1bf == 1:
                n1.leftrotate(self)
                n.rightrotate(self)
                self.updateHeights([n, n1, n.P])

    def AVLBalance(self, n):
        n.updateHeight()
        p = n.P
        if n.balance_factor() in [-2, 2]:
            self.AVLDetectRotate(n)
        if p is not None:
            self.AVLBalance(n)

    def insert(self, value):
        n = super().insert(value)
        if n is not None:
            # rebalance if the new node is not the only node
            # only node is if it does not have a parent
            self.AVLBalance(n)

    def remove(self, value):
        n = super().remove(value)
        if n is not None:
            # rebalance if the removed node is not the only node
            # only node is if it does not have a parent
            self.AVLBalance(n)

class Node:

    S = None  # value
    L, R, P = None, None, None  # pointers
    h = 1  # initial height

    def __init__(self, value):
        self.S = value

    def setLeftChild(self, node):
        self.L = node
        if node is not None:
            self.P = self

    def setRightChild(self, node):
        self.R = node
        if node is not None:
            self.P = self

    def toRoot(self):
        self.P = None
        return self

    def query(self, value):
        ''' Get pointer to value or the end of tree '''
        if value < self.S and self.L is not None:  # go left
            return self.L.query(value)
        elif value > self.S and self.R is not None:  # go right
            return self.R.query(value)
        else:
            return self  # it is me

    def insert(self, value):
        ''' Returns parent of the new node '''
        n = self.query(value)
        if value < n.S:
            n.setLeftChild(Node(value))
        elif value > n.S:
            n.setRightChild(Node(value))
        else:
            raise Exception('cannot insert duplicate')
        return n

    def children(self):
        c = 0
        if self.L is not None:
            c += 1
        if self.R is not None:
            c += 1
        return c

    def rightmost(self):
        if self.R is not None:
            return self.R.rightmost()
        else:
            return self

    def leftmost(self):
        if self.L is not None:
            return self.L.leftmost()
        else:
            return self

    def rightrotate(self, tree):
        # self is pointer to B
        C = self.L  # bottom of rotation
        if C is None:
            return None
        A = self.P  # parent of top rotation
        if A is not None:
            if A.L is self:
                A.setLeftChild(C)
            if A.R is self:
                A.setRightChild(C)
        else:
            tree.root = C.toRoot()
        t = C.R
        C.setRightChild(self)
        self.setLeftChild(t)

    def leftrotate(self, tree):
        C = self.R
        if C is None:
            return None
        A = self.P
        if A is not None:
            if A.L is self:
                A.setLeftChild(C)
            if A.R is self:
                A.setRightChild(C)
        else:
            tree.root = C.toRoot()
            t = C.L
            C.setLeftChild(self)
            self.setRightChild(t)

    def updateHeight(self):
        left_h, right_h = 0, 0
        if self.L is not None:
            left_h = self.L.h
        if self.R is not None:
            right_h = self.R.h
        self.h = 1 + max(left_h, right_h)

    def balance_factor(self):
        ''' Get balance factor BF(S) '''
        left_h, right_h = 0, 0
        if self.L is not None:
            left_h = self.L.h
        if self.R is not None:
            right_h = self.R.h
        return right_h - left_h



class SimpleBinaryTree:

    root = None

    def query(self, value):
        if self.root is None:
            return None
        else:
            n = self.root.query(value)  # n could be actual value or the end of tree
            if n.S == value:
                return n
            else:
                return None

    def insert(self, value):
        ''' Returns parent  of inserted node with value '''
        if self.root is None:
            self.root = Node(value)
            return None  # return parent
        else:
            return self.root.insert(value)  # return parent

    def remove(self, value):
        if self.root is None:
            return None
        n = self.root.query(value)  # i am the node n
        fp = n.P  # parent
        c = n.children()

        #
        # case 1 - no children
        #

        # just null pointer
        if n.P is None and c == 0:
            self.root = None

        # no children = leaf
        elif n.P is not None and c == 0:
            # i am the child with desired value
            # which child am i
            if n.P.L is n:
                # this is me, the left child, delete me
                n.p.setLeftChild(None)
            elif n.P.R is n:
                # this is me, the right child, delete me
                n.p.setRightChild(None)

        #
        # case 2 - one child
        #

        elif n.P is None and c == 1:
            # left child is now root
            if n.L is not None:
                self.root = n.L.toRoot()
            # right child is now root
            elif n.R is not None:
                self.root = n.R.toRoot()

        elif n.P is not None and c == 1:
            if n.P.L is n:  # i am the left child of my parent
                if n.L is not None:  # i have the left child
                    n.p.setLeftChild(n.L)
                elif n.R is not None:  # i have the right child
                    n.p.setLeftChild(n.R)
            elif n.p.R is n:  # i am the right child of my parent
                if n.L is not None:  # i have the left child (becomes me)
                    n.p.setRightChild(n.L)
                if n.R is not None:  # i have the right child (becomes me)
                    n.p.setRightChild(n.R)

        #
        # case 3 - two children
        #

        # remove by copy
        # predcessor = prethodnik = left child, in, the most right
        # sucessor = sljedbenik = right child, in, the most left
        elif c == 2:
            pred = n.L.rightmost()
            value = pred.S
            fp = self.remove(pred.S)
            n.S = value
        return fp

    def rightbackbone(self):
        B = self.root
        while B is not None:
            C = B.L
            if C is not None:
                B.rightrotate(self)
                B = C
            else:  # go to right while left child does not exist
                B = B.R

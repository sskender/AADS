from typing import Optional, Callable


class Node:
    """
    Class representing a single node in the BinaryTree.

    ...

    Attributes
    ----------

    value : int
        value contained in the node
    parent : Node, optional
        parent of the node, also a Node (or None)
    left : Node, optional
        left child of the node, also a Node object (or None)
    right : Node, optional
        right child of the node, also a Node object (or None)
    """

    def __init__(self, value: int) -> None:
        """
        Create a new node with the assigned value.
        The parent of the node is initialized to None, as well as the chidlren of the node.
        """
        self.value = value
        self.parent = self.right = self.left = None

    def set_left_child(self, node: Optional['Node']) -> None:
        """
        Sets the left child of self to the given node and sets the given node's parent to self (if the node is not None).

        Args:
            node (Node, optional): the node to set as the child
        """
        self.left = node
        if node is not None:
            node.parent = self

    def set_right_child(self, node: Optional['Node']) -> None:
        """
        Sets the right child of self to the given node and sets the given node's parent to self (if the node is not None).

        Args:
            node (Node, optional): the node to set as the child
        """
        self.right = node
        if node is not None:
            node.parent = self

    def __repr__(self) -> str:
        """
        Get the string representation of the Node.

        Returns:
            str: A string representation which can create the Node object.
        """
        return f'Node({self.value})'


class BinaryTree:
    """
    Class repreesenting a binary tree, consisting of Nodes.

    ...

    Attributes
    ----------
    root : Node, optional
        the root node of the BinaryTree of type Node (or None)
    """

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root = root

    def set_root(self, node: Optional[Node]) -> None:
        """
        Set the root of the tree to the provided node and set the node's parent to None (if the node is not None).

        Args:
            node (Node, optional): The Node object to set as the root (whose parent is set to None)
        """
        self.root = node
        if self.root is not None:
            self.root.parent = None

    def _rotate_impl(self,
                     rotatee: Optional[Node],
                     rotator: Optional[Node],
                     rotate_children: Callable[[Node, Node], None]) -> None:
        """
        Private helper method for implementing rotations.
        Accepts the rotatee and rotator Nodes which are used for the rotation and the rotation-specific
        'rotate_children' function which swaps the children of the rotatee and rotator as appropriate for the rotation.

        Args:
            rotatee (Node, optional): The node around which we rotate (parent).
            rotator (Node, optional): The node with which we rotate around the rotatee (child).
            rotate_children (Callable(Node, Node)): A callable which does the actual rotation by swapping nodes.
        """
        if rotatee is None or rotator is None or rotate_children is None:
            return
        parent = rotatee.parent
        if parent is None:
            self.set_root(rotator)
        else:
            if parent.left is rotatee:
                parent.set_left_child(rotator)
            else:
                parent.set_right_child(rotator)
        rotate_children(rotatee, rotator)

    @staticmethod
    def _left_rotate_children(rotatee: Node, rotator: Node) -> None:
        """
        Private static helper method for swapping the children of the rotatee and rotator.
        Specifically for left rotation.

        Args:
            rotatee (Node, optional): The node around which we rotate (parent).
            rotator (Node, optional): The node with which we rotate around the rotatee (child).
        """
        temp = rotator.left
        rotator.set_left_child(rotatee)
        rotatee.set_right_child(temp)

    @staticmethod
    def _right_rotate_children(rotatee: Node, rotator: Node) -> None:
        """
        Private static helper method for swapping the children of the rotatee and rotator.
        Specifically for right rotation.

        Args:
            rotatee (Node, optional): The node around which we rotate (parent).
            rotator (Node, optional): The node with which we rotate around the rotatee (child).

        """
        temp = rotator.right
        rotator.set_right_child(rotatee)
        rotatee.set_left_child(temp)

    def left_rotate(self, node: Optional[Node]) -> None:
        """
        Do a left rotation on the specified node.

        Args:
            node (Node, optional): The node around which we rotate (parent).
        """
        self._rotate_impl(node, node.right, BinaryTree._left_rotate_children)

    def right_rotate(self, node: Optional[Node]) -> None:
        """
        Do a right rotation on the specified node.

        Args:
            node (Node, optional): The node around which we rotate (parent).
        """
        self._rotate_impl(node, node.left, BinaryTree._right_rotate_children)


def left_backbone(tree: BinaryTree) -> None:
    """
    Turns the given BinaryTree object (tree) to a left backbone tree.

    Args:
        tree (BinaryTree): The tree to degenerate.

    """
    # TODO: Implement the degeneration to a left backbone
    B = tree.root
    while B is not None:
        C = B.R
        if C is not None:
            B.left_rotate(C)
            B = C
        else:
            B = B.L

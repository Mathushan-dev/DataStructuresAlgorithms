class Node:
    def __init__(self, key):
        """
        Initialize a new node with a given key.

        Args:
        - key: The value of the node.
        """
        self.value = key
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    def is_empty(self):
        """
        Check if the binary search tree is empty.

        Returns:
        - bool: True if the tree is empty, False otherwise.
        """
        return self.root is None

    def insert(self, key):
        """
        Insert a new key into the binary search tree.

        Args:
        - key: The value to be inserted.
        """
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        """
        Insert a new key into the binary search tree.

        Args:
        - key: The value to be inserted.
        """
        if root is None:
            return Node(key)
        if key > root.value:
            root.right = self._insert(root.right, key)
        if key < root.value:
            root.left = self._insert(root.left, key)

        return root

    def delete(self, key):
        """
        Delete a key from the binary search tree.

        Args:
        - key: The value to be deleted.
        """
        pass

    def search(self, key):
        """
        Search for a key in the binary search tree.

        Args:
        - key: The value to be searched.

        Returns:
        - bool: True if the key is found, False otherwise.
        """
        pass

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary search tree.

        Returns:
        - list: A list containing the elements of the tree in ascending order.
        """
        pass

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the binary search tree.

        Returns:
        - list: A list containing the elements of the tree in preorder.
        """
        pass

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the binary search tree.

        Returns:
        - list: A list containing the elements of the tree in postorder.
        """
        pass

    def find_min(self):
        """
        Find the minimum key in the binary search tree.

        Returns:
        - int: The minimum key.
        """
        pass

    def find_max(self):
        """
        Find the maximum key in the binary search tree.

        Returns:
        - int: The maximum key.
        """
        pass

    def inorder_traversalb(self):
        result = []
        self._inorder_traversalb(self.root, result)
        return result

    def _inorder_traversalb(self, root, result):
        if root:
            self._inorder_traversalb(root.left, result)
            result.append(root.value)
            self._inorder_traversalb(root.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(8)
    bst.insert(11)
    bst.insert(1)
    bst.insert(-7)
    print("Inorder Traversal:", bst.inorder_traversalb())

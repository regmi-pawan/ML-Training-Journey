class Node:
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.value = key  # Value of the node

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Root of the BST

    # Insertion operation: Insert a node in the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    # Helper function for recursive insertion
    def _insert_recursive(self, root, key):
        # If the key is smaller than root, go to the left subtree
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        # If the key is larger than root, go to the right subtree
        elif key > root.value:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    # Search operation: Search for a value in the BST
    def search(self, key):
        return self._search_recursive(self.root, key)

    # Helper function for recursive search
    def _search_recursive(self, root, key):
        if root is None or root.value == key:
            return root

        if key < root.value:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    # In-order traversal of the BST
    def inorder(self):
        return self._inorder_recursive(self.root)

    # Helper function for recursive in-order traversal
    def _inorder_recursive(self, root):
        if root is None:
            return []
        # Left subtree -> Root -> Right subtree
        return self._inorder_recursive(root.left) + [root.value] + self._inorder_recursive(root.right)

# Example usage
def main():
    bst = BinarySearchTree()

    # Insert nodes into the BST
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("In-order traversal of the BST:", bst.inorder())

    # Search for a value in the BST
    key = 40
    result = bst.search(key)
    if result:
        print(f"Node with value {key} found in the BST.")
    else:
        print(f"Node with value {key} not found in the BST.")

    key = 100
    result = bst.search(key)
    if result:
        print(f"Node with value {key} found in the BST.")
    else:
        print(f"Node with value {key} not found in the BST.")

if __name__ == "__main__":
    main()

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1  # Height of node (initially 1)

class AVLTree:
    def __init__(self):
        self.root = None

    # Function to get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Function to get the balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        
        # Return the new root
        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        # Return the new root
        return y

    # Insert a node in the AVL Tree
    def insert(self, root, key):
        if not root:
            return Node(key)
        
        # Perform normal BST insertion
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Update height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor of this node to check whether this node became unbalanced
        balance = self.get_balance(root)

        # If this node becomes unbalanced, then there are 4 cases to consider

        # Left Left Case (Right rotation)
        if balance > 1 and key < root.left.value:
            return self.right_rotate(root)

        # Right Right Case (Left rotation)
        if balance < -1 and key > root.right.value:
            return self.left_rotate(root)

        # Left Right Case (Left rotation followed by Right rotation)
        if balance > 1 and key > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case (Right rotation followed by Left rotation)
        if balance < -1 and key < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (unchanged) node pointer
        return root

    # Function to perform an in-order traversal of the AVL tree
    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []

    # Public method to insert a node and update root
    def insert_root(self, key):
        self.root = self.insert(self.root, key)

    # Public method to get the in-order traversal of the tree
    def get_inorder(self):
        return self.inorder(self.root)

    # Function to search a key in the AVL tree
    def search(self, root, key):
        # Base case: root is null or key is present at root
        if root is None or root.value == key:
            return root

        # Key is greater than root's key, search in the right subtree
        if root.value < key:
            return self.search(root.right, key)

        # Key is smaller, search in the left subtree
        return self.search(root.left, key)

    # Public method to search for a key in the AVL tree
    def search_key(self, key):
        result = self.search(self.root, key)
        if result:
            return f"Node with value {key} found in the AVL tree."
        else:
            return f"Node with value {key} not found in the AVL tree."

# Example usage
def main():
    avl = AVLTree()

    # Insert nodes into the AVL Tree
    avl.insert_root(30)
    avl.insert_root(20)
    avl.insert_root(40)
    avl.insert_root(10)
    avl.insert_root(25)
    avl.insert_root(50)
    avl.insert_root(5)

    # In-order traversal (should print the sorted elements)
    print("In-order traversal of the AVL tree:", avl.get_inorder())

    # Search for a value
    print(avl.search_key(25))  # Found
    print(avl.search_key(60))  # Not Found

if __name__ == "__main__":
    main()

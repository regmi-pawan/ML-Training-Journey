class Node:
    def __init__(self, value):
        self.value = value  # The data value
        self.next = None  # Pointer to the next node (initially None)
        self.prev = None  # Pointer to the previous node (initially None)

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # The list starts empty

    # Insert a new node at the end of the list
    def insert(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty, the new node becomes the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Set the next of the last node to the new node
            new_node.prev = current  # Set the previous of the new node to the current last node

    # Delete the first occurrence of a node with the given value
    def delete(self, value):
        if self.head is None:  # If the list is empty, nothing to delete
            print("List is empty!")
            return

        # If the node to be deleted is the head
        if self.head.value == value:
            if self.head.next:  # If there is more than one node
                self.head = self.head.next
                self.head.prev = None
            else:  # Only one node in the list
                self.head = None
            return

        current = self.head
        while current:
            if current.value == value:
                # If the node to be deleted is not the head
                if current.next:  # If it is not the last node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:  # If it is the last node
                    current.prev.next = None
                return
            current = current.next

        print(f"Value {value} not found in the list.")

    # Search for a value in the list
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # Traverse and print the list from head to tail
    def traverse_forward(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.value, end=" <-> " if current.next else "\n")
            current = current.next

    # Traverse and print the list from tail to head
    def traverse_backward(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        
        # Go to the last node
        while current.next:
            current = current.next
        
        # Traverse backward from the last node
        while current:
            print(current.value, end=" <-> " if current.prev else "\n")
            current = current.prev

# Example usage
def main():
    dll = DoublyLinkedList()

    # Insert nodes into the doubly linked list
    dll.insert(10)
    dll.insert(20)
    dll.insert(30)
    dll.insert(40)
    dll.insert(50)
    
    print("Linked List (Forward Traversal):")
    dll.traverse_forward()

    print("Linked List (Backward Traversal):")
    dll.traverse_backward()

    # Search for an element
    value_to_search = 30
    if dll.search(value_to_search):
        print(f"Value {value_to_search} found in the list.")
    else:
        print(f"Value {value_to_search} not found in the list.")

    # Delete an element
    dll.delete(20)
    print("Linked List (After Deleting 20):")
    dll.traverse_forward()

    # Try deleting a non-existent value
    dll.delete(100)

if __name__ == "__main__":
    main()

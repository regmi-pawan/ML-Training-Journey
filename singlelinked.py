class Node:
    def __init__(self, value):
        self.value = value  # Store the value
        self.next = None  # Pointer to the next node (initially None)

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Insert a new node at the end of the list
    def insert(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Insert the new node at the end

    # Delete the first occurrence of a value
    def delete(self, value):
        if self.head is None:  # If the list is empty, nothing to delete
            print("List is empty!")
            return
        
        # If the node to be deleted is the head node
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:  # Traverse the list to find the node
            if current.next.value == value:
                current.next = current.next.next  # Skip the node to be deleted
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

    # Traverse and print the list
    def traverse(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.value, end=" -> " if current.next else "\n")
            current = current.next

# Example usage
def main():
    sll = SinglyLinkedList()

    # Insert elements into the linked list
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)
    sll.insert(40)
    
    print("Linked List after insertion:")
    sll.traverse()

    # Search for an element
    value_to_search = 30
    if sll.search(value_to_search):
        print(f"Value {value_to_search} found in the list.")
    else:
        print(f"Value {value_to_search} not found in the list.")
    
    # Delete an element
    sll.delete(20)
    print("Linked List after deleting value 20:")
    sll.traverse()

    # Try deleting a non-existent value
    sll.delete(100)

if __name__ == "__main__":
    main()

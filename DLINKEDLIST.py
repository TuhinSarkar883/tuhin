class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                # Node to be deleted is head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                # Node to be deleted is last node
                elif temp.next is None:
                    temp.prev.next = None
                # Node to be deleted is in the middle
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print("Node not found!")

    # Traverse forward
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Traverse backward
    def display_backward(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()

print("Deleting 20...")
dll.delete(20)
dll.display_forward()

# Add the Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Add the Stack class
class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    # Add the PUSH method
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    # Adding the POP method
    def pop(self):
        if self.is_empty():
            return

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
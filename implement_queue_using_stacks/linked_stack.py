"""Linked stack"""

class Node:
    """Just a node that will be used in linked stack later"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedStack:
    """Linked stack"""
    def __init__(self):
        self.head = None

    def push(self, item):
        """Add an element to heap"""
        self.head = Node(item, self.head)

    def pop(self):
        """Return and remove an element from stack's heap"""
        if not self.head:
            raise IndexError("pop from empty stack")
        head = self.head
        self.head = self.head.next
        return head.value

    def peek(self):
        """Returns an element from heap"""
        if not self.head:
            raise IndexError("peek from empty stack")
        return self.head.value

    def is_empty(self):
        """Returns whether it's empty or not"""
        return not self.head

    def __iter__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.next

        return iter(nodes[::-1])

if __name__ == '__main__':
    linked_list = LinkedStack()
    linked_list.push(1)
    linked_list.push(2)

    for i in linked_list:
        print(i)

    print(linked_list.pop())
    print(linked_list.pop())

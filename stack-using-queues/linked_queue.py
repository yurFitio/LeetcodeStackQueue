"""Linked queue"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        if not self.tail:
            self.head = Node(item)
            self.tail = self.head
            return
        self.head.next = Node(item)
        self.head = self.head.next

    def peek(self):
        if not self.tail:
            raise IndexError("peek from empty queue")
        return self.tail.value

    def pop(self):
        if not self.tail:
            raise IndexError("pop from empty queue")
        item = self.tail.value
        self.tail = self.tail.next
        if not self.tail:
            self.head = None
        return item

    def is_empty(self):
        return not self.tail


if __name__ == '__main__':
    a = LinkedQueue()
    for i in range(3):
        a.push(i)
    print(a.peek())
    for i in range(3):
        print(a.pop())
    try:
        a.peek()
    except IndexError as e:
        print(e)

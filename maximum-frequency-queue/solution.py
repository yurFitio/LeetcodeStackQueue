class Node:
    """Just a node"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.amount = 1
        self.next = next_node

    # def __repr__(self):
    #     return f"Value: {self.value}, amount: {self.amount}, next: {self.next}"

class FreqStack:
    """constructs an empty frequency stack."""
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        """pushes an integer val onto the top of the stack"""
        current = self.head
        self.head = Node(val, self.head)
        while current:
            if current.value == self.head.value:
                self.head.amount += current.amount
                break
            current = current.next

    def pop(self) -> int:
        """removes and returns the most frequent element in the stack. """
        if not self.head:
            raise IndexError
        previous, node_max = None, self.head
        current = self.head
        while current.next:
            if current.next.amount > node_max.amount:
                node_max = current.next
                previous = current
            current = current.next
        if previous:
            previous.next = previous.next.next
        else:
            self.head = self.head.next
        return node_max.value

# Your FreqStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = FreqStack()
    for i in [5, 7, 5, 7, 4, 5]:
        obj.push(i)
    while True:
        print(obj.pop())

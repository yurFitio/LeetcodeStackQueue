"""Frequency stack"""

from collections import defaultdict

class Node:
    """Just a node"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.amount = 1
        self.next = next_node

class FreqStack:
    """constructs an empty frequency stack."""
    def __init__(self):
        self.head = None
        self.nodes_counter = defaultdict(int)

    def push(self, val: int) -> None:
        """pushes an integer val onto the top of the stack"""
        self.head = Node(val, self.head)
        self.nodes_counter[val] += 1
        self.head.amount = self.nodes_counter[val]

    def pop(self) -> int:
        """removes and returns the most frequent element in the stack. """
        if not self.head:
            raise IndexError
        max_num = max(self.nodes_counter.values())
        if self.head.amount == max_num:
            it = self.head.value
            self.head = self.head.next
            self.nodes_counter[it] -= 1
            return it
        current = self.head
        while current.next:
            if current.next.amount == max_num:
                it = current.next.value
                current.next = current.next.next
                self.nodes_counter[it] -= 1
                return it
            current = current.next
        return None

# Your FreqStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = FreqStack()
    for i in [5, 7, 5, 7, 4, 5]:
        obj.push(i)
    for _ in range(6):
        print(obj.pop())

    try:
        print(obj.pop())
    except IndexError:
        print("Tests passed!")

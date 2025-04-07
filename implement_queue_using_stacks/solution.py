"""Queue implemented with stack structure"""

from linked_stack import LinkedStack

class MyQueue:
    """Queue strcture organized with two stacks."""
    def __init__(self):
        self.stack_in = LinkedStack()
        self.stack_out = LinkedStack()

    def push(self, x: int) -> None:
        """Enqueue an element."""
        self.stack_in.push(x)

    def pop(self) -> int:
        """Pops an element from the end"""
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
            if self.stack_out.is_empty():
                raise ValueError("Pop from empty queue")
        return self.stack_out.pop()


    def peek(self) -> int:
        """Returns the element at the front of the queue."""
        if self.stack_out:
            return self.stack_out.peek()
        if self.stack_in.is_empty():
            raise ValueError("peek from empty queue")
        return self.stack_in.peek()

    def empty(self) -> bool:
        """Returns whether it's empty"""
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:

if __name__ == '__main__':
    obj = MyQueue()
    for i in range(2):
        obj.push(i)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)
    try:
        obj.pop()
        obj.peek()
    except IndexError:
        print("Error detected")

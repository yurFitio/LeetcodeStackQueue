"""Stack using queue"""

from linked_queue import LinkedQueue
class MyStack:
    """Stack implemented using queue"""
    def __init__(self):
        self.queue_in = LinkedQueue()
        self.queue_an = LinkedQueue()

    def push(self, x: int) -> None:
        """Pushes element x to the top of the stack."""
        self.queue_an.push(x)
        while not self.queue_in.is_empty():
            self.queue_an.push(self.queue_in.pop())
        self.queue_in, self.queue_an = self.queue_an, self.queue_in

    def pop(self) -> int:
        """Removes the element on the top of the stack and returns it."""
        return self.queue_in.pop()

    def top(self) -> int:
        """Returns the element on the top of the stack."""
        return self.queue_in.peek()

    def empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return self.queue_in.is_empty()


if __name__ == '__main__':
    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    for i in range(5):
        obj.push(i)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())
    for i in range(4):
        print(obj.pop())

    try:
        obj.pop()
    except IndexError as e:
        print(e)

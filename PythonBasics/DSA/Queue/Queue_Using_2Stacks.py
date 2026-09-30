

class MyQueue:

    def __init__(self):
        #initializing st1 and st2.
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:

        # Move all elements to st2
        while self.st1:
            self.st2.append(self.st1.pop())

        # Add new element
        self.st1.append(x)

        # Move everything back to st1
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:

        if not self.st1:
            return -1

        # Remove the front element
        return self.st1.pop()

    def peek(self) -> int:

        if not self.st1:
            return -1

        # Last element is the front
        return self.st1[-1]

    def empty(self) -> bool:

        # True if queue is empty
        return not self.st1

    def traversal(self):
        if not self.st1:
            print('Stack is empty')
            return

        # Print Queue from front to rear
        for i in range(len(self.st1) - 1, -1, -1):
          print(self.st1[i], end=" ")

        return

q=MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.traversal()        


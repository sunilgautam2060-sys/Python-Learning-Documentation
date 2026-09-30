

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):

        # Add new element at the top
        self.stack.insert(0, data)

    def pop(self):

        if len(self.stack) == 0:
            return "Stack is empty"

        # Remove and return top element
        return self.stack.pop(0)

    def peek(self):

        if len(self.stack) == 0:
            return "Stack is empty"

        # Top element is at index 0
        return self.stack[0]

    def is_empty(self):

        # Check whether stack is empty
        return len(self.stack) == 0

    def size(self):

        # Return number of elements
        return len(self.stack)

    def traversal(self):

        if len(self.stack) == 0:
            print("Stack is empty")
            return

        print("Top -> Down:")

        #printing the stack.
        for i in range(len(self.stack)):
            print(self.stack[i],end=" ")

        return



s = Stack()

s.push(5)
s.push(6)
s.push(7)
s.push(8)

s.traversal()

print()
print("Top:", s.peek())
print("Size:", s.size())
print("Pop:", s.pop())
print("Top:", s.peek())
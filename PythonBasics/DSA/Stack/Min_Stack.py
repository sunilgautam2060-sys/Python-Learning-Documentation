class MinStack:

    def __init__(self):
        # Each item: [actual value, minimum so far]
        self.stack = []

    def push(self, value: int) -> None:

        if len(self.stack) == 0:

            # First value is also the minimum
            self.stack.append([value, value])

        else:

            # Compare current value with previous minimum
            minimum = min(self.stack[-1][1], value)

            # Store value and minimum together
            self.stack.append([value, minimum])

    def pop(self) -> None:

        # Remove the top element
        self.stack.pop()

    def top(self) -> int:

        # [0] = actual value
        return self.stack[-1][0]

    def getMin(self) -> int:

        # [1] = minimum value so far
        return self.stack[-1][1]

s=MinStack()
s.push(5)
s.push(7)
s.push(10)
s.push(1)
s.push(0)
print(s.getMin())

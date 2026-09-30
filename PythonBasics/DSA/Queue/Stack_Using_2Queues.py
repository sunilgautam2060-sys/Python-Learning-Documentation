

class MyStack:

    def __init__(self):
        #initializing q1 and q2.
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:

        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.pop(0))

        # Put new element first
        self.q1.append(x)

        # Move everything back to q1
        while self.q2:
            self.q1.append(self.q2.pop(0))

    def pop(self) -> int:

        if not self.q1:
            return -1

        # Top of stack is at index 0
        return self.q1.pop(0)

    def top(self) -> int:

        if not self.q1:
            return -1

        # First element is the top
        return self.q1[0]

    def empty(self) -> bool:

        return not self.q1

    def traversal(self):
        if not self.q1:
          print('empty queue')
          return
        
        print(self.q1,end="")
         

s=MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.traversal()

    
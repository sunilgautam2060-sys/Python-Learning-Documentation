

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):

        # Add new element at the rear
        self.queue.append(data)

    def dequeue(self):

        if len(self.queue) == 0:
            return "Queue is empty"

        # Remove the front element
        return self.queue.pop(0)

    def peek(self):

        if len(self.queue) == 0:
            return "Queue is empty"

        # Front element is at index 0
        return self.queue[0]

    def is_empty(self):

        # Check whether queue is empty
        return len(self.queue) == 0

    def size(self):

        # Return number of elements
        return len(self.queue)

    def traversal(self):

        if len(self.queue) == 0:
            print("Queue is empty")
            return

        print("Front -> Rear:")

        for i in range(len(self.queue)):
            print(self.queue[i], end=" ")


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.traversal()

print()
print("Front:", q.peek())
print("Size:", q.size())
print("Dequeue:", q.dequeue())

print("After Dequeue:")
q.traversal()
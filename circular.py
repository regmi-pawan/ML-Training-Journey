class CircularQueue:
    def __init__(self, size):
        # Initialize the queue with a given size
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None
        self.front = self.rear = -1  # Indices for the front and rear of the queue

    def is_empty(self):
        # Check if the queue is empty
        return self.front == -1

    def is_full(self):
        # Check if the queue is full
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
        else:
            if self.front == -1:  # If the queue is empty
                self.front = 0
            self.rear = (self.rear + 1) % self.size  # Circular increment
            self.queue[self.rear] = item
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
        else:
            dequeued_item = self.queue[self.front]
            if self.front == self.rear:  # Only one element in the queue
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size  # Circular increment
            print(f"Dequeued: {dequeued_item}")
            return dequeued_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print(f"Front element: {self.queue[self.front]}")

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            i = self.front
            print("Queue elements: ", end="")
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[self.rear])


# Example Usage
queue = CircularQueue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)  # Should print "Queue is full!"

queue.display()

queue.dequeue()
queue.dequeue()

queue.display()

queue.enqueue(60)
queue.enqueue(70)

queue.display()

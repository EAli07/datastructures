class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


my_queue = Queue()
my_queue.enqueue(3)
my_queue.enqueue(2)
my_queue.enqueue(1)

print(my_queue.queue) # work on making the queue print from 1-3 not 3-1
print("Queue size:", my_queue.size()) 

print("Dequeue:", my_queue.dequeue())  
print("Dequeue:", my_queue.dequeue()) 

print("Queue size:", my_queue.size())
print("Is empty?", my_queue.is_empty())
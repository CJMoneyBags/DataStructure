```python
class ErrorHandling:


    def __init__(self):
        self.queue = []

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):

        if len(self.queue) == 0:
            print("The queue is empty.")
            return None
        high_priority = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_priority].priority:
                high_priority = index

        value = self.queue[high_priority].value
        del self.queue[high_priority]
        return value

    def __len__(self):

        return len(self.queue)

class Node:
     def __init__(self, value, priority):
        self.value = value
        self.priority = priority

CRITCAL = 3
IMPORTANT = 2
INFORMATION = 1
Error = ErrorHandling()
Error.enqueue("Sensor 1 Blocked", CRITCAL)
Error.enqueue("Front gate open", IMPORTANT)
Error.enqueue("packing complete", INFORMATION)
Error.enqueue("Critical Error", CRITCAL)

while len(Error) > 0:
   print(Error.dequeue())
```
[back](Queue.md)

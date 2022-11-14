# Queue

## Introduction to the Queue data structure
A queue is a data structure that follows the First In First Out manner. This is just like the lines we are all used to being in for things like the store, to buy a ticket, or to even take your turn at the drinking fountain.

There is a person in the 'Front' of the queue and then another person lines up behind him and so forth. When the person in front is served that is called a **Dequeue** and when someone goes into the line that is called **Enqueue**. A queue will also have functions to tell if it is **Empty** or the **Size** of the queue.

![A picture of a Queue](Queue.png)


## How to write a Queues
```python
class Queue:
  def __init__(self):
    self.queue = [] # start with empty Queue

  def enqueue(self, value):
    self.queue.append(value) # Be sure to use .append() and not .insert or you will start making a Stack (a different data structure)

  def dequeue(self):
    value = self.queue[0] # Get the value of the first item
    del self.queue[0] # Get rid of first item
    return value # return that value (Remember this is a FIFO type)

  def is_Empty(self):
    return len(self.queue) == 0

  def __len__(self):
    return len(self.queue)

  def __str__(self):
    result = "["
    for item in self.queue:
      result += str(item)
      result += ", "
    result += "]"
    return result
```

With this basic queue implementation you can write all sorts of different types of queues such as a **Turn Taking**, a **Priority**, or just a regular queue. **Priority queue** has a O(1) looking up and removing the first item and a O(n) for inserting an item in the queue.

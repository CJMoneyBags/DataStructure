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

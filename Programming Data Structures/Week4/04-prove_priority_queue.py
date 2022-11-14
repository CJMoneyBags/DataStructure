"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        # new_node = Priority_Queue.Node(priority, value) # swapped the priority and value --Test 1
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            #if self.queue[index].priority >= self.queue[high_pri_index].priority:  doesn't use FIFO for priority --Test 4
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index] # dequeue first item in the queue for FIFO and stop infinite loop -- Test2
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: queue's up items in order
# Expected Result: Chris, Susan, James, Jojo
print("Test 1")
test = Priority_Queue()
test.enqueue("Chris", 1) #
test.enqueue("Susan", 2) # higher priority
test.enqueue("James", 3) # even higher priority
test.enqueue("Jojo", 3) # same has one above.
print(test)
# Defect(s) Found: value and priority are swapped.

print("=================")

# Test 2
# Scenario: deque, items in correct order with same priority
# Expected Result: Chris, Susan, James, Jojo
print("Test 2")
test = Priority_Queue()
test.enqueue("Chris", 1)
test.enqueue("Susan", 1)
test.enqueue("James", 1)
test.enqueue("Jojo", 1)
while len(test) > 0:
   print(test.dequeue())
# Defect(s) Found: Infinite loop was created seems like dequeue() doesn't delete the item
# after that fix there is an issue with the last item being dequeue'd first with items of the same priority

print("=================")

# Add more Test Cases As Needed Below

# Test 3
# Scenario: Dequeues the highest priority first then the rest down of the items in the queue
# Expected Result: Jojo, James, Susan, Chris
print("Test 3")
test = Priority_Queue()
test.enqueue("Chris", 1)
test.enqueue("Susan", 2)
test.enqueue("James", 3)
test.enqueue("Jojo", 4)
while len(test) > 0:
   print(test.dequeue())
# Defect(s) Found: none

print("=================")

# Test 4
# Scenario:Dequeues the highest priority first with the item that came first dequeued first following FIFO rules
# Expected Result: Jordan, James, Jojo, Chris, Susan
print("Test 4")
test = Priority_Queue()
test.enqueue("Chris", 2)
test.enqueue("Susan", 2)
test.enqueue("James", 4)
test.enqueue("Jojo", 4)
test.enqueue("Jordan", 5)
while len(test) > 0:
   print(test.dequeue())
# Defect(s) Found: dequeue's the list from the back and doesn't do FIFO for same priority

print("=================")

# Test 5
# Scenario:empty queue to dequeue
# Expected Result: Error message "The queue is empty." Return 'None' to get out of the program.
print("Test 5")
test = Priority_Queue()
print(test.dequeue())
# Defect(s) Found: none
print("=================")
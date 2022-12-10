# Linked Lists

A **linked list** is a data structure that contains an ordered collection of objects. A linked list is different from a normal list in how it stores its data. A normal list stores their data in an contiguous memory fashion, where as a Linked List uses references as part of the linked list element(Node).

 A **Node** is a part of the linked list that hold the data(values) as well as pointers to the next node or previous nodes. The list will have a **Head(beginning of the list)** and a **Tail(end of the list)**. If there are no items in the list then it is an **Empty** list. If there is one item in the list then the Head and the Tail point to the same Node.

 ![A picture of a Linked list](linked-list.png)

 Linked lists have many uses they can be used in creation of **Queues**, **Stacks**, and **Graphs** which are other data structures.

We will go over **how to create a linked list**, **how to traverse a linked list**, **Inserting new nodes**,*inserting head*, *inserting tail*, *inserting middle*, **Removing a node**

# Linked List Example
## How to create a linked lists
first yo need to create a linked list class. This will start with an empty list.
```python
class LinkedList:
  def __init__(self):
    self.head = None
```
Next you create a Node class to store you data and link to the next node.
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
```
Put together it might look like something like this:
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.ext = None

class LinkedList:
  def __init__(self):
    self.head = None
```

## How to traverse a linked lists
Traversing a Linked List is to go through every single node, starting with the head all the way to the first node that has a next value of None. We will make use of the__iter__(), and the yield key word. Where the__iter__ will make the list iterable and the yield key word returns the value but then continues through the loop. Where as return just gives the value and leaves.
```python
def __iter__(self):
  node = self.head
  while node is not None:
    yield node
    node = node.next
```
## Inserting new nodes
Of course a list isn't any useful to us if we can't add items to it. We will add items to the beginning, end, and even the middle of the list.
* ### inserting head
```python
def add_first(self, node):
  node.next = self.head
  self.head = node
```
* ### inserting tail
```python
def add_last(self, node):
  if slef.head is None:
    self.head = node
    return
  for current_node in self:
    pass
  current_node.next = node
```
* ### inserting middle
inserting in the middle can be done one of two ways, before or after, I personally like after, but I will show both ways.
**After method**
```python
def add_after(self, target_node_data, new_node):
  if self.head is None:
    raise Exception("List is empty") #Nothing to add to

  for node in self:
    if node.data == target_node_data:
      new_node.next = node.next
      node.next = new_node
      return

  raise Exception("Node with data '%s' not found" %target_node_data) # if the target_node_data doesn't exist
```
**Before method**
```python
def add_before(self, target_node_data, new_node):
  if self.head is None:
    raise Exception("List is empty") #Nothing to add to

  if self.head.data == target_node_data:
    return self.add_first(new_node)

  prev_node = self.head
  for node in self:
    if node.data == target_node_data:
      prev_node.next = new_node
      new_node.next = node
      return
    prev_node = node

  raise Exception("Node with data '%s' not found" %target_node_data) # if the target_node_data doesn't exist
```
## Removing a node
```python
def remove_node(self, target_node_data):
  if self.head is None:
    raise Exception("List is empty")

  if self.head.data == target_node_data:
    self.head = self.head.next
    return

  previous_node = self.head
  for node in self:
    if node.data == target_node_data:
      previous_node.next = node.next
      return
    previous_node = node
  raise Exception("Node with data '%s' not found" %target_node_data)
```
##So why not just use Lists instead
### Performance comparison:
* inserting an element in just a list can have an O(1) or an O(n) depending on where you are inserting it. For example at the beginning or end it will be an O(1), while in the middle somewhere it will be an O(n). Whereas for the Linked List it is always an O(1) no matter where you insert the node. Thus making the Linked List more efficient.
* When retrieving an element in either a List or Linked list because you have to traverse through it will be an O(n). This scenario both the List and Linked List are the same efficiency.
## Problem Assignment
One other form of a Linked list is something called a Circular Linked list. They are a type of linked list in that the last node points back to the head allowing you to travers the whole list at any node.

![A picture of a Circular Linked List](Circular_linked.png)

One example of this is growing me and my 5 other siblings had to take turns doing dishes. Sometimes when an event would happen or we went out to eat, the order would be forgotten and there were often heated discussion on whose turn it was.

We can create a circular linked list to keep track of whose turn it is to do the dishes. We started with oldest to youngest. In my family it was(Jennifer, Robert, Rebecca, Jared, Christopher, Angela) that was the order of the kids oldest to youngest.

You are to make a Circular Linked list to keep track of use turn it is to do the dishes. at one point Jennifer will get married, then Mom and Dad step in as Robert goes on a Mission, Robert comes back but then Rebecca leaves for college. Your list must keep track of all of these changes.
### SOLUTION TO ASSIGNMENT:
[Solution to the Assignment](SolutionLinkedList.md)

[Back to home](FinalProject.md)

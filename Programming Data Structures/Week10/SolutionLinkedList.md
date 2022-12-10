```python
class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # make the list iterable for the remove functions
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

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
        raise Exception("Node with data '%s' not found" % target_node_data)

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break


# Driver program to test above function

# Initialize list as empty
cllist = CircularLinkedList()

cllist.push("Jennifer")
cllist.push("Robert")
cllist.push("Rebecca")
cllist.push("Jared")
cllist.push("Chris")
cllist.push("Angela")

print("Contents of circular Linked List")
cllist.printList()
print()

# Now Jennifer got married and left the circulations

cllist.remove_node("Jennifer")
cllist.printList()
print()

# Now Mom and Dad joins the list to pick up the slack
# because Robert leaves on a mission
cllist.remove_node("Robert")
cllist.push("Mom")
cllist.push("Dad")
cllist.printList()
print()

# Robert comes back, but Rebecca goes to college
cllist.remove_node("Rebecca")
cllist.push("Robert")
cllist.printList()
print("\nEnd Test")
```
[back](LinkedList.md)

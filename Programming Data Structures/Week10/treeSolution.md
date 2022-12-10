

class BST:
    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):

        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
                node.left.parent = node
            else:
                self._insert(data, node.left)
        elif data > node.data:

            if node.right is None:
                node.right = BST.Node(data)
                node.right.parent = node
            else:
                self._insert(data, node.right)

    def __contains__(self, data):

        return self._contains(data, self.root)

    def _contains(self, data, node):

        if data > node.data and node.right:
            return self._contains(data, node.right)
        elif data < node.data and node.left:
            return self._contains(data, node.left)
        if data == node.data:
            return True
        else:
            return False

    def find(self, data):
        if self.root != None:
            return self._find(data, self.root)
        else:
            return None
    def _find(self, data, cur_node):
        if data == cur_node.data:
            return cur_node
        elif data < cur_node.data and cur_node.left != None:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right != None:
            return self._find(data, cur_node.right)
    def delete_value(self, data):
        return self.delete_node(self.find(data))

    def delete_node(self, node):

        def min_value_node(n):
            current = n
            while current.left != None:
                current= current.left
            return current
        def num_children(n):
            num_children = 0
            if n.left != None: num_children += 1
            if n.right != None: num_children += 1
            return num_children

        node_parent = node.parent

        node_children = num_children(node)


        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_paren.right = None
        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child
            child.parent = node_parent

        if node_children == 2:

            successor = min_value_node(node.right)
            node.data = successor.data

            self.delete_node(successor)



    def __iter__(self):

        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)



tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)

for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10

print("new test")
tree.delete_value(5)
tree.delete_value(7)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10

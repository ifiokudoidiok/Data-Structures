from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        return value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        elif target < self.value and self.left is not None:
            return self.left.contains(target)
        elif target > self.value and self.right is not None:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        elif self.right is not None:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        # create an empty queue
        q = Queue()
        # add the starting node to the queue
        q.enqueue(node)
        # iterate over the queue

        while q.size > 0:
            # set the current_node to the first item in the q
            curr_node = q.dequeue()
            # then print the current value
            print(curr_node.value)
            # if the current node has a left child
            if curr_node.left:
                # call enqueue on the current left
                q.enqueue(curr_node.left)
            # if the current node has a right child
            if curr_node.right:
                # call enqueue on the current right
                q.enqueue(curr_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node is None:
            return
        # create an empty stack
        s = Stack()
        # add the starting node to the stack
        s.push(node)
        # iterate over the stack
        while s.size > 0:
            # set the current_node to the first item in the stack
            curr_node = s.pop()
            # then print the current value
            print(curr_node.value)
            # if the current node has a left child
            if curr_node.left:
                # call push on the current left
                s.push(curr_node.left)
            # if the current node has a right child
            if curr_node.right:
                # call push on the current right
                s.push(curr_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

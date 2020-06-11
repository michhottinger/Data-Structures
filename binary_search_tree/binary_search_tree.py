import sys
sys.path.append('../queue')
from crazy_queue import Queue
sys.path.append('../stack')
from crazy_stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check incoming value
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)#resets the root to the left node then reruns
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            #go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            #got right if the right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        #pass func to left child
        if self.left:
            self.left.for_each(fn)
        #pass func to the right child
        if self.right:
            self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    
    def in_order_print(self, node):
          
        if node is None:#account for the possibilty that node is None
                return
        else:

                # Then recur on left child 
                self.in_order_print(node.left)
                print(node.value)
                
                # Finally recur on right child 
                self.in_order_print(node.right) 
                

               
                       
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        #Use queue to store the node (fifo)
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            #neighbors of the node will be visited in the order they were inserted
            n = queue.dequeue()
            print(n.value)
            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

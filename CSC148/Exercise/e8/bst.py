# BinarySearchTree class
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
# Yan Zeng , zengyan
# ---------------------------------------------


class EmptyBSTError:
    pass


class EmptyValue:
    pass


class BinarySearchTree:
    def __init__(self, root=EmptyValue):
        """ (BinarySearchTree, object) -> NoneType

        Create a new binary search tree with a given root value,
        left subtree, and right subtree.
        """

        self.root = root    # root value
        if self.is_empty():
            # Set left and right to nothing,
            # because this is an empty binary tree.
            self.left = None
            self.right = None
        else:
            # Set left and right to be new empty trees.
            # Note that this is different than setting them to None!
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

    def is_empty(self):
        """ (BinarySearchTree) -> bool

        Return True if self is empty.
        Empty trees are identified by having root value EmptyValue.
        """
        return self.root is EmptyValue

    def __contains__(self, item):
        """ (BinarySearchTree, object) -> bool

        Return True if self contains item.
        """
        if self.is_empty():
            return False
        elif item == self.root:
            return True
        elif item < self.root:
            return self.left.__contains__(item)
        else:
            return self.right.__contains__(item)

    # LAB 8
    def count_all(self, item):
        """ (self, object) -> int

        Return the number of times item appears in self.
        (Return 0 if self is empty.)
        """
        if self.is_empty():
            return 0
        elif item <= self.root:
            if item == self.root:
                return 1+self.left.count_all(item)
            else:
                return self.left.count_all(item)
        return self.right.count_all(item)

    
    def range(self, low, high):
        """ (self, object, object) -> int

        Precondition: low and high can be compared with items in self.

        Return the number of items in self whose value is
        between low and high, inclusive.
        """
        if self.is_empty():
            return 0
        elif high <= self.root:
            if high == self.root:
                return 1+self.left.range(low,high)
            else:
                return self.left.range(low,high)
        return self.right.range(low,high)

    # Mutating methods

    def insert(self, item):
        """ (BinarySearchTree, object) -> NoneType

        Insert item into self in the correct location.
        Do not change positions of any other nodes.
        """
        if self.is_empty():
            # Make new leaf node
            self.root = item
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        elif item <= self.root:
            self.left.insert(item)
        else:
            self.right.insert(item)

    # Deletion

    def delete(self, item):
        """ (BinarySearchTree, object) -> NoneType

        Remove item from self.
        Do nothing is self doesn't contain item.
        """
        if not self.is_empty():
            if self.root == item:
                self.delete_root()
            elif item < self.root:
                self.left.delete(item)
            else:
                self.right.delete(item)

    def delete_root(self):
        """ (BinarySearchTree) -> NoneType

        Remove the root node of self.
        Raise EmptyBSTError is self is empty.
        """
        if self.is_empty():
            raise EmptyBSTError
        else:
            self.root = self.left.extract_max()

    def extract_max(self):
        """ (BinarySearchTree) -> object

        Remove and return the maximum value in self.
        Raise EmptyBSTError is self is empty.
        """

        if self.is_empty():
            raise EmptyBSTError
        elif self.right.is_empty():
            temp = self.root
            # Copy left subtree to self, because root node is removed.
            self.root = self.left.root
            self.right = self.left.right
            new_left = self.left.left
            self.left = new_left
            return temp
        else:
            return self.right.extract_max()

    # LAB 8 - complete extract_min and then fix delete_root
    def extract_min(self):
        """ (BinarySearchTree) -> object

        Remove and return the minimum value in self.
        """
        if self.is_empty():
            raise EmptyBSTError
        elif self.left.is_empty():
            temp = self.root
            self.root = self.right.root
            self.left = self.right.left
            new_right = self.right.right
            self.right = new_right
            return temp
        else:
            return self.left.extract_min()

    # EXERCISE 8
    def list_range(self, low, high):
        """ (BinarySearchTree, object, object) -> list

        Precondition: low and high can be compared with items in self.

        Return a sorted list of the items in self whose value is
        between low and high, inclusive.
        Note: the returned list should include any duplicates
        that appear in self.
        """
        if self.is_empty():
            return []
        elif low<= self.root <= high:
            return self.left.list_range(low,high)+ [self.root]+ self.right.list_range(low,high)        
        elif high <= self.root:
            if high == self.root:
                return self.left.list_range(low,high)+ [self.root]
            else:
                return self.left.list_range(low,high)
        return self.right.list_range(low,high)
                
        
  

        
        
        
           
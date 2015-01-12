# ListBinaryTree class
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
# Yan Zeng,   zengyan
# ---------------------------------------------


class ListBinaryTree:
    def __init__(self, items):
        """ (ListBinaryTree, list) -> NoneType

        Create a complete binary tree in list form
        with the specified items.

        The [None] is used to start indexing items at 1
        instead of 0, which is easier.
        """

        self.items = [None] + items

    def is_empty(self):
        """ (ListBinaryTree) -> bool
         Return True if self is empty.
        """
        return len(self.items) == 1

    def root(self):
        """ (ListBinaryTree) -> object

        Return the root item of the tree.
        If the tree is empty, raise IndexError.
        """

        if self.is_empty():
            raise IndexError
        else:
            return self.items[1]

    def go_down_greedy(self, index=1):
        """ (ListBinaryTree) -> list

        Return a list of items starting at the node with position index
        and ending at a leaf, where at each level the child node
        with the smaller value is chosen to recurse on
        (in case of ties, choose the left child).

        By default, the list starts at the root of the tree.

        Note: you may use either the provided subtree methods,
        or do the index arithmetic yourself.
        For maximum learning, try both!
        """
        if index > len(self.items):
            return []
        else:
            lst = [self.items[index]]
            lft = 2 * index
            rit = 2 * index + 1
            if lft >= len(self.items) and rit >=len(self.items):
                return lst
            elif rit < len(self.items):
                return lst + self.go_down_greedy(rit)
            elif lft < len(self.items):
                return lst + self.go_down_greedy(lft)
            elif self.items[lft] < self.items[rit]:
                return lst + self.go_down_greedy(lft)
            else:
                return lst + self.go_down_greedy(rit) 
           
        
        

    # Index helper functions
    def left(index):
        """ (int) -> int

        Return the index of the left child of the node as position index.
        """
        return 2 * index

    def right(index):
        """ (int) -> int

        Return the index of the right child of the node as position index.
        """
        return 2 * index + 1

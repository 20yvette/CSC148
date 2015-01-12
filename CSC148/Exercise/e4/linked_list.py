# LinkedList class
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <YAN ZENG>, <zengyan>
#
# ---------------------------------------------
"""LinkedList class.

This is the node-based implementation of a linked list
for Week 4 of the course.
Note that this class lends itself well to iteration,
but for recursion there is a simpler model.

This contains all of the linked list methods from the week:
lecture material, labs, and the exercise.
"""


class Node:
    """A node in a linked list."""

    def __init__(self, item):
        """ (Node, object) -> NoneType

        Create a new node storing item, pointing to nothing.
        """

        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT."""

    def __init__(self, items):
        """ (LinkedList, list of objects) -> NoneType

        Create Node objects linked together in the order provided in items.
        Set the first node of the list as the first item in items.
        """

        if len(items) == 0:  # No items, and an empty list!
            self.first = None
        else:
            self.first = Node(items[0])
            current_node = self.first
            for item in items[1:]:
                current_node.next = Node(item)
                current_node = current_node.next

    # Non-mutating methods

    def __len__(self):
        """ (LinkedList) -> int

        Return the number of elements in self.
        """

        curr = self.first
        size = 0
        while curr is not None:
            size = size + 1
            curr = curr.next
        return size

    def __getitem__(self, index):
        """ (LinkedList, int) -> str

        Return the item at position index in self.
        Raise IndexError if index is >= the length of self.
        """

        if len(self) < i:
            raise IndexError

        curr = self.first
        i = 0
        while i < index:
            i = i + 1
            curr = curr.next
        return curr.item

    # Mutating methods

    def remove(self, index):
        """ (LinkedList, int) -> NoneType

        Remove node at position index.
        Raise IndexError if index is >= the length of self.
        """

        if len(self) <= i:
            raise IndexError

        if index == 0:
            self.first = self.first.next
        else:
            # Iterate to (index-1)-th node
            curr = self.first
            i = 0
            while i < index - 1:
                i = i + 1
                curr = curr.next

            # Update link to skip over i-th node
            curr.next = curr.next.next

    def insert(self, index, item):
        """ (LinkedList, int, object) -> NoneType

        Insert a new node containing item at position index.
        Raise IndexError if index is > the length of self.
        Note that adding to the end of a linked list is okay.
        """

        if index > len(self):   
            raise IndexError

        # Create new node
        new_node = Node(item)

        if index == 0:
            new_node.next = self.first
            self.first = new_node
        else:
            # Iterate to (index-1)-th node
            curr = self.first
            i = 0
            while i < index - 1:
                i = i + 1
                curr = curr.next

            # Update links to insert new node
            new_node.next = curr.next
            curr.next = new_node

    # --- Lab exercises start here ---

    def __contains__(self, item):
        """ (LinkedList, object) -> bool

        Return True if item is in self.
        >>> linked = LinkedList([1,2,3])
        >>> 1 in linked
        True
        >>> 4 in linked
        False
        """
        '''curr = self.first
        new_list = [] 
        while curr is not None:
            new_list = new_list.append(curr)
            curr = curr.next
        if item is in new_list:
            return True
        else:
            return False'''
        curr = self.first
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False

    def __str__(self):
        """ (LinkedList) -> str

        Return a string representation of self in the form
        '[item1 -> item2 -> ... -> item-n]'.
        >>> str(LinkedList([1,2,3]))
        '[1 -> 2 -> 3]'
        """
        curr = self.first
        string = ''
        while curr is not None:
            string = string + str(curr.item) + '->'
            curr = curr.next
        return string
        

    def __setitem__(self, index, item):
        """ (LinkedList, int, object) -> NoneType

        Store item at position index in self.
        Raise IndexError if index is >= the length of self.
        >>>[1,2,3],2,4
        >>>[1,2,4]
        """
        if index >= len(self):
            raise IndexError
        else:
            curr = self.first
            i = 0 
            while i < index:
                curr = curr.next
                i += 1
            curr.item = item
              
          
    def delete_item(self, item):
        """ (LinkedList, object) -> NoneType

        Remove the FIRST occurrence of item in self.
        Do nothing if self does not contain item.
        [1,3,4,4,2],4
        [1,3,4,2]
        """
        if len(self) == 0:
            return None
        else:
            curr= curr.first 
            while curr.next is not None:
                if item == curr.next.item:
                    curr.next = curr.next.next
                curr = curr.next
                

    def map(self, f):
        """ (LinkedList, function) -> LinkedList

        Return a new LinkedList whose nodes store items that are obtained by
        applying f to each item in self.

        >>> list = LinkedList(['Hello', 'Goodbye'])
        >>> list.map(upper)
        ['HELLO' -> 'GOODBYE']
        >>> str(list.map(len))
        [5 -> 7]
        """
        curr = self.first
        curr_2 = self.first
        other = LinkedList()
        while curr is not None:
            curr_2.item = f(curr.item) 
            curr = curr.next
            curr_2 = curr_2.next 
        return curr_2
            
        

    # Exercise 4
    def __eq__(self, other):
        """ (LinkedList, LinkedList) -> bool

        Return True if self and other contain the same items,
        in the same order.

        You may not use any other Linked List methods in your solution!
        """
        
        curr = self.first
        size = 0
        
        while curr is not None:
            size = size + 1
            curr = curr.next
        
        size_other = 0
        curr_other = other.first
        
        while curr_other is not None:
            size_other = size_other + 1
            curr_other = curr_other.next 
            
        if size == size_other:  
            curr = self.first
            curr_other = other.first
            while curr is not None:
                if curr.item == curr_other.item:
                    curr = curr.next
                    curr_other = curr_other.next
                else:
                    return False
        else:
            return False
        return True
               

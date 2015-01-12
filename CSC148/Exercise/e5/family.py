# Exercise 5 - Family Tree
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
#
# ---------------------------------------------


class Person:
    """Person class.

    Attributes:
    - name (str): The name of this Person
    - children (list of Person): a list of the Person objects who
                                 are the children of this Person
    """

    def __init__(self, name):
        """ (Person, str) -> NoneType
        Create a new person with the given name, and no children.
        """
        self.name = name
        self.children = []

    def count_descendants(self):
        """ (Person) -> int
        Return the number of descendants of self.
        """
        if self.children == []:
            return 0
        else:
            size = 0
            for name in self.children:
                size += name.count_descendants() + 1 
            return size
                
                
    
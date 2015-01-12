# Exercise 5 - Recursive Linked Lists
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# <full name>, <utorid>
# YAN ZENG  , zengyan
# ---------------------------------------------
from linkedlistrec import LinkedListRec


def map_f(linked_list, f):
    """ (LinkedListRec, function) -> LinkedListRec

    Return a new recursive linked list whose items
    are obtained by applying f to the items in linked_list.

    Your implementation should access the attributes
    of the LinkedListRec class directly, and may not use
    any LinkedListRec methods other than the constructor
    and is_empty.
    """
    return LinkedListRec(helper(linked_list,f))

def helper(lst,f):
    """(list, function) -> list
    """
    if lst.rest == None:
        return []
    else:
        return [f(lst.first)] + helper(lst.rest,f)
# Lab 6 - More Recursion Practice
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu


# Task 1: Subsets revisited
def all_subsets(lst):
    """ (list) -> (list of lists)

    Precondition: lst contains no duplicates.
    Return a list of all of the subsets of lst; order does not matter.
    """
    if len(lst) == 0:
        return [[]]
    lst2= lst[1:]
    new_lst = all_subsets(lst2)
    for i in new_lst:
        i.append(lst[0])
    return new_lst + all_subsets(lst2)
    
# Task 2: Binary Search
def return_half(lst, side):
    """ (list, bool) -> list
    Precondition: len(lst) is a power of 2, including 1.
    If side is True, return a new list containing the items in the *left half*
    of lst; if side is False, return a new list containing the items
    in the *right half*. (Hint: use list slicing.)

    >>> nums = [10, 3, -4, 1]
    >>> return_half(nums, True)
    [10, 3]
    >>> return_half(nums, False)
    [-4, 1]
    """
    if side is True:
        return lst[0: int(len(lst)/2)]
    else:
        return lst[int(len(lst)/2):]
    


def binary_search(lst, item):
    """ (list, object) -> bool
    Precondition: lst is a sorted list.
    Return True if item is in lst.

    >>> nums = [-4, 1, 3, 10]
    >>> binary_search(nums, 1)
    True
    >>> binary_search(nums, 40)
    False
    >>> binary_search([1], 1)
    True
    """
    # What is the base case?

    # Hint for the recursive implementation: check your indexes very carefully!
    
    temp = return_half(lst, True)
    if item == temp[-1]:
        return True
    else:
        return_half(temp,Ture)
    return item in binary_search(lst2, item)
    


# Task 3: Indexed Binary Search
def print_left(lst, left=0, right=None):
    """ (list, int, int) -> NoneType
    Precondition: 0 <= left < right <= len(lst) (if left and right are given)

    If right is None, first set right = len(lst).
    Then, print all of the items in the left half of lst[left:right].
    For simplicity, assume that len(lst[left:right]) is even.

    >>> nums = [3, 10, 4, 15, -1, -1, 2, 16]
    >>> print_left(nums, 0, 4)
    3
    10
    None # in Wing only
    >>> print_left(nums, 3, 5)
    15
    None # in Wing only
    >>> print_left(nums)
    3
    10
    4
    15
    None # in Wing only
    """
    # This code handles the default value of right.
    if right is None:
        right = len(lst)

    # YOUR CODE GOES HERE
    # You may use a loop for this question.
    # Hint: the hard part of this question is actually calculating the
    # correct midpoint. Do the math carefully, because it's easy to
    # get an off-by-one error!
    pass


def indexed_binary_search(lst, item, left=0, right=None):
    """ (list, object, int, int) -> bool
    Precondition: lst is a sorted list, 0 <= left <= right <= len(lst)
                  (if left and right are given)

    Return True if item is in lst[left:right].

    >>> nums = [-1, -1, 2, 3, 4, 10, 15, 16]
    >>> indexed_binary_search(nums, 4, 0, 3)
    True
    >>> indexed_binary_search(nums, 4, 0, 4)
    False
    >>> indexed_binary_search(nums, -1)
    True
    >>> indexed_binary_search(nums, 40)
    False
    """
    if right is None:
        right = len(lst)

    # YOUR CODE GOES HERE
    # Hint: your code will be very similar to binary_search;
    # just convert your base case and recursive calls to their index versions.

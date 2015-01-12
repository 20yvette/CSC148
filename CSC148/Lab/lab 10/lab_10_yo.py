""" Lab 10 - Sorting algorithms

This module contains two incomplete recursive sorting algorithms,
mergesort and quicksort. Your task in this lab is to complete
both of them!
"""


# ---- Quicksort ----

def quicksort(lst):
    """ (list) -> list
    Return a sorted list with the same elements as lst.
    Do *not* mutate lst.
    """
    # Same base case as mergesort
    if len(lst) <= 1:
        return lst[:]
    else:
        # Pick pivot to be first element
        pivot = lst[0]

        # Partition rest of list into two parts:
        # items that are <= pivot, and items that are > pivot.
        smaller, bigger = partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def partition(lst, pivot):
    """ (list, object) -> (list, list)

    Return two lists, where the first contains the items in lst
    that are <= pivot, and the second contains the items in lst
    that are > pivot.
    """
    # Hint: this can be done just by looping over lst once
    lst1 = []
    lst2 = []
    for i in lst:
        if i <= pivot:
            lst1.append(i)
        elif i > pivot:
            lst2.append(i)
    return lst1,lst2


# ---- mergesort ----
def mergesort(lst):
    """ (list) -> list
    Return a sorted list with the same elements as lst.
    Do *not* mutate lst.
    """
    # Base cases: empty list and one element.
    if len(lst) <= 1:
        # return a *copy* of lst
        return lst[:]
    else:
        # Divide the list into two halves, and recursively sort each half.
        m = len(lst) // 2
        left_sorted = mergesort(lst[:m])
        right_sorted = mergesort(lst[m:])

        # merge the two sorted halves and return
        return merge(left_sorted, right_sorted)


def merge(left, right):
    """ (list, list) -> list

    Precondition: left and right are sorted
    Return a sorted list containing the elements in left and right.
    """
    # Hint: use variables to keep track of which items are currently
    # being compared in each list, and use a loop!
    ans = []
    while not 0 == len(right) or not 0 == len(left):
        if len(right) == 0:
            ans.append(left.pop(0))
        elif len(left) == 0:
            ans.append(right.pop(0))
        elif right[0] > left[0]:
            ans.append(left.pop(0))
        elif right[0] < left[0]:
            ans.append(right.pop(0))
    return ans



# ---- Task 2: In-Place Quicksort
def partition_warmup(lst):
    """ (lst) -> NoneType

    Reorder the elements of lst[:-1] so that all of the items <= lst[-1] are
    before all of the items > lst[-1]. This is the only restriction; within
    each group, the items can be in any order.
    This is a *mutating* method.

    Do nothing if the lst is empty, or only contains one item.

    >>> lst = [5, 10, 3, 20, 6]
    >>> partition_warmup(lst)
    >>> lst
    [5, 3, 10, 20, 6]   # but [3, 5, 20, 10, 6] is also okay!!
    """
    pass


def partition_warmup2(lst):
    """ (lst) -> NoneType
    Same as partition_warmup, except also swap the last item to its "correct"
    position in lst, so that it comes after all of the items less than or equal
    to it, and before all of the items greater than it.

    >>> lst = [5, 10, 3, 20, 6]
    >>> partition_warmup(lst)
    >>> lst
    [5, 3, 6, 20, 10]
    """
    pass


def partition_ip(lst, start=0, end=None):
    """ (lst) -> int

    Same as partition_warmup2, except don't use the whole list, only
    lst[start:end] (you must set end = len(lst) if no argument is passed in).
    """
    pass


def quicksort_ip(lst, start=0, end=None):
    """ (list) -> NoneType
    Sort the items in lst[start:end].
    (If end is None, sort items in lst[start:]).
    Note: this is a *mutating* function, and you should not create a new list.
    """
    pass
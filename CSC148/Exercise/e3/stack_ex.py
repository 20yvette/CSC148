# Exercise 3: More Stack Exercises
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
from stack import Stack, EmptyStackError


class SmallStackError(Exception):
    pass


def reverse_top_two(stack):
    """ (Stack) -> NoneType

    Reverse the top two elements on stack.
    Raise a SmallStackError if stack has fewer than two elements.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse_top_two(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    if stack.is_empty():
        raise SmallStackError
    else:
        highest = stack.pop()
        if stack.is_empty():
            raise SmallStackError
        else:
            second_highest = stack.pop()
            stack.push(highest) 
            stack.push(second_highest)

def reverse(stack):
    """ (Stack) -> NoneType

    Reverse all the elements of stack.

    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    temp_stack = Stack()
    temp_stack2 = Stack()
    while not stack.is_empty():
        temp_stack.push(stack.pop())
    while not temp_stack.is_empty():
        temp_stack2.push(temp_stack.pop()) 
    while not temp_stack2.is_empty():
        stack.push(temp_stack2.pop()) 
    
    
    
       

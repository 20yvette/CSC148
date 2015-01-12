# Exercise 1, Task 1: Runtime Errors
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your information below, in format
# YAN ZENG, zengyan
#
# ---------------------------------------------
"""Exercise 1, Task 1: Runtime Errors."""


def bad_type():
    """When run, produces a TypeError."""
    print ('1'+1)


def bad_name():
    """When run, produces a NameError."""
    print (awesome+1)


def bad_attribute():
    """When run, produces an AttributeError."""
    a = 1
    print (a.insert(2))


def bad_index():
    """When run, produces an IndexError."""
    a = [1,2]
    print (a[3])


def bad_key():
    """When run, produces a KeyError."""
    a = {'apple':1, 'banana':2}
    print (a['orange'])


def bad_zero():
    """When run, produces a ZeroDivisionError."""
    print (1/0)


def bad_import():
    """When run, produces an ImportError."""
    import david_is_awesome

# Exercise 8, Task 2 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 8, Task 2 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from list_binary_tree import ListBinaryTree


class TestGoDownGreedy(unittest.TestCase):
    def setUp(self):
        self.tree = ListBinaryTree([4, 5, 3])

    def test_simple(self):
        self.assertEqual(self.tree.go_down_greedy(), [4, 3])


if __name__ == '__main__':
    unittest.main(exit=False)

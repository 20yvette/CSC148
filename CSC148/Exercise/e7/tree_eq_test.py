# Exercise 7, Task 1 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 7, Task 1 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from tree import Tree


class TestTreeEq(unittest.TestCase):

    def setUp(self):
        self.tree = Tree(1)
        self.tree.subtrees = [Tree('Hi'), Tree(3)]
        self.tree1 = Tree()
        

    def test_simple(self):
        tree2 = Tree(1)
        tree2.subtrees = [Tree('Hi'), Tree(3)]
        self.assertTrue(self.tree == tree2)
    
    def test_simple_2(self):
        tree2 = Tree(1)
        tree2.subtrees = [Tree(3), Tree('Hi')]
        self.assertFalse(self.tree == tree2)

    def test_empty(self):
        tree2 = Tree(1)
        self.assertFalse(self.tree1 == tree2)


if __name__ == '__main__':
    unittest.main(exit=False)

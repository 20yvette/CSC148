# Exercise 7, Task 2 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 7, Task 2 TESTS.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests,
and to be confident your code is correct!
"""
import unittest
from btree import BinaryTree


class TestTraversals(unittest.TestCase):

    def setUp(self):
        self.tree1 = BinaryTree(1)
        self.tree2 = BinaryTree(2)
        self.tree3 = BinaryTree(3)
        self.tree3.left = self.tree1
        self.tree3.right = self.tree2

    def test_preorder_simple(self):
        self.assertEqual([3, 1, 2], self.tree3.preorder())

    def test_inorder_simple(self):
        self.assertEqual([1, 3, 2], self.tree3.inorder())

    def test_postorder_simple(self):
        self.assertEqual([1, 2, 3], self.tree3.postorder())


if __name__ == '__main__':
    unittest.main(exit=False)

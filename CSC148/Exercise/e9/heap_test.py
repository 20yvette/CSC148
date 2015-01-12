# Exercise 9 TESTS
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Exercise 9 TESTS.

Note: all tests provided here. In future weeks,
only a subset of the tests will be provided,
and you'll be encouraged to write your own.
"""
import unittest
from heap import Heap, heapsort


class TestIsHeap(unittest.TestCase):

    def test_simple_heap(self):
        heap = Heap()
        heap.items = [None, 1]
        self.assertTrue(heap.is_heap())

    def test_simple_not_heap(self):
        heap = Heap()
        heap.items = [None, 1,2]
        self.assertFalse(heap.is_heap())


class TestHeapSort(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(heapsort([1, 3, 2]), [3, 2, 1])


if __name__ == '__main__':
    unittest.main(exit=False)

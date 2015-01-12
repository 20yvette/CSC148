# Assignment 2 - Unit Tests for Course
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your group members below, one per line, in format
# <full name>, <utorid>
# Udara Weerasinghe,
# Yan Zeng, zengyan
# Yansen Yang, yangya26
# ---------------------------------------------
"""Unit tests for course.py

Submit this file, containing *thorough* unit tests
for your code in course.py.
Note that you should not have any tests involving
standard input or output in here.
"""
import unittest
from course import (Course, UntakeableError,
                    PrerequisiteError)


class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course1 = Course('1')
        self.course2 = Course('2')
        self.course3 = Course('3')
        self.course4 = Course('4')
        self.course5 = Course('5')
        self.course1.prereqs = [self.course2, self.course3]
        self.course3.prereqs = [self.course4]
        self.course4.prereqs = [self.course5]

    def test_is_takeable_no_prereqs(self):
        self.assertTrue(self.course5.is_takeable())

    def test_is_takeable_true_simple(self):
        self.course5.taken = True
        self.assertTrue(self.course4.is_takeable())

    def test_is_takeable_true_complex(self):
        self.course5.taken = True
        self.course4.taken = True
        self.course3.taken = True
        self.course2.taken = True
        self.assertTrue(self.course1.is_takeable())

    def test_is_takeable_false_simple(self):
        self.assertFalse(self.course3.is_takeable())

    def test_is_takeable_false_complex(self):
        self.course3.taken = True
        self.assertFalse(self.course1.is_takeable())

    def test_take_takeable_simple(self):
        self.course5.take()
        self.assertTrue(self.course5.taken)

    def test_take_takeable_complex(self):
        self.course5.take()
        self.course4.take()
        self.course3.take()
        self.course2.take()
        self.course1.take()
        self.assertTrue(self.course1.taken)

    def test_take_already_taken(self):
        self.course5.taken = True
        self.assertTrue(self.course5.taken)

    def test_take_untakeable_simple(self):
        self.assertRaises(UntakeableError, self.course4.take)

    def test_take_untakeable_complex(self):
        self.course5.take()
        self.course4.take()
        self.course3.take()
        self.assertRaises(UntakeableError, self.course1.take)

    def test_add_prereq_simple(self):
        self.course6 = Course('6')
        self.course7 = Course('7')
        self.course2.add_prereq(self.course6)
        self.course2.add_prereq(self.course7)
        self.assertEqual(self.course2.prereqs, [self.course6, self.course7])

    def test_add_prereq_fail_simple1(self):
        self.assertRaises(PrerequisiteError, self.course5.add_prereq,
                          self.course4)

    def test_add_prereq_fail_simple2(self):
        self.assertRaises(PrerequisiteError, self.course4.add_prereq,
                          self.course5)

    def test_add_prereq_fail_complex1(self):
        self.assertRaises(PrerequisiteError, self.course1.add_prereq,
                          self.course5)

    def test_add_prereq_fail_complex2(self):
        self.assertRaises(PrerequisiteError, self.course5.add_prereq,
                          self.course3)

    def test_contains_simple1(self):
        self.assertTrue(self.course1.__contains__(self.course1))

    def test_contains_simple2(self):
        self.assertTrue(self.course1.__contains__(self.course4))

    def test_contains_simple3(self):
        self.course6 = Course('6')
        self.assertFalse(self.course1.__contains__(self.course6))

    def test_missing_prereqs_simple1(self):
        self.course4.taken = True
        self.assertEqual(self.course1.missing_prereqs(), ['2', '3'])

    def test_missing_prereqs_check_order(self):
        self.course1 = Course('a')
        self.course2 = Course('b')
        self.course3 = Course('c')
        self.course4 = Course('d')
        self.course1.prereqs = [self.course4, self.course3]
        self.course3.prereqs = [self.course2]
        self.course2.taken = True
        self.assertEqual(self.course1.missing_prereqs(), ['c', 'd'])

    def test_missing_prereqs_check_order2(self):
        self.course1 = Course('a')
        self.course2 = Course('b')
        self.course3 = Course('c')
        self.course4 = Course('d')
        self.course1.prereqs = [self.course4, self.course3]
        self.course3.prereqs = [self.course2]
        self.course2.taken = False
        self.assertEqual(self.course1.missing_prereqs(), ['b', 'c', 'd'])

    def test_course_copy_simple(self):
        self.course1 = Course('a')
        self.course2 = Course('b')
        self.course3 = Course('c')
        self.course4 = Course('d')
        self.course1.prereqs = [self.course4, self.course3]
        self.course0 = self.course1.course_copy()
        self.course1l = [self.course1.name]
        self.course5l = [self.course0.name]
        self.assertEqual(self.course1l, self.course5l)

    def test_course_copy_complex(self):
        self.course1 = Course('a')
        self.course2 = Course('b')
        self.course3 = Course('c')
        self.course4 = Course('d')
        self.course1.prereqs = [self.course4, self.course3]
        self.course3.prereqs = [self.course2]
        self.course0 = self.course1.course_copy()
        self.course1l = ['a', 'd', 'c', 'b']
        self.course2l = [self.course0.name, self.course0.prereqs[0].name,
                         self.course0.prereqs[1].name,
                         self.course0.prereqs[1].prereqs[0].name]
        self.assertEqual(self.course1l, self.course2l)

if __name__ == '__main__':
    unittest.main(exit=False)
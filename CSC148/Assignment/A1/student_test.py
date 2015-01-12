# Assignment 1 - Sample unit tests
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your group members below, one per line, in format
# <Yan Zeng>, <zengyan>
# <Yansen Yang>, <yangya26>
#
#
# ---------------------------------------------
"""Unit tests for student.py

Submit this file, containing *thorough* unit tests
for your code in student.py.
Note that you should not have any tests involving
standard input or output in here.
"""
import unittest
import student

# Assignment 1 - Sample unit tests
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
"""Sample unit tests for sms.py.

Because we're the code we're testing interacts
with the console, we need to do a bit of fiddling
to handle standard input and output.
Luckily for you, we've provided a base method
that does all of the work; you just need to provide
the actual test cases.
"""
import unittest
import sys
from io import StringIO
from sms import run
from student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student1 = Student()
        self.student1.create('Amy')
        self.student_many = Student()
        for i in range(31):
            self.student_many.create('Amy' + str(i))

    def test_create_simple(self):
        self.assertEqual(self.student1.dict_of_students, {'Amy': []})
        self.assertEqual(self.student1.dict_of_courses, {})

    def test_create_many(self):
        self.assertEqual(len(self.student_many.dict_of_students), 31)
        self.assertEqual(self.student1.dict_of_courses, {})

    def test_delete_simple(self):
        self.student1.delete('Amy')
        self.assertEqual(self.student1.dict_of_students, {})
        self.assertEqual(self.student1.dict_of_courses, {})

    def test_enrol_simple(self):
        self.student1.enrol('Amy', 'CSC148')
        self.assertEqual(self.student1.dict_of_students, {'Amy': ['CSC148']})
        self.assertEqual(self.student1.dict_of_courses, {'CSC148': ['Amy']})

    def test_enrol_30(self):
        for key in self.student_many.dict_of_students:
            if key != 'Amy0':
                self.student_many.enrol(key, 'CSC148')
        self.assertEqual(len(self.student_many.dict_of_courses['CSC148']), 30)

    def test_enrol_31(self):
        for key in self.student_many.dict_of_students:
            if key != 'Amy0':
                self.student_many.enrol(key, 'CSC148')
        self.assertEqual(self.student_many.enrol('Amy0', 'CSC148'), 'ERROR: Course CSC148 is full.')


    def test_enrol_non_exist_student(self):
        self.assertEqual(self.student_many.enrol('Bob', 'CSC148'), 'ERROR: Bob does not exist.')


    def test_drop_simple(self):
        self.student1.enrol('Amy', 'CSC148')
        self.student1.drop('Amy', 'CSC148')
        self.assertEqual(self.student1.dict_of_students, {'Amy': []})
        self.assertEqual(self.student1.dict_of_courses, {'CSC148': []})

    def test_drop_non_exist_student(self):
        self.assertEqual(self.student1.drop('Bob', 'CSC148'), 'ERROR: Bob does not exist.')

    def test_list_courses_simple(self):
        self.student1.enrol('Amy', 'CSC148')
        self.student1.enrol('Amy', 'CSC165')
        self.student1.enrol('Amy', 'CSC108')
        self.assertEqual(self.student1.list_courses('Amy'),
                         'Amy is taking CSC108, CSC148, CSC165')

    def test_list_courses_non_exist(self):
        self.assertEqual(self.student1.list_courses('Bob'), 'ERROR: Bob does not exist.')

    def test_list_courses_lazy_bum(self):
        self.assertEqual(Self.student1.list_courses('Amy'), 'Amy is not taking any courses.')

    def test_common_courses_simple(self):
        self.student_many.enrol('Amy0', 'CSC148')
        self.student_many.enrol('Amy1', 'CSC148')
        self.assertEqual(self.student1.common_courses
                         ('Amy0', 'Amy1'), 'CSC148')

    def test_common_courses_non_exist(self):
        self.assertEqual(self.student1.common_courses('Bob', 'alec'), 'ERROR: Bob does not exist.'
                         'ERROR: alec does not exist.')

    def test_common_courses_same_student(self):
        self.student1.enrol('Amy', 'CSC48')
        self.assertEqual(self.student1.common_courses('Amy', 'Amy'), 'CSC148')

    def test_class_list_simple(self):
        self.student1.enrol('Amy', 'CSC148')
        self.assertEqual(self.student1.class_list('CSC148'), 'Amy')

    def test_class_list_many(self):
        self.student_many.enrol('Amy0', 'CSC148')
        self.student_many.enrol('Amy1', 'CSC148')
        self.student_many.enrol('Amy2', 'CSC148')
        self.student_many.enrol('Amy3', 'CSC148')
        self.student_many.enrol('Amy4', 'CSC148')
        self.student_many.enrol('Amy5', 'CSC148')
        self.assertEqual(self.student1.class_list('CSC148'),
                         'Amy0, Amy1, Amy2, Amy3, Amy4, Amy5')

    def test_class_list_simple(self):
        self.student1.enrol('Amy', 'CSC148')
        self.student1.drop('Amy', 'CSC148')
        self.assertEqual(self.student1.class_list('CSC148'),
                         'No one is taking CSC148.')

if __name__ == '__main__':
    unittest.main(exit=False)

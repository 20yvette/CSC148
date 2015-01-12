# Assignment 2 - Unit Tests for Course (Sample tests)
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
import unittest

from planner import TermPlanner, parse_course_data
from course import Course


class TestParser(unittest.TestCase):

    def test_binary_simple(self):
        filename = 'binary_simple.txt'

        actual = parse_course_data(filename)
        self.assertEqual('CSC207', actual.name)

        prereqs = actual.prereqs
        prereq_names = [p.name for p in prereqs]
        # User assertCountEqual when order doesn't matter
        self.assertCountEqual(['CSC165', 'CSC148'], prereq_names)

        for p in prereqs:
            self.assertEqual([], p.prereqs)
    
    def test_sample(self):
            filename = 'sample.txt'
    
            actual = parse_course_data(filename)
            self.assertEqual('AWE400', actual.name)
    
            prereqs = actual.missing_prereqs()
            print(actual.prereqs[0].name)
            # User assertCountEqual when order doesn't matter
            self.assertCountEqual(['AWE100', 'AWE200','AWE300', 'AWE101','AWE199','AWE250'], prereqs)    
            
            
class TestIsValid(unittest.TestCase):
    def setUp(self):

        # Single prereq
        self.single = TermPlanner('single.txt')
        self.sample = TermPlanner('sample.txt')

    def test_single_two(self):
        self.assertTrue(self.single.is_valid([['CSC108'], ['CSC148']]))
    
    def test_sample(self):
        self.assertTrue(self.sample.is_valid([['AWE100', 'AWE101', 'AWE199'], 
                                              ['AWE200','AWE250'],['AWE300'],['AWE400']]))

class TestPlanner(unittest.TestCase):
    def setUp(self):
        # Single prereq
        self.single = TermPlanner('single.txt')
        self.sample = TermPlanner('sample.txt')

    '''def gen_test(self, tp, courses):
        s = tp.generate_schedule(courses)
        # Uncomment this line if you implement good_schedule.
        self.assertTrue(good_schedule(tp, s, courses))'''

    def test_one_prereq(self):
        self.assertCountEqual(self.single.generate_schedule(['CSC108','CSC148']),[['CSC108'], ['CSC148']])
    
    def test_sample(self):
        self.assertCountEqual(self.sample.generate_schedule(['AWE100', 'AWE101', 'AWE199', 
                                    'AWE200','AWE250','AWE300','AWE400']),[['AWE100', 'AWE101', 'AWE199','AWE250'], 
                                              ['AWE200'],['AWE300'],['AWE400']])    


'''def good_schedule(tp, schedule, courses):
    """ (TermPlanner, list of (list of str)) -> bool
    Return True if schedule is an acceptable output
    of tp.generate_courses(courses).
    """
    # Implement this function yourself if you want to use it!
    if schedule == tp.generate_courses(courses):
        return True'''

if __name__ == '__main__':
    unittest.main(exit=False)

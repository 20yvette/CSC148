# Assignment 2 - Course Planning!
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
"""Program for helping users plan schedules.

This module contains the main class that is used to interact with users
who are trying to plan their schedules. It requires the course module
to store prerequisite information.

TermPlanner: answers queries about schedules based on prerequisite tree.
"""
from course import Course, UntakeableError


def find_root(node):
    """ (Course) -> Course

    From any node in a tree, traverse the tree until the root
    node which has no parent, and then return the root node.
    """
    curr_node = node
    while curr_node.parent is not None:
        curr_node = curr_node.parent
    return curr_node


def parse_course_data(filename):
    """ (str) -> Course

    Read in prerequisite data from the file called filename,
    create the Course data structures for the data,
    and then return the root (top-most) course.

    See assignment handout for details.
    """

    with open(filename) as file:
        content = file.readlines()
    # list of courses in file (Course objects)
    all_courses = []
    # names of the courses
    names_of_courses = []
    for courses in content:
        split_courses = courses.split()
        # keep track of course names and Course objects in two lists but
        # the lists correspond by index
        for code in split_courses:
            if code not in names_of_courses:
                names_of_courses.append(code)
                all_courses.append(Course(code))
        # find index of coursename in names_of_courses
        # since index of coursename and the index of
        # the actual course object in all_courses correspeond
        index_of_course1 = names_of_courses.index(split_courses[0])
        index_of_course2 = names_of_courses.index(split_courses[1])
        all_courses[index_of_course2].add_prereq(all_courses[index_of_course1])
    return find_root(all_courses[0])


class TermPlanner:
    """Tool for planning course enrolment over multiple terms.

    Attributes:
    - course (Course): tree containing all available courses
    """

    def __init__(self, filename):
        """ (TermPlanner, str) -> NoneType

        Create a new term planning tool based on the data in the file
        named filename.

        You may not change this method in any way!
        """
        self.course = parse_course_data(filename)
    # helper functions

    def course_exists(self, course):
        """(TermPlanner, str) -> bool
        Return true if a Course with name course is in the tree
        containing all available courses
        """
        return Course(course) in self.course

    def take_course2(self, course1, course2_name):
        """(TermPlanner, Course, str) -> bool
        navigate to the course with name course2 in the tree course1 and take
        it if course is not takeable return False, return true if succesfully
        taken Prerequisite: a course with name course2_name exists in course1
        tree
        """
        if course1.name == course2_name:
            try:
                course1.take()
            except UntakeableError:
                return False
            else:
                return True
        else:
            for course in course1.prereqs:
                if self.take_course2(course, course2_name):
                    return True
            return False

    def prereqs_in_same_term(self, course_tree, course_name, term):
        """(TermPlanner, Course, str, list of str) -> bool
        return whether prereqs for a course are being taken in the same
        semester
        """
        if course_tree.name == course_name:
            return any(pre.name in term for pre in course_tree.prereqs)
        else:
            for course in course_tree.prereqs:
                if self.prereqs_in_same_term(course, course_name, term):
                    return True
            return False

    def is_valid(self, schedule):
        """ (TermPlanner, list of (list of str)) -> bool

        Return True if schedule is a valid schedule.
        Note that you are *NOT* required to specify why a schedule is invalid,
        though this is an interesting exercise!
        """
        # create copy of all courses so we can make changes when course is
        # taken
        # without affecting original course tree
        copy = self.course.course_copy()
        # keep track of courses taken so far so no duplicates can be taken
        # later
        names_courses_so_far = []
        for term in schedule:
            for course_name in term:
                if not self.course_exists(course_name):
                    return False
                if course_name in names_courses_so_far:
                    return False
                if self.prereqs_in_same_term(copy, course_name, term):
                    return False
                if self.take_course2(copy, course_name):
                    names_courses_so_far.append(course_name)
                else:
                    return False
        return True

    def generate_schedule(self, selected_courses):
        """ (TermPlanner, list of str) -> list of (list of str)

        Return a schedule containing the courses in selected_courses that
        satisfies the restrictions given in the assignment specification.
        """
        copy_tree = self.course.course_copy()
        copy_courses = selected_courses[:]
        already_taken = []
        schedule = []

        while set(already_taken) != set(selected_courses):
            term = self.fill_term(copy_tree, already_taken, selected_courses)
            already_taken += term
            schedule.append(term)
        return schedule

    def fill_term(self, course, already_taken, selected_courses):
        """(TermPlanner,Course,list of str,list of str)
        Fill up a term with the restrictions given on the assignment page
        this is a helper function for generate schedule
        """
        term = []
        i = 0
        while len(term) < 5 and i < len(selected_courses):
            crs = selected_courses[i]
            if crs not in already_taken \
               and not self.prereqs_in_same_term(course, crs, term) and\
               self.take_course2(course, crs):
                term.append(crs)
            i += 1
        return term
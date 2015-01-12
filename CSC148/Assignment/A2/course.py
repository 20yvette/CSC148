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
"""Course prerequisite data structure.

This module contains the class that should store all of the
data about course prerequisites and track taken courses.
Note that by tracking "taken" courses, we are restricting the use
of this class to be one instance per student (otherwise,
"taken" doesn't make sense).

Course: a course and its prerequisites.
"""


class UntakeableError(Exception):
    pass


class PrerequisiteError(Exception):
    pass


class AlreadyTakenError(Exception):
    pass


class Course:
    """A tree representing a course and its prerequisites.

    This class not only tracks the underlying prerequisite relationships,
    but also can change over time by allowing courses to be "taken".

    Attributes:
    - name (str): the name of the course
    - prereqs (list of Course): a list of the course's prerequisites
    - taken (bool): represents whether the course has been taken or not
    - parent(Course): represents the course to which the created object
     is a direct prerequisite for
    """

    # Core Methods - implement all of these
    def __init__(self, name, prereqs=None):
        """ (Course, str, list of Courses) -> NoneType

        Create a new course with given name and prerequisites.
        By default, the course has no prerequisites (represent this
        with an empty list, NOT None).
        The newly created course is not taken.
        """
        self.name = name
        if prereqs is None:
            self.prereqs = []
        else:
            self.prereqs = prereqs
        self.taken = False
        self.parent = None

    def is_takeable(self):
        """ (Course) -> bool

        Return True if the user can take this course.
        A course is takeable if and only if all of its prerequisites are taken.
        """
        return all(course.taken for course in self.prereqs)

    def take(self):
        """ (Course) -> NoneType

        If this course is takeable, change self.taken to True.
        Do nothing if self.taken is already True.
        Raise UntakeableError if this course is not takeable.
        """
        if not self.is_takeable():
            raise UntakeableError
        else:
            self.taken = True

    def add_prereq(self, prereq):
        """ (Course, Course) -> NoneType

        Add a prereq as a new prerequisite for this course.

        Raise PrerequisiteError if either:
        - prereq has this course in its prerequisite tree, or
        - this course already has prereq in its prerequisite tree
        """
        if prereq in self or self in prereq:
            raise PrerequisiteError
        else:
            self.prereqs.append(prereq)
            prereq.parent = self

    def __contains__(self, prereq):
        """(Course, Course) -> bool

        Return True if a course with prereq's course name
        is in this course's prereqs tree, or if this course's name
        and prereq's name are identical. Otherwise return False
        """
        if self.name == prereq.name:
            return True
        else:
            # check if prereq is in the course's prereqs tree
            for course in self.prereqs:
                if course.__contains__(prereq):
                    return True
            return False

    def course_copy(self):
        """(Course) -> Course
        return an independant copy of self
        """
        course = Course(self.name)
        for item in self.prereqs:
            course.prereqs.append(item.course_copy())
        return course

    def missing_prereqs(self):
        """ (Course) -> list of str

        Return a list of all of the names of the prerequisites of this course
        that are not taken.

        The returned list should be in alphabetical order, and should be empty
        if this course is not missing any prerequisites.
        """
        courses_not_taken = []

        if self.prereqs is []:
            return []
        else:
            for course in self.prereqs:
                if course.taken is False:
                    courses_not_taken += [course.name]\
                        + course.missing_prereqs()
            courses_not_taken.sort()
            return courses_not_taken
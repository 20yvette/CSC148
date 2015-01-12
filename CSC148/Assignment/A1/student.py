# Assignment 1 - Managing Students!
#
# CSC148 Fall 2014, University of Toronto
# Instructor: David Liu
# ---------------------------------------------
# STUDENT INFORMATION
#
# List your group members below, one per line, in format
# <full name>, <utorid>
# <Yansen Yang>, <yangya26>
# <Yanyan Yvette>, <>
# <Kumar Chan>, <>
# ---------------------------------------------
"""The back-end data model for the program.

TODO: fill in this doctring with information about your
class(es)!
"""


def sort_and_concatenate(unsorted_list):
    return ', '.join(sorted(unsorted_list))


class EmptyStackError(Exception):
    """Exception used when calling pop on empty stack."""
    pass

class MyError(Exception):
    pass

class Stack:
    """Stack implementation.
    Stores data in a first-in, last-out order.

    Attributes:
    - items (list): the data stored in the stack
    """

    def __init__(self):
        """ (Stack) -> NoneType
        Create a new empty stack.
        """
        self.items = []

    def is_empty(self):
        """ (Stack) -> bool
        Return True if this stack contains no items.
        """
        return len(self.items) == 0

    def push(self, item):
        """ (Stack, object) -> NoneType
        Add a new element to the top of this stack.
        """
        self.items.append(item)

    def pop(self):
        """ (Stack) -> object
        Remove and return the element at the top of this stack.
        Raise EmptyStackError if this stack is empty.
        """
        try:
            return self.items.pop()
        except IndexError:
            raise EmptyStackError


class Command:
    def __init__(self):
        self.commands_stack = Stack()
        self.student = Student()

    def sort_command(self, user_input):
        command = user_input.split()

        try:
            if len(command) == 0:
                print('Unrecognized command!')

            elif command[0] == 'undo':
                try:
                    if len(command) == 1:
                        self.undo()
                        print(self.commands_stack.items) #remove later
                    else:
                        i = int(command[1])
                        if i > 0:
                            while i > 0:
                                self.undo()
                                i -= 1
                            print(self.commands_stack.items) #remove later
                        else:
                            print('ERROR:', command[1],
                                  'is not a positive natural number.')
                            print(self.commands_stack.items) #remove later
                except EmptyStackError:
                    print('ERROR: No commands to undo.')
                    print(self.commands_stack.items) #remove later

            elif command[0] == 'create' and command[1] == 'student':
                self.add(command, self.student.create(command[2]))
                print(self.commands_stack.items) #remove later

            elif command[0] == 'enrol':
                self.add(command, self.student.enrol(command[1], command[2]))
                print(self.commands_stack.items) #remove later

            elif command[0] == 'drop':
                self.add(command, self.student.drop(command[1], command[2]))
                print(self.commands_stack.items) #remove later

            elif command[0] == 'list-courses':
                self.student.list_courses(command[1])
                self.add(command, False)
                print(self.commands_stack.items) #remove later

            elif command[0] == 'common-courses':
                self.student.common_courses(command[1], command[2])
                self.add(command, False)
                print(self.commands_stack.items) #remove later

            elif command[0] == 'class-list':
                self.student.class_list(command[1])
                self.add(command, False)
                print(self.commands_stack.items) #remove later

            else:
                print('Unrecognized command!')
                self.add(command, False)
                print(self.commands_stack.items) #remove later

        except IndexError:
            print('Unrecognized command!')
            self.add(command, False)
            print(self.commands_stack.items) #remove later

        except ValueError:
            print('Unrecognized command!')
            self.add(command, False)
            print(self.commands_stack.items) #remove later

    def add(self, user_input, undoable_command):
        """(Command, list of str, bool) -> NoneType
                """
        user_input.append(undoable_command)
        self.commands_stack.push(user_input)

    def undo(self):
        last_command = self.commands_stack.pop()

        if True in last_command:

            if last_command[0] == 'create':
                self.student.delete(last_command[2])

            if last_command[0] == 'enrol':
                self.student.drop(last_command[1], last_command[2])

            if last_command[0] == 'drop':
                self.student.enrol(last_command[1], last_command[2])


class Student:
    """A student along with the courses he is enrolled in.

        The class represents a student and the courses he is enrolled in.

        Attributes:
            self.dict_of_students (dictionary): keys are stuidents and
            values are a
            list of string of courses he is enrolled in.

        """

    def __init__(self):
        """(Student) -> NoneType

                Initialize an empty dictionary without students or courses.
                """
        self.dict_of_students = {}
        self.dict_of_courses = {}

    def create(self, student_name):
        """(Student, str) -> bool

                Creates a key with str student_name with an empty list as
                value, and return True if no errors occur.
                """
        if student_name in self.dict_of_students:
            print('ERROR: Student', student_name, 'already exists.')
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
            return False
        else:
            self.dict_of_students[student_name] = []
            # creates a key/value pair in which the key is str of
            # student_name and the value is an empty
            # list of str for the courses
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
            return True

    def delete(self, student_name):
        """(Student, str) -> NoneType

                Deletes a key with str student_name from dict_of_students.
                """
        if student_name in self.dict_of_students:
            del self.dict_of_students[student_name]
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later

    def enrol(self, student_name, course_name):
        """(Student, str, str) -> bool

                Appends course_name into the list of courses in value of key
                student_name, and return True if no errors
                occur.
                """
        try:
            if course_name not in self.dict_of_courses:
                # checks if the course doesn't exist, then creates the empty
                #  key/value pair if
                # it does not
                self.dict_of_courses[course_name] = []
            if len(self.dict_of_courses[course_name]) > 29:
                raise MyError 
                print('ERROR: Course', course_name, 'is full.')
                print(self.dict_of_students) #remove later
                print(self.dict_of_courses) #remove later
            else:
                if course_name not in self.dict_of_students[student_name]:
                    # checks if student isn't already taking the course
                    self.dict_of_students[student_name].append(course_name)
                if student_name not in self.dict_of_courses[course_name]:
                    self.dict_of_courses[course_name].append(student_name)
                    print(self.dict_of_students) #remove later
                    print(self.dict_of_courses) #remove later
                    return True
        except KeyError:
            print('ERROR: Student', student_name, 'does not exist.')
            raise MyError 
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
            return False

    def drop(self, student_name, course_name):
        """(Student, str, str) -> NoneType

                Removes course_name from the list of courses in value of key
                student_name
                """
        try:
            if course_name in self.dict_of_students[student_name]:
                # checks if course being dropped is in the list of courses
                # of the student
                if course_name in self.dict_of_courses:
                    # checks if the course exists
                    self.dict_of_students[student_name].remove(course_name)
                    self.dict_of_courses[course_name].remove(student_name)
                    print(self.dict_of_students) #remove later
                    print(self.dict_of_courses) #remove later
                    return True
        except KeyError:
            print('ERROR: Student', student_name, 'does not exist.')
            raise MyError
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
            return False

    def list_courses(self, student_name):
        """(Student, str) -> NoneType

                Prints a sorted list concatenated by commas of the courses
                student_name is taking.
                """
        try:
            if len(self.dict_of_students[student_name]) == 0:
                print(student_name, 'is not taking any courses.')
                print(self.dict_of_students) #remove later
                print(self.dict_of_courses) #remove later
            else:
                print(student_name, 'is taking', sort_and_concatenate(
                    self.dict_of_students[student_name]))
                # return the list which is concatenated by commas and
                # sorted using a helper function above
                print(self.dict_of_students) #remove later
                print(self.dict_of_courses) #remove later
        except KeyError:
            print('ERROR: Student', student_name, 'does not exist.')
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later

    def common_courses(self, student_name1, student_name2):
        """(Student, str, str) -> NoneType

                Prints a sorted list concatenated by commas of the courses
                student_name1, student_name2 have in common
                """
        # cannot use try except block because handling with multiple ways
        # for the same error KeyError
        if student_name1 in self.dict_of_students and student_name2 not in \
                self.dict_of_students:
            # this is the logical equivalent to student_name1 not in dict
            # NOR student_name2 not in dict
            print('ERROR: Student', student_name2, 'does not exist.')
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
        elif student_name1 not in self.dict_of_students and student_name2 in\
                self.dict_of_students:
            # same as directly above
            print('ERROR: Student', student_name1, 'does not exist.')
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
        elif student_name1 not in self.dict_of_students and student_name2 \
                not in self.dict_of_students:
            # both not in dict
            print('ERROR: Student', student_name1, 'does not exist.')
            print('ERROR: Student', student_name2, 'does not exist.')
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
        else:
            print(sort_and_concatenate(
                set(self.dict_of_students[student_name1]) & set(
                    self.dict_of_students[student_name2])))
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later

    def class_list(self, course_name):
        """(Student, str) -> NoneType

                Prints a sorted list concatenated by commas of the students
                taking course_name.
                """
        if course_name not in self.dict_of_courses:
            # checks if the course doesn't exist, then creates the
            # empty key/value pair if it does not
            self.dict_of_courses[course_name] = []
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later

        if len(self.dict_of_courses[course_name]) == 0:
            print('No one is taking', course_name, '.')
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
        else:
            print(sort_and_concatenate(self.dict_of_courses[course_name]))
            print(self.dict_of_students) #remove later
            print(self.dict_of_courses) #remove later
            # return the list, which is concatenated by commas and sorted
            # using a helper function above

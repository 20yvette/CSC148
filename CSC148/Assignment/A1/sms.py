# Assignment 1 - Managing students!
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
"""Interactive console for assignment.

This module contains the code necessary for running the interactive console.
As provided, the console does nothing interesting: it is your job to build
on it to fulfill all the given specifications.

run: Run the main interactive loop.
"""

from student import Command, Student, sort_and_concatenate


def run():
    """ (NoneType) -> NoneType

    Run the main interactive loop.
    """

    commands = Command()

    while True:
        
        command = input('')

        if command == 'exit':
            break
        else:
            commands.sort_command(command)

if __name__ == '__main__':
    run()

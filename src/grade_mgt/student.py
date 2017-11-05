#!/usr/bin/python
# -*- coding: <utf8> -*-


class Student(object):
    ''' This class represents a student. A student is defined by a name, a class and has grades'''

    def __init__(self, name, year):
        # Public interface
        self.name = name
        self.year = year

        # Private
        self._grades = []

    def addGrade(self, grade):
        ''' Update the statistics after the student got a new grade '''
        self._grades.append(grade)
        self.update()

    def update(self):
        ''' update student's statistics: mean, max, min, etc.'''
        raise NotImplementedError("Function not yet implemented")
        return 1
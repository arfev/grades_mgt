#!/usr/bin/python
# -*- coding: <utf8> -*-

class exam(object):

    def __init__(self, year, coefficient):
        # Public interface
        self.year = year
        self.coefficient = coefficient


        # Private interface
        self._grades = { }

    def addGrade(self, name, grade):
        ''' Add a grade to a specific student '''
        if not name in self.year:
            return 1

        #TODO: handle case if student already has a grade !
        self._grades[name] = grade
        self.update()
        return 0

    def update(self):
        ''' Update statistics of this exam'''
        raise NotImplementedError(" Function not implemented ")

    def getGrade(self, name):
        ''' Return the grade of a given student '''
        if not name in self._grades.keys():
            return 1

        return self._grade[name]

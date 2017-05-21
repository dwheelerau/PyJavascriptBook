#!/usr/bin/env python

from __future__ import print_function

student_data = [
    {'name': 'Bob', 'id': 0, 'scores': [50,60,60,70]}, 
    {'name': 'Alice', 'id': 1, 'scores': [55,65,65,75]}, 
    {'name': 'Carol', 'id': 2, 'scores': [53,63,63,73]}, 
    {'name': 'Dan', 'id': 3, 'scores': [57,66,67,76]}, 
]


def proc_student_data(data, pass_threshold=60, merit_threshold=75):
    for sdata in data:
        av = sum(sdata['scores'])/float(len(sdata['scores']))
        sdata['average'] = av

        if av > merit_threshold:
            sdata['ass'] = 'passed with merit'
        elif av > pass_threshold:
            sdata['ass'] = 'passed'
        else:
            sdata['ass'] = 'failed'

        print("%s's (id: %d) final ass is: %s" % (sdata['name'], sdata['id'],
                                                sdata['ass'].upper()))

if __name__ == '__main__':
    proc_student_data(student_data)

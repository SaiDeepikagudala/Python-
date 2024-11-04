# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:21:08 2021

@author: SRINIVAS
"""
def overlapping(list1, list2):
    '''checking for common number in 2 lists'''
    result = False
    for x_mem in list1:
        for y_mem in list2:
            if x_mem == y_mem:
                result = True
                return result
print(overlapping([1,2,3,4,5], [5,6,7,8,9]))
print(overlapping([1,2,3,4,5], [6,7,8,9]))

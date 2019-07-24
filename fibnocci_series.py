# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:36:50 2019

@author: Mohankrishna.Galala
"""

def fibnocci_series(num):
    '''prints given number of fibnocci series numbers'''
    first = 0
    second = 1
    if num < 2:
        print 1
        return
    else:
        print 1
        while (num-1) > 0:
            temp = first + second
            print temp
            first, second = second, temp
            num = num -1
    return

NUMBER = raw_input("enter a number :")
fibnocci_series(int(NUMBER))

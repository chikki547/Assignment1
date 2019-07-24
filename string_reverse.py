# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:50:52 2019

@author: Mohankrishna.Galala
"""

STRING = raw_input("enter string :")

#string reverse using index
print STRING[::-1]

#string reverse using iteration
REVERSE = ""
for i in STRING:
    #print i
    REVERSE = i + REVERSE
print REVERSE

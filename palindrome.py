# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:45:06 2019

@author: Mohankrishna.Galala
"""

#palindrome


def is_palindrome(inp):
    '''return true if it is a palindrome else return false'''
    reverse = inp[::-1]
    return reverse == inp

INPUT = raw_input("enter something:")
if is_palindrome(INPUT):
    print "Palindrome\n"
else:
    print "Not a Palindrome\n"

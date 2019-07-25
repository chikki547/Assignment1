# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:42:55 2019

@author: Mohankrishna.Galala
"""
#find prime number
import math


def find_prime(num):
    """RETURNs 1 if prime else RETURNs 0."""
    if num == 1:
        return 0
    i = int(math.sqrt(num))
    for k in range(2, i+1):
        if (num % k) == 0:
            return 0
    return 1

def print_primes(numb):
    """prints all prime numbers till the given number including it"""
    print "prime numbers untill", numb, "are-"
    if numb == 1:
        print "None\n"
        return
    for i in range(2, numb+1):
        if find_prime(i) == 1:
            print i

NUMBER = int(raw_input("enter number :"))
if find_prime(float(NUMBER)) == 0:
    print NUMBER, "is not prime\n"
else:
    print NUMBER, "is prime\n"
print_primes(int(NUMBER))
